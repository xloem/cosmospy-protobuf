"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ....ethermint.evm.v1 import query_pb2 as ethermint_dot_evm_dot_v1_dot_query__pb2
from ....ethermint.evm.v1 import tx_pb2 as ethermint_dot_evm_dot_v1_dot_tx__pb2

class QueryStub(object):
    """Query defines the gRPC querier service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Account = channel.unary_unary('/ethermint.evm.v1.Query/Account', request_serializer=ethermint_dot_evm_dot_v1_dot_query__pb2.QueryAccountRequest.SerializeToString, response_deserializer=ethermint_dot_evm_dot_v1_dot_query__pb2.QueryAccountResponse.FromString)
        self.CosmosAccount = channel.unary_unary('/ethermint.evm.v1.Query/CosmosAccount', request_serializer=ethermint_dot_evm_dot_v1_dot_query__pb2.QueryCosmosAccountRequest.SerializeToString, response_deserializer=ethermint_dot_evm_dot_v1_dot_query__pb2.QueryCosmosAccountResponse.FromString)
        self.ValidatorAccount = channel.unary_unary('/ethermint.evm.v1.Query/ValidatorAccount', request_serializer=ethermint_dot_evm_dot_v1_dot_query__pb2.QueryValidatorAccountRequest.SerializeToString, response_deserializer=ethermint_dot_evm_dot_v1_dot_query__pb2.QueryValidatorAccountResponse.FromString)
        self.Balance = channel.unary_unary('/ethermint.evm.v1.Query/Balance', request_serializer=ethermint_dot_evm_dot_v1_dot_query__pb2.QueryBalanceRequest.SerializeToString, response_deserializer=ethermint_dot_evm_dot_v1_dot_query__pb2.QueryBalanceResponse.FromString)
        self.Storage = channel.unary_unary('/ethermint.evm.v1.Query/Storage', request_serializer=ethermint_dot_evm_dot_v1_dot_query__pb2.QueryStorageRequest.SerializeToString, response_deserializer=ethermint_dot_evm_dot_v1_dot_query__pb2.QueryStorageResponse.FromString)
        self.Code = channel.unary_unary('/ethermint.evm.v1.Query/Code', request_serializer=ethermint_dot_evm_dot_v1_dot_query__pb2.QueryCodeRequest.SerializeToString, response_deserializer=ethermint_dot_evm_dot_v1_dot_query__pb2.QueryCodeResponse.FromString)
        self.Params = channel.unary_unary('/ethermint.evm.v1.Query/Params', request_serializer=ethermint_dot_evm_dot_v1_dot_query__pb2.QueryParamsRequest.SerializeToString, response_deserializer=ethermint_dot_evm_dot_v1_dot_query__pb2.QueryParamsResponse.FromString)
        self.EthCall = channel.unary_unary('/ethermint.evm.v1.Query/EthCall', request_serializer=ethermint_dot_evm_dot_v1_dot_query__pb2.EthCallRequest.SerializeToString, response_deserializer=ethermint_dot_evm_dot_v1_dot_tx__pb2.MsgEthereumTxResponse.FromString)
        self.EstimateGas = channel.unary_unary('/ethermint.evm.v1.Query/EstimateGas', request_serializer=ethermint_dot_evm_dot_v1_dot_query__pb2.EthCallRequest.SerializeToString, response_deserializer=ethermint_dot_evm_dot_v1_dot_query__pb2.EstimateGasResponse.FromString)
        self.TraceTx = channel.unary_unary('/ethermint.evm.v1.Query/TraceTx', request_serializer=ethermint_dot_evm_dot_v1_dot_query__pb2.QueryTraceTxRequest.SerializeToString, response_deserializer=ethermint_dot_evm_dot_v1_dot_query__pb2.QueryTraceTxResponse.FromString)
        self.TraceBlock = channel.unary_unary('/ethermint.evm.v1.Query/TraceBlock', request_serializer=ethermint_dot_evm_dot_v1_dot_query__pb2.QueryTraceBlockRequest.SerializeToString, response_deserializer=ethermint_dot_evm_dot_v1_dot_query__pb2.QueryTraceBlockResponse.FromString)
        self.BaseFee = channel.unary_unary('/ethermint.evm.v1.Query/BaseFee', request_serializer=ethermint_dot_evm_dot_v1_dot_query__pb2.QueryBaseFeeRequest.SerializeToString, response_deserializer=ethermint_dot_evm_dot_v1_dot_query__pb2.QueryBaseFeeResponse.FromString)

class QueryServicer(object):
    """Query defines the gRPC querier service.
    """

    def Account(self, request, context):
        """Account queries an Ethereum account.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CosmosAccount(self, request, context):
        """CosmosAccount queries an Ethereum account's Cosmos Address.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ValidatorAccount(self, request, context):
        """ValidatorAccount queries an Ethereum account's from a validator consensus
        Address.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Balance(self, request, context):
        """Balance queries the balance of a the EVM denomination for a single
        EthAccount.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Storage(self, request, context):
        """Storage queries the balance of all coins for a single account.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Code(self, request, context):
        """Code queries the balance of all coins for a single account.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Params(self, request, context):
        """Params queries the parameters of x/evm module.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EthCall(self, request, context):
        """EthCall implements the `eth_call` rpc api
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EstimateGas(self, request, context):
        """EstimateGas implements the `eth_estimateGas` rpc api
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TraceTx(self, request, context):
        """TraceTx implements the `debug_traceTransaction` rpc api
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TraceBlock(self, request, context):
        """TraceBlock implements the `debug_traceBlockByNumber` and `debug_traceBlockByHash` rpc api
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BaseFee(self, request, context):
        """BaseFee queries the base fee of the parent block of the current block,
        it's similar to feemarket module's method, but also checks london hardfork status.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {'Account': grpc.unary_unary_rpc_method_handler(servicer.Account, request_deserializer=ethermint_dot_evm_dot_v1_dot_query__pb2.QueryAccountRequest.FromString, response_serializer=ethermint_dot_evm_dot_v1_dot_query__pb2.QueryAccountResponse.SerializeToString), 'CosmosAccount': grpc.unary_unary_rpc_method_handler(servicer.CosmosAccount, request_deserializer=ethermint_dot_evm_dot_v1_dot_query__pb2.QueryCosmosAccountRequest.FromString, response_serializer=ethermint_dot_evm_dot_v1_dot_query__pb2.QueryCosmosAccountResponse.SerializeToString), 'ValidatorAccount': grpc.unary_unary_rpc_method_handler(servicer.ValidatorAccount, request_deserializer=ethermint_dot_evm_dot_v1_dot_query__pb2.QueryValidatorAccountRequest.FromString, response_serializer=ethermint_dot_evm_dot_v1_dot_query__pb2.QueryValidatorAccountResponse.SerializeToString), 'Balance': grpc.unary_unary_rpc_method_handler(servicer.Balance, request_deserializer=ethermint_dot_evm_dot_v1_dot_query__pb2.QueryBalanceRequest.FromString, response_serializer=ethermint_dot_evm_dot_v1_dot_query__pb2.QueryBalanceResponse.SerializeToString), 'Storage': grpc.unary_unary_rpc_method_handler(servicer.Storage, request_deserializer=ethermint_dot_evm_dot_v1_dot_query__pb2.QueryStorageRequest.FromString, response_serializer=ethermint_dot_evm_dot_v1_dot_query__pb2.QueryStorageResponse.SerializeToString), 'Code': grpc.unary_unary_rpc_method_handler(servicer.Code, request_deserializer=ethermint_dot_evm_dot_v1_dot_query__pb2.QueryCodeRequest.FromString, response_serializer=ethermint_dot_evm_dot_v1_dot_query__pb2.QueryCodeResponse.SerializeToString), 'Params': grpc.unary_unary_rpc_method_handler(servicer.Params, request_deserializer=ethermint_dot_evm_dot_v1_dot_query__pb2.QueryParamsRequest.FromString, response_serializer=ethermint_dot_evm_dot_v1_dot_query__pb2.QueryParamsResponse.SerializeToString), 'EthCall': grpc.unary_unary_rpc_method_handler(servicer.EthCall, request_deserializer=ethermint_dot_evm_dot_v1_dot_query__pb2.EthCallRequest.FromString, response_serializer=ethermint_dot_evm_dot_v1_dot_tx__pb2.MsgEthereumTxResponse.SerializeToString), 'EstimateGas': grpc.unary_unary_rpc_method_handler(servicer.EstimateGas, request_deserializer=ethermint_dot_evm_dot_v1_dot_query__pb2.EthCallRequest.FromString, response_serializer=ethermint_dot_evm_dot_v1_dot_query__pb2.EstimateGasResponse.SerializeToString), 'TraceTx': grpc.unary_unary_rpc_method_handler(servicer.TraceTx, request_deserializer=ethermint_dot_evm_dot_v1_dot_query__pb2.QueryTraceTxRequest.FromString, response_serializer=ethermint_dot_evm_dot_v1_dot_query__pb2.QueryTraceTxResponse.SerializeToString), 'TraceBlock': grpc.unary_unary_rpc_method_handler(servicer.TraceBlock, request_deserializer=ethermint_dot_evm_dot_v1_dot_query__pb2.QueryTraceBlockRequest.FromString, response_serializer=ethermint_dot_evm_dot_v1_dot_query__pb2.QueryTraceBlockResponse.SerializeToString), 'BaseFee': grpc.unary_unary_rpc_method_handler(servicer.BaseFee, request_deserializer=ethermint_dot_evm_dot_v1_dot_query__pb2.QueryBaseFeeRequest.FromString, response_serializer=ethermint_dot_evm_dot_v1_dot_query__pb2.QueryBaseFeeResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('ethermint.evm.v1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Query(object):
    """Query defines the gRPC querier service.
    """

    @staticmethod
    def Account(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ethermint.evm.v1.Query/Account', ethermint_dot_evm_dot_v1_dot_query__pb2.QueryAccountRequest.SerializeToString, ethermint_dot_evm_dot_v1_dot_query__pb2.QueryAccountResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CosmosAccount(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ethermint.evm.v1.Query/CosmosAccount', ethermint_dot_evm_dot_v1_dot_query__pb2.QueryCosmosAccountRequest.SerializeToString, ethermint_dot_evm_dot_v1_dot_query__pb2.QueryCosmosAccountResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ValidatorAccount(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ethermint.evm.v1.Query/ValidatorAccount', ethermint_dot_evm_dot_v1_dot_query__pb2.QueryValidatorAccountRequest.SerializeToString, ethermint_dot_evm_dot_v1_dot_query__pb2.QueryValidatorAccountResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Balance(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ethermint.evm.v1.Query/Balance', ethermint_dot_evm_dot_v1_dot_query__pb2.QueryBalanceRequest.SerializeToString, ethermint_dot_evm_dot_v1_dot_query__pb2.QueryBalanceResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Storage(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ethermint.evm.v1.Query/Storage', ethermint_dot_evm_dot_v1_dot_query__pb2.QueryStorageRequest.SerializeToString, ethermint_dot_evm_dot_v1_dot_query__pb2.QueryStorageResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Code(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ethermint.evm.v1.Query/Code', ethermint_dot_evm_dot_v1_dot_query__pb2.QueryCodeRequest.SerializeToString, ethermint_dot_evm_dot_v1_dot_query__pb2.QueryCodeResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Params(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ethermint.evm.v1.Query/Params', ethermint_dot_evm_dot_v1_dot_query__pb2.QueryParamsRequest.SerializeToString, ethermint_dot_evm_dot_v1_dot_query__pb2.QueryParamsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EthCall(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ethermint.evm.v1.Query/EthCall', ethermint_dot_evm_dot_v1_dot_query__pb2.EthCallRequest.SerializeToString, ethermint_dot_evm_dot_v1_dot_tx__pb2.MsgEthereumTxResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EstimateGas(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ethermint.evm.v1.Query/EstimateGas', ethermint_dot_evm_dot_v1_dot_query__pb2.EthCallRequest.SerializeToString, ethermint_dot_evm_dot_v1_dot_query__pb2.EstimateGasResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TraceTx(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ethermint.evm.v1.Query/TraceTx', ethermint_dot_evm_dot_v1_dot_query__pb2.QueryTraceTxRequest.SerializeToString, ethermint_dot_evm_dot_v1_dot_query__pb2.QueryTraceTxResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TraceBlock(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ethermint.evm.v1.Query/TraceBlock', ethermint_dot_evm_dot_v1_dot_query__pb2.QueryTraceBlockRequest.SerializeToString, ethermint_dot_evm_dot_v1_dot_query__pb2.QueryTraceBlockResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BaseFee(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ethermint.evm.v1.Query/BaseFee', ethermint_dot_evm_dot_v1_dot_query__pb2.QueryBaseFeeRequest.SerializeToString, ethermint_dot_evm_dot_v1_dot_query__pb2.QueryBaseFeeResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)