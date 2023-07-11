from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class EventRegisterPair(_message.Message):
    __slots__ = ['denom', 'erc20_address']
    DENOM_FIELD_NUMBER: _ClassVar[int]
    ERC20_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    denom: str
    erc20_address: str

    def __init__(self, denom: _Optional[str]=..., erc20_address: _Optional[str]=...) -> None:
        ...

class EventToggleTokenConversion(_message.Message):
    __slots__ = ['denom', 'erc20_address']
    DENOM_FIELD_NUMBER: _ClassVar[int]
    ERC20_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    denom: str
    erc20_address: str

    def __init__(self, denom: _Optional[str]=..., erc20_address: _Optional[str]=...) -> None:
        ...

class EventConvertCoin(_message.Message):
    __slots__ = ['sender', 'receiver', 'amount', 'denom', 'erc20_address']
    SENDER_FIELD_NUMBER: _ClassVar[int]
    RECEIVER_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    DENOM_FIELD_NUMBER: _ClassVar[int]
    ERC20_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    sender: str
    receiver: str
    amount: str
    denom: str
    erc20_address: str

    def __init__(self, sender: _Optional[str]=..., receiver: _Optional[str]=..., amount: _Optional[str]=..., denom: _Optional[str]=..., erc20_address: _Optional[str]=...) -> None:
        ...

class EventConvertERC20(_message.Message):
    __slots__ = ['sender', 'receiver', 'amount', 'denom', 'contract_address']
    SENDER_FIELD_NUMBER: _ClassVar[int]
    RECEIVER_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    DENOM_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    sender: str
    receiver: str
    amount: str
    denom: str
    contract_address: str

    def __init__(self, sender: _Optional[str]=..., receiver: _Optional[str]=..., amount: _Optional[str]=..., denom: _Optional[str]=..., contract_address: _Optional[str]=...) -> None:
        ...