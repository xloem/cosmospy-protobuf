"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....ethermint.feemarket.v1 import feemarket_pb2 as ethermint_dot_feemarket_dot_v1_dot_feemarket__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$ethermint/feemarket/v1/genesis.proto\x12\x16ethermint.feemarket.v1\x1a&ethermint/feemarket/v1/feemarket.proto\x1a\x14gogoproto/gogo.proto"g\n\x0cGenesisState\x124\n\x06params\x18\x01 \x01(\x0b2\x1e.ethermint.feemarket.v1.ParamsB\x04\xc8\xde\x1f\x00\x12\x11\n\tblock_gas\x18\x03 \x01(\x04J\x04\x08\x02\x10\x03R\x08base_feeB.Z,github.com/evmos/evmos/v13/x/feemarket/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ethermint.feemarket.v1.genesis_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z,github.com/evmos/evmos/v13/x/feemarket/types'
    _GENESISSTATE.fields_by_name['params']._options = None
    _GENESISSTATE.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_GENESISSTATE']._serialized_start = 126
    _globals['_GENESISSTATE']._serialized_end = 229