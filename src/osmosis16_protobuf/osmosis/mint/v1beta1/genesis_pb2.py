"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....osmosis.mint.v1beta1 import mint_pb2 as osmosis_dot_mint_dot_v1beta1_dot_mint__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"osmosis/mint/v1beta1/genesis.proto\x12\x14osmosis.mint.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1fosmosis/mint/v1beta1/mint.proto"\xbb\x01\n\x0cGenesisState\x122\n\x06minter\x18\x01 \x01(\x0b2\x1c.osmosis.mint.v1beta1.MinterB\x04\xc8\xde\x1f\x00\x122\n\x06params\x18\x02 \x01(\x0b2\x1c.osmosis.mint.v1beta1.ParamsB\x04\xc8\xde\x1f\x00\x12C\n\x17reduction_started_epoch\x18\x03 \x01(\x03B"\xf2\xde\x1f\x1eyaml:"reduction_started_epoch"B2Z0github.com/osmosis-labs/osmosis/v16/x/mint/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.mint.v1beta1.genesis_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z0github.com/osmosis-labs/osmosis/v16/x/mint/types'
    _GENESISSTATE.fields_by_name['minter']._options = None
    _GENESISSTATE.fields_by_name['minter']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['params']._options = None
    _GENESISSTATE.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['reduction_started_epoch']._options = None
    _GENESISSTATE.fields_by_name['reduction_started_epoch']._serialized_options = b'\xf2\xde\x1f\x1eyaml:"reduction_started_epoch"'
    _globals['_GENESISSTATE']._serialized_start = 116
    _globals['_GENESISSTATE']._serialized_end = 303