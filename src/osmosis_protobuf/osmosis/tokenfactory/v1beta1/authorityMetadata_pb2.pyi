from gogoproto import gogo_pb2 as _gogo_pb2
from cosmos.base.v1beta1 import coin_pb2 as _coin_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class DenomAuthorityMetadata(_message.Message):
    __slots__ = ['Admin']
    ADMIN_FIELD_NUMBER: _ClassVar[int]
    Admin: str

    def __init__(self, Admin: _Optional[str]=...) -> None:
        ...