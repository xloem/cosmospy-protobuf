from gogoproto import gogo_pb2 as _gogo_pb2
from cosmos.base.v1beta1 import coin_pb2 as _coin_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Params(_message.Message):
    __slots__ = ['deployment_min_deposit']
    DEPLOYMENT_MIN_DEPOSIT_FIELD_NUMBER: _ClassVar[int]
    deployment_min_deposit: _coin_pb2.Coin

    def __init__(self, deployment_min_deposit: _Optional[_Union[_coin_pb2.Coin, _Mapping]]=...) -> None:
        ...