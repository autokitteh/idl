"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class AccountSettings(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class MemoEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text
        value: typing.Text
        def __init__(self,
            *,
            key: typing.Text = ...,
            value: typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    ENABLED_FIELD_NUMBER: builtins.int
    MEMO_FIELD_NUMBER: builtins.int
    enabled: builtins.bool
    @property
    def memo(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]:
        """General human readable data about the account.
        Not used for any automation.
        """
        pass
    def __init__(self,
        *,
        enabled: builtins.bool = ...,
        memo: typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["enabled",b"enabled","memo",b"memo"]) -> None: ...
global___AccountSettings = AccountSettings

class Account(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    SETTINGS_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    UPDATED_AT_FIELD_NUMBER: builtins.int
    name: typing.Text
    @property
    def settings(self) -> global___AccountSettings: ...
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def updated_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    def __init__(self,
        *,
        name: typing.Text = ...,
        settings: typing.Optional[global___AccountSettings] = ...,
        created_at: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        updated_at: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["created_at",b"created_at","settings",b"settings","updated_at",b"updated_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["created_at",b"created_at","name",b"name","settings",b"settings","updated_at",b"updated_at"]) -> None: ...
global___Account = Account
