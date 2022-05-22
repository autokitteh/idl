"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import program.program_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class Cycle(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PATHS_FIELD_NUMBER: builtins.int
    @property
    def paths(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[program.program_pb2.Path]: ...
    def __init__(self,
        *,
        paths: typing.Optional[typing.Iterable[program.program_pb2.Path]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["paths",b"paths"]) -> None: ...
global___Cycle = Cycle

class Dependencies(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    READY_FIELD_NUMBER: builtins.int
    MISSING_FIELD_NUMBER: builtins.int
    CYCLES_FIELD_NUMBER: builtins.int
    @property
    def ready(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[program.program_pb2.Path]: ...
    @property
    def missing(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[program.program_pb2.Path]: ...
    @property
    def cycles(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Cycle]: ...
    def __init__(self,
        *,
        ready: typing.Optional[typing.Iterable[program.program_pb2.Path]] = ...,
        missing: typing.Optional[typing.Iterable[program.program_pb2.Path]] = ...,
        cycles: typing.Optional[typing.Iterable[global___Cycle]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cycles",b"cycles","missing",b"missing","ready",b"ready"]) -> None: ...
global___Dependencies = Dependencies

class GetModuleDependenciesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    MODULE_FIELD_NUMBER: builtins.int
    @property
    def module(self) -> program.program_pb2.Module: ...
    def __init__(self,
        *,
        module: typing.Optional[program.program_pb2.Module] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["module",b"module"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["module",b"module"]) -> None: ...
global___GetModuleDependenciesRequest = GetModuleDependenciesRequest

class GetModuleDependenciesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DEPS_FIELD_NUMBER: builtins.int
    @property
    def deps(self) -> global___Dependencies: ...
    def __init__(self,
        *,
        deps: typing.Optional[global___Dependencies] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["deps",b"deps"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["deps",b"deps"]) -> None: ...
global___GetModuleDependenciesResponse = GetModuleDependenciesResponse

class IsCompilerVersionSupportedRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    LANG_FIELD_NUMBER: builtins.int
    VER_FIELD_NUMBER: builtins.int
    lang: typing.Text
    ver: typing.Text
    def __init__(self,
        *,
        lang: typing.Text = ...,
        ver: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["lang",b"lang","ver",b"ver"]) -> None: ...
global___IsCompilerVersionSupportedRequest = IsCompilerVersionSupportedRequest

class IsCompilerVersionSupportedResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SUPPORTED_FIELD_NUMBER: builtins.int
    supported: builtins.bool
    def __init__(self,
        *,
        supported: builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["supported",b"supported"]) -> None: ...
global___IsCompilerVersionSupportedResponse = IsCompilerVersionSupportedResponse

class CompileModuleRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    LANG_FIELD_NUMBER: builtins.int
    PREDECLS_FIELD_NUMBER: builtins.int
    PATH_FIELD_NUMBER: builtins.int
    SRC_FIELD_NUMBER: builtins.int
    GET_DEPS_FIELD_NUMBER: builtins.int
    lang: typing.Text
    @property
    def predecls(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    @property
    def path(self) -> program.program_pb2.Path: ...
    src: builtins.bytes
    get_deps: builtins.bool
    def __init__(self,
        *,
        lang: typing.Text = ...,
        predecls: typing.Optional[typing.Iterable[typing.Text]] = ...,
        path: typing.Optional[program.program_pb2.Path] = ...,
        src: builtins.bytes = ...,
        get_deps: builtins.bool = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["path",b"path"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["get_deps",b"get_deps","lang",b"lang","path",b"path","predecls",b"predecls","src",b"src"]) -> None: ...
global___CompileModuleRequest = CompileModuleRequest

class CompileModuleResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    MODULE_FIELD_NUMBER: builtins.int
    DEPS_FIELD_NUMBER: builtins.int
    @property
    def module(self) -> program.program_pb2.Module: ...
    @property
    def deps(self) -> global___Dependencies:
        """if req.get_deps. only the ready field is populated for now."""
        pass
    def __init__(self,
        *,
        module: typing.Optional[program.program_pb2.Module] = ...,
        deps: typing.Optional[global___Dependencies] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["deps",b"deps","module",b"module"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["deps",b"deps","module",b"module"]) -> None: ...
global___CompileModuleResponse = CompileModuleResponse

class ListLangsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___ListLangsRequest = ListLangsRequest

class CatalogLang(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    EXTS_FIELD_NUMBER: builtins.int
    @property
    def exts(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    def __init__(self,
        *,
        exts: typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["exts",b"exts"]) -> None: ...
global___CatalogLang = CatalogLang

class ListLangsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class LangsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text
        @property
        def value(self) -> global___CatalogLang: ...
        def __init__(self,
            *,
            key: typing.Text = ...,
            value: typing.Optional[global___CatalogLang] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value",b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    LANGS_FIELD_NUMBER: builtins.int
    @property
    def langs(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, global___CatalogLang]: ...
    def __init__(self,
        *,
        langs: typing.Optional[typing.Mapping[typing.Text, global___CatalogLang]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["langs",b"langs"]) -> None: ...
global___ListLangsResponse = ListLangsResponse
