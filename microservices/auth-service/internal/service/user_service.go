package service

import (
	"auth/service/internal/model"
	"auth/service/internal/repository"

	"golang.org/x/crypto/bcrypt"
)

type UserService struct {
	repo repository.UserRepository
}

func NewUserService(repo repository.UserRepository) *UserService {
	return &UserService{repo: repo}
}

func (us *UserService) GetUser(email, password string) (*model.User, error) {
	user, err := us.repo.Get(email)

	if err != nil {
		return nil, err
	}

	if err = bcrypt.CompareHashAndPassword([]byte(user.Password_hash), []byte(password)); err != nil {
		return nil, err
	}

	return user, nil
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
