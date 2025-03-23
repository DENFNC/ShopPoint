package main

import (
	"auth/service/config"
	"log"

	"github.com/golang-migrate/migrate/v4"
	_ "github.com/golang-migrate/migrate/v4/database/postgres"
	_ "github.com/golang-migrate/migrate/v4/source/file"
)

func main() {
	var config = config.LoadConfig("../.env")

	migrate, err := migrate.New(
		"file://C:/code/ShopPoint/microservices/auth-service/migrate/versions",
		config.DB.URL,
	)

	if err != nil {
		log.Fatal(err)
	}

	if err = migrate.Up(); err != nil {
		log.Fatal(err)
	}

	log.Println("Migration successful")
}
