from gogoproto import gogo_pb2 as _gogo_pb2
from google.api import annotations_pb2 as _annotations_pb2
from cosmos.base.query.v1beta1 import pagination_pb2 as _pagination_pb2
from akash.provider.v1beta3 import provider_pb2 as _provider_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class QueryProvidersRequest(_message.Message):
    __slots__ = ['pagination']
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    pagination: _pagination_pb2.PageRequest

    def __init__(self, pagination: _Optional[_Union[_pagination_pb2.PageRequest, _Mapping]]=...) -> None:
        ...

class QueryProvidersResponse(_message.Message):
    __slots__ = ['providers', 'pagination']
    PROVIDERS_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    providers: _containers.RepeatedCompositeFieldContainer[_provider_pb2.Provider]
    pagination: _pagination_pb2.PageResponse

    def __init__(self, providers: _Optional[_Iterable[_Union[_provider_pb2.Provider, _Mapping]]]=..., pagination: _Optional[_Union[_pagination_pb2.PageResponse, _Mapping]]=...) -> None:
        ...

class QueryProviderRequest(_message.Message):
    __slots__ = ['owner']
    OWNER_FIELD_NUMBER: _ClassVar[int]
    owner: str

    def __init__(self, owner: _Optional[str]=...) -> None:
        ...

class QueryProviderResponse(_message.Message):
    __slots__ = ['provider']
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    provider: _provider_pb2.Provider

    def __init__(self, provider: _Optional[_Union[_provider_pb2.Provider, _Mapping]]=...) -> None:
        ...