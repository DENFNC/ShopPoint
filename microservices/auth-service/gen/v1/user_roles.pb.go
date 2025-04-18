// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.36.6
// 	protoc        v3.21.12
// source: user_roles.proto

package v1

import (
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	emptypb "google.golang.org/protobuf/types/known/emptypb"
	timestamppb "google.golang.org/protobuf/types/known/timestamppb"
	reflect "reflect"
	sync "sync"
	unsafe "unsafe"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

// Запрос на назначение роли пользователю
type AssignRoleRequest struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	AuthUserUuid  int32                  `protobuf:"varint,1,opt,name=auth_user_uuid,json=authUserUuid,proto3" json:"auth_user_uuid,omitempty"`
	RoleName      int32                  `protobuf:"varint,2,opt,name=role_name,json=roleName,proto3" json:"role_name,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *AssignRoleRequest) Reset() {
	*x = AssignRoleRequest{}
	mi := &file_user_roles_proto_msgTypes[0]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *AssignRoleRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*AssignRoleRequest) ProtoMessage() {}

func (x *AssignRoleRequest) ProtoReflect() protoreflect.Message {
	mi := &file_user_roles_proto_msgTypes[0]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use AssignRoleRequest.ProtoReflect.Descriptor instead.
func (*AssignRoleRequest) Descriptor() ([]byte, []int) {
	return file_user_roles_proto_rawDescGZIP(), []int{0}
}

func (x *AssignRoleRequest) GetAuthUserUuid() int32 {
	if x != nil {
		return x.AuthUserUuid
	}
	return 0
}

func (x *AssignRoleRequest) GetRoleName() int32 {
	if x != nil {
		return x.RoleName
	}
	return 0
}

// Запрос на удаление роли у пользователя
type RemoveRoleRequest struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	AuthUserUuid  int32                  `protobuf:"varint,1,opt,name=auth_user_uuid,json=authUserUuid,proto3" json:"auth_user_uuid,omitempty"`
	RoleName      int32                  `protobuf:"varint,2,opt,name=role_name,json=roleName,proto3" json:"role_name,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *RemoveRoleRequest) Reset() {
	*x = RemoveRoleRequest{}
	mi := &file_user_roles_proto_msgTypes[1]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *RemoveRoleRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*RemoveRoleRequest) ProtoMessage() {}

func (x *RemoveRoleRequest) ProtoReflect() protoreflect.Message {
	mi := &file_user_roles_proto_msgTypes[1]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use RemoveRoleRequest.ProtoReflect.Descriptor instead.
func (*RemoveRoleRequest) Descriptor() ([]byte, []int) {
	return file_user_roles_proto_rawDescGZIP(), []int{1}
}

func (x *RemoveRoleRequest) GetAuthUserUuid() int32 {
	if x != nil {
		return x.AuthUserUuid
	}
	return 0
}

func (x *RemoveRoleRequest) GetRoleName() int32 {
	if x != nil {
		return x.RoleName
	}
	return 0
}

// Для получения списка ролей, назначенных пользователю,
// можно вернуть более подробную информацию о назначении.
type RoleAssignment struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	RoleId        int32                  `protobuf:"varint,1,opt,name=role_id,json=roleId,proto3" json:"role_id,omitempty"`
	RoleName      string                 `protobuf:"bytes,2,opt,name=role_name,json=roleName,proto3" json:"role_name,omitempty"`
	AssignedAt    *timestamppb.Timestamp `protobuf:"bytes,3,opt,name=assigned_at,json=assignedAt,proto3" json:"assigned_at,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *RoleAssignment) Reset() {
	*x = RoleAssignment{}
	mi := &file_user_roles_proto_msgTypes[2]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *RoleAssignment) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*RoleAssignment) ProtoMessage() {}

func (x *RoleAssignment) ProtoReflect() protoreflect.Message {
	mi := &file_user_roles_proto_msgTypes[2]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use RoleAssignment.ProtoReflect.Descriptor instead.
func (*RoleAssignment) Descriptor() ([]byte, []int) {
	return file_user_roles_proto_rawDescGZIP(), []int{2}
}

func (x *RoleAssignment) GetRoleId() int32 {
	if x != nil {
		return x.RoleId
	}
	return 0
}

func (x *RoleAssignment) GetRoleName() string {
	if x != nil {
		return x.RoleName
	}
	return ""
}

func (x *RoleAssignment) GetAssignedAt() *timestamppb.Timestamp {
	if x != nil {
		return x.AssignedAt
	}
	return nil
}

type ListUserRolesRequest struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	AuthUserId    int32                  `protobuf:"varint,1,opt,name=auth_user_id,json=authUserId,proto3" json:"auth_user_id,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *ListUserRolesRequest) Reset() {
	*x = ListUserRolesRequest{}
	mi := &file_user_roles_proto_msgTypes[3]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *ListUserRolesRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ListUserRolesRequest) ProtoMessage() {}

func (x *ListUserRolesRequest) ProtoReflect() protoreflect.Message {
	mi := &file_user_roles_proto_msgTypes[3]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ListUserRolesRequest.ProtoReflect.Descriptor instead.
func (*ListUserRolesRequest) Descriptor() ([]byte, []int) {
	return file_user_roles_proto_rawDescGZIP(), []int{3}
}

func (x *ListUserRolesRequest) GetAuthUserId() int32 {
	if x != nil {
		return x.AuthUserId
	}
	return 0
}

type ListUserRolesResponse struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	Assignments   []*RoleAssignment      `protobuf:"bytes,1,rep,name=assignments,proto3" json:"assignments,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *ListUserRolesResponse) Reset() {
	*x = ListUserRolesResponse{}
	mi := &file_user_roles_proto_msgTypes[4]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *ListUserRolesResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ListUserRolesResponse) ProtoMessage() {}

func (x *ListUserRolesResponse) ProtoReflect() protoreflect.Message {
	mi := &file_user_roles_proto_msgTypes[4]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ListUserRolesResponse.ProtoReflect.Descriptor instead.
func (*ListUserRolesResponse) Descriptor() ([]byte, []int) {
	return file_user_roles_proto_rawDescGZIP(), []int{4}
}

func (x *ListUserRolesResponse) GetAssignments() []*RoleAssignment {
	if x != nil {
		return x.Assignments
	}
	return nil
}

var File_user_roles_proto protoreflect.FileDescriptor

const file_user_roles_proto_rawDesc = "" +
	"\n" +
	"\x10user_roles.proto\x12\vuserrole.v1\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"V\n" +
	"\x11AssignRoleRequest\x12$\n" +
	"\x0eauth_user_uuid\x18\x01 \x01(\x05R\fauthUserUuid\x12\x1b\n" +
	"\trole_name\x18\x02 \x01(\x05R\broleName\"V\n" +
	"\x11RemoveRoleRequest\x12$\n" +
	"\x0eauth_user_uuid\x18\x01 \x01(\x05R\fauthUserUuid\x12\x1b\n" +
	"\trole_name\x18\x02 \x01(\x05R\broleName\"\x83\x01\n" +
	"\x0eRoleAssignment\x12\x17\n" +
	"\arole_id\x18\x01 \x01(\x05R\x06roleId\x12\x1b\n" +
	"\trole_name\x18\x02 \x01(\tR\broleName\x12;\n" +
	"\vassigned_at\x18\x03 \x01(\v2\x1a.google.protobuf.TimestampR\n" +
	"assignedAt\"8\n" +
	"\x14ListUserRolesRequest\x12 \n" +
	"\fauth_user_id\x18\x01 \x01(\x05R\n" +
	"authUserId\"V\n" +
	"\x15ListUserRolesResponse\x12=\n" +
	"\vassignments\x18\x01 \x03(\v2\x1b.userrole.v1.RoleAssignmentR\vassignments2\xf5\x01\n" +
	"\x0fUserRoleService\x12D\n" +
	"\n" +
	"AssignRole\x12\x1e.userrole.v1.AssignRoleRequest\x1a\x16.google.protobuf.Empty\x12D\n" +
	"\n" +
	"RemoveRole\x12\x1e.userrole.v1.RemoveRoleRequest\x1a\x16.google.protobuf.Empty\x12V\n" +
	"\rListUserRoles\x12!.userrole.v1.ListUserRolesRequest\x1a\".userrole.v1.ListUserRolesResponseB7Z5github.com/ShopPoint/auth-service/prot/v1/userrole;v1b\x06proto3"

var (
	file_user_roles_proto_rawDescOnce sync.Once
	file_user_roles_proto_rawDescData []byte
)

func file_user_roles_proto_rawDescGZIP() []byte {
	file_user_roles_proto_rawDescOnce.Do(func() {
		file_user_roles_proto_rawDescData = protoimpl.X.CompressGZIP(unsafe.Slice(unsafe.StringData(file_user_roles_proto_rawDesc), len(file_user_roles_proto_rawDesc)))
	})
	return file_user_roles_proto_rawDescData
}

var file_user_roles_proto_msgTypes = make([]protoimpl.MessageInfo, 5)
var file_user_roles_proto_goTypes = []any{
	(*AssignRoleRequest)(nil),     // 0: userrole.v1.AssignRoleRequest
	(*RemoveRoleRequest)(nil),     // 1: userrole.v1.RemoveRoleRequest
	(*RoleAssignment)(nil),        // 2: userrole.v1.RoleAssignment
	(*ListUserRolesRequest)(nil),  // 3: userrole.v1.ListUserRolesRequest
	(*ListUserRolesResponse)(nil), // 4: userrole.v1.ListUserRolesResponse
	(*timestamppb.Timestamp)(nil), // 5: google.protobuf.Timestamp
	(*emptypb.Empty)(nil),         // 6: google.protobuf.Empty
}
var file_user_roles_proto_depIdxs = []int32{
	5, // 0: userrole.v1.RoleAssignment.assigned_at:type_name -> google.protobuf.Timestamp
	2, // 1: userrole.v1.ListUserRolesResponse.assignments:type_name -> userrole.v1.RoleAssignment
	0, // 2: userrole.v1.UserRoleService.AssignRole:input_type -> userrole.v1.AssignRoleRequest
	1, // 3: userrole.v1.UserRoleService.RemoveRole:input_type -> userrole.v1.RemoveRoleRequest
	3, // 4: userrole.v1.UserRoleService.ListUserRoles:input_type -> userrole.v1.ListUserRolesRequest
	6, // 5: userrole.v1.UserRoleService.AssignRole:output_type -> google.protobuf.Empty
	6, // 6: userrole.v1.UserRoleService.RemoveRole:output_type -> google.protobuf.Empty
	4, // 7: userrole.v1.UserRoleService.ListUserRoles:output_type -> userrole.v1.ListUserRolesResponse
	5, // [5:8] is the sub-list for method output_type
	2, // [2:5] is the sub-list for method input_type
	2, // [2:2] is the sub-list for extension type_name
	2, // [2:2] is the sub-list for extension extendee
	0, // [0:2] is the sub-list for field type_name
}

func init() { file_user_roles_proto_init() }
func file_user_roles_proto_init() {
	if File_user_roles_proto != nil {
		return
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: unsafe.Slice(unsafe.StringData(file_user_roles_proto_rawDesc), len(file_user_roles_proto_rawDesc)),
			NumEnums:      0,
			NumMessages:   5,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_user_roles_proto_goTypes,
		DependencyIndexes: file_user_roles_proto_depIdxs,
		MessageInfos:      file_user_roles_proto_msgTypes,
	}.Build()
	File_user_roles_proto = out.File
	file_user_roles_proto_goTypes = nil
	file_user_roles_proto_depIdxs = nil
}
