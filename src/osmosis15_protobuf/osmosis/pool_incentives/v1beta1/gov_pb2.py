"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....osmosis.pool_incentives.v1beta1 import incentives_pb2 as osmosis_dot_pool__incentives_dot_v1beta1_dot_incentives__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)osmosis/pool-incentives/v1beta1/gov.proto\x12\x1eosmosis.poolincentives.v1beta1\x1a\x14gogoproto/gogo.proto\x1a0osmosis/pool-incentives/v1beta1/incentives.proto"\x95\x01\n\x1dReplacePoolIncentivesProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12B\n\x07records\x18\x03 \x03(\x0b2+.osmosis.poolincentives.v1beta1.DistrRecordB\x04\xc8\xde\x1f\x00:\x0c\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xe8\xa0\x1f\x01"\x94\x01\n\x1cUpdatePoolIncentivesProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12B\n\x07records\x18\x03 \x03(\x0b2+.osmosis.poolincentives.v1beta1.DistrRecordB\x04\xc8\xde\x1f\x00:\x0c\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xe8\xa0\x1f\x01B=Z;github.com/osmosis-labs/osmosis/v15/x/pool-incentives/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.pool_incentives.v1beta1.gov_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z;github.com/osmosis-labs/osmosis/v15/x/pool-incentives/types'
    _REPLACEPOOLINCENTIVESPROPOSAL.fields_by_name['records']._options = None
    _REPLACEPOOLINCENTIVESPROPOSAL.fields_by_name['records']._serialized_options = b'\xc8\xde\x1f\x00'
    _REPLACEPOOLINCENTIVESPROPOSAL._options = None
    _REPLACEPOOLINCENTIVESPROPOSAL._serialized_options = b'\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xe8\xa0\x1f\x01'
    _UPDATEPOOLINCENTIVESPROPOSAL.fields_by_name['records']._options = None
    _UPDATEPOOLINCENTIVESPROPOSAL.fields_by_name['records']._serialized_options = b'\xc8\xde\x1f\x00'
    _UPDATEPOOLINCENTIVESPROPOSAL._options = None
    _UPDATEPOOLINCENTIVESPROPOSAL._serialized_options = b'\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xe8\xa0\x1f\x01'
    _globals['_REPLACEPOOLINCENTIVESPROPOSAL']._serialized_start = 150
    _globals['_REPLACEPOOLINCENTIVESPROPOSAL']._serialized_end = 299
    _globals['_UPDATEPOOLINCENTIVESPROPOSAL']._serialized_start = 302
    _globals['_UPDATEPOOLINCENTIVESPROPOSAL']._serialized_end = 450