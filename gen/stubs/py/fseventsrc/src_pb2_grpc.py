# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from fseventsrc import src_pb2 as fseventsrc_dot_src__pb2


class FSEventSourceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Bind = channel.unary_unary(
                '/autokitteh.fseventsrc.FSEventSource/Bind',
                request_serializer=fseventsrc_dot_src__pb2.BindRequest.SerializeToString,
                response_deserializer=fseventsrc_dot_src__pb2.BindResponse.FromString,
                )
        self.Unbind = channel.unary_unary(
                '/autokitteh.fseventsrc.FSEventSource/Unbind',
                request_serializer=fseventsrc_dot_src__pb2.UnbindRequest.SerializeToString,
                response_deserializer=fseventsrc_dot_src__pb2.UnbindResponse.FromString,
                )


class FSEventSourceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Bind(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Unbind(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FSEventSourceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Bind': grpc.unary_unary_rpc_method_handler(
                    servicer.Bind,
                    request_deserializer=fseventsrc_dot_src__pb2.BindRequest.FromString,
                    response_serializer=fseventsrc_dot_src__pb2.BindResponse.SerializeToString,
            ),
            'Unbind': grpc.unary_unary_rpc_method_handler(
                    servicer.Unbind,
                    request_deserializer=fseventsrc_dot_src__pb2.UnbindRequest.FromString,
                    response_serializer=fseventsrc_dot_src__pb2.UnbindResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'autokitteh.fseventsrc.FSEventSource', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class FSEventSource(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Bind(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/autokitteh.fseventsrc.FSEventSource/Bind',
            fseventsrc_dot_src__pb2.BindRequest.SerializeToString,
            fseventsrc_dot_src__pb2.BindResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Unbind(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/autokitteh.fseventsrc.FSEventSource/Unbind',
            fseventsrc_dot_src__pb2.UnbindRequest.SerializeToString,
            fseventsrc_dot_src__pb2.UnbindResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
