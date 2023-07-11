import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
from .... import cosmos
from .... import ethermint
from .... import gogoproto
from .... import google
import google.protobuf.timestamp_pb2

class QueryBase(abc.ABC):

    @abc.abstractmethod
    async def Account(self, stream: 'grpclib.server.Stream[ethermint.evm.v1.query_pb2.QueryAccountRequest, ethermint.evm.v1.query_pb2.QueryAccountResponse]') -> None:
        pass

    @abc.abstractmethod
    async def CosmosAccount(self, stream: 'grpclib.server.Stream[ethermint.evm.v1.query_pb2.QueryCosmosAccountRequest, ethermint.evm.v1.query_pb2.QueryCosmosAccountResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ValidatorAccount(self, stream: 'grpclib.server.Stream[ethermint.evm.v1.query_pb2.QueryValidatorAccountRequest, ethermint.evm.v1.query_pb2.QueryValidatorAccountResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Balance(self, stream: 'grpclib.server.Stream[ethermint.evm.v1.query_pb2.QueryBalanceRequest, ethermint.evm.v1.query_pb2.QueryBalanceResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Storage(self, stream: 'grpclib.server.Stream[ethermint.evm.v1.query_pb2.QueryStorageRequest, ethermint.evm.v1.query_pb2.QueryStorageResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Code(self, stream: 'grpclib.server.Stream[ethermint.evm.v1.query_pb2.QueryCodeRequest, ethermint.evm.v1.query_pb2.QueryCodeResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Params(self, stream: 'grpclib.server.Stream[ethermint.evm.v1.query_pb2.QueryParamsRequest, ethermint.evm.v1.query_pb2.QueryParamsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def EthCall(self, stream: 'grpclib.server.Stream[ethermint.evm.v1.query_pb2.EthCallRequest, ethermint.evm.v1.tx_pb2.MsgEthereumTxResponse]') -> None:
        pass

    @abc.abstractmethod
    async def EstimateGas(self, stream: 'grpclib.server.Stream[ethermint.evm.v1.query_pb2.EthCallRequest, ethermint.evm.v1.query_pb2.EstimateGasResponse]') -> None:
        pass

    @abc.abstractmethod
    async def TraceTx(self, stream: 'grpclib.server.Stream[ethermint.evm.v1.query_pb2.QueryTraceTxRequest, ethermint.evm.v1.query_pb2.QueryTraceTxResponse]') -> None:
        pass

    @abc.abstractmethod
    async def TraceBlock(self, stream: 'grpclib.server.Stream[ethermint.evm.v1.query_pb2.QueryTraceBlockRequest, ethermint.evm.v1.query_pb2.QueryTraceBlockResponse]') -> None:
        pass

    @abc.abstractmethod
    async def BaseFee(self, stream: 'grpclib.server.Stream[ethermint.evm.v1.query_pb2.QueryBaseFeeRequest, ethermint.evm.v1.query_pb2.QueryBaseFeeResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/ethermint.evm.v1.Query/Account': grpclib.const.Handler(self.Account, grpclib.const.Cardinality.UNARY_UNARY, ethermint.evm.v1.query_pb2.QueryAccountRequest, ethermint.evm.v1.query_pb2.QueryAccountResponse), '/ethermint.evm.v1.Query/CosmosAccount': grpclib.const.Handler(self.CosmosAccount, grpclib.const.Cardinality.UNARY_UNARY, ethermint.evm.v1.query_pb2.QueryCosmosAccountRequest, ethermint.evm.v1.query_pb2.QueryCosmosAccountResponse), '/ethermint.evm.v1.Query/ValidatorAccount': grpclib.const.Handler(self.ValidatorAccount, grpclib.const.Cardinality.UNARY_UNARY, ethermint.evm.v1.query_pb2.QueryValidatorAccountRequest, ethermint.evm.v1.query_pb2.QueryValidatorAccountResponse), '/ethermint.evm.v1.Query/Balance': grpclib.const.Handler(self.Balance, grpclib.const.Cardinality.UNARY_UNARY, ethermint.evm.v1.query_pb2.QueryBalanceRequest, ethermint.evm.v1.query_pb2.QueryBalanceResponse), '/ethermint.evm.v1.Query/Storage': grpclib.const.Handler(self.Storage, grpclib.const.Cardinality.UNARY_UNARY, ethermint.evm.v1.query_pb2.QueryStorageRequest, ethermint.evm.v1.query_pb2.QueryStorageResponse), '/ethermint.evm.v1.Query/Code': grpclib.const.Handler(self.Code, grpclib.const.Cardinality.UNARY_UNARY, ethermint.evm.v1.query_pb2.QueryCodeRequest, ethermint.evm.v1.query_pb2.QueryCodeResponse), '/ethermint.evm.v1.Query/Params': grpclib.const.Handler(self.Params, grpclib.const.Cardinality.UNARY_UNARY, ethermint.evm.v1.query_pb2.QueryParamsRequest, ethermint.evm.v1.query_pb2.QueryParamsResponse), '/ethermint.evm.v1.Query/EthCall': grpclib.const.Handler(self.EthCall, grpclib.const.Cardinality.UNARY_UNARY, ethermint.evm.v1.query_pb2.EthCallRequest, ethermint.evm.v1.tx_pb2.MsgEthereumTxResponse), '/ethermint.evm.v1.Query/EstimateGas': grpclib.const.Handler(self.EstimateGas, grpclib.const.Cardinality.UNARY_UNARY, ethermint.evm.v1.query_pb2.EthCallRequest, ethermint.evm.v1.query_pb2.EstimateGasResponse), '/ethermint.evm.v1.Query/TraceTx': grpclib.const.Handler(self.TraceTx, grpclib.const.Cardinality.UNARY_UNARY, ethermint.evm.v1.query_pb2.QueryTraceTxRequest, ethermint.evm.v1.query_pb2.QueryTraceTxResponse), '/ethermint.evm.v1.Query/TraceBlock': grpclib.const.Handler(self.TraceBlock, grpclib.const.Cardinality.UNARY_UNARY, ethermint.evm.v1.query_pb2.QueryTraceBlockRequest, ethermint.evm.v1.query_pb2.QueryTraceBlockResponse), '/ethermint.evm.v1.Query/BaseFee': grpclib.const.Handler(self.BaseFee, grpclib.const.Cardinality.UNARY_UNARY, ethermint.evm.v1.query_pb2.QueryBaseFeeRequest, ethermint.evm.v1.query_pb2.QueryBaseFeeResponse)}

class QueryStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Account = grpclib.client.UnaryUnaryMethod(channel, '/ethermint.evm.v1.Query/Account', ethermint.evm.v1.query_pb2.QueryAccountRequest, ethermint.evm.v1.query_pb2.QueryAccountResponse)
        self.CosmosAccount = grpclib.client.UnaryUnaryMethod(channel, '/ethermint.evm.v1.Query/CosmosAccount', ethermint.evm.v1.query_pb2.QueryCosmosAccountRequest, ethermint.evm.v1.query_pb2.QueryCosmosAccountResponse)
        self.ValidatorAccount = grpclib.client.UnaryUnaryMethod(channel, '/ethermint.evm.v1.Query/ValidatorAccount', ethermint.evm.v1.query_pb2.QueryValidatorAccountRequest, ethermint.evm.v1.query_pb2.QueryValidatorAccountResponse)
        self.Balance = grpclib.client.UnaryUnaryMethod(channel, '/ethermint.evm.v1.Query/Balance', ethermint.evm.v1.query_pb2.QueryBalanceRequest, ethermint.evm.v1.query_pb2.QueryBalanceResponse)
        self.Storage = grpclib.client.UnaryUnaryMethod(channel, '/ethermint.evm.v1.Query/Storage', ethermint.evm.v1.query_pb2.QueryStorageRequest, ethermint.evm.v1.query_pb2.QueryStorageResponse)
        self.Code = grpclib.client.UnaryUnaryMethod(channel, '/ethermint.evm.v1.Query/Code', ethermint.evm.v1.query_pb2.QueryCodeRequest, ethermint.evm.v1.query_pb2.QueryCodeResponse)
        self.Params = grpclib.client.UnaryUnaryMethod(channel, '/ethermint.evm.v1.Query/Params', ethermint.evm.v1.query_pb2.QueryParamsRequest, ethermint.evm.v1.query_pb2.QueryParamsResponse)
        self.EthCall = grpclib.client.UnaryUnaryMethod(channel, '/ethermint.evm.v1.Query/EthCall', ethermint.evm.v1.query_pb2.EthCallRequest, ethermint.evm.v1.tx_pb2.MsgEthereumTxResponse)
        self.EstimateGas = grpclib.client.UnaryUnaryMethod(channel, '/ethermint.evm.v1.Query/EstimateGas', ethermint.evm.v1.query_pb2.EthCallRequest, ethermint.evm.v1.query_pb2.EstimateGasResponse)
        self.TraceTx = grpclib.client.UnaryUnaryMethod(channel, '/ethermint.evm.v1.Query/TraceTx', ethermint.evm.v1.query_pb2.QueryTraceTxRequest, ethermint.evm.v1.query_pb2.QueryTraceTxResponse)
        self.TraceBlock = grpclib.client.UnaryUnaryMethod(channel, '/ethermint.evm.v1.Query/TraceBlock', ethermint.evm.v1.query_pb2.QueryTraceBlockRequest, ethermint.evm.v1.query_pb2.QueryTraceBlockResponse)
        self.BaseFee = grpclib.client.UnaryUnaryMethod(channel, '/ethermint.evm.v1.Query/BaseFee', ethermint.evm.v1.query_pb2.QueryBaseFeeRequest, ethermint.evm.v1.query_pb2.QueryBaseFeeResponse)