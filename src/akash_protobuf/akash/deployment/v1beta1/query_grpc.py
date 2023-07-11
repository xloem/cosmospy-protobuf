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
    async def Deployments(self, stream: 'grpclib.server.Stream[akash.deployment.v1beta1.query_pb2.QueryDeploymentsRequest, akash.deployment.v1beta1.query_pb2.QueryDeploymentsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Deployment(self, stream: 'grpclib.server.Stream[akash.deployment.v1beta1.query_pb2.QueryDeploymentRequest, akash.deployment.v1beta1.query_pb2.QueryDeploymentResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Group(self, stream: 'grpclib.server.Stream[akash.deployment.v1beta1.query_pb2.QueryGroupRequest, akash.deployment.v1beta1.query_pb2.QueryGroupResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/akash.deployment.v1beta1.Query/Deployments': grpclib.const.Handler(self.Deployments, grpclib.const.Cardinality.UNARY_UNARY, akash.deployment.v1beta1.query_pb2.QueryDeploymentsRequest, akash.deployment.v1beta1.query_pb2.QueryDeploymentsResponse), '/akash.deployment.v1beta1.Query/Deployment': grpclib.const.Handler(self.Deployment, grpclib.const.Cardinality.UNARY_UNARY, akash.deployment.v1beta1.query_pb2.QueryDeploymentRequest, akash.deployment.v1beta1.query_pb2.QueryDeploymentResponse), '/akash.deployment.v1beta1.Query/Group': grpclib.const.Handler(self.Group, grpclib.const.Cardinality.UNARY_UNARY, akash.deployment.v1beta1.query_pb2.QueryGroupRequest, akash.deployment.v1beta1.query_pb2.QueryGroupResponse)}

class QueryStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Deployments = grpclib.client.UnaryUnaryMethod(channel, '/akash.deployment.v1beta1.Query/Deployments', akash.deployment.v1beta1.query_pb2.QueryDeploymentsRequest, akash.deployment.v1beta1.query_pb2.QueryDeploymentsResponse)
        self.Deployment = grpclib.client.UnaryUnaryMethod(channel, '/akash.deployment.v1beta1.Query/Deployment', akash.deployment.v1beta1.query_pb2.QueryDeploymentRequest, akash.deployment.v1beta1.query_pb2.QueryDeploymentResponse)
        self.Group = grpclib.client.UnaryUnaryMethod(channel, '/akash.deployment.v1beta1.Query/Group', akash.deployment.v1beta1.query_pb2.QueryGroupRequest, akash.deployment.v1beta1.query_pb2.QueryGroupResponse)