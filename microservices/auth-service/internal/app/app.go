package app

import (
	grpcapp "github.com/ShopPoint/auth-service/internal/app/grpc"
)

type App struct {
	GRPCServer *grpcapp.App
	port       int
}

func New(port int) (*App, error) {
	grpcServer, err := grpcapp.NewServer(port)
	if err != nil {
		return nil, err
	}

	return &App{
		GRPCServer: grpcServer,
		port:       port,
	}, nil
}
