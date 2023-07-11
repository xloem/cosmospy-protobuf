from cosmos.base.v1beta1 import coin_pb2 as _coin_pb2
from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Incentive(_message.Message):
    __slots__ = ['contract', 'allocations', 'epochs', 'start_time', 'total_gas']
    CONTRACT_FIELD_NUMBER: _ClassVar[int]
    ALLOCATIONS_FIELD_NUMBER: _ClassVar[int]
    EPOCHS_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    TOTAL_GAS_FIELD_NUMBER: _ClassVar[int]
    contract: str
    allocations: _containers.RepeatedCompositeFieldContainer[_coin_pb2.DecCoin]
    epochs: int
    start_time: _timestamp_pb2.Timestamp
    total_gas: int

    def __init__(self, contract: _Optional[str]=..., allocations: _Optional[_Iterable[_Union[_coin_pb2.DecCoin, _Mapping]]]=..., epochs: _Optional[int]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., total_gas: _Optional[int]=...) -> None:
        ...

class GasMeter(_message.Message):
    __slots__ = ['contract', 'participant', 'cumulative_gas']
    CONTRACT_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    CUMULATIVE_GAS_FIELD_NUMBER: _ClassVar[int]
    contract: str
    participant: str
    cumulative_gas: int

    def __init__(self, contract: _Optional[str]=..., participant: _Optional[str]=..., cumulative_gas: _Optional[int]=...) -> None:
        ...

class RegisterIncentiveProposal(_message.Message):
    __slots__ = ['title', 'description', 'contract', 'allocations', 'epochs']
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_FIELD_NUMBER: _ClassVar[int]
    ALLOCATIONS_FIELD_NUMBER: _ClassVar[int]
    EPOCHS_FIELD_NUMBER: _ClassVar[int]
    title: str
    description: str
    contract: str
    allocations: _containers.RepeatedCompositeFieldContainer[_coin_pb2.DecCoin]
    epochs: int

    def __init__(self, title: _Optional[str]=..., description: _Optional[str]=..., contract: _Optional[str]=..., allocations: _Optional[_Iterable[_Union[_coin_pb2.DecCoin, _Mapping]]]=..., epochs: _Optional[int]=...) -> None:
        ...

class CancelIncentiveProposal(_message.Message):
    __slots__ = ['title', 'description', 'contract']
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_FIELD_NUMBER: _ClassVar[int]
    title: str
    description: str
    contract: str

    def __init__(self, title: _Optional[str]=..., description: _Optional[str]=..., contract: _Optional[str]=...) -> None:
        ...