package main

import (
	"auth/service/config"
	"auth/service/internal/handler"
	"auth/service/internal/repository"
	"auth/service/internal/service"
	"auth/service/pkg/jwt-service/authtoken"
	"auth/service/pkg/jwt-service/keys"
	"auth/service/pkg/redis"
	db "auth/service/pkg/storage"
	"log"
	"net/http"
)

func main() {
	config := config.LoadConfig("../.env")
	router := http.NewServeMux()
	psql := db.PostgresDB{
		DSN: config.DB.DSN,
	}

	conn, err := psql.Connect()

	if err != nil {
		panic(err)
	}

	rdb := &redis.Client{
		Config: config,
	}

	if err := rdb.Connect(0); err != nil {
		log.Fatal(err)
	}

	privKey, err := keys.LoadPrivateKey("../config/keys/private.pem")
	if err != nil {
		log.Fatal(err)
	}

	pubKey, err := keys.LoadPublicKey("../config/keys/public.pem")
	if err != nil {
		log.Fatal(err)
	}

	tokenGen := authtoken.TokenManager{
		PrivateKey: privKey,
		PublicKey:  pubKey,
	}

	// Репозиторий
	userRepo := repository.NewUserRepository(conn)
	redisRepo := redis.NewRedisRepository(rdb)

	// Сервисы
	userService := service.NewUserService(userRepo, *redisRepo, tokenGen)

	// Обработчики
	handler.NewAuthUserHandler(router, *userService)

	// Запуск сервера

	server := &http.Server{
		Addr:    "localhost:8080",
		Handler: router,
	}

	log.Println("Server stated URL:", server.Addr)
	server.ListenAndServe()
}
