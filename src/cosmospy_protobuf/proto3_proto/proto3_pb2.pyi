from google.protobuf import any_pb2 as _any_pb2
from test_proto import test_pb2 as _test_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Message(_message.Message):
    __slots__ = ['name', 'hilarity', 'height_in_cm', 'data', 'result_count', 'true_scotsman', 'score', 'key', 'short_key', 'nested', 'r_funny', 'terrain', 'proto2_field', 'proto2_value', 'anything', 'many_things', 'submessage', 'children', 'string_map']

    class Humour(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        UNKNOWN: _ClassVar[Message.Humour]
        PUNS: _ClassVar[Message.Humour]
        SLAPSTICK: _ClassVar[Message.Humour]
        BILL_BAILEY: _ClassVar[Message.Humour]
    UNKNOWN: Message.Humour
    PUNS: Message.Humour
    SLAPSTICK: Message.Humour
    BILL_BAILEY: Message.Humour

    class TerrainEntry(_message.Message):
        __slots__ = ['key', 'value']
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Nested

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[Nested, _Mapping]]=...) -> None:
            ...

    class Proto2ValueEntry(_message.Message):
        __slots__ = ['key', 'value']
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _test_pb2.SubDefaults

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[_test_pb2.SubDefaults, _Mapping]]=...) -> None:
            ...

    class StringMapEntry(_message.Message):
        __slots__ = ['key', 'value']
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    HILARITY_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_IN_CM_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    RESULT_COUNT_FIELD_NUMBER: _ClassVar[int]
    TRUE_SCOTSMAN_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    SHORT_KEY_FIELD_NUMBER: _ClassVar[int]
    NESTED_FIELD_NUMBER: _ClassVar[int]
    R_FUNNY_FIELD_NUMBER: _ClassVar[int]
    TERRAIN_FIELD_NUMBER: _ClassVar[int]
    PROTO2_FIELD_FIELD_NUMBER: _ClassVar[int]
    PROTO2_VALUE_FIELD_NUMBER: _ClassVar[int]
    ANYTHING_FIELD_NUMBER: _ClassVar[int]
    MANY_THINGS_FIELD_NUMBER: _ClassVar[int]
    SUBMESSAGE_FIELD_NUMBER: _ClassVar[int]
    CHILDREN_FIELD_NUMBER: _ClassVar[int]
    STRING_MAP_FIELD_NUMBER: _ClassVar[int]
    name: str
    hilarity: Message.Humour
    height_in_cm: int
    data: bytes
    result_count: int
    true_scotsman: bool
    score: float
    key: _containers.RepeatedScalarFieldContainer[int]
    short_key: _containers.RepeatedScalarFieldContainer[int]
    nested: Nested
    r_funny: _containers.RepeatedScalarFieldContainer[Message.Humour]
    terrain: _containers.MessageMap[str, Nested]
    proto2_field: _test_pb2.SubDefaults
    proto2_value: _containers.MessageMap[str, _test_pb2.SubDefaults]
    anything: _any_pb2.Any
    many_things: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]
    submessage: Message
    children: _containers.RepeatedCompositeFieldContainer[Message]
    string_map: _containers.ScalarMap[str, str]

    def __init__(self, name: _Optional[str]=..., hilarity: _Optional[_Union[Message.Humour, str]]=..., height_in_cm: _Optional[int]=..., data: _Optional[bytes]=..., result_count: _Optional[int]=..., true_scotsman: bool=..., score: _Optional[float]=..., key: _Optional[_Iterable[int]]=..., short_key: _Optional[_Iterable[int]]=..., nested: _Optional[_Union[Nested, _Mapping]]=..., r_funny: _Optional[_Iterable[_Union[Message.Humour, str]]]=..., terrain: _Optional[_Mapping[str, Nested]]=..., proto2_field: _Optional[_Union[_test_pb2.SubDefaults, _Mapping]]=..., proto2_value: _Optional[_Mapping[str, _test_pb2.SubDefaults]]=..., anything: _Optional[_Union[_any_pb2.Any, _Mapping]]=..., many_things: _Optional[_Iterable[_Union[_any_pb2.Any, _Mapping]]]=..., submessage: _Optional[_Union[Message, _Mapping]]=..., children: _Optional[_Iterable[_Union[Message, _Mapping]]]=..., string_map: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class Nested(_message.Message):
    __slots__ = ['bunny', 'cute']
    BUNNY_FIELD_NUMBER: _ClassVar[int]
    CUTE_FIELD_NUMBER: _ClassVar[int]
    bunny: str
    cute: bool

    def __init__(self, bunny: _Optional[str]=..., cute: bool=...) -> None:
        ...

class MessageWithMap(_message.Message):
    __slots__ = ['byte_mapping']

    class ByteMappingEntry(_message.Message):
        __slots__ = ['key', 'value']
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: bool
        value: bytes

        def __init__(self, key: bool=..., value: _Optional[bytes]=...) -> None:
            ...
    BYTE_MAPPING_FIELD_NUMBER: _ClassVar[int]
    byte_mapping: _containers.ScalarMap[bool, bytes]

    def __init__(self, byte_mapping: _Optional[_Mapping[bool, bytes]]=...) -> None:
        ...

class IntMap(_message.Message):
    __slots__ = ['rtt']

    class RttEntry(_message.Message):
        __slots__ = ['key', 'value']
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int

        def __init__(self, key: _Optional[int]=..., value: _Optional[int]=...) -> None:
            ...
    RTT_FIELD_NUMBER: _ClassVar[int]
    rtt: _containers.ScalarMap[int, int]

    def __init__(self, rtt: _Optional[_Mapping[int, int]]=...) -> None:
        ...

class IntMaps(_message.Message):
    __slots__ = ['maps']
    MAPS_FIELD_NUMBER: _ClassVar[int]
    maps: _containers.RepeatedCompositeFieldContainer[IntMap]

    def __init__(self, maps: _Optional[_Iterable[_Union[IntMap, _Mapping]]]=...) -> None:
        ...

class TestUTF8(_message.Message):
    __slots__ = ['scalar', 'vector', 'field', 'map_key', 'map_value']

    class MapKeyEntry(_message.Message):
        __slots__ = ['key', 'value']
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int

        def __init__(self, key: _Optional[str]=..., value: _Optional[int]=...) -> None:
            ...

    class MapValueEntry(_message.Message):
        __slots__ = ['key', 'value']
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: str

        def __init__(self, key: _Optional[int]=..., value: _Optional[str]=...) -> None:
            ...
    SCALAR_FIELD_NUMBER: _ClassVar[int]
    VECTOR_FIELD_NUMBER: _ClassVar[int]
    FIELD_FIELD_NUMBER: _ClassVar[int]
    MAP_KEY_FIELD_NUMBER: _ClassVar[int]
    MAP_VALUE_FIELD_NUMBER: _ClassVar[int]
    scalar: str
    vector: _containers.RepeatedScalarFieldContainer[str]
    field: str
    map_key: _containers.ScalarMap[str, int]
    map_value: _containers.ScalarMap[int, str]

    def __init__(self, scalar: _Optional[str]=..., vector: _Optional[_Iterable[str]]=..., field: _Optional[str]=..., map_key: _Optional[_Mapping[str, int]]=..., map_value: _Optional[_Mapping[int, str]]=...) -> None:
        ...