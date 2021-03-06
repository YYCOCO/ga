# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from rpc_service import layout_pb2 as layout__pb2


class LayoutStub(object):
    # missing associated documentation comment in .proto file
    pass

    def __init__(self, channel):
        """Constructor.

        Args:
          channel: A grpc.Channel.
        """
        self.layout = channel.unary_unary(
            '/Layout/layout',
            request_serializer=layout__pb2.LayoutFeature.SerializeToString,
            response_deserializer=layout__pb2.TopK.FromString,
        )


class LayoutServicer(object):
    # missing associated documentation comment in .proto file
    pass

    def layout(self, request, context):
        """输出topK 的布局方案
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LayoutServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'layout': grpc.unary_unary_rpc_method_handler(
            servicer.layout,
            request_deserializer=layout__pb2.LayoutFeature.FromString,
            response_serializer=layout__pb2.TopK.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'Layout', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
