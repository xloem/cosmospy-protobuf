from gogoproto import gogo_pb2 as _gogo_pb2
from akash.deployment.v1beta1 import group_pb2 as _group_pb2
from cosmos.base.v1beta1 import coin_pb2 as _coin_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class MsgCreateDeployment(_message.Message):
    __slots__ = ['id', 'groups', 'version', 'deposit']
    ID_FIELD_NUMBER: _ClassVar[int]
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    DEPOSIT_FIELD_NUMBER: _ClassVar[int]
    id: DeploymentID
    groups: _containers.RepeatedCompositeFieldContainer[_group_pb2.GroupSpec]
    version: bytes
    deposit: _coin_pb2.Coin

    def __init__(self, id: _Optional[_Union[DeploymentID, _Mapping]]=..., groups: _Optional[_Iterable[_Union[_group_pb2.GroupSpec, _Mapping]]]=..., version: _Optional[bytes]=..., deposit: _Optional[_Union[_coin_pb2.Coin, _Mapping]]=...) -> None:
        ...

class MsgCreateDeploymentResponse(_message.Message):
    __slots__ = []

    def __init__(self) -> None:
        ...

class MsgDepositDeployment(_message.Message):
    __slots__ = ['id', 'amount']
    ID_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    id: DeploymentID
    amount: _coin_pb2.Coin

    def __init__(self, id: _Optional[_Union[DeploymentID, _Mapping]]=..., amount: _Optional[_Union[_coin_pb2.Coin, _Mapping]]=...) -> None:
        ...

class MsgDepositDeploymentResponse(_message.Message):
    __slots__ = []

    def __init__(self) -> None:
        ...

class MsgUpdateDeployment(_message.Message):
    __slots__ = ['id', 'groups', 'version']
    ID_FIELD_NUMBER: _ClassVar[int]
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    id: DeploymentID
    groups: _containers.RepeatedCompositeFieldContainer[_group_pb2.GroupSpec]
    version: bytes

    def __init__(self, id: _Optional[_Union[DeploymentID, _Mapping]]=..., groups: _Optional[_Iterable[_Union[_group_pb2.GroupSpec, _Mapping]]]=..., version: _Optional[bytes]=...) -> None:
        ...

class MsgUpdateDeploymentResponse(_message.Message):
    __slots__ = []

    def __init__(self) -> None:
        ...

class MsgCloseDeployment(_message.Message):
    __slots__ = ['id']
    ID_FIELD_NUMBER: _ClassVar[int]
    id: DeploymentID

    def __init__(self, id: _Optional[_Union[DeploymentID, _Mapping]]=...) -> None:
        ...

class MsgCloseDeploymentResponse(_message.Message):
    __slots__ = []

    def __init__(self) -> None:
        ...

class DeploymentID(_message.Message):
    __slots__ = ['owner', 'dseq']
    OWNER_FIELD_NUMBER: _ClassVar[int]
    DSEQ_FIELD_NUMBER: _ClassVar[int]
    owner: str
    dseq: int

    def __init__(self, owner: _Optional[str]=..., dseq: _Optional[int]=...) -> None:
        ...

class Deployment(_message.Message):
    __slots__ = ['deployment_id', 'state', 'version', 'created_at']

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        invalid: _ClassVar[Deployment.State]
        active: _ClassVar[Deployment.State]
        closed: _ClassVar[Deployment.State]
    invalid: Deployment.State
    active: Deployment.State
    closed: Deployment.State
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    deployment_id: DeploymentID
    state: Deployment.State
    version: bytes
    created_at: int

    def __init__(self, deployment_id: _Optional[_Union[DeploymentID, _Mapping]]=..., state: _Optional[_Union[Deployment.State, str]]=..., version: _Optional[bytes]=..., created_at: _Optional[int]=...) -> None:
        ...

class DeploymentFilters(_message.Message):
    __slots__ = ['owner', 'dseq', 'state']
    OWNER_FIELD_NUMBER: _ClassVar[int]
    DSEQ_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    owner: str
    dseq: int
    state: str

    def __init__(self, owner: _Optional[str]=..., dseq: _Optional[int]=..., state: _Optional[str]=...) -> None:
        ...