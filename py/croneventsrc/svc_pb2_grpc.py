# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from croneventsrc import svc_pb2 as croneventsrc_dot_svc__pb2


class CronEventSourceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Tick = channel.unary_unary(
                '/autokitteh.croneventsrc.CronEventSource/Tick',
                request_serializer=croneventsrc_dot_svc__pb2.TickRequest.SerializeToString,
                response_deserializer=croneventsrc_dot_svc__pb2.TickResponse.FromString,
                )
        self.Bind = channel.unary_unary(
                '/autokitteh.croneventsrc.CronEventSource/Bind',
                request_serializer=croneventsrc_dot_svc__pb2.BindRequest.SerializeToString,
                response_deserializer=croneventsrc_dot_svc__pb2.BindResponse.FromString,
                )
        self.Unbind = channel.unary_unary(
                '/autokitteh.croneventsrc.CronEventSource/Unbind',
                request_serializer=croneventsrc_dot_svc__pb2.UnbindRequest.SerializeToString,
                response_deserializer=croneventsrc_dot_svc__pb2.UnbindResponse.FromString,
                )


class CronEventSourceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Tick(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

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


def add_CronEventSourceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Tick': grpc.unary_unary_rpc_method_handler(
                    servicer.Tick,
                    request_deserializer=croneventsrc_dot_svc__pb2.TickRequest.FromString,
                    response_serializer=croneventsrc_dot_svc__pb2.TickResponse.SerializeToString,
            ),
            'Bind': grpc.unary_unary_rpc_method_handler(
                    servicer.Bind,
                    request_deserializer=croneventsrc_dot_svc__pb2.BindRequest.FromString,
                    response_serializer=croneventsrc_dot_svc__pb2.BindResponse.SerializeToString,
            ),
            'Unbind': grpc.unary_unary_rpc_method_handler(
                    servicer.Unbind,
                    request_deserializer=croneventsrc_dot_svc__pb2.UnbindRequest.FromString,
                    response_serializer=croneventsrc_dot_svc__pb2.UnbindResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'autokitteh.croneventsrc.CronEventSource', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CronEventSource(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Tick(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/autokitteh.croneventsrc.CronEventSource/Tick',
            croneventsrc_dot_svc__pb2.TickRequest.SerializeToString,
            croneventsrc_dot_svc__pb2.TickResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

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
        return grpc.experimental.unary_unary(request, target, '/autokitteh.croneventsrc.CronEventSource/Bind',
            croneventsrc_dot_svc__pb2.BindRequest.SerializeToString,
            croneventsrc_dot_svc__pb2.BindResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/autokitteh.croneventsrc.CronEventSource/Unbind',
            croneventsrc_dot_svc__pb2.UnbindRequest.SerializeToString,
            croneventsrc_dot_svc__pb2.UnbindResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
