"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!cosmos/crypto/multisig/keys.proto\x12\x16cosmos.crypto.multisig\x1a\x14gogoproto/gogo.proto\x1a\x19google/protobuf/any.proto"\x8c\x01\n\x11LegacyAminoPubKey\x12\'\n\tthreshold\x18\x01 \x01(\rB\x14\xf2\xde\x1f\x10yaml:"threshold"\x12H\n\x0bpublic_keys\x18\x02 \x03(\x0b2\x14.google.protobuf.AnyB\x1d\xe2\xde\x1f\x07PubKeys\xf2\xde\x1f\x0eyaml:"pubkeys":\x04\x88\xa0\x1f\x00B3Z1github.com/cosmos/cosmos-sdk/crypto/keys/multisigb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.crypto.multisig.keys_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z1github.com/cosmos/cosmos-sdk/crypto/keys/multisig'
    _LEGACYAMINOPUBKEY.fields_by_name['threshold']._options = None
    _LEGACYAMINOPUBKEY.fields_by_name['threshold']._serialized_options = b'\xf2\xde\x1f\x10yaml:"threshold"'
    _LEGACYAMINOPUBKEY.fields_by_name['public_keys']._options = None
    _LEGACYAMINOPUBKEY.fields_by_name['public_keys']._serialized_options = b'\xe2\xde\x1f\x07PubKeys\xf2\xde\x1f\x0eyaml:"pubkeys"'
    _LEGACYAMINOPUBKEY._options = None
    _LEGACYAMINOPUBKEY._serialized_options = b'\x88\xa0\x1f\x00'
    _globals['_LEGACYAMINOPUBKEY']._serialized_start = 111
    _globals['_LEGACYAMINOPUBKEY']._serialized_end = 251