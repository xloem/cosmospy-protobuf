import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
from .... import ethermint
from .... import gogoproto
from .... import google

class QueryBase(abc.ABC):

    @abc.abstractmethod
    async def Params(self, stream: 'grpclib.server.Stream[ethermint.feemarket.v1.query_pb2.QueryParamsRequest, ethermint.feemarket.v1.query_pb2.QueryParamsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def BaseFee(self, stream: 'grpclib.server.Stream[ethermint.feemarket.v1.query_pb2.QueryBaseFeeRequest, ethermint.feemarket.v1.query_pb2.QueryBaseFeeResponse]') -> None:
        pass

    @abc.abstractmethod
    async def BlockGas(self, stream: 'grpclib.server.Stream[ethermint.feemarket.v1.query_pb2.QueryBlockGasRequest, ethermint.feemarket.v1.query_pb2.QueryBlockGasResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/ethermint.feemarket.v1.Query/Params': grpclib.const.Handler(self.Params, grpclib.const.Cardinality.UNARY_UNARY, ethermint.feemarket.v1.query_pb2.QueryParamsRequest, ethermint.feemarket.v1.query_pb2.QueryParamsResponse), '/ethermint.feemarket.v1.Query/BaseFee': grpclib.const.Handler(self.BaseFee, grpclib.const.Cardinality.UNARY_UNARY, ethermint.feemarket.v1.query_pb2.QueryBaseFeeRequest, ethermint.feemarket.v1.query_pb2.QueryBaseFeeResponse), '/ethermint.feemarket.v1.Query/BlockGas': grpclib.const.Handler(self.BlockGas, grpclib.const.Cardinality.UNARY_UNARY, ethermint.feemarket.v1.query_pb2.QueryBlockGasRequest, ethermint.feemarket.v1.query_pb2.QueryBlockGasResponse)}

class QueryStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Params = grpclib.client.UnaryUnaryMethod(channel, '/ethermint.feemarket.v1.Query/Params', ethermint.feemarket.v1.query_pb2.QueryParamsRequest, ethermint.feemarket.v1.query_pb2.QueryParamsResponse)
        self.BaseFee = grpclib.client.UnaryUnaryMethod(channel, '/ethermint.feemarket.v1.Query/BaseFee', ethermint.feemarket.v1.query_pb2.QueryBaseFeeRequest, ethermint.feemarket.v1.query_pb2.QueryBaseFeeResponse)
        self.BlockGas = grpclib.client.UnaryUnaryMethod(channel, '/ethermint.feemarket.v1.Query/BlockGas', ethermint.feemarket.v1.query_pb2.QueryBlockGasRequest, ethermint.feemarket.v1.query_pb2.QueryBlockGasResponse)