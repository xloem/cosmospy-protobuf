"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....akash.base.v1beta3 import resourceunits_pb2 as akash_dot_base_dot_v1beta3_dot_resourceunits__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'akash/deployment/v1beta3/resource.proto\x12\x18akash.deployment.v1beta3\x1a\x14gogoproto/gogo.proto\x1a&akash/base/v1beta3/resourceunits.proto\x1a\x1ecosmos/base/v1beta1/coin.proto"\xd9\x01\n\x08Resource\x12Q\n\tresources\x18\x01 \x01(\x0b2!.akash.base.v1beta3.ResourceUnitsB\x1b\xc8\xde\x1f\x00\xea\xde\x1f\x04unit\xf2\xde\x1f\x0byaml:"unit"\x12(\n\x05count\x18\x02 \x01(\rB\x19\xea\xde\x1f\x05count\xf2\xde\x1f\x0cyaml:"count"\x12J\n\x05price\x18\x03 \x01(\x0b2\x1c.cosmos.base.v1beta1.DecCoinB\x1d\xc8\xde\x1f\x00\xea\xde\x1f\x05price\xf2\xde\x1f\x0cyaml:"price":\x04\xe8\xa0\x1f\x00B?Z=github.com/akash-network/akash-api/go/node/deployment/v1beta3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'akash.deployment.v1beta3.resource_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z=github.com/akash-network/akash-api/go/node/deployment/v1beta3'
    _RESOURCE.fields_by_name['resources']._options = None
    _RESOURCE.fields_by_name['resources']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x04unit\xf2\xde\x1f\x0byaml:"unit"'
    _RESOURCE.fields_by_name['count']._options = None
    _RESOURCE.fields_by_name['count']._serialized_options = b'\xea\xde\x1f\x05count\xf2\xde\x1f\x0cyaml:"count"'
    _RESOURCE.fields_by_name['price']._options = None
    _RESOURCE.fields_by_name['price']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x05price\xf2\xde\x1f\x0cyaml:"price"'
    _RESOURCE._options = None
    _RESOURCE._serialized_options = b'\xe8\xa0\x1f\x00'
    _globals['_RESOURCE']._serialized_start = 164
    _globals['_RESOURCE']._serialized_end = 381