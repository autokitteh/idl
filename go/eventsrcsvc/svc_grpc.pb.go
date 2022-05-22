// Code generated by protoc-gen-go-grpc. DO NOT EDIT.

package eventsrcsvc

import (
	context "context"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
)

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
// Requires gRPC-Go v1.32.0 or later.
const _ = grpc.SupportPackageIsVersion7

// EventSourcesClient is the client API for EventSources service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type EventSourcesClient interface {
	AddEventSource(ctx context.Context, in *AddEventSourceRequest, opts ...grpc.CallOption) (*AddEventSourceResponse, error)
	UpdateEventSource(ctx context.Context, in *UpdateEventSourceRequest, opts ...grpc.CallOption) (*UpdateEventSourceResponse, error)
	GetEventSource(ctx context.Context, in *GetEventSourceRequest, opts ...grpc.CallOption) (*GetEventSourceResponse, error)
	AddEventSourceProjectBinding(ctx context.Context, in *AddEventSourceProjectBindingRequest, opts ...grpc.CallOption) (*AddEventSourceProjectBindingResponse, error)
	UpdateEventSourceProjectBinding(ctx context.Context, in *UpdateEventSourceProjectBindingRequest, opts ...grpc.CallOption) (*UpdateEventSourceProjectBindingResponse, error)
	GetEventSourceProjectBindings(ctx context.Context, in *GetEventSourceProjectBindingsRequest, opts ...grpc.CallOption) (*GetEventSourceProjectBindingsResponse, error)
	ListEventSources(ctx context.Context, in *ListEventSourcesRequest, opts ...grpc.CallOption) (*ListEventSourcesResponse, error)
}

type eventSourcesClient struct {
	cc grpc.ClientConnInterface
}

func NewEventSourcesClient(cc grpc.ClientConnInterface) EventSourcesClient {
	return &eventSourcesClient{cc}
}

func (c *eventSourcesClient) AddEventSource(ctx context.Context, in *AddEventSourceRequest, opts ...grpc.CallOption) (*AddEventSourceResponse, error) {
	out := new(AddEventSourceResponse)
	err := c.cc.Invoke(ctx, "/autokitteh.eventsrcsvc.EventSources/AddEventSource", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *eventSourcesClient) UpdateEventSource(ctx context.Context, in *UpdateEventSourceRequest, opts ...grpc.CallOption) (*UpdateEventSourceResponse, error) {
	out := new(UpdateEventSourceResponse)
	err := c.cc.Invoke(ctx, "/autokitteh.eventsrcsvc.EventSources/UpdateEventSource", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *eventSourcesClient) GetEventSource(ctx context.Context, in *GetEventSourceRequest, opts ...grpc.CallOption) (*GetEventSourceResponse, error) {
	out := new(GetEventSourceResponse)
	err := c.cc.Invoke(ctx, "/autokitteh.eventsrcsvc.EventSources/GetEventSource", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *eventSourcesClient) AddEventSourceProjectBinding(ctx context.Context, in *AddEventSourceProjectBindingRequest, opts ...grpc.CallOption) (*AddEventSourceProjectBindingResponse, error) {
	out := new(AddEventSourceProjectBindingResponse)
	err := c.cc.Invoke(ctx, "/autokitteh.eventsrcsvc.EventSources/AddEventSourceProjectBinding", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *eventSourcesClient) UpdateEventSourceProjectBinding(ctx context.Context, in *UpdateEventSourceProjectBindingRequest, opts ...grpc.CallOption) (*UpdateEventSourceProjectBindingResponse, error) {
	out := new(UpdateEventSourceProjectBindingResponse)
	err := c.cc.Invoke(ctx, "/autokitteh.eventsrcsvc.EventSources/UpdateEventSourceProjectBinding", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *eventSourcesClient) GetEventSourceProjectBindings(ctx context.Context, in *GetEventSourceProjectBindingsRequest, opts ...grpc.CallOption) (*GetEventSourceProjectBindingsResponse, error) {
	out := new(GetEventSourceProjectBindingsResponse)
	err := c.cc.Invoke(ctx, "/autokitteh.eventsrcsvc.EventSources/GetEventSourceProjectBindings", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *eventSourcesClient) ListEventSources(ctx context.Context, in *ListEventSourcesRequest, opts ...grpc.CallOption) (*ListEventSourcesResponse, error) {
	out := new(ListEventSourcesResponse)
	err := c.cc.Invoke(ctx, "/autokitteh.eventsrcsvc.EventSources/ListEventSources", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// EventSourcesServer is the server API for EventSources service.
// All implementations must embed UnimplementedEventSourcesServer
// for forward compatibility
type EventSourcesServer interface {
	AddEventSource(context.Context, *AddEventSourceRequest) (*AddEventSourceResponse, error)
	UpdateEventSource(context.Context, *UpdateEventSourceRequest) (*UpdateEventSourceResponse, error)
	GetEventSource(context.Context, *GetEventSourceRequest) (*GetEventSourceResponse, error)
	AddEventSourceProjectBinding(context.Context, *AddEventSourceProjectBindingRequest) (*AddEventSourceProjectBindingResponse, error)
	UpdateEventSourceProjectBinding(context.Context, *UpdateEventSourceProjectBindingRequest) (*UpdateEventSourceProjectBindingResponse, error)
	GetEventSourceProjectBindings(context.Context, *GetEventSourceProjectBindingsRequest) (*GetEventSourceProjectBindingsResponse, error)
	ListEventSources(context.Context, *ListEventSourcesRequest) (*ListEventSourcesResponse, error)
	mustEmbedUnimplementedEventSourcesServer()
}

// UnimplementedEventSourcesServer must be embedded to have forward compatible implementations.
type UnimplementedEventSourcesServer struct {
}

func (UnimplementedEventSourcesServer) AddEventSource(context.Context, *AddEventSourceRequest) (*AddEventSourceResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method AddEventSource not implemented")
}
func (UnimplementedEventSourcesServer) UpdateEventSource(context.Context, *UpdateEventSourceRequest) (*UpdateEventSourceResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method UpdateEventSource not implemented")
}
func (UnimplementedEventSourcesServer) GetEventSource(context.Context, *GetEventSourceRequest) (*GetEventSourceResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetEventSource not implemented")
}
func (UnimplementedEventSourcesServer) AddEventSourceProjectBinding(context.Context, *AddEventSourceProjectBindingRequest) (*AddEventSourceProjectBindingResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method AddEventSourceProjectBinding not implemented")
}
func (UnimplementedEventSourcesServer) UpdateEventSourceProjectBinding(context.Context, *UpdateEventSourceProjectBindingRequest) (*UpdateEventSourceProjectBindingResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method UpdateEventSourceProjectBinding not implemented")
}
func (UnimplementedEventSourcesServer) GetEventSourceProjectBindings(context.Context, *GetEventSourceProjectBindingsRequest) (*GetEventSourceProjectBindingsResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetEventSourceProjectBindings not implemented")
}
func (UnimplementedEventSourcesServer) ListEventSources(context.Context, *ListEventSourcesRequest) (*ListEventSourcesResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ListEventSources not implemented")
}
func (UnimplementedEventSourcesServer) mustEmbedUnimplementedEventSourcesServer() {}

// UnsafeEventSourcesServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to EventSourcesServer will
// result in compilation errors.
type UnsafeEventSourcesServer interface {
	mustEmbedUnimplementedEventSourcesServer()
}

func RegisterEventSourcesServer(s grpc.ServiceRegistrar, srv EventSourcesServer) {
	s.RegisterService(&EventSources_ServiceDesc, srv)
}

func _EventSources_AddEventSource_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(AddEventSourceRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(EventSourcesServer).AddEventSource(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/autokitteh.eventsrcsvc.EventSources/AddEventSource",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(EventSourcesServer).AddEventSource(ctx, req.(*AddEventSourceRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _EventSources_UpdateEventSource_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(UpdateEventSourceRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(EventSourcesServer).UpdateEventSource(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/autokitteh.eventsrcsvc.EventSources/UpdateEventSource",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(EventSourcesServer).UpdateEventSource(ctx, req.(*UpdateEventSourceRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _EventSources_GetEventSource_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GetEventSourceRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(EventSourcesServer).GetEventSource(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/autokitteh.eventsrcsvc.EventSources/GetEventSource",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(EventSourcesServer).GetEventSource(ctx, req.(*GetEventSourceRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _EventSources_AddEventSourceProjectBinding_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(AddEventSourceProjectBindingRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(EventSourcesServer).AddEventSourceProjectBinding(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/autokitteh.eventsrcsvc.EventSources/AddEventSourceProjectBinding",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(EventSourcesServer).AddEventSourceProjectBinding(ctx, req.(*AddEventSourceProjectBindingRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _EventSources_UpdateEventSourceProjectBinding_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(UpdateEventSourceProjectBindingRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(EventSourcesServer).UpdateEventSourceProjectBinding(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/autokitteh.eventsrcsvc.EventSources/UpdateEventSourceProjectBinding",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(EventSourcesServer).UpdateEventSourceProjectBinding(ctx, req.(*UpdateEventSourceProjectBindingRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _EventSources_GetEventSourceProjectBindings_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GetEventSourceProjectBindingsRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(EventSourcesServer).GetEventSourceProjectBindings(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/autokitteh.eventsrcsvc.EventSources/GetEventSourceProjectBindings",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(EventSourcesServer).GetEventSourceProjectBindings(ctx, req.(*GetEventSourceProjectBindingsRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _EventSources_ListEventSources_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ListEventSourcesRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(EventSourcesServer).ListEventSources(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/autokitteh.eventsrcsvc.EventSources/ListEventSources",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(EventSourcesServer).ListEventSources(ctx, req.(*ListEventSourcesRequest))
	}
	return interceptor(ctx, in, info, handler)
}

// EventSources_ServiceDesc is the grpc.ServiceDesc for EventSources service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var EventSources_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "autokitteh.eventsrcsvc.EventSources",
	HandlerType: (*EventSourcesServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "AddEventSource",
			Handler:    _EventSources_AddEventSource_Handler,
		},
		{
			MethodName: "UpdateEventSource",
			Handler:    _EventSources_UpdateEventSource_Handler,
		},
		{
			MethodName: "GetEventSource",
			Handler:    _EventSources_GetEventSource_Handler,
		},
		{
			MethodName: "AddEventSourceProjectBinding",
			Handler:    _EventSources_AddEventSourceProjectBinding_Handler,
		},
		{
			MethodName: "UpdateEventSourceProjectBinding",
			Handler:    _EventSources_UpdateEventSourceProjectBinding_Handler,
		},
		{
			MethodName: "GetEventSourceProjectBindings",
			Handler:    _EventSources_GetEventSourceProjectBindings_Handler,
		},
		{
			MethodName: "ListEventSources",
			Handler:    _EventSources_ListEventSources_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "eventsrcsvc/svc.proto",
}