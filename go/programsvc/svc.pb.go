// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.27.1
// 	protoc        v3.17.3
// source: programsvc/svc.proto

package programsvc

import (
	_ "github.com/envoyproxy/protoc-gen-validate/validate"
	program "go.autokitteh.dev/idl/go/program"
	_ "google.golang.org/genproto/googleapis/api/annotations"
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	timestamppb "google.golang.org/protobuf/types/known/timestamppb"
	reflect "reflect"
	sync "sync"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

type File struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Path      *program.Path          `protobuf:"bytes,1,opt,name=path,proto3" json:"path,omitempty"`
	Content   []byte                 `protobuf:"bytes,2,opt,name=content,proto3" json:"content,omitempty"`
	FetchedAt *timestamppb.Timestamp `protobuf:"bytes,3,opt,name=fetched_at,json=fetchedAt,proto3" json:"fetched_at,omitempty"`
}

func (x *File) Reset() {
	*x = File{}
	if protoimpl.UnsafeEnabled {
		mi := &file_programsvc_svc_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *File) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*File) ProtoMessage() {}

func (x *File) ProtoReflect() protoreflect.Message {
	mi := &file_programsvc_svc_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use File.ProtoReflect.Descriptor instead.
func (*File) Descriptor() ([]byte, []int) {
	return file_programsvc_svc_proto_rawDescGZIP(), []int{0}
}

func (x *File) GetPath() *program.Path {
	if x != nil {
		return x.Path
	}
	return nil
}

func (x *File) GetContent() []byte {
	if x != nil {
		return x.Content
	}
	return nil
}

func (x *File) GetFetchedAt() *timestamppb.Timestamp {
	if x != nil {
		return x.FetchedAt
	}
	return nil
}

// Update the program store.
// Will first try `files`. If `only_files` if false, will try to
// find the files itself.
type UpdateRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	ProjectId string        `protobuf:"bytes,1,opt,name=project_id,json=projectId,proto3" json:"project_id,omitempty"`
	MainPath  *program.Path `protobuf:"bytes,2,opt,name=main_path,json=mainPath,proto3" json:"main_path,omitempty"`
	Files     []*File       `protobuf:"bytes,3,rep,name=files,proto3" json:"files,omitempty"`
	OnlyFiles bool          `protobuf:"varint,4,opt,name=only_files,json=onlyFiles,proto3" json:"only_files,omitempty"` // do not try to fetch files that are not in `files`.
}

func (x *UpdateRequest) Reset() {
	*x = UpdateRequest{}
	if protoimpl.UnsafeEnabled {
		mi := &file_programsvc_svc_proto_msgTypes[1]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *UpdateRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*UpdateRequest) ProtoMessage() {}

func (x *UpdateRequest) ProtoReflect() protoreflect.Message {
	mi := &file_programsvc_svc_proto_msgTypes[1]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use UpdateRequest.ProtoReflect.Descriptor instead.
func (*UpdateRequest) Descriptor() ([]byte, []int) {
	return file_programsvc_svc_proto_rawDescGZIP(), []int{1}
}

func (x *UpdateRequest) GetProjectId() string {
	if x != nil {
		return x.ProjectId
	}
	return ""
}

func (x *UpdateRequest) GetMainPath() *program.Path {
	if x != nil {
		return x.MainPath
	}
	return nil
}

func (x *UpdateRequest) GetFiles() []*File {
	if x != nil {
		return x.Files
	}
	return nil
}

func (x *UpdateRequest) GetOnlyFiles() bool {
	if x != nil {
		return x.OnlyFiles
	}
	return false
}

type UpdateResponse struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields
}

func (x *UpdateResponse) Reset() {
	*x = UpdateResponse{}
	if protoimpl.UnsafeEnabled {
		mi := &file_programsvc_svc_proto_msgTypes[2]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *UpdateResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*UpdateResponse) ProtoMessage() {}

func (x *UpdateResponse) ProtoReflect() protoreflect.Message {
	mi := &file_programsvc_svc_proto_msgTypes[2]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use UpdateResponse.ProtoReflect.Descriptor instead.
func (*UpdateResponse) Descriptor() ([]byte, []int) {
	return file_programsvc_svc_proto_rawDescGZIP(), []int{2}
}

type GetRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	ProjectId string          `protobuf:"bytes,1,opt,name=project_id,json=projectId,proto3" json:"project_id,omitempty"`
	Paths     []*program.Path `protobuf:"bytes,2,rep,name=paths,proto3" json:"paths,omitempty"`
}

func (x *GetRequest) Reset() {
	*x = GetRequest{}
	if protoimpl.UnsafeEnabled {
		mi := &file_programsvc_svc_proto_msgTypes[3]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *GetRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*GetRequest) ProtoMessage() {}

func (x *GetRequest) ProtoReflect() protoreflect.Message {
	mi := &file_programsvc_svc_proto_msgTypes[3]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use GetRequest.ProtoReflect.Descriptor instead.
func (*GetRequest) Descriptor() ([]byte, []int) {
	return file_programsvc_svc_proto_rawDescGZIP(), []int{3}
}

func (x *GetRequest) GetProjectId() string {
	if x != nil {
		return x.ProjectId
	}
	return ""
}

func (x *GetRequest) GetPaths() []*program.Path {
	if x != nil {
		return x.Paths
	}
	return nil
}

type GetResponse struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Files     []*File `protobuf:"bytes,1,rep,name=files,proto3" json:"files,omitempty"`
	NoContent bool    `protobuf:"varint,2,opt,name=no_content,json=noContent,proto3" json:"no_content,omitempty"` // just list, don't fetch actual content.
}

func (x *GetResponse) Reset() {
	*x = GetResponse{}
	if protoimpl.UnsafeEnabled {
		mi := &file_programsvc_svc_proto_msgTypes[4]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *GetResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*GetResponse) ProtoMessage() {}

func (x *GetResponse) ProtoReflect() protoreflect.Message {
	mi := &file_programsvc_svc_proto_msgTypes[4]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use GetResponse.ProtoReflect.Descriptor instead.
func (*GetResponse) Descriptor() ([]byte, []int) {
	return file_programsvc_svc_proto_rawDescGZIP(), []int{4}
}

func (x *GetResponse) GetFiles() []*File {
	if x != nil {
		return x.Files
	}
	return nil
}

func (x *GetResponse) GetNoContent() bool {
	if x != nil {
		return x.NoContent
	}
	return false
}

var File_programsvc_svc_proto protoreflect.FileDescriptor

var file_programsvc_svc_proto_rawDesc = []byte{
	0x0a, 0x14, 0x70, 0x72, 0x6f, 0x67, 0x72, 0x61, 0x6d, 0x73, 0x76, 0x63, 0x2f, 0x73, 0x76, 0x63,
	0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x12, 0x15, 0x61, 0x75, 0x74, 0x6f, 0x6b, 0x69, 0x74, 0x74,
	0x65, 0x68, 0x2e, 0x70, 0x72, 0x6f, 0x67, 0x72, 0x61, 0x6d, 0x73, 0x76, 0x63, 0x1a, 0x1c, 0x67,
	0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x61, 0x6e, 0x6e, 0x6f, 0x74, 0x61,
	0x74, 0x69, 0x6f, 0x6e, 0x73, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x1f, 0x67, 0x6f, 0x6f,
	0x67, 0x6c, 0x65, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2f, 0x74, 0x69, 0x6d,
	0x65, 0x73, 0x74, 0x61, 0x6d, 0x70, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x17, 0x76, 0x61,
	0x6c, 0x69, 0x64, 0x61, 0x74, 0x65, 0x2f, 0x76, 0x61, 0x6c, 0x69, 0x64, 0x61, 0x74, 0x65, 0x2e,
	0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x15, 0x70, 0x72, 0x6f, 0x67, 0x72, 0x61, 0x6d, 0x2f, 0x70,
	0x72, 0x6f, 0x67, 0x72, 0x61, 0x6d, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x22, 0x89, 0x01, 0x0a,
	0x04, 0x46, 0x69, 0x6c, 0x65, 0x12, 0x2c, 0x0a, 0x04, 0x70, 0x61, 0x74, 0x68, 0x18, 0x01, 0x20,
	0x01, 0x28, 0x0b, 0x32, 0x18, 0x2e, 0x61, 0x75, 0x74, 0x6f, 0x6b, 0x69, 0x74, 0x74, 0x65, 0x68,
	0x2e, 0x70, 0x72, 0x6f, 0x67, 0x72, 0x61, 0x6d, 0x2e, 0x50, 0x61, 0x74, 0x68, 0x52, 0x04, 0x70,
	0x61, 0x74, 0x68, 0x12, 0x18, 0x0a, 0x07, 0x63, 0x6f, 0x6e, 0x74, 0x65, 0x6e, 0x74, 0x18, 0x02,
	0x20, 0x01, 0x28, 0x0c, 0x52, 0x07, 0x63, 0x6f, 0x6e, 0x74, 0x65, 0x6e, 0x74, 0x12, 0x39, 0x0a,
	0x0a, 0x66, 0x65, 0x74, 0x63, 0x68, 0x65, 0x64, 0x5f, 0x61, 0x74, 0x18, 0x03, 0x20, 0x01, 0x28,
	0x0b, 0x32, 0x1a, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f,
	0x62, 0x75, 0x66, 0x2e, 0x54, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d, 0x70, 0x52, 0x09, 0x66,
	0x65, 0x74, 0x63, 0x68, 0x65, 0x64, 0x41, 0x74, 0x22, 0xf7, 0x01, 0x0a, 0x0d, 0x55, 0x70, 0x64,
	0x61, 0x74, 0x65, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x12, 0x4e, 0x0a, 0x0a, 0x70, 0x72,
	0x6f, 0x6a, 0x65, 0x63, 0x74, 0x5f, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x42, 0x2f,
	0xfa, 0x42, 0x2c, 0x72, 0x2a, 0x32, 0x28, 0x5e, 0x5b, 0x61, 0x2d, 0x7a, 0x41, 0x2d, 0x5a, 0x5d,
	0x5b, 0x30, 0x2d, 0x39, 0x61, 0x2d, 0x7a, 0x41, 0x2d, 0x5a, 0x5f, 0x2d, 0x5d, 0x2b, 0x5c, 0x2e,
	0x5b, 0x61, 0x2d, 0x7a, 0x41, 0x2d, 0x5a, 0x30, 0x2d, 0x39, 0x5f, 0x2d, 0x5d, 0x2b, 0x24, 0x52,
	0x09, 0x70, 0x72, 0x6f, 0x6a, 0x65, 0x63, 0x74, 0x49, 0x64, 0x12, 0x35, 0x0a, 0x09, 0x6d, 0x61,
	0x69, 0x6e, 0x5f, 0x70, 0x61, 0x74, 0x68, 0x18, 0x02, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x18, 0x2e,
	0x61, 0x75, 0x74, 0x6f, 0x6b, 0x69, 0x74, 0x74, 0x65, 0x68, 0x2e, 0x70, 0x72, 0x6f, 0x67, 0x72,
	0x61, 0x6d, 0x2e, 0x50, 0x61, 0x74, 0x68, 0x52, 0x08, 0x6d, 0x61, 0x69, 0x6e, 0x50, 0x61, 0x74,
	0x68, 0x12, 0x40, 0x0a, 0x05, 0x66, 0x69, 0x6c, 0x65, 0x73, 0x18, 0x03, 0x20, 0x03, 0x28, 0x0b,
	0x32, 0x1b, 0x2e, 0x61, 0x75, 0x74, 0x6f, 0x6b, 0x69, 0x74, 0x74, 0x65, 0x68, 0x2e, 0x70, 0x72,
	0x6f, 0x67, 0x72, 0x61, 0x6d, 0x73, 0x76, 0x63, 0x2e, 0x46, 0x69, 0x6c, 0x65, 0x42, 0x0d, 0xfa,
	0x42, 0x0a, 0x92, 0x01, 0x07, 0x22, 0x05, 0x8a, 0x01, 0x02, 0x10, 0x01, 0x52, 0x05, 0x66, 0x69,
	0x6c, 0x65, 0x73, 0x12, 0x1d, 0x0a, 0x0a, 0x6f, 0x6e, 0x6c, 0x79, 0x5f, 0x66, 0x69, 0x6c, 0x65,
	0x73, 0x18, 0x04, 0x20, 0x01, 0x28, 0x08, 0x52, 0x09, 0x6f, 0x6e, 0x6c, 0x79, 0x46, 0x69, 0x6c,
	0x65, 0x73, 0x22, 0x10, 0x0a, 0x0e, 0x55, 0x70, 0x64, 0x61, 0x74, 0x65, 0x52, 0x65, 0x73, 0x70,
	0x6f, 0x6e, 0x73, 0x65, 0x22, 0x9b, 0x01, 0x0a, 0x0a, 0x47, 0x65, 0x74, 0x52, 0x65, 0x71, 0x75,
	0x65, 0x73, 0x74, 0x12, 0x4e, 0x0a, 0x0a, 0x70, 0x72, 0x6f, 0x6a, 0x65, 0x63, 0x74, 0x5f, 0x69,
	0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x42, 0x2f, 0xfa, 0x42, 0x2c, 0x72, 0x2a, 0x32, 0x28,
	0x5e, 0x5b, 0x61, 0x2d, 0x7a, 0x41, 0x2d, 0x5a, 0x5d, 0x5b, 0x30, 0x2d, 0x39, 0x61, 0x2d, 0x7a,
	0x41, 0x2d, 0x5a, 0x5f, 0x2d, 0x5d, 0x2b, 0x5c, 0x2e, 0x5b, 0x61, 0x2d, 0x7a, 0x41, 0x2d, 0x5a,
	0x30, 0x2d, 0x39, 0x5f, 0x2d, 0x5d, 0x2b, 0x24, 0x52, 0x09, 0x70, 0x72, 0x6f, 0x6a, 0x65, 0x63,
	0x74, 0x49, 0x64, 0x12, 0x3d, 0x0a, 0x05, 0x70, 0x61, 0x74, 0x68, 0x73, 0x18, 0x02, 0x20, 0x03,
	0x28, 0x0b, 0x32, 0x18, 0x2e, 0x61, 0x75, 0x74, 0x6f, 0x6b, 0x69, 0x74, 0x74, 0x65, 0x68, 0x2e,
	0x70, 0x72, 0x6f, 0x67, 0x72, 0x61, 0x6d, 0x2e, 0x50, 0x61, 0x74, 0x68, 0x42, 0x0d, 0xfa, 0x42,
	0x0a, 0x92, 0x01, 0x07, 0x22, 0x05, 0x8a, 0x01, 0x02, 0x10, 0x01, 0x52, 0x05, 0x70, 0x61, 0x74,
	0x68, 0x73, 0x22, 0x6e, 0x0a, 0x0b, 0x47, 0x65, 0x74, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73,
	0x65, 0x12, 0x40, 0x0a, 0x05, 0x66, 0x69, 0x6c, 0x65, 0x73, 0x18, 0x01, 0x20, 0x03, 0x28, 0x0b,
	0x32, 0x1b, 0x2e, 0x61, 0x75, 0x74, 0x6f, 0x6b, 0x69, 0x74, 0x74, 0x65, 0x68, 0x2e, 0x70, 0x72,
	0x6f, 0x67, 0x72, 0x61, 0x6d, 0x73, 0x76, 0x63, 0x2e, 0x46, 0x69, 0x6c, 0x65, 0x42, 0x0d, 0xfa,
	0x42, 0x0a, 0x92, 0x01, 0x07, 0x22, 0x05, 0x8a, 0x01, 0x02, 0x10, 0x01, 0x52, 0x05, 0x66, 0x69,
	0x6c, 0x65, 0x73, 0x12, 0x1d, 0x0a, 0x0a, 0x6e, 0x6f, 0x5f, 0x63, 0x6f, 0x6e, 0x74, 0x65, 0x6e,
	0x74, 0x18, 0x02, 0x20, 0x01, 0x28, 0x08, 0x52, 0x09, 0x6e, 0x6f, 0x43, 0x6f, 0x6e, 0x74, 0x65,
	0x6e, 0x74, 0x32, 0x80, 0x02, 0x0a, 0x08, 0x50, 0x72, 0x6f, 0x6a, 0x65, 0x63, 0x74, 0x73, 0x12,
	0x7f, 0x0a, 0x06, 0x55, 0x70, 0x64, 0x61, 0x74, 0x65, 0x12, 0x24, 0x2e, 0x61, 0x75, 0x74, 0x6f,
	0x6b, 0x69, 0x74, 0x74, 0x65, 0x68, 0x2e, 0x70, 0x72, 0x6f, 0x67, 0x72, 0x61, 0x6d, 0x73, 0x76,
	0x63, 0x2e, 0x55, 0x70, 0x64, 0x61, 0x74, 0x65, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a,
	0x25, 0x2e, 0x61, 0x75, 0x74, 0x6f, 0x6b, 0x69, 0x74, 0x74, 0x65, 0x68, 0x2e, 0x70, 0x72, 0x6f,
	0x67, 0x72, 0x61, 0x6d, 0x73, 0x76, 0x63, 0x2e, 0x55, 0x70, 0x64, 0x61, 0x74, 0x65, 0x52, 0x65,
	0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x22, 0x28, 0x82, 0xd3, 0xe4, 0x93, 0x02, 0x22, 0x22, 0x1d,
	0x2f, 0x61, 0x70, 0x69, 0x2f, 0x76, 0x31, 0x2f, 0x70, 0x72, 0x6f, 0x67, 0x72, 0x61, 0x6d, 0x73,
	0x2f, 0x7b, 0x70, 0x72, 0x6f, 0x6a, 0x65, 0x63, 0x74, 0x5f, 0x69, 0x64, 0x7d, 0x3a, 0x01, 0x2a,
	0x12, 0x73, 0x0a, 0x03, 0x47, 0x65, 0x74, 0x12, 0x21, 0x2e, 0x61, 0x75, 0x74, 0x6f, 0x6b, 0x69,
	0x74, 0x74, 0x65, 0x68, 0x2e, 0x70, 0x72, 0x6f, 0x67, 0x72, 0x61, 0x6d, 0x73, 0x76, 0x63, 0x2e,
	0x47, 0x65, 0x74, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x22, 0x2e, 0x61, 0x75, 0x74,
	0x6f, 0x6b, 0x69, 0x74, 0x74, 0x65, 0x68, 0x2e, 0x70, 0x72, 0x6f, 0x67, 0x72, 0x61, 0x6d, 0x73,
	0x76, 0x63, 0x2e, 0x47, 0x65, 0x74, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x22, 0x25,
	0x82, 0xd3, 0xe4, 0x93, 0x02, 0x1f, 0x22, 0x1d, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x76, 0x31, 0x2f,
	0x70, 0x72, 0x6f, 0x67, 0x72, 0x61, 0x6d, 0x73, 0x2f, 0x7b, 0x70, 0x72, 0x6f, 0x6a, 0x65, 0x63,
	0x74, 0x5f, 0x69, 0x64, 0x7d, 0x42, 0x25, 0x5a, 0x23, 0x67, 0x6f, 0x2e, 0x61, 0x75, 0x74, 0x6f,
	0x6b, 0x69, 0x74, 0x74, 0x65, 0x68, 0x2e, 0x64, 0x65, 0x76, 0x2f, 0x69, 0x64, 0x6c, 0x2f, 0x67,
	0x6f, 0x2f, 0x70, 0x72, 0x6f, 0x67, 0x72, 0x61, 0x6d, 0x73, 0x76, 0x63, 0x62, 0x06, 0x70, 0x72,
	0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_programsvc_svc_proto_rawDescOnce sync.Once
	file_programsvc_svc_proto_rawDescData = file_programsvc_svc_proto_rawDesc
)

func file_programsvc_svc_proto_rawDescGZIP() []byte {
	file_programsvc_svc_proto_rawDescOnce.Do(func() {
		file_programsvc_svc_proto_rawDescData = protoimpl.X.CompressGZIP(file_programsvc_svc_proto_rawDescData)
	})
	return file_programsvc_svc_proto_rawDescData
}

var file_programsvc_svc_proto_msgTypes = make([]protoimpl.MessageInfo, 5)
var file_programsvc_svc_proto_goTypes = []interface{}{
	(*File)(nil),                  // 0: autokitteh.programsvc.File
	(*UpdateRequest)(nil),         // 1: autokitteh.programsvc.UpdateRequest
	(*UpdateResponse)(nil),        // 2: autokitteh.programsvc.UpdateResponse
	(*GetRequest)(nil),            // 3: autokitteh.programsvc.GetRequest
	(*GetResponse)(nil),           // 4: autokitteh.programsvc.GetResponse
	(*program.Path)(nil),          // 5: autokitteh.program.Path
	(*timestamppb.Timestamp)(nil), // 6: google.protobuf.Timestamp
}
var file_programsvc_svc_proto_depIdxs = []int32{
	5, // 0: autokitteh.programsvc.File.path:type_name -> autokitteh.program.Path
	6, // 1: autokitteh.programsvc.File.fetched_at:type_name -> google.protobuf.Timestamp
	5, // 2: autokitteh.programsvc.UpdateRequest.main_path:type_name -> autokitteh.program.Path
	0, // 3: autokitteh.programsvc.UpdateRequest.files:type_name -> autokitteh.programsvc.File
	5, // 4: autokitteh.programsvc.GetRequest.paths:type_name -> autokitteh.program.Path
	0, // 5: autokitteh.programsvc.GetResponse.files:type_name -> autokitteh.programsvc.File
	1, // 6: autokitteh.programsvc.Projects.Update:input_type -> autokitteh.programsvc.UpdateRequest
	3, // 7: autokitteh.programsvc.Projects.Get:input_type -> autokitteh.programsvc.GetRequest
	2, // 8: autokitteh.programsvc.Projects.Update:output_type -> autokitteh.programsvc.UpdateResponse
	4, // 9: autokitteh.programsvc.Projects.Get:output_type -> autokitteh.programsvc.GetResponse
	8, // [8:10] is the sub-list for method output_type
	6, // [6:8] is the sub-list for method input_type
	6, // [6:6] is the sub-list for extension type_name
	6, // [6:6] is the sub-list for extension extendee
	0, // [0:6] is the sub-list for field type_name
}

func init() { file_programsvc_svc_proto_init() }
func file_programsvc_svc_proto_init() {
	if File_programsvc_svc_proto != nil {
		return
	}
	if !protoimpl.UnsafeEnabled {
		file_programsvc_svc_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*File); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_programsvc_svc_proto_msgTypes[1].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*UpdateRequest); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_programsvc_svc_proto_msgTypes[2].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*UpdateResponse); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_programsvc_svc_proto_msgTypes[3].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*GetRequest); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_programsvc_svc_proto_msgTypes[4].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*GetResponse); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_programsvc_svc_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   5,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_programsvc_svc_proto_goTypes,
		DependencyIndexes: file_programsvc_svc_proto_depIdxs,
		MessageInfos:      file_programsvc_svc_proto_msgTypes,
	}.Build()
	File_programsvc_svc_proto = out.File
	file_programsvc_svc_proto_rawDesc = nil
	file_programsvc_svc_proto_goTypes = nil
	file_programsvc_svc_proto_depIdxs = nil
}
