# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from eventsvc import svc_pb2 as eventsvc_dot_svc__pb2


class EventsStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.IngestEvent = channel.unary_unary(
                '/autokitteh.eventsvc.Events/IngestEvent',
                request_serializer=eventsvc_dot_svc__pb2.IngestEventRequest.SerializeToString,
                response_deserializer=eventsvc_dot_svc__pb2.IngestEventResponse.FromString,
                )
        self.GetEvent = channel.unary_unary(
                '/autokitteh.eventsvc.Events/GetEvent',
                request_serializer=eventsvc_dot_svc__pb2.GetEventRequest.SerializeToString,
                response_deserializer=eventsvc_dot_svc__pb2.GetEventResponse.FromString,
                )
        self.GetEventState = channel.unary_unary(
                '/autokitteh.eventsvc.Events/GetEventState',
                request_serializer=eventsvc_dot_svc__pb2.GetEventStateRequest.SerializeToString,
                response_deserializer=eventsvc_dot_svc__pb2.GetEventStateResponse.FromString,
                )
        self.UpdateEventState = channel.unary_unary(
                '/autokitteh.eventsvc.Events/UpdateEventState',
                request_serializer=eventsvc_dot_svc__pb2.UpdateEventStateRequest.SerializeToString,
                response_deserializer=eventsvc_dot_svc__pb2.UpdateEventStateResponse.FromString,
                )
        self.ListEvents = channel.unary_unary(
                '/autokitteh.eventsvc.Events/ListEvents',
                request_serializer=eventsvc_dot_svc__pb2.ListEventsRequest.SerializeToString,
                response_deserializer=eventsvc_dot_svc__pb2.ListEventsResponse.FromString,
                )
        self.GetEventStateForProject = channel.unary_unary(
                '/autokitteh.eventsvc.Events/GetEventStateForProject',
                request_serializer=eventsvc_dot_svc__pb2.GetEventStateForProjectRequest.SerializeToString,
                response_deserializer=eventsvc_dot_svc__pb2.GetEventStateForProjectResponse.FromString,
                )
        self.UpdateEventStateForProject = channel.unary_unary(
                '/autokitteh.eventsvc.Events/UpdateEventStateForProject',
                request_serializer=eventsvc_dot_svc__pb2.UpdateEventStateForProjectRequest.SerializeToString,
                response_deserializer=eventsvc_dot_svc__pb2.UpdateEventStateForProjectResponse.FromString,
                )
        self.GetProjectWaitingEvents = channel.unary_unary(
                '/autokitteh.eventsvc.Events/GetProjectWaitingEvents',
                request_serializer=eventsvc_dot_svc__pb2.GetProjectWaitingEventsRequest.SerializeToString,
                response_deserializer=eventsvc_dot_svc__pb2.GetProjectWaitingEventsResponse.FromString,
                )


class EventsServicer(object):
    """Missing associated documentation comment in .proto file."""

    def IngestEvent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetEvent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetEventState(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateEventState(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListEvents(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetEventStateForProject(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateEventStateForProject(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetProjectWaitingEvents(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EventsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'IngestEvent': grpc.unary_unary_rpc_method_handler(
                    servicer.IngestEvent,
                    request_deserializer=eventsvc_dot_svc__pb2.IngestEventRequest.FromString,
                    response_serializer=eventsvc_dot_svc__pb2.IngestEventResponse.SerializeToString,
            ),
            'GetEvent': grpc.unary_unary_rpc_method_handler(
                    servicer.GetEvent,
                    request_deserializer=eventsvc_dot_svc__pb2.GetEventRequest.FromString,
                    response_serializer=eventsvc_dot_svc__pb2.GetEventResponse.SerializeToString,
            ),
            'GetEventState': grpc.unary_unary_rpc_method_handler(
                    servicer.GetEventState,
                    request_deserializer=eventsvc_dot_svc__pb2.GetEventStateRequest.FromString,
                    response_serializer=eventsvc_dot_svc__pb2.GetEventStateResponse.SerializeToString,
            ),
            'UpdateEventState': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateEventState,
                    request_deserializer=eventsvc_dot_svc__pb2.UpdateEventStateRequest.FromString,
                    response_serializer=eventsvc_dot_svc__pb2.UpdateEventStateResponse.SerializeToString,
            ),
            'ListEvents': grpc.unary_unary_rpc_method_handler(
                    servicer.ListEvents,
                    request_deserializer=eventsvc_dot_svc__pb2.ListEventsRequest.FromString,
                    response_serializer=eventsvc_dot_svc__pb2.ListEventsResponse.SerializeToString,
            ),
            'GetEventStateForProject': grpc.unary_unary_rpc_method_handler(
                    servicer.GetEventStateForProject,
                    request_deserializer=eventsvc_dot_svc__pb2.GetEventStateForProjectRequest.FromString,
                    response_serializer=eventsvc_dot_svc__pb2.GetEventStateForProjectResponse.SerializeToString,
            ),
            'UpdateEventStateForProject': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateEventStateForProject,
                    request_deserializer=eventsvc_dot_svc__pb2.UpdateEventStateForProjectRequest.FromString,
                    response_serializer=eventsvc_dot_svc__pb2.UpdateEventStateForProjectResponse.SerializeToString,
            ),
            'GetProjectWaitingEvents': grpc.unary_unary_rpc_method_handler(
                    servicer.GetProjectWaitingEvents,
                    request_deserializer=eventsvc_dot_svc__pb2.GetProjectWaitingEventsRequest.FromString,
                    response_serializer=eventsvc_dot_svc__pb2.GetProjectWaitingEventsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'autokitteh.eventsvc.Events', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Events(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def IngestEvent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/autokitteh.eventsvc.Events/IngestEvent',
            eventsvc_dot_svc__pb2.IngestEventRequest.SerializeToString,
            eventsvc_dot_svc__pb2.IngestEventResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetEvent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/autokitteh.eventsvc.Events/GetEvent',
            eventsvc_dot_svc__pb2.GetEventRequest.SerializeToString,
            eventsvc_dot_svc__pb2.GetEventResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetEventState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/autokitteh.eventsvc.Events/GetEventState',
            eventsvc_dot_svc__pb2.GetEventStateRequest.SerializeToString,
            eventsvc_dot_svc__pb2.GetEventStateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateEventState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/autokitteh.eventsvc.Events/UpdateEventState',
            eventsvc_dot_svc__pb2.UpdateEventStateRequest.SerializeToString,
            eventsvc_dot_svc__pb2.UpdateEventStateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListEvents(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/autokitteh.eventsvc.Events/ListEvents',
            eventsvc_dot_svc__pb2.ListEventsRequest.SerializeToString,
            eventsvc_dot_svc__pb2.ListEventsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetEventStateForProject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/autokitteh.eventsvc.Events/GetEventStateForProject',
            eventsvc_dot_svc__pb2.GetEventStateForProjectRequest.SerializeToString,
            eventsvc_dot_svc__pb2.GetEventStateForProjectResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateEventStateForProject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/autokitteh.eventsvc.Events/UpdateEventStateForProject',
            eventsvc_dot_svc__pb2.UpdateEventStateForProjectRequest.SerializeToString,
            eventsvc_dot_svc__pb2.UpdateEventStateForProjectResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetProjectWaitingEvents(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/autokitteh.eventsvc.Events/GetProjectWaitingEvents',
            eventsvc_dot_svc__pb2.GetProjectWaitingEventsRequest.SerializeToString,
            eventsvc_dot_svc__pb2.GetProjectWaitingEventsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
