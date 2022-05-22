// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.27.1
// 	protoc        v3.17.3
// source: eventsrc/src.proto

package eventsrc

import (
	_ "github.com/envoyproxy/protoc-gen-validate/validate"
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

type EventSourceSettings struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Enabled bool     `protobuf:"varint,1,opt,name=enabled,proto3" json:"enabled,omitempty"`
	Types   []string `protobuf:"bytes,2,rep,name=types,proto3" json:"types,omitempty"` // emitted event types.
}

func (x *EventSourceSettings) Reset() {
	*x = EventSourceSettings{}
	if protoimpl.UnsafeEnabled {
		mi := &file_eventsrc_src_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *EventSourceSettings) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*EventSourceSettings) ProtoMessage() {}

func (x *EventSourceSettings) ProtoReflect() protoreflect.Message {
	mi := &file_eventsrc_src_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use EventSourceSettings.ProtoReflect.Descriptor instead.
func (*EventSourceSettings) Descriptor() ([]byte, []int) {
	return file_eventsrc_src_proto_rawDescGZIP(), []int{0}
}

func (x *EventSourceSettings) GetEnabled() bool {
	if x != nil {
		return x.Enabled
	}
	return false
}

func (x *EventSourceSettings) GetTypes() []string {
	if x != nil {
		return x.Types
	}
	return nil
}

type EventSource struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Id        string                 `protobuf:"bytes,1,opt,name=id,proto3" json:"id,omitempty"`
	Settings  *EventSourceSettings   `protobuf:"bytes,3,opt,name=settings,proto3" json:"settings,omitempty"`
	CreatedAt *timestamppb.Timestamp `protobuf:"bytes,100,opt,name=created_at,json=createdAt,proto3" json:"created_at,omitempty"`
	UpdatedAt *timestamppb.Timestamp `protobuf:"bytes,101,opt,name=updated_at,json=updatedAt,proto3" json:"updated_at,omitempty"`
}

func (x *EventSource) Reset() {
	*x = EventSource{}
	if protoimpl.UnsafeEnabled {
		mi := &file_eventsrc_src_proto_msgTypes[1]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *EventSource) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*EventSource) ProtoMessage() {}

func (x *EventSource) ProtoReflect() protoreflect.Message {
	mi := &file_eventsrc_src_proto_msgTypes[1]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use EventSource.ProtoReflect.Descriptor instead.
func (*EventSource) Descriptor() ([]byte, []int) {
	return file_eventsrc_src_proto_rawDescGZIP(), []int{1}
}

func (x *EventSource) GetId() string {
	if x != nil {
		return x.Id
	}
	return ""
}

func (x *EventSource) GetSettings() *EventSourceSettings {
	if x != nil {
		return x.Settings
	}
	return nil
}

func (x *EventSource) GetCreatedAt() *timestamppb.Timestamp {
	if x != nil {
		return x.CreatedAt
	}
	return nil
}

func (x *EventSource) GetUpdatedAt() *timestamppb.Timestamp {
	if x != nil {
		return x.UpdatedAt
	}
	return nil
}

type EventSourceProjectBindingSettings struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Enabled bool `protobuf:"varint,1,opt,name=enabled,proto3" json:"enabled,omitempty"`
}

func (x *EventSourceProjectBindingSettings) Reset() {
	*x = EventSourceProjectBindingSettings{}
	if protoimpl.UnsafeEnabled {
		mi := &file_eventsrc_src_proto_msgTypes[2]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *EventSourceProjectBindingSettings) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*EventSourceProjectBindingSettings) ProtoMessage() {}

func (x *EventSourceProjectBindingSettings) ProtoReflect() protoreflect.Message {
	mi := &file_eventsrc_src_proto_msgTypes[2]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use EventSourceProjectBindingSettings.ProtoReflect.Descriptor instead.
func (*EventSourceProjectBindingSettings) Descriptor() ([]byte, []int) {
	return file_eventsrc_src_proto_rawDescGZIP(), []int{2}
}

func (x *EventSourceProjectBindingSettings) GetEnabled() bool {
	if x != nil {
		return x.Enabled
	}
	return false
}

// Need to negotiate with event source to determine if eligible to receive events.
// Essentially this should be carefully managed by the system and not the user
// to prevent unwanted projects getting events.
type EventSourceProjectBinding struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	SrcId            string                             `protobuf:"bytes,1,opt,name=src_id,json=srcId,proto3" json:"src_id,omitempty"`
	ProjectId        string                             `protobuf:"bytes,2,opt,name=project_id,json=projectId,proto3" json:"project_id,omitempty"`
	Name             string                             `protobuf:"bytes,3,opt,name=name,proto3" json:"name,omitempty"`                                                 // might not be set if not approved.
	AssociationToken string                             `protobuf:"bytes,4,opt,name=association_token,json=associationToken,proto3" json:"association_token,omitempty"` // "multicast group" set by source.
	SourceConfig     string                             `protobuf:"bytes,5,opt,name=source_config,json=sourceConfig,proto3" json:"source_config,omitempty"`             //                   set by source.
	Approved         bool                               `protobuf:"varint,6,opt,name=approved,proto3" json:"approved,omitempty"`
	Settings         *EventSourceProjectBindingSettings `protobuf:"bytes,10,opt,name=settings,proto3" json:"settings,omitempty"`
	CreatedAt        *timestamppb.Timestamp             `protobuf:"bytes,100,opt,name=created_at,json=createdAt,proto3" json:"created_at,omitempty"`
	UpdatedAt        *timestamppb.Timestamp             `protobuf:"bytes,101,opt,name=updated_at,json=updatedAt,proto3" json:"updated_at,omitempty"`
}

func (x *EventSourceProjectBinding) Reset() {
	*x = EventSourceProjectBinding{}
	if protoimpl.UnsafeEnabled {
		mi := &file_eventsrc_src_proto_msgTypes[3]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *EventSourceProjectBinding) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*EventSourceProjectBinding) ProtoMessage() {}

func (x *EventSourceProjectBinding) ProtoReflect() protoreflect.Message {
	mi := &file_eventsrc_src_proto_msgTypes[3]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use EventSourceProjectBinding.ProtoReflect.Descriptor instead.
func (*EventSourceProjectBinding) Descriptor() ([]byte, []int) {
	return file_eventsrc_src_proto_rawDescGZIP(), []int{3}
}

func (x *EventSourceProjectBinding) GetSrcId() string {
	if x != nil {
		return x.SrcId
	}
	return ""
}

func (x *EventSourceProjectBinding) GetProjectId() string {
	if x != nil {
		return x.ProjectId
	}
	return ""
}

func (x *EventSourceProjectBinding) GetName() string {
	if x != nil {
		return x.Name
	}
	return ""
}

func (x *EventSourceProjectBinding) GetAssociationToken() string {
	if x != nil {
		return x.AssociationToken
	}
	return ""
}

func (x *EventSourceProjectBinding) GetSourceConfig() string {
	if x != nil {
		return x.SourceConfig
	}
	return ""
}

func (x *EventSourceProjectBinding) GetApproved() bool {
	if x != nil {
		return x.Approved
	}
	return false
}

func (x *EventSourceProjectBinding) GetSettings() *EventSourceProjectBindingSettings {
	if x != nil {
		return x.Settings
	}
	return nil
}

func (x *EventSourceProjectBinding) GetCreatedAt() *timestamppb.Timestamp {
	if x != nil {
		return x.CreatedAt
	}
	return nil
}

func (x *EventSourceProjectBinding) GetUpdatedAt() *timestamppb.Timestamp {
	if x != nil {
		return x.UpdatedAt
	}
	return nil
}

var File_eventsrc_src_proto protoreflect.FileDescriptor

var file_eventsrc_src_proto_rawDesc = []byte{
	0x0a, 0x12, 0x65, 0x76, 0x65, 0x6e, 0x74, 0x73, 0x72, 0x63, 0x2f, 0x73, 0x72, 0x63, 0x2e, 0x70,
	0x72, 0x6f, 0x74, 0x6f, 0x12, 0x13, 0x61, 0x75, 0x74, 0x6f, 0x6b, 0x69, 0x74, 0x74, 0x65, 0x68,
	0x2e, 0x65, 0x76, 0x65, 0x6e, 0x74, 0x73, 0x72, 0x63, 0x1a, 0x1f, 0x67, 0x6f, 0x6f, 0x67, 0x6c,
	0x65, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2f, 0x74, 0x69, 0x6d, 0x65, 0x73,
	0x74, 0x61, 0x6d, 0x70, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x17, 0x76, 0x61, 0x6c, 0x69,
	0x64, 0x61, 0x74, 0x65, 0x2f, 0x76, 0x61, 0x6c, 0x69, 0x64, 0x61, 0x74, 0x65, 0x2e, 0x70, 0x72,
	0x6f, 0x74, 0x6f, 0x22, 0x45, 0x0a, 0x13, 0x45, 0x76, 0x65, 0x6e, 0x74, 0x53, 0x6f, 0x75, 0x72,
	0x63, 0x65, 0x53, 0x65, 0x74, 0x74, 0x69, 0x6e, 0x67, 0x73, 0x12, 0x18, 0x0a, 0x07, 0x65, 0x6e,
	0x61, 0x62, 0x6c, 0x65, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x08, 0x52, 0x07, 0x65, 0x6e, 0x61,
	0x62, 0x6c, 0x65, 0x64, 0x12, 0x14, 0x0a, 0x05, 0x74, 0x79, 0x70, 0x65, 0x73, 0x18, 0x02, 0x20,
	0x03, 0x28, 0x09, 0x52, 0x05, 0x74, 0x79, 0x70, 0x65, 0x73, 0x22, 0x92, 0x02, 0x0a, 0x0b, 0x45,
	0x76, 0x65, 0x6e, 0x74, 0x53, 0x6f, 0x75, 0x72, 0x63, 0x65, 0x12, 0x47, 0x0a, 0x02, 0x69, 0x64,
	0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x42, 0x37, 0xfa, 0x42, 0x34, 0x72, 0x32, 0x32, 0x30, 0x5e,
	0x5b, 0x61, 0x2d, 0x7a, 0x41, 0x2d, 0x5a, 0x5d, 0x5b, 0x30, 0x2d, 0x39, 0x61, 0x2d, 0x7a, 0x41,
	0x2d, 0x5a, 0x5f, 0x2d, 0x5d, 0x2b, 0x5c, 0x2e, 0x5b, 0x61, 0x2d, 0x7a, 0x41, 0x2d, 0x5a, 0x5d,
	0x5b, 0x30, 0x2d, 0x39, 0x61, 0x2d, 0x7a, 0x41, 0x2d, 0x5a, 0x5f, 0x2d, 0x5d, 0x2b, 0x24, 0x52,
	0x02, 0x69, 0x64, 0x12, 0x44, 0x0a, 0x08, 0x73, 0x65, 0x74, 0x74, 0x69, 0x6e, 0x67, 0x73, 0x18,
	0x03, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x28, 0x2e, 0x61, 0x75, 0x74, 0x6f, 0x6b, 0x69, 0x74, 0x74,
	0x65, 0x68, 0x2e, 0x65, 0x76, 0x65, 0x6e, 0x74, 0x73, 0x72, 0x63, 0x2e, 0x45, 0x76, 0x65, 0x6e,
	0x74, 0x53, 0x6f, 0x75, 0x72, 0x63, 0x65, 0x53, 0x65, 0x74, 0x74, 0x69, 0x6e, 0x67, 0x73, 0x52,
	0x08, 0x73, 0x65, 0x74, 0x74, 0x69, 0x6e, 0x67, 0x73, 0x12, 0x39, 0x0a, 0x0a, 0x63, 0x72, 0x65,
	0x61, 0x74, 0x65, 0x64, 0x5f, 0x61, 0x74, 0x18, 0x64, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x1a, 0x2e,
	0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2e,
	0x54, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d, 0x70, 0x52, 0x09, 0x63, 0x72, 0x65, 0x61, 0x74,
	0x65, 0x64, 0x41, 0x74, 0x12, 0x39, 0x0a, 0x0a, 0x75, 0x70, 0x64, 0x61, 0x74, 0x65, 0x64, 0x5f,
	0x61, 0x74, 0x18, 0x65, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x1a, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c,
	0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2e, 0x54, 0x69, 0x6d, 0x65, 0x73,
	0x74, 0x61, 0x6d, 0x70, 0x52, 0x09, 0x75, 0x70, 0x64, 0x61, 0x74, 0x65, 0x64, 0x41, 0x74, 0x22,
	0x3d, 0x0a, 0x21, 0x45, 0x76, 0x65, 0x6e, 0x74, 0x53, 0x6f, 0x75, 0x72, 0x63, 0x65, 0x50, 0x72,
	0x6f, 0x6a, 0x65, 0x63, 0x74, 0x42, 0x69, 0x6e, 0x64, 0x69, 0x6e, 0x67, 0x53, 0x65, 0x74, 0x74,
	0x69, 0x6e, 0x67, 0x73, 0x12, 0x18, 0x0a, 0x07, 0x65, 0x6e, 0x61, 0x62, 0x6c, 0x65, 0x64, 0x18,
	0x01, 0x20, 0x01, 0x28, 0x08, 0x52, 0x07, 0x65, 0x6e, 0x61, 0x62, 0x6c, 0x65, 0x64, 0x22, 0xab,
	0x04, 0x0a, 0x19, 0x45, 0x76, 0x65, 0x6e, 0x74, 0x53, 0x6f, 0x75, 0x72, 0x63, 0x65, 0x50, 0x72,
	0x6f, 0x6a, 0x65, 0x63, 0x74, 0x42, 0x69, 0x6e, 0x64, 0x69, 0x6e, 0x67, 0x12, 0x4e, 0x0a, 0x06,
	0x73, 0x72, 0x63, 0x5f, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x42, 0x37, 0xfa, 0x42,
	0x34, 0x72, 0x32, 0x32, 0x30, 0x5e, 0x5b, 0x61, 0x2d, 0x7a, 0x41, 0x2d, 0x5a, 0x5d, 0x5b, 0x30,
	0x2d, 0x39, 0x61, 0x2d, 0x7a, 0x41, 0x2d, 0x5a, 0x5f, 0x2d, 0x5d, 0x2b, 0x5c, 0x2e, 0x5b, 0x61,
	0x2d, 0x7a, 0x41, 0x2d, 0x5a, 0x5d, 0x5b, 0x30, 0x2d, 0x39, 0x61, 0x2d, 0x7a, 0x41, 0x2d, 0x5a,
	0x5f, 0x2d, 0x5d, 0x2b, 0x24, 0x52, 0x05, 0x73, 0x72, 0x63, 0x49, 0x64, 0x12, 0x4e, 0x0a, 0x0a,
	0x70, 0x72, 0x6f, 0x6a, 0x65, 0x63, 0x74, 0x5f, 0x69, 0x64, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09,
	0x42, 0x2f, 0xfa, 0x42, 0x2c, 0x72, 0x2a, 0x32, 0x28, 0x5e, 0x5b, 0x61, 0x2d, 0x7a, 0x41, 0x2d,
	0x5a, 0x5d, 0x5b, 0x30, 0x2d, 0x39, 0x61, 0x2d, 0x7a, 0x41, 0x2d, 0x5a, 0x5f, 0x2d, 0x5d, 0x2b,
	0x5c, 0x2e, 0x5b, 0x61, 0x2d, 0x7a, 0x41, 0x2d, 0x5a, 0x30, 0x2d, 0x39, 0x5f, 0x2d, 0x5d, 0x2b,
	0x24, 0x52, 0x09, 0x70, 0x72, 0x6f, 0x6a, 0x65, 0x63, 0x74, 0x49, 0x64, 0x12, 0x36, 0x0a, 0x04,
	0x6e, 0x61, 0x6d, 0x65, 0x18, 0x03, 0x20, 0x01, 0x28, 0x09, 0x42, 0x22, 0xfa, 0x42, 0x1f, 0x72,
	0x1d, 0x32, 0x18, 0x5e, 0x5b, 0x61, 0x2d, 0x7a, 0x41, 0x2d, 0x5a, 0x5f, 0x5d, 0x5b, 0x61, 0x2d,
	0x7a, 0x41, 0x2d, 0x5a, 0x30, 0x2d, 0x39, 0x5f, 0x5d, 0x2a, 0x24, 0xd0, 0x01, 0x01, 0x52, 0x04,
	0x6e, 0x61, 0x6d, 0x65, 0x12, 0x2b, 0x0a, 0x11, 0x61, 0x73, 0x73, 0x6f, 0x63, 0x69, 0x61, 0x74,
	0x69, 0x6f, 0x6e, 0x5f, 0x74, 0x6f, 0x6b, 0x65, 0x6e, 0x18, 0x04, 0x20, 0x01, 0x28, 0x09, 0x52,
	0x10, 0x61, 0x73, 0x73, 0x6f, 0x63, 0x69, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x54, 0x6f, 0x6b, 0x65,
	0x6e, 0x12, 0x23, 0x0a, 0x0d, 0x73, 0x6f, 0x75, 0x72, 0x63, 0x65, 0x5f, 0x63, 0x6f, 0x6e, 0x66,
	0x69, 0x67, 0x18, 0x05, 0x20, 0x01, 0x28, 0x09, 0x52, 0x0c, 0x73, 0x6f, 0x75, 0x72, 0x63, 0x65,
	0x43, 0x6f, 0x6e, 0x66, 0x69, 0x67, 0x12, 0x1a, 0x0a, 0x08, 0x61, 0x70, 0x70, 0x72, 0x6f, 0x76,
	0x65, 0x64, 0x18, 0x06, 0x20, 0x01, 0x28, 0x08, 0x52, 0x08, 0x61, 0x70, 0x70, 0x72, 0x6f, 0x76,
	0x65, 0x64, 0x12, 0x52, 0x0a, 0x08, 0x73, 0x65, 0x74, 0x74, 0x69, 0x6e, 0x67, 0x73, 0x18, 0x0a,
	0x20, 0x01, 0x28, 0x0b, 0x32, 0x36, 0x2e, 0x61, 0x75, 0x74, 0x6f, 0x6b, 0x69, 0x74, 0x74, 0x65,
	0x68, 0x2e, 0x65, 0x76, 0x65, 0x6e, 0x74, 0x73, 0x72, 0x63, 0x2e, 0x45, 0x76, 0x65, 0x6e, 0x74,
	0x53, 0x6f, 0x75, 0x72, 0x63, 0x65, 0x50, 0x72, 0x6f, 0x6a, 0x65, 0x63, 0x74, 0x42, 0x69, 0x6e,
	0x64, 0x69, 0x6e, 0x67, 0x53, 0x65, 0x74, 0x74, 0x69, 0x6e, 0x67, 0x73, 0x52, 0x08, 0x73, 0x65,
	0x74, 0x74, 0x69, 0x6e, 0x67, 0x73, 0x12, 0x39, 0x0a, 0x0a, 0x63, 0x72, 0x65, 0x61, 0x74, 0x65,
	0x64, 0x5f, 0x61, 0x74, 0x18, 0x64, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x1a, 0x2e, 0x67, 0x6f, 0x6f,
	0x67, 0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2e, 0x54, 0x69, 0x6d,
	0x65, 0x73, 0x74, 0x61, 0x6d, 0x70, 0x52, 0x09, 0x63, 0x72, 0x65, 0x61, 0x74, 0x65, 0x64, 0x41,
	0x74, 0x12, 0x39, 0x0a, 0x0a, 0x75, 0x70, 0x64, 0x61, 0x74, 0x65, 0x64, 0x5f, 0x61, 0x74, 0x18,
	0x65, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x1a, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x70,
	0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2e, 0x54, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d,
	0x70, 0x52, 0x09, 0x75, 0x70, 0x64, 0x61, 0x74, 0x65, 0x64, 0x41, 0x74, 0x42, 0x23, 0x5a, 0x21,
	0x67, 0x6f, 0x2e, 0x61, 0x75, 0x74, 0x6f, 0x6b, 0x69, 0x74, 0x74, 0x65, 0x68, 0x2e, 0x64, 0x65,
	0x76, 0x2f, 0x69, 0x64, 0x6c, 0x2f, 0x67, 0x6f, 0x2f, 0x65, 0x76, 0x65, 0x6e, 0x74, 0x73, 0x72,
	0x63, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_eventsrc_src_proto_rawDescOnce sync.Once
	file_eventsrc_src_proto_rawDescData = file_eventsrc_src_proto_rawDesc
)

func file_eventsrc_src_proto_rawDescGZIP() []byte {
	file_eventsrc_src_proto_rawDescOnce.Do(func() {
		file_eventsrc_src_proto_rawDescData = protoimpl.X.CompressGZIP(file_eventsrc_src_proto_rawDescData)
	})
	return file_eventsrc_src_proto_rawDescData
}

var file_eventsrc_src_proto_msgTypes = make([]protoimpl.MessageInfo, 4)
var file_eventsrc_src_proto_goTypes = []interface{}{
	(*EventSourceSettings)(nil),               // 0: autokitteh.eventsrc.EventSourceSettings
	(*EventSource)(nil),                       // 1: autokitteh.eventsrc.EventSource
	(*EventSourceProjectBindingSettings)(nil), // 2: autokitteh.eventsrc.EventSourceProjectBindingSettings
	(*EventSourceProjectBinding)(nil),         // 3: autokitteh.eventsrc.EventSourceProjectBinding
	(*timestamppb.Timestamp)(nil),             // 4: google.protobuf.Timestamp
}
var file_eventsrc_src_proto_depIdxs = []int32{
	0, // 0: autokitteh.eventsrc.EventSource.settings:type_name -> autokitteh.eventsrc.EventSourceSettings
	4, // 1: autokitteh.eventsrc.EventSource.created_at:type_name -> google.protobuf.Timestamp
	4, // 2: autokitteh.eventsrc.EventSource.updated_at:type_name -> google.protobuf.Timestamp
	2, // 3: autokitteh.eventsrc.EventSourceProjectBinding.settings:type_name -> autokitteh.eventsrc.EventSourceProjectBindingSettings
	4, // 4: autokitteh.eventsrc.EventSourceProjectBinding.created_at:type_name -> google.protobuf.Timestamp
	4, // 5: autokitteh.eventsrc.EventSourceProjectBinding.updated_at:type_name -> google.protobuf.Timestamp
	6, // [6:6] is the sub-list for method output_type
	6, // [6:6] is the sub-list for method input_type
	6, // [6:6] is the sub-list for extension type_name
	6, // [6:6] is the sub-list for extension extendee
	0, // [0:6] is the sub-list for field type_name
}

func init() { file_eventsrc_src_proto_init() }
func file_eventsrc_src_proto_init() {
	if File_eventsrc_src_proto != nil {
		return
	}
	if !protoimpl.UnsafeEnabled {
		file_eventsrc_src_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*EventSourceSettings); i {
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
		file_eventsrc_src_proto_msgTypes[1].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*EventSource); i {
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
		file_eventsrc_src_proto_msgTypes[2].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*EventSourceProjectBindingSettings); i {
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
		file_eventsrc_src_proto_msgTypes[3].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*EventSourceProjectBinding); i {
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
			RawDescriptor: file_eventsrc_src_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   4,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_eventsrc_src_proto_goTypes,
		DependencyIndexes: file_eventsrc_src_proto_depIdxs,
		MessageInfos:      file_eventsrc_src_proto_msgTypes,
	}.Build()
	File_eventsrc_src_proto = out.File
	file_eventsrc_src_proto_rawDesc = nil
	file_eventsrc_src_proto_goTypes = nil
	file_eventsrc_src_proto_depIdxs = nil
}