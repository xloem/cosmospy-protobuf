import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
from .... import gogoproto
from .... import google
from .... import cosmos
from .... import akash

class QueryBase(abc.ABC):

    @abc.abstractmethod
    async def Providers(self, stream: 'grpclib.server.Stream[akash.provider.v1beta2.query_pb2.QueryProvidersRequest, akash.provider.v1beta2.query_pb2.QueryProvidersResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Provider(self, stream: 'grpclib.server.Stream[akash.provider.v1beta2.query_pb2.QueryProviderRequest, akash.provider.v1beta2.query_pb2.QueryProviderResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/akash.provider.v1beta2.Query/Providers': grpclib.const.Handler(self.Providers, grpclib.const.Cardinality.UNARY_UNARY, akash.provider.v1beta2.query_pb2.QueryProvidersRequest, akash.provider.v1beta2.query_pb2.QueryProvidersResponse), '/akash.provider.v1beta2.Query/Provider': grpclib.const.Handler(self.Provider, grpclib.const.Cardinality.UNARY_UNARY, akash.provider.v1beta2.query_pb2.QueryProviderRequest, akash.provider.v1beta2.query_pb2.QueryProviderResponse)}

class QueryStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Providers = grpclib.client.UnaryUnaryMethod(channel, '/akash.provider.v1beta2.Query/Providers', akash.provider.v1beta2.query_pb2.QueryProvidersRequest, akash.provider.v1beta2.query_pb2.QueryProvidersResponse)
        self.Provider = grpclib.client.UnaryUnaryMethod(channel, '/akash.provider.v1beta2.Query/Provider', akash.provider.v1beta2.query_pb2.QueryProviderRequest, akash.provider.v1beta2.query_pb2.QueryProviderResponse)