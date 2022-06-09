# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from event import track_pb2 as event_dot_track__pb2
from litterboxsvc import svc_pb2 as litterboxsvc_dot_svc__pb2


class LitterBoxStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Setup = channel.unary_unary(
                '/autokitteh.litterbox.LitterBox/Setup',
                request_serializer=litterboxsvc_dot_svc__pb2.SetupRequest.SerializeToString,
                response_deserializer=litterboxsvc_dot_svc__pb2.SetupResponse.FromString,
                )
        self.Get = channel.unary_unary(
                '/autokitteh.litterbox.LitterBox/Get',
                request_serializer=litterboxsvc_dot_svc__pb2.GetRequest.SerializeToString,
                response_deserializer=litterboxsvc_dot_svc__pb2.GetResponse.FromString,
                )
        self.Event = channel.unary_stream(
                '/autokitteh.litterbox.LitterBox/Event',
                request_serializer=litterboxsvc_dot_svc__pb2.EventRequest.SerializeToString,
                response_deserializer=event_dot_track__pb2.TrackIngestEventUpdate.FromString,
                )
        self.Run = channel.unary_stream(
                '/autokitteh.litterbox.LitterBox/Run',
                request_serializer=litterboxsvc_dot_svc__pb2.RunRequest.SerializeToString,
                response_deserializer=event_dot_track__pb2.TrackIngestEventUpdate.FromString,
                )
        self.Scoop = channel.unary_unary(
                '/autokitteh.litterbox.LitterBox/Scoop',
                request_serializer=litterboxsvc_dot_svc__pb2.ScoopRequest.SerializeToString,
                response_deserializer=litterboxsvc_dot_svc__pb2.ScoopResponse.FromString,
                )


class LitterBoxServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Setup(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Event(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Run(self, request, context):
        """Enable live sources and track all incoming events.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Scoop(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LitterBoxServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Setup': grpc.unary_unary_rpc_method_handler(
                    servicer.Setup,
                    request_deserializer=litterboxsvc_dot_svc__pb2.SetupRequest.FromString,
                    response_serializer=litterboxsvc_dot_svc__pb2.SetupResponse.SerializeToString,
            ),
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=litterboxsvc_dot_svc__pb2.GetRequest.FromString,
                    response_serializer=litterboxsvc_dot_svc__pb2.GetResponse.SerializeToString,
            ),
            'Event': grpc.unary_stream_rpc_method_handler(
                    servicer.Event,
                    request_deserializer=litterboxsvc_dot_svc__pb2.EventRequest.FromString,
                    response_serializer=event_dot_track__pb2.TrackIngestEventUpdate.SerializeToString,
            ),
            'Run': grpc.unary_stream_rpc_method_handler(
                    servicer.Run,
                    request_deserializer=litterboxsvc_dot_svc__pb2.RunRequest.FromString,
                    response_serializer=event_dot_track__pb2.TrackIngestEventUpdate.SerializeToString,
            ),
            'Scoop': grpc.unary_unary_rpc_method_handler(
                    servicer.Scoop,
                    request_deserializer=litterboxsvc_dot_svc__pb2.ScoopRequest.FromString,
                    response_serializer=litterboxsvc_dot_svc__pb2.ScoopResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'autokitteh.litterbox.LitterBox', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class LitterBox(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Setup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/autokitteh.litterbox.LitterBox/Setup',
            litterboxsvc_dot_svc__pb2.SetupRequest.SerializeToString,
            litterboxsvc_dot_svc__pb2.SetupResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/autokitteh.litterbox.LitterBox/Get',
            litterboxsvc_dot_svc__pb2.GetRequest.SerializeToString,
            litterboxsvc_dot_svc__pb2.GetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Event(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/autokitteh.litterbox.LitterBox/Event',
            litterboxsvc_dot_svc__pb2.EventRequest.SerializeToString,
            event_dot_track__pb2.TrackIngestEventUpdate.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Run(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/autokitteh.litterbox.LitterBox/Run',
            litterboxsvc_dot_svc__pb2.RunRequest.SerializeToString,
            event_dot_track__pb2.TrackIngestEventUpdate.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Scoop(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/autokitteh.litterbox.LitterBox/Scoop',
            litterboxsvc_dot_svc__pb2.ScoopRequest.SerializeToString,
            litterboxsvc_dot_svc__pb2.ScoopResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
