from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Endpoint(_message.Message):
    __slots__ = ['kind']

    class Kind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        SHARED_HTTP: _ClassVar[Endpoint.Kind]
        RANDOM_PORT: _ClassVar[Endpoint.Kind]
    SHARED_HTTP: Endpoint.Kind
    RANDOM_PORT: Endpoint.Kind
    KIND_FIELD_NUMBER: _ClassVar[int]
    kind: Endpoint.Kind

    def __init__(self, kind: _Optional[_Union[Endpoint.Kind, str]]=...) -> None:
        ...