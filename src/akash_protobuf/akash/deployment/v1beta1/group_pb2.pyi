from gogoproto import gogo_pb2 as _gogo_pb2
from akash.base.v1beta1 import resource_pb2 as _resource_pb2
from akash.base.v1beta1 import attribute_pb2 as _attribute_pb2
from cosmos.base.v1beta1 import coin_pb2 as _coin_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class MsgCloseGroup(_message.Message):
    __slots__ = ['id']
    ID_FIELD_NUMBER: _ClassVar[int]
    id: GroupID

    def __init__(self, id: _Optional[_Union[GroupID, _Mapping]]=...) -> None:
        ...

class MsgCloseGroupResponse(_message.Message):
    __slots__ = []

    def __init__(self) -> None:
        ...

class MsgPauseGroup(_message.Message):
    __slots__ = ['id']
    ID_FIELD_NUMBER: _ClassVar[int]
    id: GroupID

    def __init__(self, id: _Optional[_Union[GroupID, _Mapping]]=...) -> None:
        ...

class MsgPauseGroupResponse(_message.Message):
    __slots__ = []

    def __init__(self) -> None:
        ...

class MsgStartGroup(_message.Message):
    __slots__ = ['id']
    ID_FIELD_NUMBER: _ClassVar[int]
    id: GroupID

    def __init__(self, id: _Optional[_Union[GroupID, _Mapping]]=...) -> None:
        ...

class MsgStartGroupResponse(_message.Message):
    __slots__ = []

    def __init__(self) -> None:
        ...

class GroupID(_message.Message):
    __slots__ = ['owner', 'dseq', 'gseq']
    OWNER_FIELD_NUMBER: _ClassVar[int]
    DSEQ_FIELD_NUMBER: _ClassVar[int]
    GSEQ_FIELD_NUMBER: _ClassVar[int]
    owner: str
    dseq: int
    gseq: int

    def __init__(self, owner: _Optional[str]=..., dseq: _Optional[int]=..., gseq: _Optional[int]=...) -> None:
        ...

class GroupSpec(_message.Message):
    __slots__ = ['name', 'requirements', 'resources']
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUIREMENTS_FIELD_NUMBER: _ClassVar[int]
    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    name: str
    requirements: _attribute_pb2.PlacementRequirements
    resources: _containers.RepeatedCompositeFieldContainer[Resource]

    def __init__(self, name: _Optional[str]=..., requirements: _Optional[_Union[_attribute_pb2.PlacementRequirements, _Mapping]]=..., resources: _Optional[_Iterable[_Union[Resource, _Mapping]]]=...) -> None:
        ...

class Group(_message.Message):
    __slots__ = ['group_id', 'state', 'group_spec', 'created_at']

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        invalid: _ClassVar[Group.State]
        open: _ClassVar[Group.State]
        paused: _ClassVar[Group.State]
        insufficient_funds: _ClassVar[Group.State]
        closed: _ClassVar[Group.State]
    invalid: Group.State
    open: Group.State
    paused: Group.State
    insufficient_funds: Group.State
    closed: Group.State
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    GROUP_SPEC_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    group_id: GroupID
    state: Group.State
    group_spec: GroupSpec
    created_at: int

    def __init__(self, group_id: _Optional[_Union[GroupID, _Mapping]]=..., state: _Optional[_Union[Group.State, str]]=..., group_spec: _Optional[_Union[GroupSpec, _Mapping]]=..., created_at: _Optional[int]=...) -> None:
        ...

class Resource(_message.Message):
    __slots__ = ['resources', 'count', 'price']
    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    resources: _resource_pb2.ResourceUnits
    count: int
    price: _coin_pb2.Coin

    def __init__(self, resources: _Optional[_Union[_resource_pb2.ResourceUnits, _Mapping]]=..., count: _Optional[int]=..., price: _Optional[_Union[_coin_pb2.Coin, _Mapping]]=...) -> None:
        ...