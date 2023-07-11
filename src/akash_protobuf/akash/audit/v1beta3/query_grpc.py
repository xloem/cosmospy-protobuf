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
    async def AllProvidersAttributes(self, stream: 'grpclib.server.Stream[akash.audit.v1beta3.query_pb2.QueryAllProvidersAttributesRequest, akash.audit.v1beta3.query_pb2.QueryProvidersResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ProviderAttributes(self, stream: 'grpclib.server.Stream[akash.audit.v1beta3.query_pb2.QueryProviderAttributesRequest, akash.audit.v1beta3.query_pb2.QueryProvidersResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ProviderAuditorAttributes(self, stream: 'grpclib.server.Stream[akash.audit.v1beta3.query_pb2.QueryProviderAuditorRequest, akash.audit.v1beta3.query_pb2.QueryProvidersResponse]') -> None:
        pass

    @abc.abstractmethod
    async def AuditorAttributes(self, stream: 'grpclib.server.Stream[akash.audit.v1beta3.query_pb2.QueryAuditorAttributesRequest, akash.audit.v1beta3.query_pb2.QueryProvidersResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/akash.audit.v1beta3.Query/AllProvidersAttributes': grpclib.const.Handler(self.AllProvidersAttributes, grpclib.const.Cardinality.UNARY_UNARY, akash.audit.v1beta3.query_pb2.QueryAllProvidersAttributesRequest, akash.audit.v1beta3.query_pb2.QueryProvidersResponse), '/akash.audit.v1beta3.Query/ProviderAttributes': grpclib.const.Handler(self.ProviderAttributes, grpclib.const.Cardinality.UNARY_UNARY, akash.audit.v1beta3.query_pb2.QueryProviderAttributesRequest, akash.audit.v1beta3.query_pb2.QueryProvidersResponse), '/akash.audit.v1beta3.Query/ProviderAuditorAttributes': grpclib.const.Handler(self.ProviderAuditorAttributes, grpclib.const.Cardinality.UNARY_UNARY, akash.audit.v1beta3.query_pb2.QueryProviderAuditorRequest, akash.audit.v1beta3.query_pb2.QueryProvidersResponse), '/akash.audit.v1beta3.Query/AuditorAttributes': grpclib.const.Handler(self.AuditorAttributes, grpclib.const.Cardinality.UNARY_UNARY, akash.audit.v1beta3.query_pb2.QueryAuditorAttributesRequest, akash.audit.v1beta3.query_pb2.QueryProvidersResponse)}

class QueryStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.AllProvidersAttributes = grpclib.client.UnaryUnaryMethod(channel, '/akash.audit.v1beta3.Query/AllProvidersAttributes', akash.audit.v1beta3.query_pb2.QueryAllProvidersAttributesRequest, akash.audit.v1beta3.query_pb2.QueryProvidersResponse)
        self.ProviderAttributes = grpclib.client.UnaryUnaryMethod(channel, '/akash.audit.v1beta3.Query/ProviderAttributes', akash.audit.v1beta3.query_pb2.QueryProviderAttributesRequest, akash.audit.v1beta3.query_pb2.QueryProvidersResponse)
        self.ProviderAuditorAttributes = grpclib.client.UnaryUnaryMethod(channel, '/akash.audit.v1beta3.Query/ProviderAuditorAttributes', akash.audit.v1beta3.query_pb2.QueryProviderAuditorRequest, akash.audit.v1beta3.query_pb2.QueryProvidersResponse)
        self.AuditorAttributes = grpclib.client.UnaryUnaryMethod(channel, '/akash.audit.v1beta3.Query/AuditorAttributes', akash.audit.v1beta3.query_pb2.QueryAuditorAttributesRequest, akash.audit.v1beta3.query_pb2.QueryProvidersResponse)