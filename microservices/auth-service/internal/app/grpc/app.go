package grpc

import (
	"fmt"
	"net"

	"github.com/ShopPoint/auth-service/internal/grpc/auth"
	"google.golang.org/grpc"
)

type App struct {
	gRPCServer *grpc.Server
	port       int
}

func NewServer(port int) (*App, error) {
	gRPCServer := grpc.NewServer()

	auth.RegisterAPI(gRPCServer)

	return &App{
		gRPCServer: gRPCServer,
		port:       port,
	}, nil
}

func (a *App) Run() error {
	listen, err := net.Listen("tcp", fmt.Sprintf(":%d", a.port))
	if err != nil {
		return fmt.Errorf("failed to listen: %v", err)
	}

	fmt.Printf("Server is running on port %d...\n", a.port)

	if err = a.gRPCServer.Serve(listen); err != nil {
		return err
	}

	return nil
}

func (a *App) Stop() {
	a.gRPCServer.GracefulStop()
}
