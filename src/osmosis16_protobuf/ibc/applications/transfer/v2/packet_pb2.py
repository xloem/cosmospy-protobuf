"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)ibc/applications/transfer/v2/packet.proto\x12\x1cibc.applications.transfer.v2"h\n\x17FungibleTokenPacketData\x12\r\n\x05denom\x18\x01 \x01(\t\x12\x0e\n\x06amount\x18\x02 \x01(\t\x12\x0e\n\x06sender\x18\x03 \x01(\t\x12\x10\n\x08receiver\x18\x04 \x01(\t\x12\x0c\n\x04memo\x18\x05 \x01(\tB9Z7github.com/cosmos/ibc-go/v4/modules/apps/transfer/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ibc.applications.transfer.v2.packet_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z7github.com/cosmos/ibc-go/v4/modules/apps/transfer/types'
    _globals['_FUNGIBLETOKENPACKETDATA']._serialized_start = 75
    _globals['_FUNGIBLETOKENPACKETDATA']._serialized_end = 179