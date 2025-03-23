package config

import (
	"log"
	"os"

	"github.com/joho/godotenv"
)

type Config struct {
	DB    *PostgresDB
	Redis *RedisConfig
}

type PostgresDB struct {
	DSN string
	URL string
}

type RedisConfig struct {
	Addr     string
	Username string
	Password string
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
		Redis: &RedisConfig{
			Addr:     os.Getenv("REDIS_ADDR"),
			Password: os.Getenv("REDIS_PASS"),
		},
	}

	return config
}
