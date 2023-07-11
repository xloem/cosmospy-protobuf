"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....akash.escrow.v1beta1 import types_pb2 as akash_dot_escrow_dot_v1beta1_dot_types__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"akash/escrow/v1beta1/genesis.proto\x12\x14akash.escrow.v1beta1\x1a\x14gogoproto/gogo.proto\x1a akash/escrow/v1beta1/types.proto"\xba\x01\n\x0cGenesisState\x12T\n\x08accounts\x18\x01 \x03(\x0b2\x1d.akash.escrow.v1beta1.AccountB#\xc8\xde\x1f\x00\xea\xde\x1f\x08accounts\xf2\xde\x1f\x0fyaml:"accounts"\x12T\n\x08payments\x18\x02 \x03(\x0b2\x1d.akash.escrow.v1beta1.PaymentB#\xc8\xde\x1f\x00\xea\xde\x1f\x08payments\xf2\xde\x1f\x0fyaml:"payments"B;Z9github.com/akash-network/akash-api/go/node/escrow/v1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'akash.escrow.v1beta1.genesis_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z9github.com/akash-network/akash-api/go/node/escrow/v1beta1'
    _GENESISSTATE.fields_by_name['accounts']._options = None
    _GENESISSTATE.fields_by_name['accounts']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x08accounts\xf2\xde\x1f\x0fyaml:"accounts"'
    _GENESISSTATE.fields_by_name['payments']._options = None
    _GENESISSTATE.fields_by_name['payments']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x08payments\xf2\xde\x1f\x0fyaml:"payments"'
    _globals['_GENESISSTATE']._serialized_start = 117
    _globals['_GENESISSTATE']._serialized_end = 303