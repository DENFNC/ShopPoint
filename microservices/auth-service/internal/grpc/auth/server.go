package auth

import (
	v1 "github.com/ShopPoint/auth-service/gen/v1"
	"google.golang.org/grpc"
)

type serverAPI struct {
	v1.UnimplementedAuthServiceServer
}

func RegisterAPI(gRPC *grpc.Server) {
	v1.RegisterAuthServiceServer(gRPC, &serverAPI{})
}

// func (s *serverAPI) DeactivateUser(context.Context, *v1.GetUserRequest) (*emptypb.Empty, error) {
// 	return nil, nil
// }
// func (s *serverAPI) GetUser(context.Context, *v1.GetUserRequest) (*v1.User, error) {
// 	return nil, nil
// }
// func (s *serverAPI) Login(ctx context.Context, req *v1.LoginRequest) (*v1.LoginResponse, error) {
// 	return nil, nil
// }
// func (s *serverAPI) Register(ctx context.Context, req *v1.LoginRequest) (*emptypb.Empty, error) {
// 	return nil, nil
// }
// func (s *serverAPI) RenewToken(context.Context, *v1.RenewTokenRequest) (*v1.RenewTokenResponse, error) {
// 	return nil, nil
// }
// func (s *serverAPI) UpdateUser(context.Context, *v1.UpdateUserRequest) (*emptypb.Empty, error) {
// 	return nil, nil
// }
