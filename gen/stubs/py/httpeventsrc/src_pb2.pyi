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

class Route(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    PATH_FIELD_NUMBER: builtins.int
    METHODS_FIELD_NUMBER: builtins.int
    name: typing.Text
    path: typing.Text
    @property
    def methods(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    def __init__(self,
        *,
        name: typing.Text = ...,
        path: typing.Text = ...,
        methods: typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["methods",b"methods","name",b"name","path",b"path"]) -> None: ...
global___Route = Route

class BindRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PROJECT_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    ROUTES_FIELD_NUMBER: builtins.int
    project_id: typing.Text
    name: typing.Text
    @property
    def routes(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Route]: ...
    def __init__(self,
        *,
        project_id: typing.Text = ...,
        name: typing.Text = ...,
        routes: typing.Optional[typing.Iterable[global___Route]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name","project_id",b"project_id","routes",b"routes"]) -> None: ...
global___BindRequest = BindRequest

class BindResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___BindResponse = BindResponse

class UnbindRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PROJECT_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    project_id: typing.Text
    name: typing.Text
    def __init__(self,
        *,
        project_id: typing.Text = ...,
        name: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name","project_id",b"project_id"]) -> None: ...
global___UnbindRequest = UnbindRequest

class UnbindResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___UnbindResponse = UnbindResponse
