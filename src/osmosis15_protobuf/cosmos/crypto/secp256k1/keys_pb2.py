"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"cosmos/crypto/secp256k1/keys.proto\x12\x17cosmos.crypto.secp256k1\x1a\x14gogoproto/gogo.proto"\x1b\n\x06PubKey\x12\x0b\n\x03key\x18\x01 \x01(\x0c:\x04\x98\xa0\x1f\x00"\x16\n\x07PrivKey\x12\x0b\n\x03key\x18\x01 \x01(\x0cB4Z2github.com/cosmos/cosmos-sdk/crypto/keys/secp256k1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.crypto.secp256k1.keys_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z2github.com/cosmos/cosmos-sdk/crypto/keys/secp256k1'
    _PUBKEY._options = None
    _PUBKEY._serialized_options = b'\x98\xa0\x1f\x00'
    _globals['_PUBKEY']._serialized_start = 85
    _globals['_PUBKEY']._serialized_end = 112
    _globals['_PRIVKEY']._serialized_start = 114
    _globals['_PRIVKEY']._serialized_end = 136