"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from ....osmosis.ibc_rate_limit.v1beta1 import params_pb2 as osmosis_dot_ibc__rate__limit_dot_v1beta1_dot_params__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*osmosis/ibc-rate-limit/v1beta1/query.proto\x12\x1cosmosis.ibcratelimit.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a+osmosis/ibc-rate-limit/v1beta1/params.proto"\x0f\n\rParamsRequest"L\n\x0eParamsResponse\x12:\n\x06params\x18\x01 \x01(\x0b2$.osmosis.ibcratelimit.v1beta1.ParamsB\x04\xc8\xde\x1f\x002\x9d\x01\n\x05Query\x12\x93\x01\n\x06Params\x12+.osmosis.ibcratelimit.v1beta1.ParamsRequest\x1a,.osmosis.ibcratelimit.v1beta1.ParamsResponse".\x82\xd3\xe4\x93\x02(\x12&/osmosis/ibc-rate-limit/v1beta1/paramsBHZFgithub.com/osmosis-labs/osmosis/v16/x/ibc-rate-limit/client/queryprotob\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.ibc_rate_limit.v1beta1.query_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'ZFgithub.com/osmosis-labs/osmosis/v16/x/ibc-rate-limit/client/queryproto'
    _PARAMSRESPONSE.fields_by_name['params']._options = None
    _PARAMSRESPONSE.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERY.methods_by_name['Params']._options = None
    _QUERY.methods_by_name['Params']._serialized_options = b'\x82\xd3\xe4\x93\x02(\x12&/osmosis/ibc-rate-limit/v1beta1/params'
    _globals['_PARAMSREQUEST']._serialized_start = 217
    _globals['_PARAMSREQUEST']._serialized_end = 232
    _globals['_PARAMSRESPONSE']._serialized_start = 234
    _globals['_PARAMSRESPONSE']._serialized_end = 310
    _globals['_QUERY']._serialized_start = 313
    _globals['_QUERY']._serialized_end = 470