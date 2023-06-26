from gogoproto import gogo_pb2 as _gogo_pb2
from osmosis.gamm.v1beta1 import tx_pb2 as _tx_pb2
from cosmos.base.v1beta1 import coin_pb2 as _coin_pb2
from cosmos.base.query.v1beta1 import pagination_pb2 as _pagination_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import any_pb2 as _any_pb2
from cosmos_proto import cosmos_pb2 as _cosmos_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class QueryPoolRequest(_message.Message):
    __slots__ = ['poolId']
    POOLID_FIELD_NUMBER: _ClassVar[int]
    poolId: int

    def __init__(self, poolId: _Optional[int]=...) -> None:
        ...

class QueryPoolResponse(_message.Message):
    __slots__ = ['pool']
    POOL_FIELD_NUMBER: _ClassVar[int]
    pool: _any_pb2.Any

    def __init__(self, pool: _Optional[_Union[_any_pb2.Any, _Mapping]]=...) -> None:
        ...

class QueryPoolsRequest(_message.Message):
    __slots__ = ['pagination']
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    pagination: _pagination_pb2.PageRequest

    def __init__(self, pagination: _Optional[_Union[_pagination_pb2.PageRequest, _Mapping]]=...) -> None:
        ...

class QueryPoolsResponse(_message.Message):
    __slots__ = ['pools', 'pagination']
    POOLS_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    pools: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]
    pagination: _pagination_pb2.PageResponse

    def __init__(self, pools: _Optional[_Iterable[_Union[_any_pb2.Any, _Mapping]]]=..., pagination: _Optional[_Union[_pagination_pb2.PageResponse, _Mapping]]=...) -> None:
        ...

class QueryNumPoolsRequest(_message.Message):
    __slots__ = []

    def __init__(self) -> None:
        ...

class QueryNumPoolsResponse(_message.Message):
    __slots__ = ['numPools']
    NUMPOOLS_FIELD_NUMBER: _ClassVar[int]
    numPools: int

    def __init__(self, numPools: _Optional[int]=...) -> None:
        ...

class QueryPoolParamsRequest(_message.Message):
    __slots__ = ['poolId']
    POOLID_FIELD_NUMBER: _ClassVar[int]
    poolId: int

    def __init__(self, poolId: _Optional[int]=...) -> None:
        ...

class QueryPoolParamsResponse(_message.Message):
    __slots__ = ['params']
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    params: _any_pb2.Any

    def __init__(self, params: _Optional[_Union[_any_pb2.Any, _Mapping]]=...) -> None:
        ...

class QueryTotalPoolLiquidityRequest(_message.Message):
    __slots__ = ['poolId']
    POOLID_FIELD_NUMBER: _ClassVar[int]
    poolId: int

    def __init__(self, poolId: _Optional[int]=...) -> None:
        ...

class QueryTotalPoolLiquidityResponse(_message.Message):
    __slots__ = ['liquidity']
    LIQUIDITY_FIELD_NUMBER: _ClassVar[int]
    liquidity: _containers.RepeatedCompositeFieldContainer[_coin_pb2.Coin]

    def __init__(self, liquidity: _Optional[_Iterable[_Union[_coin_pb2.Coin, _Mapping]]]=...) -> None:
        ...

class QueryTotalSharesRequest(_message.Message):
    __slots__ = ['poolId']
    POOLID_FIELD_NUMBER: _ClassVar[int]
    poolId: int

    def __init__(self, poolId: _Optional[int]=...) -> None:
        ...

class QueryTotalSharesResponse(_message.Message):
    __slots__ = ['totalShares']
    TOTALSHARES_FIELD_NUMBER: _ClassVar[int]
    totalShares: _coin_pb2.Coin

    def __init__(self, totalShares: _Optional[_Union[_coin_pb2.Coin, _Mapping]]=...) -> None:
        ...

class QuerySpotPriceRequest(_message.Message):
    __slots__ = ['poolId', 'base_asset_denom', 'quote_asset_denom']
    POOLID_FIELD_NUMBER: _ClassVar[int]
    BASE_ASSET_DENOM_FIELD_NUMBER: _ClassVar[int]
    QUOTE_ASSET_DENOM_FIELD_NUMBER: _ClassVar[int]
    poolId: int
    base_asset_denom: str
    quote_asset_denom: str

    def __init__(self, poolId: _Optional[int]=..., base_asset_denom: _Optional[str]=..., quote_asset_denom: _Optional[str]=...) -> None:
        ...

class QuerySpotPriceResponse(_message.Message):
    __slots__ = ['spotPrice']
    SPOTPRICE_FIELD_NUMBER: _ClassVar[int]
    spotPrice: str

    def __init__(self, spotPrice: _Optional[str]=...) -> None:
        ...

class QuerySwapExactAmountInRequest(_message.Message):
    __slots__ = ['sender', 'poolId', 'tokenIn', 'routes']
    SENDER_FIELD_NUMBER: _ClassVar[int]
    POOLID_FIELD_NUMBER: _ClassVar[int]
    TOKENIN_FIELD_NUMBER: _ClassVar[int]
    ROUTES_FIELD_NUMBER: _ClassVar[int]
    sender: str
    poolId: int
    tokenIn: str
    routes: _containers.RepeatedCompositeFieldContainer[_tx_pb2.SwapAmountInRoute]

    def __init__(self, sender: _Optional[str]=..., poolId: _Optional[int]=..., tokenIn: _Optional[str]=..., routes: _Optional[_Iterable[_Union[_tx_pb2.SwapAmountInRoute, _Mapping]]]=...) -> None:
        ...

class QuerySwapExactAmountInResponse(_message.Message):
    __slots__ = ['tokenOutAmount']
    TOKENOUTAMOUNT_FIELD_NUMBER: _ClassVar[int]
    tokenOutAmount: str

    def __init__(self, tokenOutAmount: _Optional[str]=...) -> None:
        ...

class QuerySwapExactAmountOutRequest(_message.Message):
    __slots__ = ['sender', 'poolId', 'routes', 'tokenOut']
    SENDER_FIELD_NUMBER: _ClassVar[int]
    POOLID_FIELD_NUMBER: _ClassVar[int]
    ROUTES_FIELD_NUMBER: _ClassVar[int]
    TOKENOUT_FIELD_NUMBER: _ClassVar[int]
    sender: str
    poolId: int
    routes: _containers.RepeatedCompositeFieldContainer[_tx_pb2.SwapAmountOutRoute]
    tokenOut: str

    def __init__(self, sender: _Optional[str]=..., poolId: _Optional[int]=..., routes: _Optional[_Iterable[_Union[_tx_pb2.SwapAmountOutRoute, _Mapping]]]=..., tokenOut: _Optional[str]=...) -> None:
        ...

class QuerySwapExactAmountOutResponse(_message.Message):
    __slots__ = ['tokenInAmount']
    TOKENINAMOUNT_FIELD_NUMBER: _ClassVar[int]
    tokenInAmount: str

    def __init__(self, tokenInAmount: _Optional[str]=...) -> None:
        ...

class QueryTotalLiquidityRequest(_message.Message):
    __slots__ = []

    def __init__(self) -> None:
        ...

class QueryTotalLiquidityResponse(_message.Message):
    __slots__ = ['liquidity']
    LIQUIDITY_FIELD_NUMBER: _ClassVar[int]
    liquidity: _containers.RepeatedCompositeFieldContainer[_coin_pb2.Coin]

    def __init__(self, liquidity: _Optional[_Iterable[_Union[_coin_pb2.Coin, _Mapping]]]=...) -> None:
        ...