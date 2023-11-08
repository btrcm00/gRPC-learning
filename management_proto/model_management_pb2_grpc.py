# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import management_proto.model_management_pb2 as model__management__pb2


class ManagementStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Setup = channel.unary_unary(
                '/Management/Setup',
                request_serializer=model__management__pb2.SetupRequest.SerializeToString,
                response_deserializer=model__management__pb2.SetupResponse.FromString,
                )
        self.Import = channel.unary_unary(
                '/Management/Import',
                request_serializer=model__management__pb2.ImportRequest.SerializeToString,
                response_deserializer=model__management__pb2.ImportResponse.FromString,
                )
        self.Commands = channel.unary_unary(
                '/Management/Commands',
                request_serializer=model__management__pb2.CommandRequest.SerializeToString,
                response_deserializer=model__management__pb2.CommandResponse.FromString,
                )


class ManagementServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Setup(self, request, context):
        """Store and monitor the processing status of machine learning (ML), including active, training, etc.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Import(self, request, context):
        """Upload raw data into the system, allowing multiple files uploads simultaneously
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Commands(self, request, context):
        """Execute an action corresponding to the command type in the request
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ManagementServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Setup': grpc.unary_unary_rpc_method_handler(
                    servicer.Setup,
                    request_deserializer=model__management__pb2.SetupRequest.FromString,
                    response_serializer=model__management__pb2.SetupResponse.SerializeToString,
            ),
            'Import': grpc.unary_unary_rpc_method_handler(
                    servicer.Import,
                    request_deserializer=model__management__pb2.ImportRequest.FromString,
                    response_serializer=model__management__pb2.ImportResponse.SerializeToString,
            ),
            'Commands': grpc.unary_unary_rpc_method_handler(
                    servicer.Commands,
                    request_deserializer=model__management__pb2.CommandRequest.FromString,
                    response_serializer=model__management__pb2.CommandResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Management', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Management(object):
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
        return grpc.experimental.unary_unary(request, target, '/Management/Setup',
            model__management__pb2.SetupRequest.SerializeToString,
            model__management__pb2.SetupResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Import(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Management/Import',
            model__management__pb2.ImportRequest.SerializeToString,
            model__management__pb2.ImportResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Commands(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Management/Commands',
            model__management__pb2.CommandRequest.SerializeToString,
            model__management__pb2.CommandResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
