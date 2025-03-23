package service

import (
	"auth/service/internal/model"
	"auth/service/internal/repository"
	"auth/service/pkg/jwt-service/authtoken"
	"auth/service/pkg/redis"
	"context"
	"encoding/json"
	"log"
	"time"

	"github.com/google/uuid"
	"golang.org/x/crypto/bcrypt"
)

type UserService struct {
	repo  repository.UserRepository
	rdb   redis.RedisRepository
	token authtoken.TokenManager
}

func NewUserService(repo repository.UserRepository, rdb redis.RedisRepository, token authtoken.TokenManager) *UserService {
	return &UserService{
		repo:  repo,
		rdb:   rdb,
		token: token,
	}
}

func (us *UserService) GetUser(email, password string) (string, error) {
	uuid := uuid.NewString()
	ctx, cancel := context.WithTimeout(context.Background(), 3*time.Second)
	defer cancel()

	user, err := us.repo.Get(email)

	if err != nil {
		return "", err
	}

	if err = bcrypt.CompareHashAndPassword([]byte(user.Password_hash), []byte(password)); err != nil {
		return "", err
	}

	tokenGen, err := us.token.GenerateToken(user.Username, uuid)
	if err != nil {
		return "", err
	}

	userData, err := json.Marshal(user)
	if err != nil {
		log.Printf("Ошибка сериализации пользователя: %v", err)
		return "", err
	}

	if err = us.rdb.SetData(ctx, uuid, userData, 3600); err != nil {
		log.Printf("Ошибка сохранения пользователя в Redis: %v", err)
		return "", err
	}

	return tokenGen, nil
}

func (us *UserService) CreateUser(name, email, password string) error {
	password_hash, err := bcrypt.GenerateFromPassword([]byte(password), bcrypt.DefaultCost)

	if err != nil {
		return err
	}

	user := &model.User{
		Username:      name,
		Email:         email,
		Password_hash: string(password_hash),
	}

	err = us.repo.Create(user)

	if err != nil {
		return err
	}

	return nil
}
