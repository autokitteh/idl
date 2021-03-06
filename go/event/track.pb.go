// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.27.1
// 	protoc        v3.17.3
// source: event/track.proto

package event

import (
	_ "github.com/envoyproxy/protoc-gen-validate/validate"
	lang "go.autokitteh.dev/idl/go/lang"
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	reflect "reflect"
	sync "sync"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

type TrackIngestEventUpdate struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	EventId             string                   `protobuf:"bytes,1,opt,name=event_id,json=eventId,proto3" json:"event_id,omitempty"`
	EventState          *EventStateRecord        `protobuf:"bytes,2,opt,name=event_state,json=eventState,proto3" json:"event_state,omitempty"`
	ProjectId           string                   `protobuf:"bytes,3,opt,name=project_id,json=projectId,proto3" json:"project_id,omitempty"`
	ProjectEventState   *ProjectEventStateRecord `protobuf:"bytes,4,opt,name=project_event_state,json=projectEventState,proto3" json:"project_event_state,omitempty"` // set if project_id is set
	FlattenedRunSummary *lang.RunSummary         `protobuf:"bytes,5,opt,name=flattened_run_summary,json=flattenedRunSummary,proto3" json:"flattened_run_summary,omitempty"`
}

func (x *TrackIngestEventUpdate) Reset() {
	*x = TrackIngestEventUpdate{}
	if protoimpl.UnsafeEnabled {
		mi := &file_event_track_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *TrackIngestEventUpdate) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*TrackIngestEventUpdate) ProtoMessage() {}

func (x *TrackIngestEventUpdate) ProtoReflect() protoreflect.Message {
	mi := &file_event_track_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use TrackIngestEventUpdate.ProtoReflect.Descriptor instead.
func (*TrackIngestEventUpdate) Descriptor() ([]byte, []int) {
	return file_event_track_proto_rawDescGZIP(), []int{0}
}

func (x *TrackIngestEventUpdate) GetEventId() string {
	if x != nil {
		return x.EventId
	}
	return ""
}

func (x *TrackIngestEventUpdate) GetEventState() *EventStateRecord {
	if x != nil {
		return x.EventState
	}
	return nil
}

func (x *TrackIngestEventUpdate) GetProjectId() string {
	if x != nil {
		return x.ProjectId
	}
	return ""
}

func (x *TrackIngestEventUpdate) GetProjectEventState() *ProjectEventStateRecord {
	if x != nil {
		return x.ProjectEventState
	}
	return nil
}

func (x *TrackIngestEventUpdate) GetFlattenedRunSummary() *lang.RunSummary {
	if x != nil {
		return x.FlattenedRunSummary
	}
	return nil
}

var File_event_track_proto protoreflect.FileDescriptor

var file_event_track_proto_rawDesc = []byte{
	0x0a, 0x11, 0x65, 0x76, 0x65, 0x6e, 0x74, 0x2f, 0x74, 0x72, 0x61, 0x63, 0x6b, 0x2e, 0x70, 0x72,
	0x6f, 0x74, 0x6f, 0x12, 0x10, 0x61, 0x75, 0x74, 0x6f, 0x6b, 0x69, 0x74, 0x74, 0x65, 0x68, 0x2e,
	0x65, 0x76, 0x65, 0x6e, 0x74, 0x1a, 0x17, 0x76, 0x61, 0x6c, 0x69, 0x64, 0x61, 0x74, 0x65, 0x2f,
	0x76, 0x61, 0x6c, 0x69, 0x64, 0x61, 0x74, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x17,
	0x65, 0x76, 0x65, 0x6e, 0x74, 0x2f, 0x65, 0x76, 0x65, 0x6e, 0x74, 0x5f, 0x73, 0x74, 0x61, 0x74,
	0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x19, 0x65, 0x76, 0x65, 0x6e, 0x74, 0x2f, 0x70,
	0x72, 0x6f, 0x6a, 0x65, 0x63, 0x74, 0x5f, 0x73, 0x74, 0x61, 0x74, 0x65, 0x2e, 0x70, 0x72, 0x6f,
	0x74, 0x6f, 0x1a, 0x0e, 0x6c, 0x61, 0x6e, 0x67, 0x2f, 0x72, 0x75, 0x6e, 0x2e, 0x70, 0x72, 0x6f,
	0x74, 0x6f, 0x22, 0x8c, 0x03, 0x0a, 0x16, 0x54, 0x72, 0x61, 0x63, 0x6b, 0x49, 0x6e, 0x67, 0x65,
	0x73, 0x74, 0x45, 0x76, 0x65, 0x6e, 0x74, 0x55, 0x70, 0x64, 0x61, 0x74, 0x65, 0x12, 0x2e, 0x0a,
	0x08, 0x65, 0x76, 0x65, 0x6e, 0x74, 0x5f, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x42,
	0x13, 0xfa, 0x42, 0x10, 0x72, 0x0e, 0x32, 0x0c, 0x5e, 0x45, 0x5b, 0x30, 0x2d, 0x39, 0x61, 0x2d,
	0x66, 0x5d, 0x2b, 0x24, 0x52, 0x07, 0x65, 0x76, 0x65, 0x6e, 0x74, 0x49, 0x64, 0x12, 0x43, 0x0a,
	0x0b, 0x65, 0x76, 0x65, 0x6e, 0x74, 0x5f, 0x73, 0x74, 0x61, 0x74, 0x65, 0x18, 0x02, 0x20, 0x01,
	0x28, 0x0b, 0x32, 0x22, 0x2e, 0x61, 0x75, 0x74, 0x6f, 0x6b, 0x69, 0x74, 0x74, 0x65, 0x68, 0x2e,
	0x65, 0x76, 0x65, 0x6e, 0x74, 0x2e, 0x45, 0x76, 0x65, 0x6e, 0x74, 0x53, 0x74, 0x61, 0x74, 0x65,
	0x52, 0x65, 0x63, 0x6f, 0x72, 0x64, 0x52, 0x0a, 0x65, 0x76, 0x65, 0x6e, 0x74, 0x53, 0x74, 0x61,
	0x74, 0x65, 0x12, 0x51, 0x0a, 0x0a, 0x70, 0x72, 0x6f, 0x6a, 0x65, 0x63, 0x74, 0x5f, 0x69, 0x64,
	0x18, 0x03, 0x20, 0x01, 0x28, 0x09, 0x42, 0x32, 0xfa, 0x42, 0x2f, 0x72, 0x2d, 0x32, 0x28, 0x5e,
	0x5b, 0x61, 0x2d, 0x7a, 0x41, 0x2d, 0x5a, 0x5d, 0x5b, 0x30, 0x2d, 0x39, 0x61, 0x2d, 0x7a, 0x41,
	0x2d, 0x5a, 0x5f, 0x2d, 0x5d, 0x2b, 0x5c, 0x2e, 0x5b, 0x61, 0x2d, 0x7a, 0x41, 0x2d, 0x5a, 0x30,
	0x2d, 0x39, 0x5f, 0x2d, 0x5d, 0x2b, 0x24, 0xd0, 0x01, 0x01, 0x52, 0x09, 0x70, 0x72, 0x6f, 0x6a,
	0x65, 0x63, 0x74, 0x49, 0x64, 0x12, 0x59, 0x0a, 0x13, 0x70, 0x72, 0x6f, 0x6a, 0x65, 0x63, 0x74,
	0x5f, 0x65, 0x76, 0x65, 0x6e, 0x74, 0x5f, 0x73, 0x74, 0x61, 0x74, 0x65, 0x18, 0x04, 0x20, 0x01,
	0x28, 0x0b, 0x32, 0x29, 0x2e, 0x61, 0x75, 0x74, 0x6f, 0x6b, 0x69, 0x74, 0x74, 0x65, 0x68, 0x2e,
	0x65, 0x76, 0x65, 0x6e, 0x74, 0x2e, 0x50, 0x72, 0x6f, 0x6a, 0x65, 0x63, 0x74, 0x45, 0x76, 0x65,
	0x6e, 0x74, 0x53, 0x74, 0x61, 0x74, 0x65, 0x52, 0x65, 0x63, 0x6f, 0x72, 0x64, 0x52, 0x11, 0x70,
	0x72, 0x6f, 0x6a, 0x65, 0x63, 0x74, 0x45, 0x76, 0x65, 0x6e, 0x74, 0x53, 0x74, 0x61, 0x74, 0x65,
	0x12, 0x4f, 0x0a, 0x15, 0x66, 0x6c, 0x61, 0x74, 0x74, 0x65, 0x6e, 0x65, 0x64, 0x5f, 0x72, 0x75,
	0x6e, 0x5f, 0x73, 0x75, 0x6d, 0x6d, 0x61, 0x72, 0x79, 0x18, 0x05, 0x20, 0x01, 0x28, 0x0b, 0x32,
	0x1b, 0x2e, 0x61, 0x75, 0x74, 0x6f, 0x6b, 0x69, 0x74, 0x74, 0x65, 0x68, 0x2e, 0x6c, 0x61, 0x6e,
	0x67, 0x2e, 0x52, 0x75, 0x6e, 0x53, 0x75, 0x6d, 0x6d, 0x61, 0x72, 0x79, 0x52, 0x13, 0x66, 0x6c,
	0x61, 0x74, 0x74, 0x65, 0x6e, 0x65, 0x64, 0x52, 0x75, 0x6e, 0x53, 0x75, 0x6d, 0x6d, 0x61, 0x72,
	0x79, 0x42, 0x20, 0x5a, 0x1e, 0x67, 0x6f, 0x2e, 0x61, 0x75, 0x74, 0x6f, 0x6b, 0x69, 0x74, 0x74,
	0x65, 0x68, 0x2e, 0x64, 0x65, 0x76, 0x2f, 0x69, 0x64, 0x6c, 0x2f, 0x67, 0x6f, 0x2f, 0x65, 0x76,
	0x65, 0x6e, 0x74, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_event_track_proto_rawDescOnce sync.Once
	file_event_track_proto_rawDescData = file_event_track_proto_rawDesc
)

func file_event_track_proto_rawDescGZIP() []byte {
	file_event_track_proto_rawDescOnce.Do(func() {
		file_event_track_proto_rawDescData = protoimpl.X.CompressGZIP(file_event_track_proto_rawDescData)
	})
	return file_event_track_proto_rawDescData
}

var file_event_track_proto_msgTypes = make([]protoimpl.MessageInfo, 1)
var file_event_track_proto_goTypes = []interface{}{
	(*TrackIngestEventUpdate)(nil),  // 0: autokitteh.event.TrackIngestEventUpdate
	(*EventStateRecord)(nil),        // 1: autokitteh.event.EventStateRecord
	(*ProjectEventStateRecord)(nil), // 2: autokitteh.event.ProjectEventStateRecord
	(*lang.RunSummary)(nil),         // 3: autokitteh.lang.RunSummary
}
var file_event_track_proto_depIdxs = []int32{
	1, // 0: autokitteh.event.TrackIngestEventUpdate.event_state:type_name -> autokitteh.event.EventStateRecord
	2, // 1: autokitteh.event.TrackIngestEventUpdate.project_event_state:type_name -> autokitteh.event.ProjectEventStateRecord
	3, // 2: autokitteh.event.TrackIngestEventUpdate.flattened_run_summary:type_name -> autokitteh.lang.RunSummary
	3, // [3:3] is the sub-list for method output_type
	3, // [3:3] is the sub-list for method input_type
	3, // [3:3] is the sub-list for extension type_name
	3, // [3:3] is the sub-list for extension extendee
	0, // [0:3] is the sub-list for field type_name
}

func init() { file_event_track_proto_init() }
func file_event_track_proto_init() {
	if File_event_track_proto != nil {
		return
	}
	file_event_event_state_proto_init()
	file_event_project_state_proto_init()
	if !protoimpl.UnsafeEnabled {
		file_event_track_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*TrackIngestEventUpdate); i {
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
			RawDescriptor: file_event_track_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   1,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_event_track_proto_goTypes,
		DependencyIndexes: file_event_track_proto_depIdxs,
		MessageInfos:      file_event_track_proto_msgTypes,
	}.Build()
	File_event_track_proto = out.File
	file_event_track_proto_rawDesc = nil
	file_event_track_proto_goTypes = nil
	file_event_track_proto_depIdxs = nil
}
