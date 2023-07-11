from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class Params(_message.Message):
    __slots__ = ['denom_take_rates', 'default_take_rate']

    class DenomTakeRatesEntry(_message.Message):
        __slots__ = ['key', 'value']
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int

        def __init__(self, key: _Optional[str]=..., value: _Optional[int]=...) -> None:
            ...
    DENOM_TAKE_RATES_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_TAKE_RATE_FIELD_NUMBER: _ClassVar[int]
    denom_take_rates: _containers.ScalarMap[str, int]
    default_take_rate: int

    def __init__(self, denom_take_rates: _Optional[_Mapping[str, int]]=..., default_take_rate: _Optional[int]=...) -> None:
        ...