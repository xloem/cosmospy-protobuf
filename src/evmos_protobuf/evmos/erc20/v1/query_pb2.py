"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from ....evmos.erc20.v1 import erc20_pb2 as evmos_dot_erc20_dot_v1_dot_erc20__pb2
from ....evmos.erc20.v1 import genesis_pb2 as evmos_dot_erc20_dot_v1_dot_genesis__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1aevmos/erc20/v1/query.proto\x12\x0eevmos.erc20.v1\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x1aevmos/erc20/v1/erc20.proto\x1a\x1cevmos/erc20/v1/genesis.proto\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto"T\n\x16QueryTokenPairsRequest\x12:\n\npagination\x18\x01 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\x8c\x01\n\x17QueryTokenPairsResponse\x124\n\x0btoken_pairs\x18\x01 \x03(\x0b2\x19.evmos.erc20.v1.TokenPairB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"&\n\x15QueryTokenPairRequest\x12\r\n\x05token\x18\x01 \x01(\t"M\n\x16QueryTokenPairResponse\x123\n\ntoken_pair\x18\x01 \x01(\x0b2\x19.evmos.erc20.v1.TokenPairB\x04\xc8\xde\x1f\x00"\x14\n\x12QueryParamsRequest"C\n\x13QueryParamsResponse\x12,\n\x06params\x18\x01 \x01(\x0b2\x16.evmos.erc20.v1.ParamsB\x04\xc8\xde\x1f\x002\x89\x03\n\x05Query\x12\x82\x01\n\nTokenPairs\x12&.evmos.erc20.v1.QueryTokenPairsRequest\x1a\'.evmos.erc20.v1.QueryTokenPairsResponse"#\x82\xd3\xe4\x93\x02\x1d\x12\x1b/evmos/erc20/v1/token_pairs\x12\x87\x01\n\tTokenPair\x12%.evmos.erc20.v1.QueryTokenPairRequest\x1a&.evmos.erc20.v1.QueryTokenPairResponse"+\x82\xd3\xe4\x93\x02%\x12#/evmos/erc20/v1/token_pairs/{token}\x12q\n\x06Params\x12".evmos.erc20.v1.QueryParamsRequest\x1a#.evmos.erc20.v1.QueryParamsResponse"\x1e\x82\xd3\xe4\x93\x02\x18\x12\x16/evmos/erc20/v1/paramsB*Z(github.com/evmos/evmos/v13/x/erc20/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'evmos.erc20.v1.query_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z(github.com/evmos/evmos/v13/x/erc20/types'
    _QUERYTOKENPAIRSRESPONSE.fields_by_name['token_pairs']._options = None
    _QUERYTOKENPAIRSRESPONSE.fields_by_name['token_pairs']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYTOKENPAIRRESPONSE.fields_by_name['token_pair']._options = None
    _QUERYTOKENPAIRRESPONSE.fields_by_name['token_pair']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYPARAMSRESPONSE.fields_by_name['params']._options = None
    _QUERYPARAMSRESPONSE.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERY.methods_by_name['TokenPairs']._options = None
    _QUERY.methods_by_name['TokenPairs']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1d\x12\x1b/evmos/erc20/v1/token_pairs'
    _QUERY.methods_by_name['TokenPair']._options = None
    _QUERY.methods_by_name['TokenPair']._serialized_options = b'\x82\xd3\xe4\x93\x02%\x12#/evmos/erc20/v1/token_pairs/{token}'
    _QUERY.methods_by_name['Params']._options = None
    _QUERY.methods_by_name['Params']._serialized_options = b'\x82\xd3\xe4\x93\x02\x18\x12\x16/evmos/erc20/v1/params'
    _globals['_QUERYTOKENPAIRSREQUEST']._serialized_start = 200
    _globals['_QUERYTOKENPAIRSREQUEST']._serialized_end = 284
    _globals['_QUERYTOKENPAIRSRESPONSE']._serialized_start = 287
    _globals['_QUERYTOKENPAIRSRESPONSE']._serialized_end = 427
    _globals['_QUERYTOKENPAIRREQUEST']._serialized_start = 429
    _globals['_QUERYTOKENPAIRREQUEST']._serialized_end = 467
    _globals['_QUERYTOKENPAIRRESPONSE']._serialized_start = 469
    _globals['_QUERYTOKENPAIRRESPONSE']._serialized_end = 546
    _globals['_QUERYPARAMSREQUEST']._serialized_start = 548
    _globals['_QUERYPARAMSREQUEST']._serialized_end = 568
    _globals['_QUERYPARAMSRESPONSE']._serialized_start = 570
    _globals['_QUERYPARAMSRESPONSE']._serialized_end = 637
    _globals['_QUERY']._serialized_start = 640
    _globals['_QUERY']._serialized_end = 1033