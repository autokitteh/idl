"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import plugin.plugin_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class RegisterRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    SETTINGS_FIELD_NUMBER: builtins.int
    id: typing.Text
    @property
    def settings(self) -> plugin.plugin_pb2.PluginSettings: ...
    def __init__(self,
        *,
        id: typing.Text = ...,
        settings: typing.Optional[plugin.plugin_pb2.PluginSettings] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["settings",b"settings"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["id",b"id","settings",b"settings"]) -> None: ...
global___RegisterRequest = RegisterRequest

class RegisterResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___RegisterResponse = RegisterResponse

class ListRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ACCOUNT_NAME_FIELD_NUMBER: builtins.int
    account_name: typing.Text
    """optional filter."""

    def __init__(self,
        *,
        account_name: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["account_name",b"account_name"]) -> None: ...
global___ListRequest = ListRequest

class ListResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    IDS_FIELD_NUMBER: builtins.int
    @property
    def ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    def __init__(self,
        *,
        ids: typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["ids",b"ids"]) -> None: ...
global___ListResponse = ListResponse

class GetRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    id: typing.Text
    def __init__(self,
        *,
        id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["id",b"id"]) -> None: ...
global___GetRequest = GetRequest

class GetResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PLUGIN_FIELD_NUMBER: builtins.int
    @property
    def plugin(self) -> plugin.plugin_pb2.Plugin: ...
    def __init__(self,
        *,
        plugin: typing.Optional[plugin.plugin_pb2.Plugin] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["plugin",b"plugin"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["plugin",b"plugin"]) -> None: ...
global___GetResponse = GetResponse
