// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.5.1
// - protoc             v3.21.12
// source: user_roles.proto

package v1

import (
	context "context"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
	emptypb "google.golang.org/protobuf/types/known/emptypb"
)

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
// Requires gRPC-Go v1.64.0 or later.
const _ = grpc.SupportPackageIsVersion9

const (
	UserRoleService_AssignRole_FullMethodName    = "/userrole.v1.UserRoleService/AssignRole"
	UserRoleService_RemoveRole_FullMethodName    = "/userrole.v1.UserRoleService/RemoveRole"
	UserRoleService_ListUserRoles_FullMethodName = "/userrole.v1.UserRoleService/ListUserRoles"
)

// UserRoleServiceClient is the client API for UserRoleService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
//
// Сервис для работы с назначением ролей пользователям
type UserRoleServiceClient interface {
	AssignRole(ctx context.Context, in *AssignRoleRequest, opts ...grpc.CallOption) (*emptypb.Empty, error)
	RemoveRole(ctx context.Context, in *RemoveRoleRequest, opts ...grpc.CallOption) (*emptypb.Empty, error)
	ListUserRoles(ctx context.Context, in *ListUserRolesRequest, opts ...grpc.CallOption) (*ListUserRolesResponse, error)
}

type userRoleServiceClient struct {
	cc grpc.ClientConnInterface
}

func NewUserRoleServiceClient(cc grpc.ClientConnInterface) UserRoleServiceClient {
	return &userRoleServiceClient{cc}
}

func (c *userRoleServiceClient) AssignRole(ctx context.Context, in *AssignRoleRequest, opts ...grpc.CallOption) (*emptypb.Empty, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(emptypb.Empty)
	err := c.cc.Invoke(ctx, UserRoleService_AssignRole_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *userRoleServiceClient) RemoveRole(ctx context.Context, in *RemoveRoleRequest, opts ...grpc.CallOption) (*emptypb.Empty, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(emptypb.Empty)
	err := c.cc.Invoke(ctx, UserRoleService_RemoveRole_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *userRoleServiceClient) ListUserRoles(ctx context.Context, in *ListUserRolesRequest, opts ...grpc.CallOption) (*ListUserRolesResponse, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(ListUserRolesResponse)
	err := c.cc.Invoke(ctx, UserRoleService_ListUserRoles_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// UserRoleServiceServer is the server API for UserRoleService service.
// All implementations must embed UnimplementedUserRoleServiceServer
// for forward compatibility.
//
// Сервис для работы с назначением ролей пользователям
type UserRoleServiceServer interface {
	AssignRole(context.Context, *AssignRoleRequest) (*emptypb.Empty, error)
	RemoveRole(context.Context, *RemoveRoleRequest) (*emptypb.Empty, error)
	ListUserRoles(context.Context, *ListUserRolesRequest) (*ListUserRolesResponse, error)
	mustEmbedUnimplementedUserRoleServiceServer()
}

// UnimplementedUserRoleServiceServer must be embedded to have
// forward compatible implementations.
//
// NOTE: this should be embedded by value instead of pointer to avoid a nil
// pointer dereference when methods are called.
type UnimplementedUserRoleServiceServer struct{}

func (UnimplementedUserRoleServiceServer) AssignRole(context.Context, *AssignRoleRequest) (*emptypb.Empty, error) {
	return nil, status.Errorf(codes.Unimplemented, "method AssignRole not implemented")
}
func (UnimplementedUserRoleServiceServer) RemoveRole(context.Context, *RemoveRoleRequest) (*emptypb.Empty, error) {
	return nil, status.Errorf(codes.Unimplemented, "method RemoveRole not implemented")
}
func (UnimplementedUserRoleServiceServer) ListUserRoles(context.Context, *ListUserRolesRequest) (*ListUserRolesResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ListUserRoles not implemented")
}
func (UnimplementedUserRoleServiceServer) mustEmbedUnimplementedUserRoleServiceServer() {}
func (UnimplementedUserRoleServiceServer) testEmbeddedByValue()                         {}

// UnsafeUserRoleServiceServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to UserRoleServiceServer will
// result in compilation errors.
type UnsafeUserRoleServiceServer interface {
	mustEmbedUnimplementedUserRoleServiceServer()
}

func RegisterUserRoleServiceServer(s grpc.ServiceRegistrar, srv UserRoleServiceServer) {
	// If the following call pancis, it indicates UnimplementedUserRoleServiceServer was
	// embedded by pointer and is nil.  This will cause panics if an
	// unimplemented method is ever invoked, so we test this at initialization
	// time to prevent it from happening at runtime later due to I/O.
	if t, ok := srv.(interface{ testEmbeddedByValue() }); ok {
		t.testEmbeddedByValue()
	}
	s.RegisterService(&UserRoleService_ServiceDesc, srv)
}

func _UserRoleService_AssignRole_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(AssignRoleRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(UserRoleServiceServer).AssignRole(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: UserRoleService_AssignRole_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(UserRoleServiceServer).AssignRole(ctx, req.(*AssignRoleRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _UserRoleService_RemoveRole_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(RemoveRoleRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(UserRoleServiceServer).RemoveRole(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: UserRoleService_RemoveRole_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(UserRoleServiceServer).RemoveRole(ctx, req.(*RemoveRoleRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _UserRoleService_ListUserRoles_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ListUserRolesRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(UserRoleServiceServer).ListUserRoles(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: UserRoleService_ListUserRoles_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(UserRoleServiceServer).ListUserRoles(ctx, req.(*ListUserRolesRequest))
	}
	return interceptor(ctx, in, info, handler)
}

// UserRoleService_ServiceDesc is the grpc.ServiceDesc for UserRoleService service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var UserRoleService_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "userrole.v1.UserRoleService",
	HandlerType: (*UserRoleServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "AssignRole",
			Handler:    _UserRoleService_AssignRole_Handler,
		},
		{
			MethodName: "RemoveRole",
			Handler:    _UserRoleService_RemoveRole_Handler,
		},
		{
			MethodName: "ListUserRoles",
			Handler:    _UserRoleService_ListUserRoles_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "user_roles.proto",
}
