package config

import (
	"os"

	"github.com/joho/godotenv"
)

type Config struct {
	Server *ServerConfig
}

type ServerConfig struct {
	Addr string
}

func LoadConfig(filepath string) (*Config, error) {
	if err := godotenv.Load(filepath); err != nil {
		return nil, err
	}

	return &Config{
		Server: &ServerConfig{
			Addr: os.Getenv("SERVER_ADDR"),
		},
	}, nil
}
