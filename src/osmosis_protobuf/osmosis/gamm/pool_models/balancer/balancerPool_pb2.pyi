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

class SmoothWeightChangeParams(_message.Message):
    __slots__ = ['start_time', 'duration', 'initialPoolWeights', 'targetPoolWeights']
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    INITIALPOOLWEIGHTS_FIELD_NUMBER: _ClassVar[int]
    TARGETPOOLWEIGHTS_FIELD_NUMBER: _ClassVar[int]
    start_time: _timestamp_pb2.Timestamp
    duration: _duration_pb2.Duration
    initialPoolWeights: _containers.RepeatedCompositeFieldContainer[PoolAsset]
    targetPoolWeights: _containers.RepeatedCompositeFieldContainer[PoolAsset]

    def __init__(self, start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., initialPoolWeights: _Optional[_Iterable[_Union[PoolAsset, _Mapping]]]=..., targetPoolWeights: _Optional[_Iterable[_Union[PoolAsset, _Mapping]]]=...) -> None:
        ...

class PoolParams(_message.Message):
    __slots__ = ['swapFee', 'exitFee', 'smoothWeightChangeParams']
    SWAPFEE_FIELD_NUMBER: _ClassVar[int]
    EXITFEE_FIELD_NUMBER: _ClassVar[int]
    SMOOTHWEIGHTCHANGEPARAMS_FIELD_NUMBER: _ClassVar[int]
    swapFee: str
    exitFee: str
    smoothWeightChangeParams: SmoothWeightChangeParams

    def __init__(self, swapFee: _Optional[str]=..., exitFee: _Optional[str]=..., smoothWeightChangeParams: _Optional[_Union[SmoothWeightChangeParams, _Mapping]]=...) -> None:
        ...

class PoolAsset(_message.Message):
    __slots__ = ['token', 'weight']
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    token: _coin_pb2.Coin
    weight: str

    def __init__(self, token: _Optional[_Union[_coin_pb2.Coin, _Mapping]]=..., weight: _Optional[str]=...) -> None:
        ...

class Pool(_message.Message):
    __slots__ = ['address', 'id', 'poolParams', 'future_pool_governor', 'totalShares', 'poolAssets', 'totalWeight']
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    POOLPARAMS_FIELD_NUMBER: _ClassVar[int]
    FUTURE_POOL_GOVERNOR_FIELD_NUMBER: _ClassVar[int]
    TOTALSHARES_FIELD_NUMBER: _ClassVar[int]
    POOLASSETS_FIELD_NUMBER: _ClassVar[int]
    TOTALWEIGHT_FIELD_NUMBER: _ClassVar[int]
    address: str
    id: int
    poolParams: PoolParams
    future_pool_governor: str
    totalShares: _coin_pb2.Coin
    poolAssets: _containers.RepeatedCompositeFieldContainer[PoolAsset]
    totalWeight: str

    def __init__(self, address: _Optional[str]=..., id: _Optional[int]=..., poolParams: _Optional[_Union[PoolParams, _Mapping]]=..., future_pool_governor: _Optional[str]=..., totalShares: _Optional[_Union[_coin_pb2.Coin, _Mapping]]=..., poolAssets: _Optional[_Iterable[_Union[PoolAsset, _Mapping]]]=..., totalWeight: _Optional[str]=...) -> None:
        ...