package db

import (
	"gorm.io/driver/postgres"
	"gorm.io/gorm"
)

type Database interface {
	Connect() (*gorm.DB, error)
}

type PostgresDB struct {
	DSN string
}

func (db *PostgresDB) Connect() (*gorm.DB, error) {
	conn, err := gorm.Open(postgres.Open(db.DSN))

	if err != nil {
		return nil, err
	}

	return conn, nil
}

// func NewDB(db Database) (*gorm.DB, error) {
// 	conn, err := db.Connect()

// 	if err != nil {
// 		return nil, err
// 	}

// 	return conn, nil
// }
