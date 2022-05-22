"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class BindRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PROJECT_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    CRONSPEC_FIELD_NUMBER: builtins.int
    project_id: typing.Text
    name: typing.Text
    cronspec: typing.Text
    def __init__(self,
        *,
        project_id: typing.Text = ...,
        name: typing.Text = ...,
        cronspec: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cronspec",b"cronspec","name",b"name","project_id",b"project_id"]) -> None: ...
global___BindRequest = BindRequest

class BindResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___BindResponse = BindResponse

class UnbindRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PROJECT_ID_FIELD_NUMBER: builtins.int
    project_id: typing.Text
    def __init__(self,
        *,
        project_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["project_id",b"project_id"]) -> None: ...
global___UnbindRequest = UnbindRequest

class UnbindResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___UnbindResponse = UnbindResponse

class TickRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___TickRequest = TickRequest

class TickResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___TickResponse = TickResponse