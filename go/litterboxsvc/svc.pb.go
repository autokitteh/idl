// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.27.1
// 	protoc        v3.17.3
// source: litterboxsvc/svc.proto

package litterboxsvc

import (
	_ "github.com/envoyproxy/protoc-gen-validate/validate"
	lang "go.autokitteh.dev/idl/go/lang"
	values "go.autokitteh.dev/idl/go/values"
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

type SetupRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields
}

func (x *SetupRequest) Reset() {
	*x = SetupRequest{}
	if protoimpl.UnsafeEnabled {
		mi := &file_litterboxsvc_svc_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *SetupRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SetupRequest) ProtoMessage() {}

func (x *SetupRequest) ProtoReflect() protoreflect.Message {
	mi := &file_litterboxsvc_svc_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SetupRequest.ProtoReflect.Descriptor instead.
func (*SetupRequest) Descriptor() ([]byte, []int) {
	return file_litterboxsvc_svc_proto_rawDescGZIP(), []int{0}
}

type SetupResponse struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Id string `protobuf:"bytes,1,opt,name=id,proto3" json:"id,omitempty"`
}

func (x *SetupResponse) Reset() {
	*x = SetupResponse{}
	if protoimpl.UnsafeEnabled {
		mi := &file_litterboxsvc_svc_proto_msgTypes[1]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *SetupResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SetupResponse) ProtoMessage() {}

func (x *SetupResponse) ProtoReflect() protoreflect.Message {
	mi := &file_litterboxsvc_svc_proto_msgTypes[1]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SetupResponse.ProtoReflect.Descriptor instead.
func (*SetupResponse) Descriptor() ([]byte, []int) {
	return file_litterboxsvc_svc_proto_rawDescGZIP(), []int{1}
}

func (x *SetupResponse) GetId() string {
	if x != nil {
		return x.Id
	}
	return ""
}

type ScoopRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Id string `protobuf:"bytes,1,opt,name=id,proto3" json:"id,omitempty"`
}

func (x *ScoopRequest) Reset() {
	*x = ScoopRequest{}
	if protoimpl.UnsafeEnabled {
		mi := &file_litterboxsvc_svc_proto_msgTypes[2]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *ScoopRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ScoopRequest) ProtoMessage() {}

func (x *ScoopRequest) ProtoReflect() protoreflect.Message {
	mi := &file_litterboxsvc_svc_proto_msgTypes[2]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ScoopRequest.ProtoReflect.Descriptor instead.
func (*ScoopRequest) Descriptor() ([]byte, []int) {
	return file_litterboxsvc_svc_proto_rawDescGZIP(), []int{2}
}

func (x *ScoopRequest) GetId() string {
	if x != nil {
		return x.Id
	}
	return ""
}

type ScoopResponse struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields
}

func (x *ScoopResponse) Reset() {
	*x = ScoopResponse{}
	if protoimpl.UnsafeEnabled {
		mi := &file_litterboxsvc_svc_proto_msgTypes[3]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *ScoopResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ScoopResponse) ProtoMessage() {}

func (x *ScoopResponse) ProtoReflect() protoreflect.Message {
	mi := &file_litterboxsvc_svc_proto_msgTypes[3]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ScoopResponse.ProtoReflect.Descriptor instead.
func (*ScoopResponse) Descriptor() ([]byte, []int) {
	return file_litterboxsvc_svc_proto_rawDescGZIP(), []int{3}
}

type SyntheticEvent struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	SrcBinding string                   `protobuf:"bytes,1,opt,name=src_binding,json=srcBinding,proto3" json:"src_binding,omitempty"`
	Type       string                   `protobuf:"bytes,2,opt,name=type,proto3" json:"type,omitempty"`
	Data       map[string]*values.Value `protobuf:"bytes,3,rep,name=data,proto3" json:"data,omitempty" protobuf_key:"bytes,1,opt,name=key,proto3" protobuf_val:"bytes,2,opt,name=value,proto3"`
	OriginalId string                   `protobuf:"bytes,4,opt,name=original_id,json=originalId,proto3" json:"original_id,omitempty"`
}

func (x *SyntheticEvent) Reset() {
	*x = SyntheticEvent{}
	if protoimpl.UnsafeEnabled {
		mi := &file_litterboxsvc_svc_proto_msgTypes[4]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *SyntheticEvent) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SyntheticEvent) ProtoMessage() {}

func (x *SyntheticEvent) ProtoReflect() protoreflect.Message {
	mi := &file_litterboxsvc_svc_proto_msgTypes[4]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SyntheticEvent.ProtoReflect.Descriptor instead.
func (*SyntheticEvent) Descriptor() ([]byte, []int) {
	return file_litterboxsvc_svc_proto_rawDescGZIP(), []int{4}
}

func (x *SyntheticEvent) GetSrcBinding() string {
	if x != nil {
		return x.SrcBinding
	}
	return ""
}

func (x *SyntheticEvent) GetType() string {
	if x != nil {
		return x.Type
	}
	return ""
}

func (x *SyntheticEvent) GetData() map[string]*values.Value {
	if x != nil {
		return x.Data
	}
	return nil
}

func (x *SyntheticEvent) GetOriginalId() string {
	if x != nil {
		return x.OriginalId
	}
	return ""
}

type RunRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// If id is empty, run will setup, use and scoop the litterbox by itself.
	Id     string          `protobuf:"bytes,1,opt,name=id,proto3" json:"id,omitempty"`
	Source string          `protobuf:"bytes,2,opt,name=source,proto3" json:"source,omitempty"`
	Event  *SyntheticEvent `protobuf:"bytes,3,opt,name=event,proto3" json:"event,omitempty"`
}

func (x *RunRequest) Reset() {
	*x = RunRequest{}
	if protoimpl.UnsafeEnabled {
		mi := &file_litterboxsvc_svc_proto_msgTypes[5]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *RunRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*RunRequest) ProtoMessage() {}

func (x *RunRequest) ProtoReflect() protoreflect.Message {
	mi := &file_litterboxsvc_svc_proto_msgTypes[5]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use RunRequest.ProtoReflect.Descriptor instead.
func (*RunRequest) Descriptor() ([]byte, []int) {
	return file_litterboxsvc_svc_proto_rawDescGZIP(), []int{5}
}

func (x *RunRequest) GetId() string {
	if x != nil {
		return x.Id
	}
	return ""
}

func (x *RunRequest) GetSource() string {
	if x != nil {
		return x.Source
	}
	return ""
}

func (x *RunRequest) GetEvent() *SyntheticEvent {
	if x != nil {
		return x.Event
	}
	return nil
}

type RunUpdate struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	T     *timestamppb.Timestamp `protobuf:"bytes,1,opt,name=t,proto3" json:"t,omitempty"`
	Id    string                 `protobuf:"bytes,2,opt,name=id,proto3" json:"id,omitempty"`
	State *lang.RunState         `protobuf:"bytes,3,opt,name=state,proto3" json:"state,omitempty"`
}

func (x *RunUpdate) Reset() {
	*x = RunUpdate{}
	if protoimpl.UnsafeEnabled {
		mi := &file_litterboxsvc_svc_proto_msgTypes[6]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *RunUpdate) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*RunUpdate) ProtoMessage() {}

func (x *RunUpdate) ProtoReflect() protoreflect.Message {
	mi := &file_litterboxsvc_svc_proto_msgTypes[6]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use RunUpdate.ProtoReflect.Descriptor instead.
func (*RunUpdate) Descriptor() ([]byte, []int) {
	return file_litterboxsvc_svc_proto_rawDescGZIP(), []int{6}
}

func (x *RunUpdate) GetT() *timestamppb.Timestamp {
	if x != nil {
		return x.T
	}
	return nil
}

func (x *RunUpdate) GetId() string {
	if x != nil {
		return x.Id
	}
	return ""
}

func (x *RunUpdate) GetState() *lang.RunState {
	if x != nil {
		return x.State
	}
	return nil
}

var File_litterboxsvc_svc_proto protoreflect.FileDescriptor

var file_litterboxsvc_svc_proto_rawDesc = []byte{
	0x0a, 0x16, 0x6c, 0x69, 0x74, 0x74, 0x65, 0x72, 0x62, 0x6f, 0x78, 0x73, 0x76, 0x63, 0x2f, 0x73,
	0x76, 0x63, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x12, 0x14, 0x61, 0x75, 0x74, 0x6f, 0x6b, 0x69,
	0x74, 0x74, 0x65, 0x68, 0x2e, 0x6c, 0x69, 0x74, 0x74, 0x65, 0x72, 0x62, 0x6f, 0x78, 0x1a, 0x1c,
	0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x61, 0x6e, 0x6e, 0x6f, 0x74,
	0x61, 0x74, 0x69, 0x6f, 0x6e, 0x73, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x1f, 0x67, 0x6f,
	0x6f, 0x67, 0x6c, 0x65, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2f, 0x74, 0x69,
	0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d, 0x70, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x17, 0x76,
	0x61, 0x6c, 0x69, 0x64, 0x61, 0x74, 0x65, 0x2f, 0x76, 0x61, 0x6c, 0x69, 0x64, 0x61, 0x74, 0x65,
	0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x0e, 0x6c, 0x61, 0x6e, 0x67, 0x2f, 0x72, 0x75, 0x6e,
	0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x13, 0x76, 0x61, 0x6c, 0x75, 0x65, 0x73, 0x2f, 0x76,
	0x61, 0x6c, 0x75, 0x65, 0x73, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x22, 0x0e, 0x0a, 0x0c, 0x53,
	0x65, 0x74, 0x75, 0x70, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x22, 0x34, 0x0a, 0x0d, 0x53,
	0x65, 0x74, 0x75, 0x70, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x23, 0x0a, 0x02,
	0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x42, 0x13, 0xfa, 0x42, 0x10, 0x72, 0x0e, 0x32,
	0x0c, 0x5e, 0x42, 0x5b, 0x30, 0x2d, 0x39, 0x61, 0x2d, 0x66, 0x5d, 0x2b, 0x24, 0x52, 0x02, 0x69,
	0x64, 0x22, 0x33, 0x0a, 0x0c, 0x53, 0x63, 0x6f, 0x6f, 0x70, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73,
	0x74, 0x12, 0x23, 0x0a, 0x02, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x42, 0x13, 0xfa,
	0x42, 0x10, 0x72, 0x0e, 0x32, 0x0c, 0x5e, 0x42, 0x5b, 0x30, 0x2d, 0x39, 0x61, 0x2d, 0x66, 0x5d,
	0x2b, 0x24, 0x52, 0x02, 0x69, 0x64, 0x22, 0x0f, 0x0a, 0x0d, 0x53, 0x63, 0x6f, 0x6f, 0x70, 0x52,
	0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x22, 0xc6, 0x02, 0x0a, 0x0e, 0x53, 0x79, 0x6e, 0x74,
	0x68, 0x65, 0x74, 0x69, 0x63, 0x45, 0x76, 0x65, 0x6e, 0x74, 0x12, 0x40, 0x0a, 0x0b, 0x73, 0x72,
	0x63, 0x5f, 0x62, 0x69, 0x6e, 0x64, 0x69, 0x6e, 0x67, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x42,
	0x1f, 0xfa, 0x42, 0x1c, 0x72, 0x1a, 0x32, 0x18, 0x5e, 0x5b, 0x61, 0x2d, 0x7a, 0x41, 0x2d, 0x5a,
	0x5f, 0x5d, 0x5b, 0x61, 0x2d, 0x7a, 0x41, 0x2d, 0x5a, 0x30, 0x2d, 0x39, 0x5f, 0x5d, 0x2a, 0x24,
	0x52, 0x0a, 0x73, 0x72, 0x63, 0x42, 0x69, 0x6e, 0x64, 0x69, 0x6e, 0x67, 0x12, 0x12, 0x0a, 0x04,
	0x74, 0x79, 0x70, 0x65, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x04, 0x74, 0x79, 0x70, 0x65,
	0x12, 0x6a, 0x0a, 0x04, 0x64, 0x61, 0x74, 0x61, 0x18, 0x03, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x2e,
	0x2e, 0x61, 0x75, 0x74, 0x6f, 0x6b, 0x69, 0x74, 0x74, 0x65, 0x68, 0x2e, 0x6c, 0x69, 0x74, 0x74,
	0x65, 0x72, 0x62, 0x6f, 0x78, 0x2e, 0x53, 0x79, 0x6e, 0x74, 0x68, 0x65, 0x74, 0x69, 0x63, 0x45,
	0x76, 0x65, 0x6e, 0x74, 0x2e, 0x44, 0x61, 0x74, 0x61, 0x45, 0x6e, 0x74, 0x72, 0x79, 0x42, 0x26,
	0xfa, 0x42, 0x23, 0x9a, 0x01, 0x20, 0x18, 0x01, 0x22, 0x1c, 0x72, 0x1a, 0x32, 0x18, 0x5e, 0x5b,
	0x61, 0x2d, 0x7a, 0x41, 0x2d, 0x5a, 0x5f, 0x5d, 0x5b, 0x61, 0x2d, 0x7a, 0x41, 0x2d, 0x5a, 0x30,
	0x2d, 0x39, 0x5f, 0x5d, 0x2a, 0x24, 0x52, 0x04, 0x64, 0x61, 0x74, 0x61, 0x12, 0x1f, 0x0a, 0x0b,
	0x6f, 0x72, 0x69, 0x67, 0x69, 0x6e, 0x61, 0x6c, 0x5f, 0x69, 0x64, 0x18, 0x04, 0x20, 0x01, 0x28,
	0x09, 0x52, 0x0a, 0x6f, 0x72, 0x69, 0x67, 0x69, 0x6e, 0x61, 0x6c, 0x49, 0x64, 0x1a, 0x51, 0x0a,
	0x09, 0x44, 0x61, 0x74, 0x61, 0x45, 0x6e, 0x74, 0x72, 0x79, 0x12, 0x10, 0x0a, 0x03, 0x6b, 0x65,
	0x79, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x03, 0x6b, 0x65, 0x79, 0x12, 0x2e, 0x0a, 0x05,
	0x76, 0x61, 0x6c, 0x75, 0x65, 0x18, 0x02, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x18, 0x2e, 0x61, 0x75,
	0x74, 0x6f, 0x6b, 0x69, 0x74, 0x74, 0x65, 0x68, 0x2e, 0x76, 0x61, 0x6c, 0x75, 0x65, 0x73, 0x2e,
	0x56, 0x61, 0x6c, 0x75, 0x65, 0x52, 0x05, 0x76, 0x61, 0x6c, 0x75, 0x65, 0x3a, 0x02, 0x38, 0x01,
	0x22, 0x92, 0x01, 0x0a, 0x0a, 0x52, 0x75, 0x6e, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x12,
	0x26, 0x0a, 0x02, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x42, 0x16, 0xfa, 0x42, 0x13,
	0x72, 0x11, 0x32, 0x0c, 0x5e, 0x42, 0x5b, 0x30, 0x2d, 0x39, 0x61, 0x2d, 0x66, 0x5d, 0x2b, 0x24,
	0xd0, 0x01, 0x01, 0x52, 0x02, 0x69, 0x64, 0x12, 0x16, 0x0a, 0x06, 0x73, 0x6f, 0x75, 0x72, 0x63,
	0x65, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x06, 0x73, 0x6f, 0x75, 0x72, 0x63, 0x65, 0x12,
	0x44, 0x0a, 0x05, 0x65, 0x76, 0x65, 0x6e, 0x74, 0x18, 0x03, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x24,
	0x2e, 0x61, 0x75, 0x74, 0x6f, 0x6b, 0x69, 0x74, 0x74, 0x65, 0x68, 0x2e, 0x6c, 0x69, 0x74, 0x74,
	0x65, 0x72, 0x62, 0x6f, 0x78, 0x2e, 0x53, 0x79, 0x6e, 0x74, 0x68, 0x65, 0x74, 0x69, 0x63, 0x45,
	0x76, 0x65, 0x6e, 0x74, 0x42, 0x08, 0xfa, 0x42, 0x05, 0x8a, 0x01, 0x02, 0x10, 0x01, 0x52, 0x05,
	0x65, 0x76, 0x65, 0x6e, 0x74, 0x22, 0x9f, 0x01, 0x0a, 0x09, 0x52, 0x75, 0x6e, 0x55, 0x70, 0x64,
	0x61, 0x74, 0x65, 0x12, 0x32, 0x0a, 0x01, 0x74, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x1a,
	0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66,
	0x2e, 0x54, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d, 0x70, 0x42, 0x08, 0xfa, 0x42, 0x05, 0xb2,
	0x01, 0x02, 0x08, 0x01, 0x52, 0x01, 0x74, 0x12, 0x23, 0x0a, 0x02, 0x69, 0x64, 0x18, 0x02, 0x20,
	0x01, 0x28, 0x09, 0x42, 0x13, 0xfa, 0x42, 0x10, 0x72, 0x0e, 0x32, 0x0c, 0x5e, 0x42, 0x5b, 0x30,
	0x2d, 0x39, 0x61, 0x2d, 0x66, 0x5d, 0x2b, 0x24, 0x52, 0x02, 0x69, 0x64, 0x12, 0x39, 0x0a, 0x05,
	0x73, 0x74, 0x61, 0x74, 0x65, 0x18, 0x03, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x19, 0x2e, 0x61, 0x75,
	0x74, 0x6f, 0x6b, 0x69, 0x74, 0x74, 0x65, 0x68, 0x2e, 0x6c, 0x61, 0x6e, 0x67, 0x2e, 0x52, 0x75,
	0x6e, 0x53, 0x74, 0x61, 0x74, 0x65, 0x42, 0x08, 0xfa, 0x42, 0x05, 0x8a, 0x01, 0x02, 0x10, 0x01,
	0x52, 0x05, 0x73, 0x74, 0x61, 0x74, 0x65, 0x32, 0xec, 0x02, 0x0a, 0x09, 0x4c, 0x69, 0x74, 0x74,
	0x65, 0x72, 0x42, 0x6f, 0x78, 0x12, 0x70, 0x0a, 0x05, 0x53, 0x65, 0x74, 0x75, 0x70, 0x12, 0x22,
	0x2e, 0x61, 0x75, 0x74, 0x6f, 0x6b, 0x69, 0x74, 0x74, 0x65, 0x68, 0x2e, 0x6c, 0x69, 0x74, 0x74,
	0x65, 0x72, 0x62, 0x6f, 0x78, 0x2e, 0x53, 0x65, 0x74, 0x75, 0x70, 0x52, 0x65, 0x71, 0x75, 0x65,
	0x73, 0x74, 0x1a, 0x23, 0x2e, 0x61, 0x75, 0x74, 0x6f, 0x6b, 0x69, 0x74, 0x74, 0x65, 0x68, 0x2e,
	0x6c, 0x69, 0x74, 0x74, 0x65, 0x72, 0x62, 0x6f, 0x78, 0x2e, 0x53, 0x65, 0x74, 0x75, 0x70, 0x52,
	0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x22, 0x1e, 0x82, 0xd3, 0xe4, 0x93, 0x02, 0x18, 0x22,
	0x13, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x76, 0x31, 0x2f, 0x6c, 0x69, 0x74, 0x74, 0x65, 0x72, 0x62,
	0x6f, 0x78, 0x65, 0x73, 0x3a, 0x01, 0x2a, 0x12, 0x73, 0x0a, 0x03, 0x52, 0x75, 0x6e, 0x12, 0x20,
	0x2e, 0x61, 0x75, 0x74, 0x6f, 0x6b, 0x69, 0x74, 0x74, 0x65, 0x68, 0x2e, 0x6c, 0x69, 0x74, 0x74,
	0x65, 0x72, 0x62, 0x6f, 0x78, 0x2e, 0x52, 0x75, 0x6e, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74,
	0x1a, 0x1f, 0x2e, 0x61, 0x75, 0x74, 0x6f, 0x6b, 0x69, 0x74, 0x74, 0x65, 0x68, 0x2e, 0x6c, 0x69,
	0x74, 0x74, 0x65, 0x72, 0x62, 0x6f, 0x78, 0x2e, 0x52, 0x75, 0x6e, 0x55, 0x70, 0x64, 0x61, 0x74,
	0x65, 0x22, 0x27, 0x82, 0xd3, 0xe4, 0x93, 0x02, 0x21, 0x22, 0x1c, 0x2f, 0x61, 0x70, 0x69, 0x2f,
	0x76, 0x31, 0x2f, 0x6c, 0x69, 0x74, 0x74, 0x65, 0x72, 0x62, 0x6f, 0x78, 0x65, 0x73, 0x2f, 0x7b,
	0x69, 0x64, 0x7d, 0x2f, 0x72, 0x75, 0x6e, 0x3a, 0x01, 0x2a, 0x30, 0x01, 0x12, 0x78, 0x0a, 0x05,
	0x53, 0x63, 0x6f, 0x6f, 0x70, 0x12, 0x22, 0x2e, 0x61, 0x75, 0x74, 0x6f, 0x6b, 0x69, 0x74, 0x74,
	0x65, 0x68, 0x2e, 0x6c, 0x69, 0x74, 0x74, 0x65, 0x72, 0x62, 0x6f, 0x78, 0x2e, 0x53, 0x63, 0x6f,
	0x6f, 0x70, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x23, 0x2e, 0x61, 0x75, 0x74, 0x6f,
	0x6b, 0x69, 0x74, 0x74, 0x65, 0x68, 0x2e, 0x6c, 0x69, 0x74, 0x74, 0x65, 0x72, 0x62, 0x6f, 0x78,
	0x2e, 0x53, 0x63, 0x6f, 0x6f, 0x70, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x22, 0x26,
	0x82, 0xd3, 0xe4, 0x93, 0x02, 0x20, 0x22, 0x1e, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x76, 0x31, 0x2f,
	0x6c, 0x69, 0x74, 0x74, 0x65, 0x72, 0x62, 0x6f, 0x78, 0x65, 0x73, 0x2f, 0x7b, 0x69, 0x64, 0x7d,
	0x2f, 0x73, 0x63, 0x6f, 0x6f, 0x70, 0x42, 0x27, 0x5a, 0x25, 0x67, 0x6f, 0x2e, 0x61, 0x75, 0x74,
	0x6f, 0x6b, 0x69, 0x74, 0x74, 0x65, 0x68, 0x2e, 0x64, 0x65, 0x76, 0x2f, 0x69, 0x64, 0x6c, 0x2f,
	0x67, 0x6f, 0x2f, 0x6c, 0x69, 0x74, 0x74, 0x65, 0x72, 0x62, 0x6f, 0x78, 0x73, 0x76, 0x63, 0x62,
	0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_litterboxsvc_svc_proto_rawDescOnce sync.Once
	file_litterboxsvc_svc_proto_rawDescData = file_litterboxsvc_svc_proto_rawDesc
)

func file_litterboxsvc_svc_proto_rawDescGZIP() []byte {
	file_litterboxsvc_svc_proto_rawDescOnce.Do(func() {
		file_litterboxsvc_svc_proto_rawDescData = protoimpl.X.CompressGZIP(file_litterboxsvc_svc_proto_rawDescData)
	})
	return file_litterboxsvc_svc_proto_rawDescData
}

var file_litterboxsvc_svc_proto_msgTypes = make([]protoimpl.MessageInfo, 8)
var file_litterboxsvc_svc_proto_goTypes = []interface{}{
	(*SetupRequest)(nil),          // 0: autokitteh.litterbox.SetupRequest
	(*SetupResponse)(nil),         // 1: autokitteh.litterbox.SetupResponse
	(*ScoopRequest)(nil),          // 2: autokitteh.litterbox.ScoopRequest
	(*ScoopResponse)(nil),         // 3: autokitteh.litterbox.ScoopResponse
	(*SyntheticEvent)(nil),        // 4: autokitteh.litterbox.SyntheticEvent
	(*RunRequest)(nil),            // 5: autokitteh.litterbox.RunRequest
	(*RunUpdate)(nil),             // 6: autokitteh.litterbox.RunUpdate
	nil,                           // 7: autokitteh.litterbox.SyntheticEvent.DataEntry
	(*timestamppb.Timestamp)(nil), // 8: google.protobuf.Timestamp
	(*lang.RunState)(nil),         // 9: autokitteh.lang.RunState
	(*values.Value)(nil),          // 10: autokitteh.values.Value
}
var file_litterboxsvc_svc_proto_depIdxs = []int32{
	7,  // 0: autokitteh.litterbox.SyntheticEvent.data:type_name -> autokitteh.litterbox.SyntheticEvent.DataEntry
	4,  // 1: autokitteh.litterbox.RunRequest.event:type_name -> autokitteh.litterbox.SyntheticEvent
	8,  // 2: autokitteh.litterbox.RunUpdate.t:type_name -> google.protobuf.Timestamp
	9,  // 3: autokitteh.litterbox.RunUpdate.state:type_name -> autokitteh.lang.RunState
	10, // 4: autokitteh.litterbox.SyntheticEvent.DataEntry.value:type_name -> autokitteh.values.Value
	0,  // 5: autokitteh.litterbox.LitterBox.Setup:input_type -> autokitteh.litterbox.SetupRequest
	5,  // 6: autokitteh.litterbox.LitterBox.Run:input_type -> autokitteh.litterbox.RunRequest
	2,  // 7: autokitteh.litterbox.LitterBox.Scoop:input_type -> autokitteh.litterbox.ScoopRequest
	1,  // 8: autokitteh.litterbox.LitterBox.Setup:output_type -> autokitteh.litterbox.SetupResponse
	6,  // 9: autokitteh.litterbox.LitterBox.Run:output_type -> autokitteh.litterbox.RunUpdate
	3,  // 10: autokitteh.litterbox.LitterBox.Scoop:output_type -> autokitteh.litterbox.ScoopResponse
	8,  // [8:11] is the sub-list for method output_type
	5,  // [5:8] is the sub-list for method input_type
	5,  // [5:5] is the sub-list for extension type_name
	5,  // [5:5] is the sub-list for extension extendee
	0,  // [0:5] is the sub-list for field type_name
}

func init() { file_litterboxsvc_svc_proto_init() }
func file_litterboxsvc_svc_proto_init() {
	if File_litterboxsvc_svc_proto != nil {
		return
	}
	if !protoimpl.UnsafeEnabled {
		file_litterboxsvc_svc_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*SetupRequest); i {
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
		file_litterboxsvc_svc_proto_msgTypes[1].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*SetupResponse); i {
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
		file_litterboxsvc_svc_proto_msgTypes[2].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*ScoopRequest); i {
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
		file_litterboxsvc_svc_proto_msgTypes[3].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*ScoopResponse); i {
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
		file_litterboxsvc_svc_proto_msgTypes[4].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*SyntheticEvent); i {
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
		file_litterboxsvc_svc_proto_msgTypes[5].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*RunRequest); i {
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
		file_litterboxsvc_svc_proto_msgTypes[6].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*RunUpdate); i {
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
			RawDescriptor: file_litterboxsvc_svc_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   8,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_litterboxsvc_svc_proto_goTypes,
		DependencyIndexes: file_litterboxsvc_svc_proto_depIdxs,
		MessageInfos:      file_litterboxsvc_svc_proto_msgTypes,
	}.Build()
	File_litterboxsvc_svc_proto = out.File
	file_litterboxsvc_svc_proto_rawDesc = nil
	file_litterboxsvc_svc_proto_goTypes = nil
	file_litterboxsvc_svc_proto_depIdxs = nil
}