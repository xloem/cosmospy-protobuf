from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class Params(_message.Message):
    __slots__ = ['min_deposits']

    class MinDepositsEntry(_message.Message):
        __slots__ = ['key', 'value']
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int

        def __init__(self, key: _Optional[str]=..., value: _Optional[int]=...) -> None:
            ...
    MIN_DEPOSITS_FIELD_NUMBER: _ClassVar[int]
    min_deposits: _containers.ScalarMap[str, int]

    def __init__(self, min_deposits: _Optional[_Mapping[str, int]]=...) -> None:
        ...