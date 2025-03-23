package config

import (
	"log"
	"os"

	"github.com/joho/godotenv"
)

type Config struct {
	DB *PostgresDB
}

type PostgresDB struct {
	DSN string
	URL string
}

func LoadConfig(path string) *Config {
	if err := godotenv.Load(path); err != nil {
		log.Fatal(err)
		return nil
	}

	config := &Config{
		DB: &PostgresDB{
			DSN: os.Getenv("POSTGRES_DSN"),
			URL: os.Getenv("POSTGRES_URL"),
		},
	}

	return config
}
