"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ...gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ...osmosis.superfluid import superfluid_pb2 as osmosis_dot_superfluid_dot_superfluid__pb2
from ...osmosis.superfluid import params_pb2 as osmosis_dot_superfluid_dot_params__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n osmosis/superfluid/genesis.proto\x12\x12osmosis.superfluid\x1a\x14gogoproto/gogo.proto\x1a#osmosis/superfluid/superfluid.proto\x1a\x1fosmosis/superfluid/params.proto"\xa5\x03\n\x0cGenesisState\x120\n\x06params\x18\x01 \x01(\x0b2\x1a.osmosis.superfluid.ParamsB\x04\xc8\xde\x1f\x00\x12D\n\x11superfluid_assets\x18\x02 \x03(\x0b2#.osmosis.superfluid.SuperfluidAssetB\x04\xc8\xde\x1f\x00\x12]\n\x1bosmo_equivalent_multipliers\x18\x03 \x03(\x0b22.osmosis.superfluid.OsmoEquivalentMultiplierRecordB\x04\xc8\xde\x1f\x00\x12V\n\x15intermediary_accounts\x18\x04 \x03(\x0b21.osmosis.superfluid.SuperfluidIntermediaryAccountB\x04\xc8\xde\x1f\x00\x12f\n\x1fintemediary_account_connections\x18\x05 \x03(\x0b27.osmosis.superfluid.LockIdIntermediaryAccountConnectionB\x04\xc8\xde\x1f\x00B8Z6github.com/osmosis-labs/osmosis/v16/x/superfluid/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.superfluid.genesis_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z6github.com/osmosis-labs/osmosis/v16/x/superfluid/types'
    _GENESISSTATE.fields_by_name['params']._options = None
    _GENESISSTATE.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['superfluid_assets']._options = None
    _GENESISSTATE.fields_by_name['superfluid_assets']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['osmo_equivalent_multipliers']._options = None
    _GENESISSTATE.fields_by_name['osmo_equivalent_multipliers']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['intermediary_accounts']._options = None
    _GENESISSTATE.fields_by_name['intermediary_accounts']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['intemediary_account_connections']._options = None
    _GENESISSTATE.fields_by_name['intemediary_account_connections']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_GENESISSTATE']._serialized_start = 149
    _globals['_GENESISSTATE']._serialized_end = 570