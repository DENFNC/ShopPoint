package main

import (
	"auth/service/config"
	"auth/service/internal/handler"
	"auth/service/internal/repository"
	"auth/service/internal/service"
	db "auth/service/pkg/storage"
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

	// Репозиторий
	userRepo := repository.NewUserRepository(conn)

	// Сервисы
	userService := service.NewUserService(userRepo)

	// Обработчики
	handler.NewAuthUserHandler(router, *userService)

	// Запуск сервера

	server := &http.Server{
		Addr:    ":8080",
		Handler: router,
	}

	server.ListenAndServe()
}
