package repository

import (
	"auth/service/internal/model"

	"gorm.io/gorm"
)

type UserRepository interface {
	Get(email string) (*model.User, error)
	GetAll()
	Create(user *model.User) error
	Update()
	Delete()
}

type userRepository struct {
	db *gorm.DB
}

func NewUserRepository(db *gorm.DB) *userRepository {
	return &userRepository{db: db}
}

func (repo *userRepository) Get(email string) (*model.User, error) {
	var user *model.User

	result := repo.db.First(&user, "email = ?", email)

	if result.Error != nil {
		return nil, result.Error
	}

	return user, nil
}

func (repo *userRepository) GetAll() {}
func (repo *userRepository) Create(user *model.User) error {
	result := repo.db.Create(user)

	return result.Error
}

func (repo *userRepository) Update() {}

func (repo *userRepository) Delete() {}
