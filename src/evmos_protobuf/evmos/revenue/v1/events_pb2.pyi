from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class EventRegisterRevenue(_message.Message):
    __slots__ = ['deployer_address', 'contract_address', 'effective_withdrawer']
    DEPLOYER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_WITHDRAWER_FIELD_NUMBER: _ClassVar[int]
    deployer_address: str
    contract_address: str
    effective_withdrawer: str

    def __init__(self, deployer_address: _Optional[str]=..., contract_address: _Optional[str]=..., effective_withdrawer: _Optional[str]=...) -> None:
        ...

class EventUpdateRevenue(_message.Message):
    __slots__ = ['contract_address', 'deployer_address', 'withdrawer_address']
    CONTRACT_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    DEPLOYER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    WITHDRAWER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    contract_address: str
    deployer_address: str
    withdrawer_address: str

    def __init__(self, contract_address: _Optional[str]=..., deployer_address: _Optional[str]=..., withdrawer_address: _Optional[str]=...) -> None:
        ...

class EventCancelRevenue(_message.Message):
    __slots__ = ['deployer_address', 'contract_address']
    DEPLOYER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    deployer_address: str
    contract_address: str

    def __init__(self, deployer_address: _Optional[str]=..., contract_address: _Optional[str]=...) -> None:
        ...

class EventDistributeRevenue(_message.Message):
    __slots__ = ['sender', 'contract', 'withdrawer_address', 'amount']
    SENDER_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_FIELD_NUMBER: _ClassVar[int]
    WITHDRAWER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    sender: str
    contract: str
    withdrawer_address: str
    amount: str

    def __init__(self, sender: _Optional[str]=..., contract: _Optional[str]=..., withdrawer_address: _Optional[str]=..., amount: _Optional[str]=...) -> None:
        ...