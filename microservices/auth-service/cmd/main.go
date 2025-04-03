package main

import (
	"log"

	"github.com/ShopPoint/auth-service/internal/app"
)

func main() {
	application, err := app.New(8080)
	if err != nil {
		log.Println(err)
	}

	application.GRPCServer.Run()
}
