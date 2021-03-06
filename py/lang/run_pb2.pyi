"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import program.error_pb2
import program.program_pb2
import typing
import typing_extensions
import values.values_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class RunStateLogRecord(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    T_FIELD_NUMBER: builtins.int
    STATE_FIELD_NUMBER: builtins.int
    SOURCE_FIELD_NUMBER: builtins.int
    @property
    def t(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def state(self) -> global___RunState: ...
    @property
    def source(self) -> program.program_pb2.Path:
        """set only by akd for ui use."""
        pass
    def __init__(self,
        *,
        t: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        state: typing.Optional[global___RunState] = ...,
        source: typing.Optional[program.program_pb2.Path] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["source",b"source","state",b"state","t",b"t"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["source",b"source","state",b"state","t",b"t"]) -> None: ...
global___RunStateLogRecord = RunStateLogRecord

class RunSummary(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    LOG_FIELD_NUMBER: builtins.int
    PRINTS_FIELD_NUMBER: builtins.int
    @property
    def log(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___RunStateLogRecord]: ...
    @property
    def prints(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    def __init__(self,
        *,
        log: typing.Optional[typing.Iterable[global___RunStateLogRecord]] = ...,
        prints: typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["log",b"log","prints",b"prints"]) -> None: ...
global___RunSummary = RunSummary

class RunState(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    RUNNING_FIELD_NUMBER: builtins.int
    CALL_FIELD_NUMBER: builtins.int
    LOAD_FIELD_NUMBER: builtins.int
    COMPLETED_FIELD_NUMBER: builtins.int
    CANCELED_FIELD_NUMBER: builtins.int
    ERROR_FIELD_NUMBER: builtins.int
    PRINT_FIELD_NUMBER: builtins.int
    CALLRET_FIELD_NUMBER: builtins.int
    LOADRET_FIELD_NUMBER: builtins.int
    CLIENT_ERROR_FIELD_NUMBER: builtins.int
    @property
    def running(self) -> global___RunningRunState: ...
    @property
    def call(self) -> global___CallWaitRunState:
        """waiting for callback response."""
        pass
    @property
    def load(self) -> global___LoadWaitRunState:
        """waiting for load response."""
        pass
    @property
    def completed(self) -> global___CompletedRunState:
        """successfuly, otherwise error."""
        pass
    @property
    def canceled(self) -> global___CanceledRunState: ...
    @property
    def error(self) -> global___ErrorRunState: ...
    @property
    def print(self) -> global___PrintRunUpdate:
        """These are not a states, just logs of events that happened for the record.
        sent to client.
        """
        pass
    @property
    def callret(self) -> global___CallReturnedRunUpdate:
        """not sent to client."""
        pass
    @property
    def loadret(self) -> global___LoadReturnedRunUpdate:
        """not sent to client."""
        pass
    @property
    def client_error(self) -> global___ClientErrorRunState:
        """Generated only in a client."""
        pass
    def __init__(self,
        *,
        running: typing.Optional[global___RunningRunState] = ...,
        call: typing.Optional[global___CallWaitRunState] = ...,
        load: typing.Optional[global___LoadWaitRunState] = ...,
        completed: typing.Optional[global___CompletedRunState] = ...,
        canceled: typing.Optional[global___CanceledRunState] = ...,
        error: typing.Optional[global___ErrorRunState] = ...,
        print: typing.Optional[global___PrintRunUpdate] = ...,
        callret: typing.Optional[global___CallReturnedRunUpdate] = ...,
        loadret: typing.Optional[global___LoadReturnedRunUpdate] = ...,
        client_error: typing.Optional[global___ClientErrorRunState] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["call",b"call","callret",b"callret","canceled",b"canceled","client_error",b"client_error","completed",b"completed","error",b"error","load",b"load","loadret",b"loadret","print",b"print","running",b"running","type",b"type"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["call",b"call","callret",b"callret","canceled",b"canceled","client_error",b"client_error","completed",b"completed","error",b"error","load",b"load","loadret",b"loadret","print",b"print","running",b"running","type",b"type"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["type",b"type"]) -> typing.Optional[typing_extensions.Literal["running","call","load","completed","canceled","error","print","callret","loadret","client_error"]]: ...
global___RunState = RunState

class RunningRunState(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___RunningRunState = RunningRunState

class CallWaitRunState(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class KwsEntry(google.protobuf.message.Message):
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

    CALL_FIELD_NUMBER: builtins.int
    ARGS_FIELD_NUMBER: builtins.int
    KWS_FIELD_NUMBER: builtins.int
    @property
    def call(self) -> values.values_pb2.Value: ...
    @property
    def args(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[values.values_pb2.Value]: ...
    @property
    def kws(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, values.values_pb2.Value]: ...
    def __init__(self,
        *,
        call: typing.Optional[values.values_pb2.Value] = ...,
        args: typing.Optional[typing.Iterable[values.values_pb2.Value]] = ...,
        kws: typing.Optional[typing.Mapping[typing.Text, values.values_pb2.Value]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["call",b"call"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["args",b"args","call",b"call","kws",b"kws"]) -> None: ...
global___CallWaitRunState = CallWaitRunState

class LoadWaitRunState(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PATH_FIELD_NUMBER: builtins.int
    @property
    def path(self) -> program.program_pb2.Path: ...
    def __init__(self,
        *,
        path: typing.Optional[program.program_pb2.Path] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["path",b"path"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["path",b"path"]) -> None: ...
global___LoadWaitRunState = LoadWaitRunState

class CompletedRunState(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class ValsEntry(google.protobuf.message.Message):
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

    VALS_FIELD_NUMBER: builtins.int
    @property
    def vals(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, values.values_pb2.Value]: ...
    def __init__(self,
        *,
        vals: typing.Optional[typing.Mapping[typing.Text, values.values_pb2.Value]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["vals",b"vals"]) -> None: ...
global___CompletedRunState = CompletedRunState

class CanceledRunState(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    REASON_FIELD_NUMBER: builtins.int
    CALLSTACK_FIELD_NUMBER: builtins.int
    reason: typing.Text
    @property
    def callstack(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[program.error_pb2.CallFrame]: ...
    def __init__(self,
        *,
        reason: typing.Text = ...,
        callstack: typing.Optional[typing.Iterable[program.error_pb2.CallFrame]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["callstack",b"callstack","reason",b"reason"]) -> None: ...
global___CanceledRunState = CanceledRunState

class ErrorRunState(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ERROR_FIELD_NUMBER: builtins.int
    @property
    def error(self) -> program.error_pb2.Error: ...
    def __init__(self,
        *,
        error: typing.Optional[program.error_pb2.Error] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["error",b"error"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["error",b"error"]) -> None: ...
global___ErrorRunState = ErrorRunState

class PrintRunUpdate(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TEXT_FIELD_NUMBER: builtins.int
    text: typing.Text
    def __init__(self,
        *,
        text: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["text",b"text"]) -> None: ...
global___PrintRunUpdate = PrintRunUpdate

class CallReturnedRunUpdate(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ERROR_FIELD_NUMBER: builtins.int
    RETVAL_FIELD_NUMBER: builtins.int
    @property
    def error(self) -> program.error_pb2.Error: ...
    @property
    def retval(self) -> values.values_pb2.Value: ...
    def __init__(self,
        *,
        error: typing.Optional[program.error_pb2.Error] = ...,
        retval: typing.Optional[values.values_pb2.Value] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["error",b"error","retval",b"retval"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["error",b"error","retval",b"retval"]) -> None: ...
global___CallReturnedRunUpdate = CallReturnedRunUpdate

class LoadReturnedRunUpdate(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class ValsEntry(google.protobuf.message.Message):
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

    ERROR_FIELD_NUMBER: builtins.int
    RUN_SUMMARY_FIELD_NUMBER: builtins.int
    VALS_FIELD_NUMBER: builtins.int
    @property
    def error(self) -> program.error_pb2.Error: ...
    @property
    def run_summary(self) -> global___RunSummary: ...
    @property
    def vals(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, values.values_pb2.Value]: ...
    def __init__(self,
        *,
        error: typing.Optional[program.error_pb2.Error] = ...,
        run_summary: typing.Optional[global___RunSummary] = ...,
        vals: typing.Optional[typing.Mapping[typing.Text, values.values_pb2.Value]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["error",b"error","run_summary",b"run_summary"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["error",b"error","run_summary",b"run_summary","vals",b"vals"]) -> None: ...
global___LoadReturnedRunUpdate = LoadReturnedRunUpdate

class ClientErrorRunState(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ERROR_FIELD_NUMBER: builtins.int
    error: typing.Text
    def __init__(self,
        *,
        error: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["error",b"error"]) -> None: ...
global___ClientErrorRunState = ClientErrorRunState
