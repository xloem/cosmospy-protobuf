from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from cosmos.base.v1beta1 import coin_pb2 as _coin_pb2
from osmosis.superfluid import superfluid_pb2 as _superfluid_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class MsgSuperfluidDelegate(_message.Message):
    __slots__ = ['sender', 'lock_id', 'val_addr']
    SENDER_FIELD_NUMBER: _ClassVar[int]
    LOCK_ID_FIELD_NUMBER: _ClassVar[int]
    VAL_ADDR_FIELD_NUMBER: _ClassVar[int]
    sender: str
    lock_id: int
    val_addr: str

    def __init__(self, sender: _Optional[str]=..., lock_id: _Optional[int]=..., val_addr: _Optional[str]=...) -> None:
        ...

class MsgSuperfluidDelegateResponse(_message.Message):
    __slots__ = []

    def __init__(self) -> None:
        ...

class MsgSuperfluidUndelegate(_message.Message):
    __slots__ = ['sender', 'lock_id']
    SENDER_FIELD_NUMBER: _ClassVar[int]
    LOCK_ID_FIELD_NUMBER: _ClassVar[int]
    sender: str
    lock_id: int

    def __init__(self, sender: _Optional[str]=..., lock_id: _Optional[int]=...) -> None:
        ...

class MsgSuperfluidUndelegateResponse(_message.Message):
    __slots__ = []

    def __init__(self) -> None:
        ...

class MsgSuperfluidUnbondLock(_message.Message):
    __slots__ = ['sender', 'lock_id']
    SENDER_FIELD_NUMBER: _ClassVar[int]
    LOCK_ID_FIELD_NUMBER: _ClassVar[int]
    sender: str
    lock_id: int

    def __init__(self, sender: _Optional[str]=..., lock_id: _Optional[int]=...) -> None:
        ...

class MsgSuperfluidUnbondLockResponse(_message.Message):
    __slots__ = []

    def __init__(self) -> None:
        ...

class MsgLockAndSuperfluidDelegate(_message.Message):
    __slots__ = ['sender', 'coins', 'val_addr']
    SENDER_FIELD_NUMBER: _ClassVar[int]
    COINS_FIELD_NUMBER: _ClassVar[int]
    VAL_ADDR_FIELD_NUMBER: _ClassVar[int]
    sender: str
    coins: _containers.RepeatedCompositeFieldContainer[_coin_pb2.Coin]
    val_addr: str

    def __init__(self, sender: _Optional[str]=..., coins: _Optional[_Iterable[_Union[_coin_pb2.Coin, _Mapping]]]=..., val_addr: _Optional[str]=...) -> None:
        ...

class MsgLockAndSuperfluidDelegateResponse(_message.Message):
    __slots__ = ['ID']
    ID_FIELD_NUMBER: _ClassVar[int]
    ID: int

    def __init__(self, ID: _Optional[int]=...) -> None:
        ...

class MsgUnPoolWhitelistedPool(_message.Message):
    __slots__ = ['sender', 'pool_id']
    SENDER_FIELD_NUMBER: _ClassVar[int]
    POOL_ID_FIELD_NUMBER: _ClassVar[int]
    sender: str
    pool_id: int

    def __init__(self, sender: _Optional[str]=..., pool_id: _Optional[int]=...) -> None:
        ...

class MsgUnPoolWhitelistedPoolResponse(_message.Message):
    __slots__ = ['exitedLockIds']
    EXITEDLOCKIDS_FIELD_NUMBER: _ClassVar[int]
    exitedLockIds: _containers.RepeatedScalarFieldContainer[int]

    def __init__(self, exitedLockIds: _Optional[_Iterable[int]]=...) -> None:
        ...