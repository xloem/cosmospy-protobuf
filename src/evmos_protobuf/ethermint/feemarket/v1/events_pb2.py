"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#ethermint/feemarket/v1/events.proto\x12\x16ethermint.feemarket.v1""\n\x0eEventFeeMarket\x12\x10\n\x08base_fee\x18\x01 \x01(\t"/\n\rEventBlockGas\x12\x0e\n\x06height\x18\x01 \x01(\t\x12\x0e\n\x06amount\x18\x02 \x01(\tB.Z,github.com/evmos/evmos/v13/x/feemarket/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ethermint.feemarket.v1.events_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z,github.com/evmos/evmos/v13/x/feemarket/types'
    _globals['_EVENTFEEMARKET']._serialized_start = 63
    _globals['_EVENTFEEMARKET']._serialized_end = 97
    _globals['_EVENTBLOCKGAS']._serialized_start = 99
    _globals['_EVENTBLOCKGAS']._serialized_end = 146