import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
from .... import akash

class MsgBase(abc.ABC):

    @abc.abstractmethod
    async def CreateDeployment(self, stream: 'grpclib.server.Stream[akash.deployment.v1beta3.deploymentmsg_pb2.MsgCreateDeployment, akash.deployment.v1beta3.deploymentmsg_pb2.MsgCreateDeploymentResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DepositDeployment(self, stream: 'grpclib.server.Stream[akash.deployment.v1beta3.deploymentmsg_pb2.MsgDepositDeployment, akash.deployment.v1beta3.deploymentmsg_pb2.MsgDepositDeploymentResponse]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateDeployment(self, stream: 'grpclib.server.Stream[akash.deployment.v1beta3.deploymentmsg_pb2.MsgUpdateDeployment, akash.deployment.v1beta3.deploymentmsg_pb2.MsgUpdateDeploymentResponse]') -> None:
        pass

    @abc.abstractmethod
    async def CloseDeployment(self, stream: 'grpclib.server.Stream[akash.deployment.v1beta3.deploymentmsg_pb2.MsgCloseDeployment, akash.deployment.v1beta3.deploymentmsg_pb2.MsgCloseDeploymentResponse]') -> None:
        pass

    @abc.abstractmethod
    async def CloseGroup(self, stream: 'grpclib.server.Stream[akash.deployment.v1beta3.groupmsg_pb2.MsgCloseGroup, akash.deployment.v1beta3.groupmsg_pb2.MsgCloseGroupResponse]') -> None:
        pass

    @abc.abstractmethod
    async def PauseGroup(self, stream: 'grpclib.server.Stream[akash.deployment.v1beta3.groupmsg_pb2.MsgPauseGroup, akash.deployment.v1beta3.groupmsg_pb2.MsgPauseGroupResponse]') -> None:
        pass

    @abc.abstractmethod
    async def StartGroup(self, stream: 'grpclib.server.Stream[akash.deployment.v1beta3.groupmsg_pb2.MsgStartGroup, akash.deployment.v1beta3.groupmsg_pb2.MsgStartGroupResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/akash.deployment.v1beta3.Msg/CreateDeployment': grpclib.const.Handler(self.CreateDeployment, grpclib.const.Cardinality.UNARY_UNARY, akash.deployment.v1beta3.deploymentmsg_pb2.MsgCreateDeployment, akash.deployment.v1beta3.deploymentmsg_pb2.MsgCreateDeploymentResponse), '/akash.deployment.v1beta3.Msg/DepositDeployment': grpclib.const.Handler(self.DepositDeployment, grpclib.const.Cardinality.UNARY_UNARY, akash.deployment.v1beta3.deploymentmsg_pb2.MsgDepositDeployment, akash.deployment.v1beta3.deploymentmsg_pb2.MsgDepositDeploymentResponse), '/akash.deployment.v1beta3.Msg/UpdateDeployment': grpclib.const.Handler(self.UpdateDeployment, grpclib.const.Cardinality.UNARY_UNARY, akash.deployment.v1beta3.deploymentmsg_pb2.MsgUpdateDeployment, akash.deployment.v1beta3.deploymentmsg_pb2.MsgUpdateDeploymentResponse), '/akash.deployment.v1beta3.Msg/CloseDeployment': grpclib.const.Handler(self.CloseDeployment, grpclib.const.Cardinality.UNARY_UNARY, akash.deployment.v1beta3.deploymentmsg_pb2.MsgCloseDeployment, akash.deployment.v1beta3.deploymentmsg_pb2.MsgCloseDeploymentResponse), '/akash.deployment.v1beta3.Msg/CloseGroup': grpclib.const.Handler(self.CloseGroup, grpclib.const.Cardinality.UNARY_UNARY, akash.deployment.v1beta3.groupmsg_pb2.MsgCloseGroup, akash.deployment.v1beta3.groupmsg_pb2.MsgCloseGroupResponse), '/akash.deployment.v1beta3.Msg/PauseGroup': grpclib.const.Handler(self.PauseGroup, grpclib.const.Cardinality.UNARY_UNARY, akash.deployment.v1beta3.groupmsg_pb2.MsgPauseGroup, akash.deployment.v1beta3.groupmsg_pb2.MsgPauseGroupResponse), '/akash.deployment.v1beta3.Msg/StartGroup': grpclib.const.Handler(self.StartGroup, grpclib.const.Cardinality.UNARY_UNARY, akash.deployment.v1beta3.groupmsg_pb2.MsgStartGroup, akash.deployment.v1beta3.groupmsg_pb2.MsgStartGroupResponse)}

class MsgStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.CreateDeployment = grpclib.client.UnaryUnaryMethod(channel, '/akash.deployment.v1beta3.Msg/CreateDeployment', akash.deployment.v1beta3.deploymentmsg_pb2.MsgCreateDeployment, akash.deployment.v1beta3.deploymentmsg_pb2.MsgCreateDeploymentResponse)
        self.DepositDeployment = grpclib.client.UnaryUnaryMethod(channel, '/akash.deployment.v1beta3.Msg/DepositDeployment', akash.deployment.v1beta3.deploymentmsg_pb2.MsgDepositDeployment, akash.deployment.v1beta3.deploymentmsg_pb2.MsgDepositDeploymentResponse)
        self.UpdateDeployment = grpclib.client.UnaryUnaryMethod(channel, '/akash.deployment.v1beta3.Msg/UpdateDeployment', akash.deployment.v1beta3.deploymentmsg_pb2.MsgUpdateDeployment, akash.deployment.v1beta3.deploymentmsg_pb2.MsgUpdateDeploymentResponse)
        self.CloseDeployment = grpclib.client.UnaryUnaryMethod(channel, '/akash.deployment.v1beta3.Msg/CloseDeployment', akash.deployment.v1beta3.deploymentmsg_pb2.MsgCloseDeployment, akash.deployment.v1beta3.deploymentmsg_pb2.MsgCloseDeploymentResponse)
        self.CloseGroup = grpclib.client.UnaryUnaryMethod(channel, '/akash.deployment.v1beta3.Msg/CloseGroup', akash.deployment.v1beta3.groupmsg_pb2.MsgCloseGroup, akash.deployment.v1beta3.groupmsg_pb2.MsgCloseGroupResponse)
        self.PauseGroup = grpclib.client.UnaryUnaryMethod(channel, '/akash.deployment.v1beta3.Msg/PauseGroup', akash.deployment.v1beta3.groupmsg_pb2.MsgPauseGroup, akash.deployment.v1beta3.groupmsg_pb2.MsgPauseGroupResponse)
        self.StartGroup = grpclib.client.UnaryUnaryMethod(channel, '/akash.deployment.v1beta3.Msg/StartGroup', akash.deployment.v1beta3.groupmsg_pb2.MsgStartGroup, akash.deployment.v1beta3.groupmsg_pb2.MsgStartGroupResponse)