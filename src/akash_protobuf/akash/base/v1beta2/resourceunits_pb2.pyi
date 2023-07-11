from gogoproto import gogo_pb2 as _gogo_pb2
from akash.base.v1beta2 import resource_pb2 as _resource_pb2
from akash.base.v1beta2 import endpoint_pb2 as _endpoint_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ResourceUnits(_message.Message):
    __slots__ = ['cpu', 'memory', 'storage', 'endpoints']
    CPU_FIELD_NUMBER: _ClassVar[int]
    MEMORY_FIELD_NUMBER: _ClassVar[int]
    STORAGE_FIELD_NUMBER: _ClassVar[int]
    ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
    cpu: _resource_pb2.CPU
    memory: _resource_pb2.Memory
    storage: _containers.RepeatedCompositeFieldContainer[_resource_pb2.Storage]
    endpoints: _containers.RepeatedCompositeFieldContainer[_endpoint_pb2.Endpoint]

    def __init__(self, cpu: _Optional[_Union[_resource_pb2.CPU, _Mapping]]=..., memory: _Optional[_Union[_resource_pb2.Memory, _Mapping]]=..., storage: _Optional[_Iterable[_Union[_resource_pb2.Storage, _Mapping]]]=..., endpoints: _Optional[_Iterable[_Union[_endpoint_pb2.Endpoint, _Mapping]]]=...) -> None:
        ...