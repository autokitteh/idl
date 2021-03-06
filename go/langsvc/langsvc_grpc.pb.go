// Code generated by protoc-gen-go-grpc. DO NOT EDIT.

package langsvc

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

// LangClient is the client API for Lang service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type LangClient interface {
	ListLangs(ctx context.Context, in *ListLangsRequest, opts ...grpc.CallOption) (*ListLangsResponse, error)
	IsCompilerVersionSupported(ctx context.Context, in *IsCompilerVersionSupportedRequest, opts ...grpc.CallOption) (*IsCompilerVersionSupportedResponse, error)
	GetModuleDependencies(ctx context.Context, in *GetModuleDependenciesRequest, opts ...grpc.CallOption) (*GetModuleDependenciesResponse, error)
	CompileModule(ctx context.Context, in *CompileModuleRequest, opts ...grpc.CallOption) (*CompileModuleResponse, error)
}

type langClient struct {
	cc grpc.ClientConnInterface
}

func NewLangClient(cc grpc.ClientConnInterface) LangClient {
	return &langClient{cc}
}

func (c *langClient) ListLangs(ctx context.Context, in *ListLangsRequest, opts ...grpc.CallOption) (*ListLangsResponse, error) {
	out := new(ListLangsResponse)
	err := c.cc.Invoke(ctx, "/autokitteh.langsvc.Lang/ListLangs", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *langClient) IsCompilerVersionSupported(ctx context.Context, in *IsCompilerVersionSupportedRequest, opts ...grpc.CallOption) (*IsCompilerVersionSupportedResponse, error) {
	out := new(IsCompilerVersionSupportedResponse)
	err := c.cc.Invoke(ctx, "/autokitteh.langsvc.Lang/IsCompilerVersionSupported", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *langClient) GetModuleDependencies(ctx context.Context, in *GetModuleDependenciesRequest, opts ...grpc.CallOption) (*GetModuleDependenciesResponse, error) {
	out := new(GetModuleDependenciesResponse)
	err := c.cc.Invoke(ctx, "/autokitteh.langsvc.Lang/GetModuleDependencies", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *langClient) CompileModule(ctx context.Context, in *CompileModuleRequest, opts ...grpc.CallOption) (*CompileModuleResponse, error) {
	out := new(CompileModuleResponse)
	err := c.cc.Invoke(ctx, "/autokitteh.langsvc.Lang/CompileModule", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// LangServer is the server API for Lang service.
// All implementations must embed UnimplementedLangServer
// for forward compatibility
type LangServer interface {
	ListLangs(context.Context, *ListLangsRequest) (*ListLangsResponse, error)
	IsCompilerVersionSupported(context.Context, *IsCompilerVersionSupportedRequest) (*IsCompilerVersionSupportedResponse, error)
	GetModuleDependencies(context.Context, *GetModuleDependenciesRequest) (*GetModuleDependenciesResponse, error)
	CompileModule(context.Context, *CompileModuleRequest) (*CompileModuleResponse, error)
	mustEmbedUnimplementedLangServer()
}

// UnimplementedLangServer must be embedded to have forward compatible implementations.
type UnimplementedLangServer struct {
}

func (UnimplementedLangServer) ListLangs(context.Context, *ListLangsRequest) (*ListLangsResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ListLangs not implemented")
}
func (UnimplementedLangServer) IsCompilerVersionSupported(context.Context, *IsCompilerVersionSupportedRequest) (*IsCompilerVersionSupportedResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method IsCompilerVersionSupported not implemented")
}
func (UnimplementedLangServer) GetModuleDependencies(context.Context, *GetModuleDependenciesRequest) (*GetModuleDependenciesResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetModuleDependencies not implemented")
}
func (UnimplementedLangServer) CompileModule(context.Context, *CompileModuleRequest) (*CompileModuleResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method CompileModule not implemented")
}
func (UnimplementedLangServer) mustEmbedUnimplementedLangServer() {}

// UnsafeLangServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to LangServer will
// result in compilation errors.
type UnsafeLangServer interface {
	mustEmbedUnimplementedLangServer()
}

func RegisterLangServer(s grpc.ServiceRegistrar, srv LangServer) {
	s.RegisterService(&Lang_ServiceDesc, srv)
}

func _Lang_ListLangs_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ListLangsRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(LangServer).ListLangs(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/autokitteh.langsvc.Lang/ListLangs",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(LangServer).ListLangs(ctx, req.(*ListLangsRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _Lang_IsCompilerVersionSupported_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(IsCompilerVersionSupportedRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(LangServer).IsCompilerVersionSupported(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/autokitteh.langsvc.Lang/IsCompilerVersionSupported",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(LangServer).IsCompilerVersionSupported(ctx, req.(*IsCompilerVersionSupportedRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _Lang_GetModuleDependencies_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GetModuleDependenciesRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(LangServer).GetModuleDependencies(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/autokitteh.langsvc.Lang/GetModuleDependencies",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(LangServer).GetModuleDependencies(ctx, req.(*GetModuleDependenciesRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _Lang_CompileModule_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(CompileModuleRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(LangServer).CompileModule(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/autokitteh.langsvc.Lang/CompileModule",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(LangServer).CompileModule(ctx, req.(*CompileModuleRequest))
	}
	return interceptor(ctx, in, info, handler)
}

// Lang_ServiceDesc is the grpc.ServiceDesc for Lang service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var Lang_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "autokitteh.langsvc.Lang",
	HandlerType: (*LangServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "ListLangs",
			Handler:    _Lang_ListLangs_Handler,
		},
		{
			MethodName: "IsCompilerVersionSupported",
			Handler:    _Lang_IsCompilerVersionSupported_Handler,
		},
		{
			MethodName: "GetModuleDependencies",
			Handler:    _Lang_GetModuleDependencies_Handler,
		},
		{
			MethodName: "CompileModule",
			Handler:    _Lang_CompileModule_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "langsvc/langsvc.proto",
}
