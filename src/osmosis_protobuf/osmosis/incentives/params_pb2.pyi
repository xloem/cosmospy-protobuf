from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class Params(_message.Message):
    __slots__ = ['distr_epoch_identifier']
    DISTR_EPOCH_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    distr_epoch_identifier: str

    def __init__(self, distr_epoch_identifier: _Optional[str]=...) -> None:
        ...