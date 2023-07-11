"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from ..test_proto import test_pb2 as test__proto_dot_test__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19proto3_proto/proto3.proto\x12\x0cproto3_proto\x1a\x19google/protobuf/any.proto\x1a\x15test_proto/test.proto"\xa5\x07\n\x07Message\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\x08hilarity\x18\x02 \x01(\x0e2\x1c.proto3_proto.Message.Humour\x12\x14\n\x0cheight_in_cm\x18\x03 \x01(\r\x12\x0c\n\x04data\x18\x04 \x01(\x0c\x12\x14\n\x0cresult_count\x18\x07 \x01(\x03\x12\x15\n\rtrue_scotsman\x18\x08 \x01(\x08\x12\r\n\x05score\x18\t \x01(\x02\x12\x0b\n\x03key\x18\x05 \x03(\x04\x12\x11\n\tshort_key\x18\x13 \x03(\x05\x12$\n\x06nested\x18\x06 \x01(\x0b2\x14.proto3_proto.Nested\x12-\n\x07r_funny\x18\x10 \x03(\x0e2\x1c.proto3_proto.Message.Humour\x123\n\x07terrain\x18\n \x03(\x0b2".proto3_proto.Message.TerrainEntry\x12-\n\x0cproto2_field\x18\x0b \x01(\x0b2\x17.test_proto.SubDefaults\x12<\n\x0cproto2_value\x18\r \x03(\x0b2&.proto3_proto.Message.Proto2ValueEntry\x12&\n\x08anything\x18\x0e \x01(\x0b2\x14.google.protobuf.Any\x12)\n\x0bmany_things\x18\x0f \x03(\x0b2\x14.google.protobuf.Any\x12)\n\nsubmessage\x18\x11 \x01(\x0b2\x15.proto3_proto.Message\x12\'\n\x08children\x18\x12 \x03(\x0b2\x15.proto3_proto.Message\x128\n\nstring_map\x18\x14 \x03(\x0b2$.proto3_proto.Message.StringMapEntry\x1aD\n\x0cTerrainEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b2\x14.proto3_proto.Nested:\x028\x01\x1aK\n\x10Proto2ValueEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12&\n\x05value\x18\x02 \x01(\x0b2\x17.test_proto.SubDefaults:\x028\x01\x1a0\n\x0eStringMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"?\n\x06Humour\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x08\n\x04PUNS\x10\x01\x12\r\n\tSLAPSTICK\x10\x02\x12\x0f\n\x0bBILL_BAILEY\x10\x03"%\n\x06Nested\x12\r\n\x05bunny\x18\x01 \x01(\t\x12\x0c\n\x04cute\x18\x02 \x01(\x08"\x89\x01\n\x0eMessageWithMap\x12C\n\x0cbyte_mapping\x18\x01 \x03(\x0b2-.proto3_proto.MessageWithMap.ByteMappingEntry\x1a2\n\x10ByteMappingEntry\x12\x0b\n\x03key\x18\x01 \x01(\x08\x12\r\n\x05value\x18\x02 \x01(\x0c:\x028\x01"`\n\x06IntMap\x12*\n\x03rtt\x18\x01 \x03(\x0b2\x1d.proto3_proto.IntMap.RttEntry\x1a*\n\x08RttEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x05:\x028\x01"-\n\x07IntMaps\x12"\n\x04maps\x18\x01 \x03(\x0b2\x14.proto3_proto.IntMap"\x92\x02\n\x08TestUTF8\x12\x0e\n\x06scalar\x18\x01 \x01(\t\x12\x0e\n\x06vector\x18\x02 \x03(\t\x12\x0f\n\x05field\x18\x03 \x01(\tH\x00\x123\n\x07map_key\x18\x04 \x03(\x0b2".proto3_proto.TestUTF8.MapKeyEntry\x127\n\tmap_value\x18\x05 \x03(\x0b2$.proto3_proto.TestUTF8.MapValueEntry\x1a-\n\x0bMapKeyEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x03:\x028\x01\x1a/\n\rMapValueEntry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01B\x07\n\x05oneofb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto3_proto.proto3_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _MESSAGE_TERRAINENTRY._options = None
    _MESSAGE_TERRAINENTRY._serialized_options = b'8\x01'
    _MESSAGE_PROTO2VALUEENTRY._options = None
    _MESSAGE_PROTO2VALUEENTRY._serialized_options = b'8\x01'
    _MESSAGE_STRINGMAPENTRY._options = None
    _MESSAGE_STRINGMAPENTRY._serialized_options = b'8\x01'
    _MESSAGEWITHMAP_BYTEMAPPINGENTRY._options = None
    _MESSAGEWITHMAP_BYTEMAPPINGENTRY._serialized_options = b'8\x01'
    _INTMAP_RTTENTRY._options = None
    _INTMAP_RTTENTRY._serialized_options = b'8\x01'
    _TESTUTF8_MAPKEYENTRY._options = None
    _TESTUTF8_MAPKEYENTRY._serialized_options = b'8\x01'
    _TESTUTF8_MAPVALUEENTRY._options = None
    _TESTUTF8_MAPVALUEENTRY._serialized_options = b'8\x01'
    _globals['_MESSAGE']._serialized_start = 94
    _globals['_MESSAGE']._serialized_end = 1027
    _globals['_MESSAGE_TERRAINENTRY']._serialized_start = 767
    _globals['_MESSAGE_TERRAINENTRY']._serialized_end = 835
    _globals['_MESSAGE_PROTO2VALUEENTRY']._serialized_start = 837
    _globals['_MESSAGE_PROTO2VALUEENTRY']._serialized_end = 912
    _globals['_MESSAGE_STRINGMAPENTRY']._serialized_start = 914
    _globals['_MESSAGE_STRINGMAPENTRY']._serialized_end = 962
    _globals['_MESSAGE_HUMOUR']._serialized_start = 964
    _globals['_MESSAGE_HUMOUR']._serialized_end = 1027
    _globals['_NESTED']._serialized_start = 1029
    _globals['_NESTED']._serialized_end = 1066
    _globals['_MESSAGEWITHMAP']._serialized_start = 1069
    _globals['_MESSAGEWITHMAP']._serialized_end = 1206
    _globals['_MESSAGEWITHMAP_BYTEMAPPINGENTRY']._serialized_start = 1156
    _globals['_MESSAGEWITHMAP_BYTEMAPPINGENTRY']._serialized_end = 1206
    _globals['_INTMAP']._serialized_start = 1208
    _globals['_INTMAP']._serialized_end = 1304
    _globals['_INTMAP_RTTENTRY']._serialized_start = 1262
    _globals['_INTMAP_RTTENTRY']._serialized_end = 1304
    _globals['_INTMAPS']._serialized_start = 1306
    _globals['_INTMAPS']._serialized_end = 1351
    _globals['_TESTUTF8']._serialized_start = 1354
    _globals['_TESTUTF8']._serialized_end = 1628
    _globals['_TESTUTF8_MAPKEYENTRY']._serialized_start = 1525
    _globals['_TESTUTF8_MAPKEYENTRY']._serialized_end = 1570
    _globals['_TESTUTF8_MAPVALUEENTRY']._serialized_start = 1572
    _globals['_TESTUTF8_MAPVALUEENTRY']._serialized_end = 1619