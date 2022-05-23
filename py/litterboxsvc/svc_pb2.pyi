"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import lang.run_pb2
import typing
import typing_extensions
import values.values_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class SyntheticEvent(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class DataEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text
        @property
        def value(self) -> values.values_pb2.Value: ...
        def __init__(self,
            *,
            key: typing.Text = ...,
            value: typing.Optional[values.values_pb2.Value] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value",b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

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

    SRC_ID_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    DATA_FIELD_NUMBER: builtins.int
    ORIGINAL_ID_FIELD_NUMBER: builtins.int
    MEMO_FIELD_NUMBER: builtins.int
    src_id: typing.Text
    type: typing.Text
    @property
    def data(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, values.values_pb2.Value]: ...
    original_id: typing.Text
    @property
    def memo(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]:
        """for caller use only - not used in event processing."""
        pass
    def __init__(self,
        *,
        src_id: typing.Text = ...,
        type: typing.Text = ...,
        data: typing.Optional[typing.Mapping[typing.Text, values.values_pb2.Value]] = ...,
        original_id: typing.Text = ...,
        memo: typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["data",b"data","memo",b"memo","original_id",b"original_id","src_id",b"src_id","type",b"type"]) -> None: ...
global___SyntheticEvent = SyntheticEvent

class RunRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SOURCE_FIELD_NUMBER: builtins.int
    EVENT_FIELD_NUMBER: builtins.int
    source: typing.Text
    @property
    def event(self) -> global___SyntheticEvent: ...
    def __init__(self,
        *,
        source: typing.Text = ...,
        event: typing.Optional[global___SyntheticEvent] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["event",b"event"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["event",b"event","source",b"source"]) -> None: ...
global___RunRequest = RunRequest

class RunUpdate(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    T_FIELD_NUMBER: builtins.int
    STATE_FIELD_NUMBER: builtins.int
    @property
    def t(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def state(self) -> lang.run_pb2.RunState: ...
    def __init__(self,
        *,
        t: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        state: typing.Optional[lang.run_pb2.RunState] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["state",b"state","t",b"t"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["state",b"state","t",b"t"]) -> None: ...
global___RunUpdate = RunUpdate
