"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos.slashing.v1beta1 import slashing_pb2 as cosmos_dot_slashing_dot_v1beta1_dot_slashing__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%cosmos/slashing/v1beta1/genesis.proto\x12\x17cosmos.slashing.v1beta1\x1a\x14gogoproto/gogo.proto\x1a&cosmos/slashing/v1beta1/slashing.proto"\x85\x02\n\x0cGenesisState\x125\n\x06params\x18\x01 \x01(\x0b2\x1f.cosmos.slashing.v1beta1.ParamsB\x04\xc8\xde\x1f\x00\x12Y\n\rsigning_infos\x18\x02 \x03(\x0b2$.cosmos.slashing.v1beta1.SigningInfoB\x1c\xc8\xde\x1f\x00\xf2\xde\x1f\x14yaml:"signing_infos"\x12c\n\rmissed_blocks\x18\x03 \x03(\x0b2..cosmos.slashing.v1beta1.ValidatorMissedBlocksB\x1c\xc8\xde\x1f\x00\xf2\xde\x1f\x14yaml:"missed_blocks""\x94\x01\n\x0bSigningInfo\x12\x0f\n\x07address\x18\x01 \x01(\t\x12t\n\x16validator_signing_info\x18\x02 \x01(\x0b2-.cosmos.slashing.v1beta1.ValidatorSigningInfoB%\xc8\xde\x1f\x00\xf2\xde\x1f\x1dyaml:"validator_signing_info""\x83\x01\n\x15ValidatorMissedBlocks\x12\x0f\n\x07address\x18\x01 \x01(\t\x12Y\n\rmissed_blocks\x18\x02 \x03(\x0b2$.cosmos.slashing.v1beta1.MissedBlockB\x1c\xc8\xde\x1f\x00\xf2\xde\x1f\x14yaml:"missed_blocks"",\n\x0bMissedBlock\x12\r\n\x05index\x18\x01 \x01(\x03\x12\x0e\n\x06missed\x18\x02 \x01(\x08B/Z-github.com/cosmos/cosmos-sdk/x/slashing/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.slashing.v1beta1.genesis_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z-github.com/cosmos/cosmos-sdk/x/slashing/types'
    _GENESISSTATE.fields_by_name['params']._options = None
    _GENESISSTATE.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['signing_infos']._options = None
    _GENESISSTATE.fields_by_name['signing_infos']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x14yaml:"signing_infos"'
    _GENESISSTATE.fields_by_name['missed_blocks']._options = None
    _GENESISSTATE.fields_by_name['missed_blocks']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x14yaml:"missed_blocks"'
    _SIGNINGINFO.fields_by_name['validator_signing_info']._options = None
    _SIGNINGINFO.fields_by_name['validator_signing_info']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x1dyaml:"validator_signing_info"'
    _VALIDATORMISSEDBLOCKS.fields_by_name['missed_blocks']._options = None
    _VALIDATORMISSEDBLOCKS.fields_by_name['missed_blocks']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x14yaml:"missed_blocks"'
    _globals['_GENESISSTATE']._serialized_start = 129
    _globals['_GENESISSTATE']._serialized_end = 390
    _globals['_SIGNINGINFO']._serialized_start = 393
    _globals['_SIGNINGINFO']._serialized_end = 541
    _globals['_VALIDATORMISSEDBLOCKS']._serialized_start = 544
    _globals['_VALIDATORMISSEDBLOCKS']._serialized_end = 675
    _globals['_MISSEDBLOCK']._serialized_start = 677
    _globals['_MISSEDBLOCK']._serialized_end = 721