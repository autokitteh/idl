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
import program.error_pb2
import program.program_pb2
import typing
import typing_extensions
import values.values_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class RunRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class PredeclsEntry(google.protobuf.message.Message):
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

    SCOPE_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    MODULE_FIELD_NUMBER: builtins.int
    PREDECLS_FIELD_NUMBER: builtins.int
    scope: typing.Text
    id: typing.Text
    @property
    def module(self) -> program.program_pb2.Module: ...
    @property
    def predecls(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, values.values_pb2.Value]: ...
    def __init__(self,
        *,
        scope: typing.Text = ...,
        id: typing.Text = ...,
        module: typing.Optional[program.program_pb2.Module] = ...,
        predecls: typing.Optional[typing.Mapping[typing.Text, values.values_pb2.Value]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["module",b"module"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["id",b"id","module",b"module","predecls",b"predecls","scope",b"scope"]) -> None: ...
global___RunRequest = RunRequest

class CallFunctionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class KwargsEntry(google.protobuf.message.Message):
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

    RUN_ID_FIELD_NUMBER: builtins.int
    F_FIELD_NUMBER: builtins.int
    ARGS_FIELD_NUMBER: builtins.int
    KWARGS_FIELD_NUMBER: builtins.int
    run_id: typing.Text
    @property
    def f(self) -> values.values_pb2.Value: ...
    @property
    def args(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[values.values_pb2.Value]: ...
    @property
    def kwargs(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, values.values_pb2.Value]: ...
    def __init__(self,
        *,
        run_id: typing.Text = ...,
        f: typing.Optional[values.values_pb2.Value] = ...,
        args: typing.Optional[typing.Iterable[values.values_pb2.Value]] = ...,
        kwargs: typing.Optional[typing.Mapping[typing.Text, values.values_pb2.Value]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["f",b"f"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["args",b"args","f",b"f","kwargs",b"kwargs","run_id",b"run_id"]) -> None: ...
global___CallFunctionRequest = CallFunctionRequest

class RunGetRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    RUN_ID_FIELD_NUMBER: builtins.int
    GET_SUMMARY_FIELD_NUMBER: builtins.int
    run_id: typing.Text
    get_summary: builtins.bool
    def __init__(self,
        *,
        run_id: typing.Text = ...,
        get_summary: builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["get_summary",b"get_summary","run_id",b"run_id"]) -> None: ...
global___RunGetRequest = RunGetRequest

class RunDiscardRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    id: typing.Text
    def __init__(self,
        *,
        id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["id",b"id"]) -> None: ...
global___RunDiscardRequest = RunDiscardRequest

class RunDiscardResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___RunDiscardResponse = RunDiscardResponse

class RunGetResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SUMMARY_FIELD_NUMBER: builtins.int
    @property
    def summary(self) -> lang.run_pb2.RunSummary: ...
    def __init__(self,
        *,
        summary: typing.Optional[lang.run_pb2.RunSummary] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["summary",b"summary"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["summary",b"summary"]) -> None: ...
global___RunGetResponse = RunGetResponse

class RunUpdate(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    RUN_ID_FIELD_NUMBER: builtins.int
    T_FIELD_NUMBER: builtins.int
    PREV_FIELD_NUMBER: builtins.int
    NEXT_FIELD_NUMBER: builtins.int
    run_id: typing.Text
    @property
    def t(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def prev(self) -> lang.run_pb2.RunState:
        """will be nil on first update."""
        pass
    @property
    def next(self) -> lang.run_pb2.RunState: ...
    def __init__(self,
        *,
        run_id: typing.Text = ...,
        t: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        prev: typing.Optional[lang.run_pb2.RunState] = ...,
        next: typing.Optional[lang.run_pb2.RunState] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["next",b"next","prev",b"prev","t",b"t"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["next",b"next","prev",b"prev","run_id",b"run_id","t",b"t"]) -> None: ...
global___RunUpdate = RunUpdate

class RunCallReturnRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    RUN_ID_FIELD_NUMBER: builtins.int
    ERROR_FIELD_NUMBER: builtins.int
    RETVAL_FIELD_NUMBER: builtins.int
    run_id: typing.Text
    @property
    def error(self) -> program.error_pb2.Error: ...
    @property
    def retval(self) -> values.values_pb2.Value: ...
    def __init__(self,
        *,
        run_id: typing.Text = ...,
        error: typing.Optional[program.error_pb2.Error] = ...,
        retval: typing.Optional[values.values_pb2.Value] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["error",b"error","retval",b"retval"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["error",b"error","retval",b"retval","run_id",b"run_id"]) -> None: ...
global___RunCallReturnRequest = RunCallReturnRequest

class RunCallReturnResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___RunCallReturnResponse = RunCallReturnResponse

class RunLoadReturnRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class ValuesEntry(google.protobuf.message.Message):
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

    RUN_ID_FIELD_NUMBER: builtins.int
    ERROR_FIELD_NUMBER: builtins.int
    RUN_SUMMARY_FIELD_NUMBER: builtins.int
    VALUES_FIELD_NUMBER: builtins.int
    run_id: typing.Text
    @property
    def error(self) -> program.error_pb2.Error: ...
    @property
    def run_summary(self) -> lang.run_pb2.RunSummary: ...
    @property
    def values(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, values.values_pb2.Value]: ...
    def __init__(self,
        *,
        run_id: typing.Text = ...,
        error: typing.Optional[program.error_pb2.Error] = ...,
        run_summary: typing.Optional[lang.run_pb2.RunSummary] = ...,
        values: typing.Optional[typing.Mapping[typing.Text, values.values_pb2.Value]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["error",b"error","run_summary",b"run_summary"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["error",b"error","run_id",b"run_id","run_summary",b"run_summary","values",b"values"]) -> None: ...
global___RunLoadReturnRequest = RunLoadReturnRequest

class RunLoadReturnResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___RunLoadReturnResponse = RunLoadReturnResponse

class RunCancelRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    RUN_ID_FIELD_NUMBER: builtins.int
    REASON_FIELD_NUMBER: builtins.int
    run_id: typing.Text
    reason: typing.Text
    def __init__(self,
        *,
        run_id: typing.Text = ...,
        reason: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["reason",b"reason","run_id",b"run_id"]) -> None: ...
global___RunCancelRequest = RunCancelRequest

class RunCancelResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___RunCancelResponse = RunCancelResponse

class ListRunsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___ListRunsRequest = ListRunsRequest

class ListRun(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    id: typing.Text
    def __init__(self,
        *,
        id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["id",b"id"]) -> None: ...
global___ListRun = ListRun

class ListRuns(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    RUNS_FIELD_NUMBER: builtins.int
    @property
    def runs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ListRun]: ...
    def __init__(self,
        *,
        runs: typing.Optional[typing.Iterable[global___ListRun]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["runs",b"runs"]) -> None: ...
global___ListRuns = ListRuns

class ListRunsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class StatesEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text
        @property
        def value(self) -> global___ListRuns: ...
        def __init__(self,
            *,
            key: typing.Text = ...,
            value: typing.Optional[global___ListRuns] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value",b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    STATES_FIELD_NUMBER: builtins.int
    @property
    def states(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, global___ListRuns]: ...
    def __init__(self,
        *,
        states: typing.Optional[typing.Mapping[typing.Text, global___ListRuns]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["states",b"states"]) -> None: ...
global___ListRunsResponse = ListRunsResponse
