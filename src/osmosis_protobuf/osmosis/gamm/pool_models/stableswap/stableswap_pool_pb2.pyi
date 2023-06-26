from cosmos_proto import cosmos_pb2 as _cosmos_pb2
from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from cosmos.auth.v1beta1 import auth_pb2 as _auth_pb2
from cosmos.base.v1beta1 import coin_pb2 as _coin_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class PoolParams(_message.Message):
    __slots__ = ['swapFee', 'exitFee']
    SWAPFEE_FIELD_NUMBER: _ClassVar[int]
    EXITFEE_FIELD_NUMBER: _ClassVar[int]
    swapFee: str
    exitFee: str

    def __init__(self, swapFee: _Optional[str]=..., exitFee: _Optional[str]=...) -> None:
        ...

class Pool(_message.Message):
    __slots__ = ['address', 'id', 'poolParams', 'future_pool_governor', 'totalShares', 'poolLiquidity', 'scaling_factor', 'scaling_factor_governor']
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    POOLPARAMS_FIELD_NUMBER: _ClassVar[int]
    FUTURE_POOL_GOVERNOR_FIELD_NUMBER: _ClassVar[int]
    TOTALSHARES_FIELD_NUMBER: _ClassVar[int]
    POOLLIQUIDITY_FIELD_NUMBER: _ClassVar[int]
    SCALING_FACTOR_FIELD_NUMBER: _ClassVar[int]
    SCALING_FACTOR_GOVERNOR_FIELD_NUMBER: _ClassVar[int]
    address: str
    id: int
    poolParams: PoolParams
    future_pool_governor: str
    totalShares: _coin_pb2.Coin
    poolLiquidity: _containers.RepeatedCompositeFieldContainer[_coin_pb2.Coin]
    scaling_factor: _containers.RepeatedScalarFieldContainer[int]
    scaling_factor_governor: str

    def __init__(self, address: _Optional[str]=..., id: _Optional[int]=..., poolParams: _Optional[_Union[PoolParams, _Mapping]]=..., future_pool_governor: _Optional[str]=..., totalShares: _Optional[_Union[_coin_pb2.Coin, _Mapping]]=..., poolLiquidity: _Optional[_Iterable[_Union[_coin_pb2.Coin, _Mapping]]]=..., scaling_factor: _Optional[_Iterable[int]]=..., scaling_factor_governor: _Optional[str]=...) -> None:
        ...