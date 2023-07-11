from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class InflationDistribution(_message.Message):
    __slots__ = ['staking_rewards', 'usage_incentives', 'community_pool']
    STAKING_REWARDS_FIELD_NUMBER: _ClassVar[int]
    USAGE_INCENTIVES_FIELD_NUMBER: _ClassVar[int]
    COMMUNITY_POOL_FIELD_NUMBER: _ClassVar[int]
    staking_rewards: str
    usage_incentives: str
    community_pool: str

    def __init__(self, staking_rewards: _Optional[str]=..., usage_incentives: _Optional[str]=..., community_pool: _Optional[str]=...) -> None:
        ...

class ExponentialCalculation(_message.Message):
    __slots__ = ['a', 'r', 'c', 'bonding_target', 'max_variance']
    A_FIELD_NUMBER: _ClassVar[int]
    R_FIELD_NUMBER: _ClassVar[int]
    C_FIELD_NUMBER: _ClassVar[int]
    BONDING_TARGET_FIELD_NUMBER: _ClassVar[int]
    MAX_VARIANCE_FIELD_NUMBER: _ClassVar[int]
    a: str
    r: str
    c: str
    bonding_target: str
    max_variance: str

    def __init__(self, a: _Optional[str]=..., r: _Optional[str]=..., c: _Optional[str]=..., bonding_target: _Optional[str]=..., max_variance: _Optional[str]=...) -> None:
        ...