package model

import "time"

type User struct {
	ID            int64     `gorm:"primaryKey"`
	Username      string    `gorm:"unique,not null"`
	Email         string    `gorm:"unique,not null"`
	Password_hash string    `gorm:"not null"`
	CreatedAt     time.Time `gorm:"autoCreateTime "`
	UpdatedAt     time.Time `gorm:"autoUpdateTime"`
}

type Role struct {
	ID        int64     `gorm:"primaryKey"`
	Name      string    `gorm:"unique,not null"`
	CreatedAt time.Time `gorm:"autoCreateTime"`
}

type UserRole struct {
	UserID     int64     `gorm:"primaryKey"`
	RoleID     int64     `gorm:"primaryKey"`
	AssignedAt time.Time `gorm:"autoCreateTime"`
}
