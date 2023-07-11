"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dethermint/evm/v1/events.proto\x12\x10ethermint.evm.v1"\x8c\x01\n\x0fEventEthereumTx\x12\x0e\n\x06amount\x18\x01 \x01(\t\x12\x10\n\x08eth_hash\x18\x02 \x01(\t\x12\r\n\x05index\x18\x03 \x01(\t\x12\x10\n\x08gas_used\x18\x04 \x01(\t\x12\x0c\n\x04hash\x18\x05 \x01(\t\x12\x11\n\trecipient\x18\x06 \x01(\t\x12\x15\n\reth_tx_failed\x18\x07 \x01(\t"\x1d\n\nEventTxLog\x12\x0f\n\x07tx_logs\x18\x01 \x03(\t"?\n\x0cEventMessage\x12\x0e\n\x06module\x18\x01 \x01(\t\x12\x0e\n\x06sender\x18\x02 \x01(\t\x12\x0f\n\x07tx_type\x18\x03 \x01(\t" \n\x0fEventBlockBloom\x12\r\n\x05bloom\x18\x01 \x01(\tB(Z&github.com/evmos/evmos/v13/x/evm/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ethermint.evm.v1.events_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z&github.com/evmos/evmos/v13/x/evm/types'
    _globals['_EVENTETHEREUMTX']._serialized_start = 52
    _globals['_EVENTETHEREUMTX']._serialized_end = 192
    _globals['_EVENTTXLOG']._serialized_start = 194
    _globals['_EVENTTXLOG']._serialized_end = 223
    _globals['_EVENTMESSAGE']._serialized_start = 225
    _globals['_EVENTMESSAGE']._serialized_end = 288
    _globals['_EVENTBLOCKBLOOM']._serialized_start = 290
    _globals['_EVENTBLOCKBLOOM']._serialized_end = 322