"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class Path(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SCHEME_FIELD_NUMBER: builtins.int
    PATH_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    scheme: typing.Text
    path: typing.Text
    version: typing.Text
    def __init__(self,
        *,
        scheme: typing.Text = ...,
        path: typing.Text = ...,
        version: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["path",b"path","scheme",b"scheme","version",b"version"]) -> None: ...
global___Path = Path

class Location(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PATH_FIELD_NUMBER: builtins.int
    LINE_FIELD_NUMBER: builtins.int
    COLUMN_FIELD_NUMBER: builtins.int
    @property
    def path(self) -> global___Path: ...
    line: builtins.int
    column: builtins.int
    def __init__(self,
        *,
        path: typing.Optional[global___Path] = ...,
        line: builtins.int = ...,
        column: builtins.int = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["path",b"path"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["column",b"column","line",b"line","path",b"path"]) -> None: ...
global___Location = Location

class Module(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    LANG_FIELD_NUMBER: builtins.int
    PREDECLS_FIELD_NUMBER: builtins.int
    COMPILER_VERSION_FIELD_NUMBER: builtins.int
    SOURCE_PATH_FIELD_NUMBER: builtins.int
    COMPILED_CODE_FIELD_NUMBER: builtins.int
    lang: typing.Text
    """starlark, lua, some-kind-of-yaml, etc..."""

    @property
    def predecls(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    compiler_version: typing.Text
    @property
    def source_path(self) -> global___Path: ...
    compiled_code: builtins.bytes
    """if empty, fetch from path."""

    def __init__(self,
        *,
        lang: typing.Text = ...,
        predecls: typing.Optional[typing.Iterable[typing.Text]] = ...,
        compiler_version: typing.Text = ...,
        source_path: typing.Optional[global___Path] = ...,
        compiled_code: builtins.bytes = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["source_path",b"source_path"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["compiled_code",b"compiled_code","compiler_version",b"compiler_version","lang",b"lang","predecls",b"predecls","source_path",b"source_path"]) -> None: ...
global___Module = Module
