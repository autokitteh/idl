// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.27.1
// 	protoc        v3.17.3
// source: event/event.proto

package event

import (
	_ "github.com/envoyproxy/protoc-gen-validate/validate"
	values "go.autokitteh.dev/idl/go/values"
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

type Event struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	T                *timestamppb.Timestamp   `protobuf:"bytes,1,opt,name=t,proto3" json:"t,omitempty"`
	Id               string                   `protobuf:"bytes,2,opt,name=id,proto3" json:"id,omitempty"`
	SrcId            string                   `protobuf:"bytes,3,opt,name=src_id,json=srcId,proto3" json:"src_id,omitempty"`
	AssociationToken string                   `protobuf:"bytes,4,opt,name=association_token,json=associationToken,proto3" json:"association_token,omitempty"`
	OriginalId       string                   `protobuf:"bytes,5,opt,name=original_id,json=originalId,proto3" json:"original_id,omitempty"`
	Type             string                   `protobuf:"bytes,6,opt,name=type,proto3" json:"type,omitempty"`
	Data             map[string]*values.Value `protobuf:"bytes,7,rep,name=data,proto3" json:"data,omitempty" protobuf_key:"bytes,1,opt,name=key,proto3" protobuf_val:"bytes,2,opt,name=value,proto3"`
	Memo             map[string]string        `protobuf:"bytes,8,rep,name=memo,proto3" json:"memo,omitempty" protobuf_key:"bytes,1,opt,name=key,proto3" protobuf_val:"bytes,2,opt,name=value,proto3"`
}

func (x *Event) Reset() {
	*x = Event{}
	if protoimpl.UnsafeEnabled {
		mi := &file_event_event_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *Event) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Event) ProtoMessage() {}

func (x *Event) ProtoReflect() protoreflect.Message {
	mi := &file_event_event_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use Event.ProtoReflect.Descriptor instead.
func (*Event) Descriptor() ([]byte, []int) {
	return file_event_event_proto_rawDescGZIP(), []int{0}
}

func (x *Event) GetT() *timestamppb.Timestamp {
	if x != nil {
		return x.T
	}
	return nil
}

func (x *Event) GetId() string {
	if x != nil {
		return x.Id
	}
	return ""
}

func (x *Event) GetSrcId() string {
	if x != nil {
		return x.SrcId
	}
	return ""
}

func (x *Event) GetAssociationToken() string {
	if x != nil {
		return x.AssociationToken
	}
	return ""
}

func (x *Event) GetOriginalId() string {
	if x != nil {
		return x.OriginalId
	}
	return ""
}

func (x *Event) GetType() string {
	if x != nil {
		return x.Type
	}
	return ""
}

func (x *Event) GetData() map[string]*values.Value {
	if x != nil {
		return x.Data
	}
	return nil
}

func (x *Event) GetMemo() map[string]string {
	if x != nil {
		return x.Memo
	}
	return nil
}

var File_event_event_proto protoreflect.FileDescriptor

var file_event_event_proto_rawDesc = []byte{
	0x0a, 0x11, 0x65, 0x76, 0x65, 0x6e, 0x74, 0x2f, 0x65, 0x76, 0x65, 0x6e, 0x74, 0x2e, 0x70, 0x72,
	0x6f, 0x74, 0x6f, 0x12, 0x10, 0x61, 0x75, 0x74, 0x6f, 0x6b, 0x69, 0x74, 0x74, 0x65, 0x68, 0x2e,
	0x65, 0x76, 0x65, 0x6e, 0x74, 0x1a, 0x1f, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2f, 0x70, 0x72,
	0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2f, 0x74, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d, 0x70,
	0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x17, 0x76, 0x61, 0x6c, 0x69, 0x64, 0x61, 0x74, 0x65,
	0x2f, 0x76, 0x61, 0x6c, 0x69, 0x64, 0x61, 0x74, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a,
	0x13, 0x76, 0x61, 0x6c, 0x75, 0x65, 0x73, 0x2f, 0x76, 0x61, 0x6c, 0x75, 0x65, 0x73, 0x2e, 0x70,
	0x72, 0x6f, 0x74, 0x6f, 0x22, 0xcb, 0x04, 0x0a, 0x05, 0x45, 0x76, 0x65, 0x6e, 0x74, 0x12, 0x32,
	0x0a, 0x01, 0x74, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x1a, 0x2e, 0x67, 0x6f, 0x6f, 0x67,
	0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2e, 0x54, 0x69, 0x6d, 0x65,
	0x73, 0x74, 0x61, 0x6d, 0x70, 0x42, 0x08, 0xfa, 0x42, 0x05, 0xb2, 0x01, 0x02, 0x08, 0x01, 0x52,
	0x01, 0x74, 0x12, 0x23, 0x0a, 0x02, 0x69, 0x64, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x42, 0x13,
	0xfa, 0x42, 0x10, 0x72, 0x0e, 0x32, 0x0c, 0x5e, 0x45, 0x5b, 0x30, 0x2d, 0x39, 0x61, 0x2d, 0x66,
	0x5d, 0x2b, 0x24, 0x52, 0x02, 0x69, 0x64, 0x12, 0x4e, 0x0a, 0x06, 0x73, 0x72, 0x63, 0x5f, 0x69,
	0x64, 0x18, 0x03, 0x20, 0x01, 0x28, 0x09, 0x42, 0x37, 0xfa, 0x42, 0x34, 0x72, 0x32, 0x32, 0x30,
	0x5e, 0x5b, 0x61, 0x2d, 0x7a, 0x41, 0x2d, 0x5a, 0x5d, 0x5b, 0x30, 0x2d, 0x39, 0x61, 0x2d, 0x7a,
	0x41, 0x2d, 0x5a, 0x5f, 0x2d, 0x5d, 0x2b, 0x5c, 0x2e, 0x5b, 0x61, 0x2d, 0x7a, 0x41, 0x2d, 0x5a,
	0x5d, 0x5b, 0x30, 0x2d, 0x39, 0x61, 0x2d, 0x7a, 0x41, 0x2d, 0x5a, 0x5f, 0x2d, 0x5d, 0x2b, 0x24,
	0x52, 0x05, 0x73, 0x72, 0x63, 0x49, 0x64, 0x12, 0x2b, 0x0a, 0x11, 0x61, 0x73, 0x73, 0x6f, 0x63,
	0x69, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x5f, 0x74, 0x6f, 0x6b, 0x65, 0x6e, 0x18, 0x04, 0x20, 0x01,
	0x28, 0x09, 0x52, 0x10, 0x61, 0x73, 0x73, 0x6f, 0x63, 0x69, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x54,
	0x6f, 0x6b, 0x65, 0x6e, 0x12, 0x1f, 0x0a, 0x0b, 0x6f, 0x72, 0x69, 0x67, 0x69, 0x6e, 0x61, 0x6c,
	0x5f, 0x69, 0x64, 0x18, 0x05, 0x20, 0x01, 0x28, 0x09, 0x52, 0x0a, 0x6f, 0x72, 0x69, 0x67, 0x69,
	0x6e, 0x61, 0x6c, 0x49, 0x64, 0x12, 0x1b, 0x0a, 0x04, 0x74, 0x79, 0x70, 0x65, 0x18, 0x06, 0x20,
	0x01, 0x28, 0x09, 0x42, 0x07, 0xfa, 0x42, 0x04, 0x72, 0x02, 0x10, 0x01, 0x52, 0x04, 0x74, 0x79,
	0x70, 0x65, 0x12, 0x5d, 0x0a, 0x04, 0x64, 0x61, 0x74, 0x61, 0x18, 0x07, 0x20, 0x03, 0x28, 0x0b,
	0x32, 0x21, 0x2e, 0x61, 0x75, 0x74, 0x6f, 0x6b, 0x69, 0x74, 0x74, 0x65, 0x68, 0x2e, 0x65, 0x76,
	0x65, 0x6e, 0x74, 0x2e, 0x45, 0x76, 0x65, 0x6e, 0x74, 0x2e, 0x44, 0x61, 0x74, 0x61, 0x45, 0x6e,
	0x74, 0x72, 0x79, 0x42, 0x26, 0xfa, 0x42, 0x23, 0x9a, 0x01, 0x20, 0x18, 0x01, 0x22, 0x1c, 0x72,
	0x1a, 0x32, 0x18, 0x5e, 0x5b, 0x61, 0x2d, 0x7a, 0x41, 0x2d, 0x5a, 0x5f, 0x5d, 0x5b, 0x61, 0x2d,
	0x7a, 0x41, 0x2d, 0x5a, 0x30, 0x2d, 0x39, 0x5f, 0x5d, 0x2a, 0x24, 0x52, 0x04, 0x64, 0x61, 0x74,
	0x61, 0x12, 0x43, 0x0a, 0x04, 0x6d, 0x65, 0x6d, 0x6f, 0x18, 0x08, 0x20, 0x03, 0x28, 0x0b, 0x32,
	0x21, 0x2e, 0x61, 0x75, 0x74, 0x6f, 0x6b, 0x69, 0x74, 0x74, 0x65, 0x68, 0x2e, 0x65, 0x76, 0x65,
	0x6e, 0x74, 0x2e, 0x45, 0x76, 0x65, 0x6e, 0x74, 0x2e, 0x4d, 0x65, 0x6d, 0x6f, 0x45, 0x6e, 0x74,
	0x72, 0x79, 0x42, 0x0c, 0xfa, 0x42, 0x09, 0x9a, 0x01, 0x06, 0x22, 0x04, 0x72, 0x02, 0x10, 0x01,
	0x52, 0x04, 0x6d, 0x65, 0x6d, 0x6f, 0x1a, 0x51, 0x0a, 0x09, 0x44, 0x61, 0x74, 0x61, 0x45, 0x6e,
	0x74, 0x72, 0x79, 0x12, 0x10, 0x0a, 0x03, 0x6b, 0x65, 0x79, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09,
	0x52, 0x03, 0x6b, 0x65, 0x79, 0x12, 0x2e, 0x0a, 0x05, 0x76, 0x61, 0x6c, 0x75, 0x65, 0x18, 0x02,
	0x20, 0x01, 0x28, 0x0b, 0x32, 0x18, 0x2e, 0x61, 0x75, 0x74, 0x6f, 0x6b, 0x69, 0x74, 0x74, 0x65,
	0x68, 0x2e, 0x76, 0x61, 0x6c, 0x75, 0x65, 0x73, 0x2e, 0x56, 0x61, 0x6c, 0x75, 0x65, 0x52, 0x05,
	0x76, 0x61, 0x6c, 0x75, 0x65, 0x3a, 0x02, 0x38, 0x01, 0x1a, 0x37, 0x0a, 0x09, 0x4d, 0x65, 0x6d,
	0x6f, 0x45, 0x6e, 0x74, 0x72, 0x79, 0x12, 0x10, 0x0a, 0x03, 0x6b, 0x65, 0x79, 0x18, 0x01, 0x20,
	0x01, 0x28, 0x09, 0x52, 0x03, 0x6b, 0x65, 0x79, 0x12, 0x14, 0x0a, 0x05, 0x76, 0x61, 0x6c, 0x75,
	0x65, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x05, 0x76, 0x61, 0x6c, 0x75, 0x65, 0x3a, 0x02,
	0x38, 0x01, 0x42, 0x20, 0x5a, 0x1e, 0x67, 0x6f, 0x2e, 0x61, 0x75, 0x74, 0x6f, 0x6b, 0x69, 0x74,
	0x74, 0x65, 0x68, 0x2e, 0x64, 0x65, 0x76, 0x2f, 0x69, 0x64, 0x6c, 0x2f, 0x67, 0x6f, 0x2f, 0x65,
	0x76, 0x65, 0x6e, 0x74, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_event_event_proto_rawDescOnce sync.Once
	file_event_event_proto_rawDescData = file_event_event_proto_rawDesc
)

func file_event_event_proto_rawDescGZIP() []byte {
	file_event_event_proto_rawDescOnce.Do(func() {
		file_event_event_proto_rawDescData = protoimpl.X.CompressGZIP(file_event_event_proto_rawDescData)
	})
	return file_event_event_proto_rawDescData
}

var file_event_event_proto_msgTypes = make([]protoimpl.MessageInfo, 3)
var file_event_event_proto_goTypes = []interface{}{
	(*Event)(nil),                 // 0: autokitteh.event.Event
	nil,                           // 1: autokitteh.event.Event.DataEntry
	nil,                           // 2: autokitteh.event.Event.MemoEntry
	(*timestamppb.Timestamp)(nil), // 3: google.protobuf.Timestamp
	(*values.Value)(nil),          // 4: autokitteh.values.Value
}
var file_event_event_proto_depIdxs = []int32{
	3, // 0: autokitteh.event.Event.t:type_name -> google.protobuf.Timestamp
	1, // 1: autokitteh.event.Event.data:type_name -> autokitteh.event.Event.DataEntry
	2, // 2: autokitteh.event.Event.memo:type_name -> autokitteh.event.Event.MemoEntry
	4, // 3: autokitteh.event.Event.DataEntry.value:type_name -> autokitteh.values.Value
	4, // [4:4] is the sub-list for method output_type
	4, // [4:4] is the sub-list for method input_type
	4, // [4:4] is the sub-list for extension type_name
	4, // [4:4] is the sub-list for extension extendee
	0, // [0:4] is the sub-list for field type_name
}

func init() { file_event_event_proto_init() }
func file_event_event_proto_init() {
	if File_event_event_proto != nil {
		return
	}
	if !protoimpl.UnsafeEnabled {
		file_event_event_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*Event); i {
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
			RawDescriptor: file_event_event_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   3,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_event_event_proto_goTypes,
		DependencyIndexes: file_event_event_proto_depIdxs,
		MessageInfos:      file_event_event_proto_msgTypes,
	}.Build()
	File_event_event_proto = out.File
	file_event_event_proto_rawDesc = nil
	file_event_event_proto_goTypes = nil
	file_event_event_proto_depIdxs = nil
}
