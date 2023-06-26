from gogoproto import gogo_pb2 as _gogo_pb2
from cosmos.base.v1beta1 import coin_pb2 as _coin_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class MsgJoinPool(_message.Message):
    __slots__ = ['sender', 'poolId', 'shareOutAmount', 'tokenInMaxs']
    SENDER_FIELD_NUMBER: _ClassVar[int]
    POOLID_FIELD_NUMBER: _ClassVar[int]
    SHAREOUTAMOUNT_FIELD_NUMBER: _ClassVar[int]
    TOKENINMAXS_FIELD_NUMBER: _ClassVar[int]
    sender: str
    poolId: int
    shareOutAmount: str
    tokenInMaxs: _containers.RepeatedCompositeFieldContainer[_coin_pb2.Coin]

    def __init__(self, sender: _Optional[str]=..., poolId: _Optional[int]=..., shareOutAmount: _Optional[str]=..., tokenInMaxs: _Optional[_Iterable[_Union[_coin_pb2.Coin, _Mapping]]]=...) -> None:
        ...

class MsgJoinPoolResponse(_message.Message):
    __slots__ = []

    def __init__(self) -> None:
        ...

class MsgExitPool(_message.Message):
    __slots__ = ['sender', 'poolId', 'shareInAmount', 'tokenOutMins']
    SENDER_FIELD_NUMBER: _ClassVar[int]
    POOLID_FIELD_NUMBER: _ClassVar[int]
    SHAREINAMOUNT_FIELD_NUMBER: _ClassVar[int]
    TOKENOUTMINS_FIELD_NUMBER: _ClassVar[int]
    sender: str
    poolId: int
    shareInAmount: str
    tokenOutMins: _containers.RepeatedCompositeFieldContainer[_coin_pb2.Coin]

    def __init__(self, sender: _Optional[str]=..., poolId: _Optional[int]=..., shareInAmount: _Optional[str]=..., tokenOutMins: _Optional[_Iterable[_Union[_coin_pb2.Coin, _Mapping]]]=...) -> None:
        ...

class MsgExitPoolResponse(_message.Message):
    __slots__ = []

    def __init__(self) -> None:
        ...

class SwapAmountInRoute(_message.Message):
    __slots__ = ['poolId', 'tokenOutDenom']
    POOLID_FIELD_NUMBER: _ClassVar[int]
    TOKENOUTDENOM_FIELD_NUMBER: _ClassVar[int]
    poolId: int
    tokenOutDenom: str

    def __init__(self, poolId: _Optional[int]=..., tokenOutDenom: _Optional[str]=...) -> None:
        ...

class MsgSwapExactAmountIn(_message.Message):
    __slots__ = ['sender', 'routes', 'tokenIn', 'tokenOutMinAmount']
    SENDER_FIELD_NUMBER: _ClassVar[int]
    ROUTES_FIELD_NUMBER: _ClassVar[int]
    TOKENIN_FIELD_NUMBER: _ClassVar[int]
    TOKENOUTMINAMOUNT_FIELD_NUMBER: _ClassVar[int]
    sender: str
    routes: _containers.RepeatedCompositeFieldContainer[SwapAmountInRoute]
    tokenIn: _coin_pb2.Coin
    tokenOutMinAmount: str

    def __init__(self, sender: _Optional[str]=..., routes: _Optional[_Iterable[_Union[SwapAmountInRoute, _Mapping]]]=..., tokenIn: _Optional[_Union[_coin_pb2.Coin, _Mapping]]=..., tokenOutMinAmount: _Optional[str]=...) -> None:
        ...

class MsgSwapExactAmountInResponse(_message.Message):
    __slots__ = ['tokenOutAmount']
    TOKENOUTAMOUNT_FIELD_NUMBER: _ClassVar[int]
    tokenOutAmount: str

    def __init__(self, tokenOutAmount: _Optional[str]=...) -> None:
        ...

class SwapAmountOutRoute(_message.Message):
    __slots__ = ['poolId', 'tokenInDenom']
    POOLID_FIELD_NUMBER: _ClassVar[int]
    TOKENINDENOM_FIELD_NUMBER: _ClassVar[int]
    poolId: int
    tokenInDenom: str

    def __init__(self, poolId: _Optional[int]=..., tokenInDenom: _Optional[str]=...) -> None:
        ...

class MsgSwapExactAmountOut(_message.Message):
    __slots__ = ['sender', 'routes', 'tokenInMaxAmount', 'tokenOut']
    SENDER_FIELD_NUMBER: _ClassVar[int]
    ROUTES_FIELD_NUMBER: _ClassVar[int]
    TOKENINMAXAMOUNT_FIELD_NUMBER: _ClassVar[int]
    TOKENOUT_FIELD_NUMBER: _ClassVar[int]
    sender: str
    routes: _containers.RepeatedCompositeFieldContainer[SwapAmountOutRoute]
    tokenInMaxAmount: str
    tokenOut: _coin_pb2.Coin

    def __init__(self, sender: _Optional[str]=..., routes: _Optional[_Iterable[_Union[SwapAmountOutRoute, _Mapping]]]=..., tokenInMaxAmount: _Optional[str]=..., tokenOut: _Optional[_Union[_coin_pb2.Coin, _Mapping]]=...) -> None:
        ...

class MsgSwapExactAmountOutResponse(_message.Message):
    __slots__ = ['tokenInAmount']
    TOKENINAMOUNT_FIELD_NUMBER: _ClassVar[int]
    tokenInAmount: str

    def __init__(self, tokenInAmount: _Optional[str]=...) -> None:
        ...

class MsgJoinSwapExternAmountIn(_message.Message):
    __slots__ = ['sender', 'poolId', 'tokenIn', 'shareOutMinAmount']
    SENDER_FIELD_NUMBER: _ClassVar[int]
    POOLID_FIELD_NUMBER: _ClassVar[int]
    TOKENIN_FIELD_NUMBER: _ClassVar[int]
    SHAREOUTMINAMOUNT_FIELD_NUMBER: _ClassVar[int]
    sender: str
    poolId: int
    tokenIn: _coin_pb2.Coin
    shareOutMinAmount: str

    def __init__(self, sender: _Optional[str]=..., poolId: _Optional[int]=..., tokenIn: _Optional[_Union[_coin_pb2.Coin, _Mapping]]=..., shareOutMinAmount: _Optional[str]=...) -> None:
        ...

class MsgJoinSwapExternAmountInResponse(_message.Message):
    __slots__ = ['shareOutAmount']
    SHAREOUTAMOUNT_FIELD_NUMBER: _ClassVar[int]
    shareOutAmount: str

    def __init__(self, shareOutAmount: _Optional[str]=...) -> None:
        ...

class MsgJoinSwapShareAmountOut(_message.Message):
    __slots__ = ['sender', 'poolId', 'tokenInDenom', 'shareOutAmount', 'tokenInMaxAmount']
    SENDER_FIELD_NUMBER: _ClassVar[int]
    POOLID_FIELD_NUMBER: _ClassVar[int]
    TOKENINDENOM_FIELD_NUMBER: _ClassVar[int]
    SHAREOUTAMOUNT_FIELD_NUMBER: _ClassVar[int]
    TOKENINMAXAMOUNT_FIELD_NUMBER: _ClassVar[int]
    sender: str
    poolId: int
    tokenInDenom: str
    shareOutAmount: str
    tokenInMaxAmount: str

    def __init__(self, sender: _Optional[str]=..., poolId: _Optional[int]=..., tokenInDenom: _Optional[str]=..., shareOutAmount: _Optional[str]=..., tokenInMaxAmount: _Optional[str]=...) -> None:
        ...

class MsgJoinSwapShareAmountOutResponse(_message.Message):
    __slots__ = ['tokenInAmount']
    TOKENINAMOUNT_FIELD_NUMBER: _ClassVar[int]
    tokenInAmount: str

    def __init__(self, tokenInAmount: _Optional[str]=...) -> None:
        ...

class MsgExitSwapShareAmountIn(_message.Message):
    __slots__ = ['sender', 'poolId', 'tokenOutDenom', 'shareInAmount', 'tokenOutMinAmount']
    SENDER_FIELD_NUMBER: _ClassVar[int]
    POOLID_FIELD_NUMBER: _ClassVar[int]
    TOKENOUTDENOM_FIELD_NUMBER: _ClassVar[int]
    SHAREINAMOUNT_FIELD_NUMBER: _ClassVar[int]
    TOKENOUTMINAMOUNT_FIELD_NUMBER: _ClassVar[int]
    sender: str
    poolId: int
    tokenOutDenom: str
    shareInAmount: str
    tokenOutMinAmount: str

    def __init__(self, sender: _Optional[str]=..., poolId: _Optional[int]=..., tokenOutDenom: _Optional[str]=..., shareInAmount: _Optional[str]=..., tokenOutMinAmount: _Optional[str]=...) -> None:
        ...

class MsgExitSwapShareAmountInResponse(_message.Message):
    __slots__ = ['tokenOutAmount']
    TOKENOUTAMOUNT_FIELD_NUMBER: _ClassVar[int]
    tokenOutAmount: str

    def __init__(self, tokenOutAmount: _Optional[str]=...) -> None:
        ...

class MsgExitSwapExternAmountOut(_message.Message):
    __slots__ = ['sender', 'poolId', 'tokenOut', 'shareInMaxAmount']
    SENDER_FIELD_NUMBER: _ClassVar[int]
    POOLID_FIELD_NUMBER: _ClassVar[int]
    TOKENOUT_FIELD_NUMBER: _ClassVar[int]
    SHAREINMAXAMOUNT_FIELD_NUMBER: _ClassVar[int]
    sender: str
    poolId: int
    tokenOut: _coin_pb2.Coin
    shareInMaxAmount: str

    def __init__(self, sender: _Optional[str]=..., poolId: _Optional[int]=..., tokenOut: _Optional[_Union[_coin_pb2.Coin, _Mapping]]=..., shareInMaxAmount: _Optional[str]=...) -> None:
        ...

class MsgExitSwapExternAmountOutResponse(_message.Message):
    __slots__ = ['shareInAmount']
    SHAREINAMOUNT_FIELD_NUMBER: _ClassVar[int]
    shareInAmount: str

    def __init__(self, shareInAmount: _Optional[str]=...) -> None:
        ...