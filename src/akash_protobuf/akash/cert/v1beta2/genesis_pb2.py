"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....akash.cert.v1beta2 import cert_pb2 as akash_dot_cert_dot_v1beta2_dot_cert__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n akash/cert/v1beta2/genesis.proto\x12\x12akash.cert.v1beta2\x1a\x1dakash/cert/v1beta2/cert.proto\x1a\x14gogoproto/gogo.proto"\x9f\x01\n\x12GenesisCertificate\x12(\n\x05owner\x18\x01 \x01(\tB\x19\xea\xde\x1f\x05owner\xf2\xde\x1f\x0cyaml:"owner"\x12_\n\x0bcertificate\x18\x02 \x01(\x0b2\x1f.akash.cert.v1beta2.CertificateB)\xc8\xde\x1f\x00\xea\xde\x1f\x0bcertificate\xf2\xde\x1f\x12yaml:"certificate""\x91\x01\n\x0cGenesisState\x12\x80\x01\n\x0ccertificates\x18\x01 \x03(\x0b2&.akash.cert.v1beta2.GenesisCertificateBB\xc8\xde\x1f\x00\xea\xde\x1f\x0ccertificates\xf2\xde\x1f\x13yaml:"certificates"\xaa\xdf\x1f\x13GenesisCertificatesB9Z7github.com/akash-network/akash-api/go/node/cert/v1beta2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'akash.cert.v1beta2.genesis_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z7github.com/akash-network/akash-api/go/node/cert/v1beta2'
    _GENESISCERTIFICATE.fields_by_name['owner']._options = None
    _GENESISCERTIFICATE.fields_by_name['owner']._serialized_options = b'\xea\xde\x1f\x05owner\xf2\xde\x1f\x0cyaml:"owner"'
    _GENESISCERTIFICATE.fields_by_name['certificate']._options = None
    _GENESISCERTIFICATE.fields_by_name['certificate']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x0bcertificate\xf2\xde\x1f\x12yaml:"certificate"'
    _GENESISSTATE.fields_by_name['certificates']._options = None
    _GENESISSTATE.fields_by_name['certificates']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x0ccertificates\xf2\xde\x1f\x13yaml:"certificates"\xaa\xdf\x1f\x13GenesisCertificates'
    _globals['_GENESISCERTIFICATE']._serialized_start = 110
    _globals['_GENESISCERTIFICATE']._serialized_end = 269
    _globals['_GENESISSTATE']._serialized_start = 272
    _globals['_GENESISSTATE']._serialized_end = 417