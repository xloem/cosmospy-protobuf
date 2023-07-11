from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class Params(_message.Message):
    __slots__ = ['min_commission_rate']
    MIN_COMMISSION_RATE_FIELD_NUMBER: _ClassVar[int]
    min_commission_rate: str

    def __init__(self, min_commission_rate: _Optional[str]=...) -> None:
        ...