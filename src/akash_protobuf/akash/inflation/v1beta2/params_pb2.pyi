from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class Params(_message.Message):
    __slots__ = ['inflation_decay_factor', 'initial_inflation', 'variance']
    INFLATION_DECAY_FACTOR_FIELD_NUMBER: _ClassVar[int]
    INITIAL_INFLATION_FIELD_NUMBER: _ClassVar[int]
    VARIANCE_FIELD_NUMBER: _ClassVar[int]
    inflation_decay_factor: str
    initial_inflation: str
    variance: str

    def __init__(self, inflation_decay_factor: _Optional[str]=..., initial_inflation: _Optional[str]=..., variance: _Optional[str]=...) -> None:
        ...