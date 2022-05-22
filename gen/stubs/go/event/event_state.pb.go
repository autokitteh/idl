// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.27.1
// 	protoc        v3.17.3
// source: event/event_state.proto

package event

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

type EventStateRecord struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	T     *timestamppb.Timestamp `protobuf:"bytes,1,opt,name=t,proto3" json:"t,omitempty"`
	State *EventState            `protobuf:"bytes,2,opt,name=state,proto3" json:"state,omitempty"`
}

func (x *EventStateRecord) Reset() {
	*x = EventStateRecord{}
	if protoimpl.UnsafeEnabled {
		mi := &file_event_event_state_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *EventStateRecord) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*EventStateRecord) ProtoMessage() {}

func (x *EventStateRecord) ProtoReflect() protoreflect.Message {
	mi := &file_event_event_state_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use EventStateRecord.ProtoReflect.Descriptor instead.
func (*EventStateRecord) Descriptor() ([]byte, []int) {
	return file_event_event_state_proto_rawDescGZIP(), []int{0}
}

func (x *EventStateRecord) GetT() *timestamppb.Timestamp {
	if x != nil {
		return x.T
	}
	return nil
}

func (x *EventStateRecord) GetState() *EventState {
	if x != nil {
		return x.State
	}
	return nil
}

type EventState struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// Types that are assignable to Type:
	//	*EventState_Ignored
	//	*EventState_Error
	//	*EventState_Pending
	//	*EventState_Processing
	//	*EventState_Processed
	Type isEventState_Type `protobuf_oneof:"type"`
}

func (x *EventState) Reset() {
	*x = EventState{}
	if protoimpl.UnsafeEnabled {
		mi := &file_event_event_state_proto_msgTypes[1]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *EventState) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*EventState) ProtoMessage() {}

func (x *EventState) ProtoReflect() protoreflect.Message {
	mi := &file_event_event_state_proto_msgTypes[1]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use EventState.ProtoReflect.Descriptor instead.
func (*EventState) Descriptor() ([]byte, []int) {
	return file_event_event_state_proto_rawDescGZIP(), []int{1}
}

func (m *EventState) GetType() isEventState_Type {
	if m != nil {
		return m.Type
	}
	return nil
}

func (x *EventState) GetIgnored() *IgnoredEventState {
	if x, ok := x.GetType().(*EventState_Ignored); ok {
		return x.Ignored
	}
	return nil
}

func (x *EventState) GetError() *ErrorEventState {
	if x, ok := x.GetType().(*EventState_Error); ok {
		return x.Error
	}
	return nil
}

func (x *EventState) GetPending() *PendingEventState {
	if x, ok := x.GetType().(*EventState_Pending); ok {
		return x.Pending
	}
	return nil
}

func (x *EventState) GetProcessing() *ProcessingEventState {
	if x, ok := x.GetType().(*EventState_Processing); ok {
		return x.Processing
	}
	return nil
}

func (x *EventState) GetProcessed() *ProcessedEventState {
	if x, ok := x.GetType().(*EventState_Processed); ok {
		return x.Processed
	}
	return nil
}

type isEventState_Type interface {
	isEventState_Type()
}

type EventState_Ignored struct {
	Ignored *IgnoredEventState `protobuf:"bytes,1,opt,name=ignored,proto3,oneof"`
}

type EventState_Error struct {
	Error *ErrorEventState `protobuf:"bytes,2,opt,name=error,proto3,oneof"`
}

type EventState_Pending struct {
	Pending *PendingEventState `protobuf:"bytes,3,opt,name=pending,proto3,oneof"`
}

type EventState_Processing struct {
	Processing *ProcessingEventState `protobuf:"bytes,4,opt,name=processing,proto3,oneof"`
}

type EventState_Processed struct {
	Processed *ProcessedEventState `protobuf:"bytes,5,opt,name=processed,proto3,oneof"`
}

func (*EventState_Ignored) isEventState_Type() {}

func (*EventState_Error) isEventState_Type() {}

func (*EventState_Pending) isEventState_Type() {}

func (*EventState_Processing) isEventState_Type() {}

func (*EventState_Processed) isEventState_Type() {}

type IgnoredEventState struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Reason string `protobuf:"bytes,1,opt,name=reason,proto3" json:"reason,omitempty"`
}

func (x *IgnoredEventState) Reset() {
	*x = IgnoredEventState{}
	if protoimpl.UnsafeEnabled {
		mi := &file_event_event_state_proto_msgTypes[2]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *IgnoredEventState) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*IgnoredEventState) ProtoMessage() {}

func (x *IgnoredEventState) ProtoReflect() protoreflect.Message {
	mi := &file_event_event_state_proto_msgTypes[2]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use IgnoredEventState.ProtoReflect.Descriptor instead.
func (*IgnoredEventState) Descriptor() ([]byte, []int) {
	return file_event_event_state_proto_rawDescGZIP(), []int{2}
}

func (x *IgnoredEventState) GetReason() string {
	if x != nil {
		return x.Reason
	}
	return ""
}

type ErrorEventState struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Error string `protobuf:"bytes,1,opt,name=error,proto3" json:"error,omitempty"`
}

func (x *ErrorEventState) Reset() {
	*x = ErrorEventState{}
	if protoimpl.UnsafeEnabled {
		mi := &file_event_event_state_proto_msgTypes[3]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *ErrorEventState) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ErrorEventState) ProtoMessage() {}

func (x *ErrorEventState) ProtoReflect() protoreflect.Message {
	mi := &file_event_event_state_proto_msgTypes[3]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ErrorEventState.ProtoReflect.Descriptor instead.
func (*ErrorEventState) Descriptor() ([]byte, []int) {
	return file_event_event_state_proto_rawDescGZIP(), []int{3}
}

func (x *ErrorEventState) GetError() string {
	if x != nil {
		return x.Error
	}
	return ""
}

type PendingEventState struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields
}

func (x *PendingEventState) Reset() {
	*x = PendingEventState{}
	if protoimpl.UnsafeEnabled {
		mi := &file_event_event_state_proto_msgTypes[4]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *PendingEventState) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*PendingEventState) ProtoMessage() {}

func (x *PendingEventState) ProtoReflect() protoreflect.Message {
	mi := &file_event_event_state_proto_msgTypes[4]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use PendingEventState.ProtoReflect.Descriptor instead.
func (*PendingEventState) Descriptor() ([]byte, []int) {
	return file_event_event_state_proto_rawDescGZIP(), []int{4}
}

type ProcessingEventState struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	ProjectIds        []string `protobuf:"bytes,1,rep,name=project_ids,json=projectIds,proto3" json:"project_ids,omitempty"`
	IgnoredProjectIds []string `protobuf:"bytes,2,rep,name=ignored_project_ids,json=ignoredProjectIds,proto3" json:"ignored_project_ids,omitempty"`
}

func (x *ProcessingEventState) Reset() {
	*x = ProcessingEventState{}
	if protoimpl.UnsafeEnabled {
		mi := &file_event_event_state_proto_msgTypes[5]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *ProcessingEventState) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ProcessingEventState) ProtoMessage() {}

func (x *ProcessingEventState) ProtoReflect() protoreflect.Message {
	mi := &file_event_event_state_proto_msgTypes[5]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ProcessingEventState.ProtoReflect.Descriptor instead.
func (*ProcessingEventState) Descriptor() ([]byte, []int) {
	return file_event_event_state_proto_rawDescGZIP(), []int{5}
}

func (x *ProcessingEventState) GetProjectIds() []string {
	if x != nil {
		return x.ProjectIds
	}
	return nil
}

func (x *ProcessingEventState) GetIgnoredProjectIds() []string {
	if x != nil {
		return x.IgnoredProjectIds
	}
	return nil
}

type ProcessedEventState struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	ProjectIds     []string `protobuf:"bytes,1,rep,name=project_ids,json=projectIds,proto3" json:"project_ids,omitempty"`
	AttnProjectIds []string `protobuf:"bytes,2,rep,name=attn_project_ids,json=attnProjectIds,proto3" json:"attn_project_ids,omitempty"`
}

func (x *ProcessedEventState) Reset() {
	*x = ProcessedEventState{}
	if protoimpl.UnsafeEnabled {
		mi := &file_event_event_state_proto_msgTypes[6]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *ProcessedEventState) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ProcessedEventState) ProtoMessage() {}

func (x *ProcessedEventState) ProtoReflect() protoreflect.Message {
	mi := &file_event_event_state_proto_msgTypes[6]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ProcessedEventState.ProtoReflect.Descriptor instead.
func (*ProcessedEventState) Descriptor() ([]byte, []int) {
	return file_event_event_state_proto_rawDescGZIP(), []int{6}
}

func (x *ProcessedEventState) GetProjectIds() []string {
	if x != nil {
		return x.ProjectIds
	}
	return nil
}

func (x *ProcessedEventState) GetAttnProjectIds() []string {
	if x != nil {
		return x.AttnProjectIds
	}
	return nil
}

var File_event_event_state_proto protoreflect.FileDescriptor

var file_event_event_state_proto_rawDesc = []byte{
	0x0a, 0x17, 0x65, 0x76, 0x65, 0x6e, 0x74, 0x2f, 0x65, 0x76, 0x65, 0x6e, 0x74, 0x5f, 0x73, 0x74,
	0x61, 0x74, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x12, 0x10, 0x61, 0x75, 0x74, 0x6f, 0x6b,
	0x69, 0x74, 0x74, 0x65, 0x68, 0x2e, 0x65, 0x76, 0x65, 0x6e, 0x74, 0x1a, 0x1f, 0x67, 0x6f, 0x6f,
	0x67, 0x6c, 0x65, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2f, 0x74, 0x69, 0x6d,
	0x65, 0x73, 0x74, 0x61, 0x6d, 0x70, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x17, 0x76, 0x61,
	0x6c, 0x69, 0x64, 0x61, 0x74, 0x65, 0x2f, 0x76, 0x61, 0x6c, 0x69, 0x64, 0x61, 0x74, 0x65, 0x2e,
	0x70, 0x72, 0x6f, 0x74, 0x6f, 0x22, 0x84, 0x01, 0x0a, 0x10, 0x45, 0x76, 0x65, 0x6e, 0x74, 0x53,
	0x74, 0x61, 0x74, 0x65, 0x52, 0x65, 0x63, 0x6f, 0x72, 0x64, 0x12, 0x32, 0x0a, 0x01, 0x74, 0x18,
	0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x1a, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x70,
	0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2e, 0x54, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d,
	0x70, 0x42, 0x08, 0xfa, 0x42, 0x05, 0xb2, 0x01, 0x02, 0x08, 0x01, 0x52, 0x01, 0x74, 0x12, 0x3c,
	0x0a, 0x05, 0x73, 0x74, 0x61, 0x74, 0x65, 0x18, 0x02, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x1c, 0x2e,
	0x61, 0x75, 0x74, 0x6f, 0x6b, 0x69, 0x74, 0x74, 0x65, 0x68, 0x2e, 0x65, 0x76, 0x65, 0x6e, 0x74,
	0x2e, 0x45, 0x76, 0x65, 0x6e, 0x74, 0x53, 0x74, 0x61, 0x74, 0x65, 0x42, 0x08, 0xfa, 0x42, 0x05,
	0x8a, 0x01, 0x02, 0x10, 0x01, 0x52, 0x05, 0x73, 0x74, 0x61, 0x74, 0x65, 0x22, 0xe7, 0x02, 0x0a,
	0x0a, 0x45, 0x76, 0x65, 0x6e, 0x74, 0x53, 0x74, 0x61, 0x74, 0x65, 0x12, 0x3f, 0x0a, 0x07, 0x69,
	0x67, 0x6e, 0x6f, 0x72, 0x65, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x23, 0x2e, 0x61,
	0x75, 0x74, 0x6f, 0x6b, 0x69, 0x74, 0x74, 0x65, 0x68, 0x2e, 0x65, 0x76, 0x65, 0x6e, 0x74, 0x2e,
	0x49, 0x67, 0x6e, 0x6f, 0x72, 0x65, 0x64, 0x45, 0x76, 0x65, 0x6e, 0x74, 0x53, 0x74, 0x61, 0x74,
	0x65, 0x48, 0x00, 0x52, 0x07, 0x69, 0x67, 0x6e, 0x6f, 0x72, 0x65, 0x64, 0x12, 0x39, 0x0a, 0x05,
	0x65, 0x72, 0x72, 0x6f, 0x72, 0x18, 0x02, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x21, 0x2e, 0x61, 0x75,
	0x74, 0x6f, 0x6b, 0x69, 0x74, 0x74, 0x65, 0x68, 0x2e, 0x65, 0x76, 0x65, 0x6e, 0x74, 0x2e, 0x45,
	0x72, 0x72, 0x6f, 0x72, 0x45, 0x76, 0x65, 0x6e, 0x74, 0x53, 0x74, 0x61, 0x74, 0x65, 0x48, 0x00,
	0x52, 0x05, 0x65, 0x72, 0x72, 0x6f, 0x72, 0x12, 0x3f, 0x0a, 0x07, 0x70, 0x65, 0x6e, 0x64, 0x69,
	0x6e, 0x67, 0x18, 0x03, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x23, 0x2e, 0x61, 0x75, 0x74, 0x6f, 0x6b,
	0x69, 0x74, 0x74, 0x65, 0x68, 0x2e, 0x65, 0x76, 0x65, 0x6e, 0x74, 0x2e, 0x50, 0x65, 0x6e, 0x64,
	0x69, 0x6e, 0x67, 0x45, 0x76, 0x65, 0x6e, 0x74, 0x53, 0x74, 0x61, 0x74, 0x65, 0x48, 0x00, 0x52,
	0x07, 0x70, 0x65, 0x6e, 0x64, 0x69, 0x6e, 0x67, 0x12, 0x48, 0x0a, 0x0a, 0x70, 0x72, 0x6f, 0x63,
	0x65, 0x73, 0x73, 0x69, 0x6e, 0x67, 0x18, 0x04, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x26, 0x2e, 0x61,
	0x75, 0x74, 0x6f, 0x6b, 0x69, 0x74, 0x74, 0x65, 0x68, 0x2e, 0x65, 0x76, 0x65, 0x6e, 0x74, 0x2e,
	0x50, 0x72, 0x6f, 0x63, 0x65, 0x73, 0x73, 0x69, 0x6e, 0x67, 0x45, 0x76, 0x65, 0x6e, 0x74, 0x53,
	0x74, 0x61, 0x74, 0x65, 0x48, 0x00, 0x52, 0x0a, 0x70, 0x72, 0x6f, 0x63, 0x65, 0x73, 0x73, 0x69,
	0x6e, 0x67, 0x12, 0x45, 0x0a, 0x09, 0x70, 0x72, 0x6f, 0x63, 0x65, 0x73, 0x73, 0x65, 0x64, 0x18,
	0x05, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x25, 0x2e, 0x61, 0x75, 0x74, 0x6f, 0x6b, 0x69, 0x74, 0x74,
	0x65, 0x68, 0x2e, 0x65, 0x76, 0x65, 0x6e, 0x74, 0x2e, 0x50, 0x72, 0x6f, 0x63, 0x65, 0x73, 0x73,
	0x65, 0x64, 0x45, 0x76, 0x65, 0x6e, 0x74, 0x53, 0x74, 0x61, 0x74, 0x65, 0x48, 0x00, 0x52, 0x09,
	0x70, 0x72, 0x6f, 0x63, 0x65, 0x73, 0x73, 0x65, 0x64, 0x42, 0x0b, 0x0a, 0x04, 0x74, 0x79, 0x70,
	0x65, 0x12, 0x03, 0xf8, 0x42, 0x01, 0x22, 0x2b, 0x0a, 0x11, 0x49, 0x67, 0x6e, 0x6f, 0x72, 0x65,
	0x64, 0x45, 0x76, 0x65, 0x6e, 0x74, 0x53, 0x74, 0x61, 0x74, 0x65, 0x12, 0x16, 0x0a, 0x06, 0x72,
	0x65, 0x61, 0x73, 0x6f, 0x6e, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x06, 0x72, 0x65, 0x61,
	0x73, 0x6f, 0x6e, 0x22, 0x27, 0x0a, 0x0f, 0x45, 0x72, 0x72, 0x6f, 0x72, 0x45, 0x76, 0x65, 0x6e,
	0x74, 0x53, 0x74, 0x61, 0x74, 0x65, 0x12, 0x14, 0x0a, 0x05, 0x65, 0x72, 0x72, 0x6f, 0x72, 0x18,
	0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x05, 0x65, 0x72, 0x72, 0x6f, 0x72, 0x22, 0x13, 0x0a, 0x11,
	0x50, 0x65, 0x6e, 0x64, 0x69, 0x6e, 0x67, 0x45, 0x76, 0x65, 0x6e, 0x74, 0x53, 0x74, 0x61, 0x74,
	0x65, 0x22, 0xd3, 0x01, 0x0a, 0x14, 0x50, 0x72, 0x6f, 0x63, 0x65, 0x73, 0x73, 0x69, 0x6e, 0x67,
	0x45, 0x76, 0x65, 0x6e, 0x74, 0x53, 0x74, 0x61, 0x74, 0x65, 0x12, 0x55, 0x0a, 0x0b, 0x70, 0x72,
	0x6f, 0x6a, 0x65, 0x63, 0x74, 0x5f, 0x69, 0x64, 0x73, 0x18, 0x01, 0x20, 0x03, 0x28, 0x09, 0x42,
	0x34, 0xfa, 0x42, 0x31, 0x92, 0x01, 0x2e, 0x22, 0x2c, 0x72, 0x2a, 0x32, 0x28, 0x5e, 0x5b, 0x61,
	0x2d, 0x7a, 0x41, 0x2d, 0x5a, 0x5d, 0x5b, 0x30, 0x2d, 0x39, 0x61, 0x2d, 0x7a, 0x41, 0x2d, 0x5a,
	0x5f, 0x2d, 0x5d, 0x2b, 0x5c, 0x2e, 0x5b, 0x61, 0x2d, 0x7a, 0x41, 0x2d, 0x5a, 0x30, 0x2d, 0x39,
	0x5f, 0x2d, 0x5d, 0x2b, 0x24, 0x52, 0x0a, 0x70, 0x72, 0x6f, 0x6a, 0x65, 0x63, 0x74, 0x49, 0x64,
	0x73, 0x12, 0x64, 0x0a, 0x13, 0x69, 0x67, 0x6e, 0x6f, 0x72, 0x65, 0x64, 0x5f, 0x70, 0x72, 0x6f,
	0x6a, 0x65, 0x63, 0x74, 0x5f, 0x69, 0x64, 0x73, 0x18, 0x02, 0x20, 0x03, 0x28, 0x09, 0x42, 0x34,
	0xfa, 0x42, 0x31, 0x92, 0x01, 0x2e, 0x22, 0x2c, 0x72, 0x2a, 0x32, 0x28, 0x5e, 0x5b, 0x61, 0x2d,
	0x7a, 0x41, 0x2d, 0x5a, 0x5d, 0x5b, 0x30, 0x2d, 0x39, 0x61, 0x2d, 0x7a, 0x41, 0x2d, 0x5a, 0x5f,
	0x2d, 0x5d, 0x2b, 0x5c, 0x2e, 0x5b, 0x61, 0x2d, 0x7a, 0x41, 0x2d, 0x5a, 0x30, 0x2d, 0x39, 0x5f,
	0x2d, 0x5d, 0x2b, 0x24, 0x52, 0x11, 0x69, 0x67, 0x6e, 0x6f, 0x72, 0x65, 0x64, 0x50, 0x72, 0x6f,
	0x6a, 0x65, 0x63, 0x74, 0x49, 0x64, 0x73, 0x22, 0xcc, 0x01, 0x0a, 0x13, 0x50, 0x72, 0x6f, 0x63,
	0x65, 0x73, 0x73, 0x65, 0x64, 0x45, 0x76, 0x65, 0x6e, 0x74, 0x53, 0x74, 0x61, 0x74, 0x65, 0x12,
	0x55, 0x0a, 0x0b, 0x70, 0x72, 0x6f, 0x6a, 0x65, 0x63, 0x74, 0x5f, 0x69, 0x64, 0x73, 0x18, 0x01,
	0x20, 0x03, 0x28, 0x09, 0x42, 0x34, 0xfa, 0x42, 0x31, 0x92, 0x01, 0x2e, 0x22, 0x2c, 0x72, 0x2a,
	0x32, 0x28, 0x5e, 0x5b, 0x61, 0x2d, 0x7a, 0x41, 0x2d, 0x5a, 0x5d, 0x5b, 0x30, 0x2d, 0x39, 0x61,
	0x2d, 0x7a, 0x41, 0x2d, 0x5a, 0x5f, 0x2d, 0x5d, 0x2b, 0x5c, 0x2e, 0x5b, 0x61, 0x2d, 0x7a, 0x41,
	0x2d, 0x5a, 0x30, 0x2d, 0x39, 0x5f, 0x2d, 0x5d, 0x2b, 0x24, 0x52, 0x0a, 0x70, 0x72, 0x6f, 0x6a,
	0x65, 0x63, 0x74, 0x49, 0x64, 0x73, 0x12, 0x5e, 0x0a, 0x10, 0x61, 0x74, 0x74, 0x6e, 0x5f, 0x70,
	0x72, 0x6f, 0x6a, 0x65, 0x63, 0x74, 0x5f, 0x69, 0x64, 0x73, 0x18, 0x02, 0x20, 0x03, 0x28, 0x09,
	0x42, 0x34, 0xfa, 0x42, 0x31, 0x92, 0x01, 0x2e, 0x22, 0x2c, 0x72, 0x2a, 0x32, 0x28, 0x5e, 0x5b,
	0x61, 0x2d, 0x7a, 0x41, 0x2d, 0x5a, 0x5d, 0x5b, 0x30, 0x2d, 0x39, 0x61, 0x2d, 0x7a, 0x41, 0x2d,
	0x5a, 0x5f, 0x2d, 0x5d, 0x2b, 0x5c, 0x2e, 0x5b, 0x61, 0x2d, 0x7a, 0x41, 0x2d, 0x5a, 0x30, 0x2d,
	0x39, 0x5f, 0x2d, 0x5d, 0x2b, 0x24, 0x52, 0x0e, 0x61, 0x74, 0x74, 0x6e, 0x50, 0x72, 0x6f, 0x6a,
	0x65, 0x63, 0x74, 0x49, 0x64, 0x73, 0x42, 0x1d, 0x5a, 0x1b, 0x67, 0x6f, 0x2e, 0x61, 0x75, 0x74,
	0x6f, 0x6b, 0x69, 0x74, 0x74, 0x65, 0x68, 0x2e, 0x64, 0x65, 0x76, 0x2f, 0x69, 0x64, 0x6c, 0x2f,
	0x65, 0x76, 0x65, 0x6e, 0x74, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_event_event_state_proto_rawDescOnce sync.Once
	file_event_event_state_proto_rawDescData = file_event_event_state_proto_rawDesc
)

func file_event_event_state_proto_rawDescGZIP() []byte {
	file_event_event_state_proto_rawDescOnce.Do(func() {
		file_event_event_state_proto_rawDescData = protoimpl.X.CompressGZIP(file_event_event_state_proto_rawDescData)
	})
	return file_event_event_state_proto_rawDescData
}

var file_event_event_state_proto_msgTypes = make([]protoimpl.MessageInfo, 7)
var file_event_event_state_proto_goTypes = []interface{}{
	(*EventStateRecord)(nil),      // 0: autokitteh.event.EventStateRecord
	(*EventState)(nil),            // 1: autokitteh.event.EventState
	(*IgnoredEventState)(nil),     // 2: autokitteh.event.IgnoredEventState
	(*ErrorEventState)(nil),       // 3: autokitteh.event.ErrorEventState
	(*PendingEventState)(nil),     // 4: autokitteh.event.PendingEventState
	(*ProcessingEventState)(nil),  // 5: autokitteh.event.ProcessingEventState
	(*ProcessedEventState)(nil),   // 6: autokitteh.event.ProcessedEventState
	(*timestamppb.Timestamp)(nil), // 7: google.protobuf.Timestamp
}
var file_event_event_state_proto_depIdxs = []int32{
	7, // 0: autokitteh.event.EventStateRecord.t:type_name -> google.protobuf.Timestamp
	1, // 1: autokitteh.event.EventStateRecord.state:type_name -> autokitteh.event.EventState
	2, // 2: autokitteh.event.EventState.ignored:type_name -> autokitteh.event.IgnoredEventState
	3, // 3: autokitteh.event.EventState.error:type_name -> autokitteh.event.ErrorEventState
	4, // 4: autokitteh.event.EventState.pending:type_name -> autokitteh.event.PendingEventState
	5, // 5: autokitteh.event.EventState.processing:type_name -> autokitteh.event.ProcessingEventState
	6, // 6: autokitteh.event.EventState.processed:type_name -> autokitteh.event.ProcessedEventState
	7, // [7:7] is the sub-list for method output_type
	7, // [7:7] is the sub-list for method input_type
	7, // [7:7] is the sub-list for extension type_name
	7, // [7:7] is the sub-list for extension extendee
	0, // [0:7] is the sub-list for field type_name
}

func init() { file_event_event_state_proto_init() }
func file_event_event_state_proto_init() {
	if File_event_event_state_proto != nil {
		return
	}
	if !protoimpl.UnsafeEnabled {
		file_event_event_state_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*EventStateRecord); i {
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
		file_event_event_state_proto_msgTypes[1].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*EventState); i {
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
		file_event_event_state_proto_msgTypes[2].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*IgnoredEventState); i {
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
		file_event_event_state_proto_msgTypes[3].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*ErrorEventState); i {
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
		file_event_event_state_proto_msgTypes[4].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*PendingEventState); i {
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
		file_event_event_state_proto_msgTypes[5].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*ProcessingEventState); i {
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
		file_event_event_state_proto_msgTypes[6].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*ProcessedEventState); i {
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
	file_event_event_state_proto_msgTypes[1].OneofWrappers = []interface{}{
		(*EventState_Ignored)(nil),
		(*EventState_Error)(nil),
		(*EventState_Pending)(nil),
		(*EventState_Processing)(nil),
		(*EventState_Processed)(nil),
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_event_event_state_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   7,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_event_event_state_proto_goTypes,
		DependencyIndexes: file_event_event_state_proto_depIdxs,
		MessageInfos:      file_event_event_state_proto_msgTypes,
	}.Build()
	File_event_event_state_proto = out.File
	file_event_event_state_proto_rawDesc = nil
	file_event_event_state_proto_goTypes = nil
	file_event_event_state_proto_depIdxs = nil
}
