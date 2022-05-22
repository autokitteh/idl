# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from secretssvc import svc_pb2 as secretssvc_dot_svc__pb2


class SecretsStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Set = channel.unary_unary(
                '/autokitteh.secretssvc.Secrets/Set',
                request_serializer=secretssvc_dot_svc__pb2.SetRequest.SerializeToString,
                response_deserializer=secretssvc_dot_svc__pb2.SetResponse.FromString,
                )
        self.Get = channel.unary_unary(
                '/autokitteh.secretssvc.Secrets/Get',
                request_serializer=secretssvc_dot_svc__pb2.GetRequest.SerializeToString,
                response_deserializer=secretssvc_dot_svc__pb2.GetResponse.FromString,
                )
        self.List = channel.unary_unary(
                '/autokitteh.secretssvc.Secrets/List',
                request_serializer=secretssvc_dot_svc__pb2.ListRequest.SerializeToString,
                response_deserializer=secretssvc_dot_svc__pb2.ListResponse.FromString,
                )


class SecretsServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Set(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SecretsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Set': grpc.unary_unary_rpc_method_handler(
                    servicer.Set,
                    request_deserializer=secretssvc_dot_svc__pb2.SetRequest.FromString,
                    response_serializer=secretssvc_dot_svc__pb2.SetResponse.SerializeToString,
            ),
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=secretssvc_dot_svc__pb2.GetRequest.FromString,
                    response_serializer=secretssvc_dot_svc__pb2.GetResponse.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=secretssvc_dot_svc__pb2.ListRequest.FromString,
                    response_serializer=secretssvc_dot_svc__pb2.ListResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'autokitteh.secretssvc.Secrets', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Secrets(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Set(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/autokitteh.secretssvc.Secrets/Set',
            secretssvc_dot_svc__pb2.SetRequest.SerializeToString,
            secretssvc_dot_svc__pb2.SetResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/autokitteh.secretssvc.Secrets/Get',
            secretssvc_dot_svc__pb2.GetRequest.SerializeToString,
            secretssvc_dot_svc__pb2.GetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/autokitteh.secretssvc.Secrets/List',
            secretssvc_dot_svc__pb2.ListRequest.SerializeToString,
            secretssvc_dot_svc__pb2.ListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)