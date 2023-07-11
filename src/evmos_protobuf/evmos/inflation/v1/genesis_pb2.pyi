from gogoproto import gogo_pb2 as _gogo_pb2
from evmos.inflation.v1 import inflation_pb2 as _inflation_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GenesisState(_message.Message):
    __slots__ = ['params', 'period', 'epoch_identifier', 'epochs_per_period', 'skipped_epochs']
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    PERIOD_FIELD_NUMBER: _ClassVar[int]
    EPOCH_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    EPOCHS_PER_PERIOD_FIELD_NUMBER: _ClassVar[int]
    SKIPPED_EPOCHS_FIELD_NUMBER: _ClassVar[int]
    params: Params
    period: int
    epoch_identifier: str
    epochs_per_period: int
    skipped_epochs: int

    def __init__(self, params: _Optional[_Union[Params, _Mapping]]=..., period: _Optional[int]=..., epoch_identifier: _Optional[str]=..., epochs_per_period: _Optional[int]=..., skipped_epochs: _Optional[int]=...) -> None:
        ...

class Params(_message.Message):
    __slots__ = ['mint_denom', 'exponential_calculation', 'inflation_distribution', 'enable_inflation']
    MINT_DENOM_FIELD_NUMBER: _ClassVar[int]
    EXPONENTIAL_CALCULATION_FIELD_NUMBER: _ClassVar[int]
    INFLATION_DISTRIBUTION_FIELD_NUMBER: _ClassVar[int]
    ENABLE_INFLATION_FIELD_NUMBER: _ClassVar[int]
    mint_denom: str
    exponential_calculation: _inflation_pb2.ExponentialCalculation
    inflation_distribution: _inflation_pb2.InflationDistribution
    enable_inflation: bool

    def __init__(self, mint_denom: _Optional[str]=..., exponential_calculation: _Optional[_Union[_inflation_pb2.ExponentialCalculation, _Mapping]]=..., inflation_distribution: _Optional[_Union[_inflation_pb2.InflationDistribution, _Mapping]]=..., enable_inflation: bool=...) -> None:
        ...