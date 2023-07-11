from cosmos.bank.v1beta1 import bank_pb2 as _bank_pb2
from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Owner(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    OWNER_UNSPECIFIED: _ClassVar[Owner]
    OWNER_MODULE: _ClassVar[Owner]
    OWNER_EXTERNAL: _ClassVar[Owner]
OWNER_UNSPECIFIED: Owner
OWNER_MODULE: Owner
OWNER_EXTERNAL: Owner

class TokenPair(_message.Message):
    __slots__ = ['erc20_address', 'denom', 'enabled', 'contract_owner']
    ERC20_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    DENOM_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_OWNER_FIELD_NUMBER: _ClassVar[int]
    erc20_address: str
    denom: str
    enabled: bool
    contract_owner: Owner

    def __init__(self, erc20_address: _Optional[str]=..., denom: _Optional[str]=..., enabled: bool=..., contract_owner: _Optional[_Union[Owner, str]]=...) -> None:
        ...

class RegisterCoinProposal(_message.Message):
    __slots__ = ['title', 'description', 'metadata']
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    title: str
    description: str
    metadata: _containers.RepeatedCompositeFieldContainer[_bank_pb2.Metadata]

    def __init__(self, title: _Optional[str]=..., description: _Optional[str]=..., metadata: _Optional[_Iterable[_Union[_bank_pb2.Metadata, _Mapping]]]=...) -> None:
        ...

class RegisterERC20Proposal(_message.Message):
    __slots__ = ['title', 'description', 'erc20addresses']
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ERC20ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    title: str
    description: str
    erc20addresses: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, title: _Optional[str]=..., description: _Optional[str]=..., erc20addresses: _Optional[_Iterable[str]]=...) -> None:
        ...

class ToggleTokenConversionProposal(_message.Message):
    __slots__ = ['title', 'description', 'token']
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    title: str
    description: str
    token: str

    def __init__(self, title: _Optional[str]=..., description: _Optional[str]=..., token: _Optional[str]=...) -> None:
        ...

class ProposalMetadata(_message.Message):
    __slots__ = ['metadata']
    METADATA_FIELD_NUMBER: _ClassVar[int]
    metadata: _containers.RepeatedCompositeFieldContainer[_bank_pb2.Metadata]

    def __init__(self, metadata: _Optional[_Iterable[_Union[_bank_pb2.Metadata, _Mapping]]]=...) -> None:
        ...