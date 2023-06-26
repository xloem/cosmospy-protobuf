"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....osmosis.mint.v1beta1 import mint_pb2 as osmosis_dot_mint_dot_v1beta1_dot_mint__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n osmosis/mint/v1beta1/query.proto\x12\x14osmosis.mint.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1fosmosis/mint/v1beta1/mint.proto"\x14\n\x12QueryParamsRequest"I\n\x13QueryParamsResponse\x122\n\x06params\x18\x01 \x01(\x0b2\x1c.osmosis.mint.v1beta1.ParamsB\x04\xc8\xde\x1f\x00"\x1d\n\x1bQueryEpochProvisionsRequest"h\n\x1cQueryEpochProvisionsResponse\x12H\n\x10epoch_provisions\x18\x01 \x01(\x0cB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec2\xb8\x02\n\x05Query\x12\x83\x01\n\x06Params\x12(.osmosis.mint.v1beta1.QueryParamsRequest\x1a).osmosis.mint.v1beta1.QueryParamsResponse"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/osmosis/mint/v1beta1/params\x12\xa8\x01\n\x0fEpochProvisions\x121.osmosis.mint.v1beta1.QueryEpochProvisionsRequest\x1a2.osmosis.mint.v1beta1.QueryEpochProvisionsResponse".\x82\xd3\xe4\x93\x02(\x12&/osmosis/mint/v1beta1/epoch_provisionsB1Z/github.com/osmosis-labs/osmosis/v9/x/mint/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.mint.v1beta1.query_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z/github.com/osmosis-labs/osmosis/v9/x/mint/types'
    _QUERYPARAMSRESPONSE.fields_by_name['params']._options = None
    _QUERYPARAMSRESPONSE.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYEPOCHPROVISIONSRESPONSE.fields_by_name['epoch_provisions']._options = None
    _QUERYEPOCHPROVISIONSRESPONSE.fields_by_name['epoch_provisions']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec'
    _QUERY.methods_by_name['Params']._options = None
    _QUERY.methods_by_name['Params']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1e\x12\x1c/osmosis/mint/v1beta1/params'
    _QUERY.methods_by_name['EpochProvisions']._options = None
    _QUERY.methods_by_name['EpochProvisions']._serialized_options = b'\x82\xd3\xe4\x93\x02(\x12&/osmosis/mint/v1beta1/epoch_provisions'
    _globals['_QUERYPARAMSREQUEST']._serialized_start = 143
    _globals['_QUERYPARAMSREQUEST']._serialized_end = 163
    _globals['_QUERYPARAMSRESPONSE']._serialized_start = 165
    _globals['_QUERYPARAMSRESPONSE']._serialized_end = 238
    _globals['_QUERYEPOCHPROVISIONSREQUEST']._serialized_start = 240
    _globals['_QUERYEPOCHPROVISIONSREQUEST']._serialized_end = 269
    _globals['_QUERYEPOCHPROVISIONSRESPONSE']._serialized_start = 271
    _globals['_QUERYEPOCHPROVISIONSRESPONSE']._serialized_end = 375
    _globals['_QUERY']._serialized_start = 378
    _globals['_QUERY']._serialized_end = 690