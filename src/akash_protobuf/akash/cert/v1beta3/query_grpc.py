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
    async def Certificates(self, stream: 'grpclib.server.Stream[akash.cert.v1beta3.query_pb2.QueryCertificatesRequest, akash.cert.v1beta3.query_pb2.QueryCertificatesResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/akash.cert.v1beta3.Query/Certificates': grpclib.const.Handler(self.Certificates, grpclib.const.Cardinality.UNARY_UNARY, akash.cert.v1beta3.query_pb2.QueryCertificatesRequest, akash.cert.v1beta3.query_pb2.QueryCertificatesResponse)}

class QueryStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Certificates = grpclib.client.UnaryUnaryMethod(channel, '/akash.cert.v1beta3.Query/Certificates', akash.cert.v1beta3.query_pb2.QueryCertificatesRequest, akash.cert.v1beta3.query_pb2.QueryCertificatesResponse)