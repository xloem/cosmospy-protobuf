from gogoproto import gogo_pb2 as _gogo_pb2
from akash.base.v1beta1 import attribute_pb2 as _attribute_pb2
from akash.base.v1beta1 import resourcevalue_pb2 as _resourcevalue_pb2
from akash.base.v1beta1 import endpoint_pb2 as _endpoint_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CPU(_message.Message):
    __slots__ = ['units', 'attributes']
    UNITS_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    units: _resourcevalue_pb2.ResourceValue
    attributes: _containers.RepeatedCompositeFieldContainer[_attribute_pb2.Attribute]

    def __init__(self, units: _Optional[_Union[_resourcevalue_pb2.ResourceValue, _Mapping]]=..., attributes: _Optional[_Iterable[_Union[_attribute_pb2.Attribute, _Mapping]]]=...) -> None:
        ...

class Memory(_message.Message):
    __slots__ = ['quantity', 'attributes']
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    quantity: _resourcevalue_pb2.ResourceValue
    attributes: _containers.RepeatedCompositeFieldContainer[_attribute_pb2.Attribute]

    def __init__(self, quantity: _Optional[_Union[_resourcevalue_pb2.ResourceValue, _Mapping]]=..., attributes: _Optional[_Iterable[_Union[_attribute_pb2.Attribute, _Mapping]]]=...) -> None:
        ...

class Storage(_message.Message):
    __slots__ = ['quantity', 'attributes']
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    quantity: _resourcevalue_pb2.ResourceValue
    attributes: _containers.RepeatedCompositeFieldContainer[_attribute_pb2.Attribute]

    def __init__(self, quantity: _Optional[_Union[_resourcevalue_pb2.ResourceValue, _Mapping]]=..., attributes: _Optional[_Iterable[_Union[_attribute_pb2.Attribute, _Mapping]]]=...) -> None:
        ...

class ResourceUnits(_message.Message):
    __slots__ = ['cpu', 'memory', 'storage', 'endpoints']
    CPU_FIELD_NUMBER: _ClassVar[int]
    MEMORY_FIELD_NUMBER: _ClassVar[int]
    STORAGE_FIELD_NUMBER: _ClassVar[int]
    ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
    cpu: CPU
    memory: Memory
    storage: Storage
    endpoints: _containers.RepeatedCompositeFieldContainer[_endpoint_pb2.Endpoint]

    def __init__(self, cpu: _Optional[_Union[CPU, _Mapping]]=..., memory: _Optional[_Union[Memory, _Mapping]]=..., storage: _Optional[_Union[Storage, _Mapping]]=..., endpoints: _Optional[_Iterable[_Union[_endpoint_pb2.Endpoint, _Mapping]]]=...) -> None:
        ...