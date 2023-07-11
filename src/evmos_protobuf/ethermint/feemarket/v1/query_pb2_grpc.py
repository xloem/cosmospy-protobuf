"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ....ethermint.feemarket.v1 import query_pb2 as ethermint_dot_feemarket_dot_v1_dot_query__pb2

class QueryStub(object):
    """Query defines the gRPC querier service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Params = channel.unary_unary('/ethermint.feemarket.v1.Query/Params', request_serializer=ethermint_dot_feemarket_dot_v1_dot_query__pb2.QueryParamsRequest.SerializeToString, response_deserializer=ethermint_dot_feemarket_dot_v1_dot_query__pb2.QueryParamsResponse.FromString)
        self.BaseFee = channel.unary_unary('/ethermint.feemarket.v1.Query/BaseFee', request_serializer=ethermint_dot_feemarket_dot_v1_dot_query__pb2.QueryBaseFeeRequest.SerializeToString, response_deserializer=ethermint_dot_feemarket_dot_v1_dot_query__pb2.QueryBaseFeeResponse.FromString)
        self.BlockGas = channel.unary_unary('/ethermint.feemarket.v1.Query/BlockGas', request_serializer=ethermint_dot_feemarket_dot_v1_dot_query__pb2.QueryBlockGasRequest.SerializeToString, response_deserializer=ethermint_dot_feemarket_dot_v1_dot_query__pb2.QueryBlockGasResponse.FromString)

class QueryServicer(object):
    """Query defines the gRPC querier service.
    """

    def Params(self, request, context):
        """Params queries the parameters of x/feemarket module.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BaseFee(self, request, context):
        """BaseFee queries the base fee of the parent block of the current block.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BlockGas(self, request, context):
        """BlockGas queries the gas used at a given block height
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {'Params': grpc.unary_unary_rpc_method_handler(servicer.Params, request_deserializer=ethermint_dot_feemarket_dot_v1_dot_query__pb2.QueryParamsRequest.FromString, response_serializer=ethermint_dot_feemarket_dot_v1_dot_query__pb2.QueryParamsResponse.SerializeToString), 'BaseFee': grpc.unary_unary_rpc_method_handler(servicer.BaseFee, request_deserializer=ethermint_dot_feemarket_dot_v1_dot_query__pb2.QueryBaseFeeRequest.FromString, response_serializer=ethermint_dot_feemarket_dot_v1_dot_query__pb2.QueryBaseFeeResponse.SerializeToString), 'BlockGas': grpc.unary_unary_rpc_method_handler(servicer.BlockGas, request_deserializer=ethermint_dot_feemarket_dot_v1_dot_query__pb2.QueryBlockGasRequest.FromString, response_serializer=ethermint_dot_feemarket_dot_v1_dot_query__pb2.QueryBlockGasResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('ethermint.feemarket.v1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Query(object):
    """Query defines the gRPC querier service.
    """

    @staticmethod
    def Params(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ethermint.feemarket.v1.Query/Params', ethermint_dot_feemarket_dot_v1_dot_query__pb2.QueryParamsRequest.SerializeToString, ethermint_dot_feemarket_dot_v1_dot_query__pb2.QueryParamsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BaseFee(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ethermint.feemarket.v1.Query/BaseFee', ethermint_dot_feemarket_dot_v1_dot_query__pb2.QueryBaseFeeRequest.SerializeToString, ethermint_dot_feemarket_dot_v1_dot_query__pb2.QueryBaseFeeResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BlockGas(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ethermint.feemarket.v1.Query/BlockGas', ethermint_dot_feemarket_dot_v1_dot_query__pb2.QueryBlockGasRequest.SerializeToString, ethermint_dot_feemarket_dot_v1_dot_query__pb2.QueryBlockGasResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)