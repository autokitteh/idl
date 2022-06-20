"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class PluginExecutionSettings(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PATH_FIELD_NUMBER: builtins.int
    path: typing.Text
    def __init__(self,
        *,
        path: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["path",b"path"]) -> None: ...
global___PluginExecutionSettings = PluginExecutionSettings

class PluginSettings(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ENABLED_FIELD_NUMBER: builtins.int
    ADDRESS_FIELD_NUMBER: builtins.int
    PORT_FIELD_NUMBER: builtins.int
    EXEC_FIELD_NUMBER: builtins.int
    enabled: builtins.bool
    address: typing.Text
    port: builtins.int
    @property
    def exec(self) -> global___PluginExecutionSettings: ...
    def __init__(self,
        *,
        enabled: builtins.bool = ...,
        address: typing.Text = ...,
        port: builtins.int = ...,
        exec: typing.Optional[global___PluginExecutionSettings] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["exec",b"exec"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["address",b"address","enabled",b"enabled","exec",b"exec","port",b"port"]) -> None: ...
global___PluginSettings = PluginSettings

class Plugin(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    SETTINGS_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    UPDATED_AT_FIELD_NUMBER: builtins.int
    id: typing.Text
    @property
    def settings(self) -> global___PluginSettings: ...
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def updated_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    def __init__(self,
        *,
        id: typing.Text = ...,
        settings: typing.Optional[global___PluginSettings] = ...,
        created_at: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        updated_at: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["created_at",b"created_at","settings",b"settings","updated_at",b"updated_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["created_at",b"created_at","id",b"id","settings",b"settings","updated_at",b"updated_at"]) -> None: ...
global___Plugin = Plugin
