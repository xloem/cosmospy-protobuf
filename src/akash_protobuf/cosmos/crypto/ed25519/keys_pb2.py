"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n cosmos/crypto/ed25519/keys.proto\x12\x15cosmos.crypto.ed25519\x1a\x14gogoproto/gogo.proto"9\n\x06PubKey\x12)\n\x03key\x18\x01 \x01(\x0cB\x1c\xfa\xde\x1f\x18crypto/ed25519.PublicKey:\x04\x98\xa0\x1f\x00"5\n\x07PrivKey\x12*\n\x03key\x18\x01 \x01(\x0cB\x1d\xfa\xde\x1f\x19crypto/ed25519.PrivateKeyB2Z0github.com/cosmos/cosmos-sdk/crypto/keys/ed25519b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.crypto.ed25519.keys_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z0github.com/cosmos/cosmos-sdk/crypto/keys/ed25519'
    _PUBKEY.fields_by_name['key']._options = None
    _PUBKEY.fields_by_name['key']._serialized_options = b'\xfa\xde\x1f\x18crypto/ed25519.PublicKey'
    _PUBKEY._options = None
    _PUBKEY._serialized_options = b'\x98\xa0\x1f\x00'
    _PRIVKEY.fields_by_name['key']._options = None
    _PRIVKEY.fields_by_name['key']._serialized_options = b'\xfa\xde\x1f\x19crypto/ed25519.PrivateKey'
    _globals['_PUBKEY']._serialized_start = 81
    _globals['_PUBKEY']._serialized_end = 138
    _globals['_PRIVKEY']._serialized_start = 140
    _globals['_PRIVKEY']._serialized_end = 193