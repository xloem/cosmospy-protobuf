from gogoproto import gogo_pb2 as _gogo_pb2
from akash.gov.v1beta3 import params_pb2 as _params_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GenesisState(_message.Message):
    __slots__ = ['deposit_params']
    DEPOSIT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    deposit_params: _params_pb2.DepositParams

    def __init__(self, deposit_params: _Optional[_Union[_params_pb2.DepositParams, _Mapping]]=...) -> None:
        ...