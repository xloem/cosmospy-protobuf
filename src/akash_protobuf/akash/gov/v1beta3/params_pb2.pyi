from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class DepositParams(_message.Message):
    __slots__ = ['min_initial_deposit_rate']
    MIN_INITIAL_DEPOSIT_RATE_FIELD_NUMBER: _ClassVar[int]
    min_initial_deposit_rate: bytes

    def __init__(self, min_initial_deposit_rate: _Optional[bytes]=...) -> None:
        ...