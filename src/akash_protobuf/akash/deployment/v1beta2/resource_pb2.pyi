from gogoproto import gogo_pb2 as _gogo_pb2
from cosmos.base.v1beta1 import coin_pb2 as _coin_pb2
from akash.base.v1beta2 import resourceunits_pb2 as _resourceunits_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Resource(_message.Message):
    __slots__ = ['resources', 'count', 'price']
    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    resources: _resourceunits_pb2.ResourceUnits
    count: int
    price: _coin_pb2.DecCoin

    def __init__(self, resources: _Optional[_Union[_resourceunits_pb2.ResourceUnits, _Mapping]]=..., count: _Optional[int]=..., price: _Optional[_Union[_coin_pb2.DecCoin, _Mapping]]=...) -> None:
        ...