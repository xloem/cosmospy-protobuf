from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class EventCreateClawbackVestingAccount(_message.Message):
    __slots__ = ['sender', 'coins', 'start_time', 'merge', 'account']
    SENDER_FIELD_NUMBER: _ClassVar[int]
    COINS_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    MERGE_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    sender: str
    coins: str
    start_time: str
    merge: str
    account: str

    def __init__(self, sender: _Optional[str]=..., coins: _Optional[str]=..., start_time: _Optional[str]=..., merge: _Optional[str]=..., account: _Optional[str]=...) -> None:
        ...

class EventClawback(_message.Message):
    __slots__ = ['funder', 'account', 'destination']
    FUNDER_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    funder: str
    account: str
    destination: str

    def __init__(self, funder: _Optional[str]=..., account: _Optional[str]=..., destination: _Optional[str]=...) -> None:
        ...

class EventUpdateVestingFunder(_message.Message):
    __slots__ = ['funder', 'account', 'new_funder']
    FUNDER_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    NEW_FUNDER_FIELD_NUMBER: _ClassVar[int]
    funder: str
    account: str
    new_funder: str

    def __init__(self, funder: _Optional[str]=..., account: _Optional[str]=..., new_funder: _Optional[str]=...) -> None:
        ...