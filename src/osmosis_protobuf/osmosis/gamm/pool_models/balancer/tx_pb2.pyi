from gogoproto import gogo_pb2 as _gogo_pb2
from osmosis.gamm.pool_models.balancer import balancerPool_pb2 as _balancerPool_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class MsgCreateBalancerPool(_message.Message):
    __slots__ = ['sender', 'poolParams', 'poolAssets', 'future_pool_governor']
    SENDER_FIELD_NUMBER: _ClassVar[int]
    POOLPARAMS_FIELD_NUMBER: _ClassVar[int]
    POOLASSETS_FIELD_NUMBER: _ClassVar[int]
    FUTURE_POOL_GOVERNOR_FIELD_NUMBER: _ClassVar[int]
    sender: str
    poolParams: _balancerPool_pb2.PoolParams
    poolAssets: _containers.RepeatedCompositeFieldContainer[_balancerPool_pb2.PoolAsset]
    future_pool_governor: str

    def __init__(self, sender: _Optional[str]=..., poolParams: _Optional[_Union[_balancerPool_pb2.PoolParams, _Mapping]]=..., poolAssets: _Optional[_Iterable[_Union[_balancerPool_pb2.PoolAsset, _Mapping]]]=..., future_pool_governor: _Optional[str]=...) -> None:
        ...

class MsgCreateBalancerPoolResponse(_message.Message):
    __slots__ = ['pool_id']
    POOL_ID_FIELD_NUMBER: _ClassVar[int]
    pool_id: int

    def __init__(self, pool_id: _Optional[int]=...) -> None:
        ...