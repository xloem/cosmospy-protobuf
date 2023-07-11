"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....evmos.claims.v1 import claims_pb2 as evmos_dot_claims_dot_v1_dot_claims__pb2
from ....evmos.claims.v1 import genesis_pb2 as evmos_dot_claims_dot_v1_dot_genesis__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bevmos/claims/v1/query.proto\x12\x0fevmos.claims.v1\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a\x1cevmos/claims/v1/claims.proto\x1a\x1devmos/claims/v1/genesis.proto\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto"\x1c\n\x1aQueryTotalUnclaimedRequest"y\n\x1bQueryTotalUnclaimedResponse\x12Z\n\x05coins\x18\x01 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins"\x14\n\x12QueryParamsRequest"D\n\x13QueryParamsResponse\x12-\n\x06params\x18\x01 \x01(\x0b2\x17.evmos.claims.v1.ParamsB\x04\xc8\xde\x1f\x00"W\n\x19QueryClaimsRecordsRequest\x12:\n\npagination\x18\x01 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\x95\x01\n\x1aQueryClaimsRecordsResponse\x12:\n\x06claims\x18\x01 \x03(\x0b2$.evmos.claims.v1.ClaimsRecordAddressB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"+\n\x18QueryClaimsRecordRequest\x12\x0f\n\x07address\x18\x01 \x01(\t"\x9b\x01\n\x19QueryClaimsRecordResponse\x12P\n\x18initial_claimable_amount\x18\x01 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\x12,\n\x06claims\x18\x02 \x03(\x0b2\x16.evmos.claims.v1.ClaimB\x04\xc8\xde\x1f\x002\xc4\x04\n\x05Query\x12\x95\x01\n\x0eTotalUnclaimed\x12+.evmos.claims.v1.QueryTotalUnclaimedRequest\x1a,.evmos.claims.v1.QueryTotalUnclaimedResponse"(\x82\xd3\xe4\x93\x02"\x12 /evmos/claims/v1/total_unclaimed\x12t\n\x06Params\x12#.evmos.claims.v1.QueryParamsRequest\x1a$.evmos.claims.v1.QueryParamsResponse"\x1f\x82\xd3\xe4\x93\x02\x19\x12\x17/evmos/claims/v1/params\x12\x91\x01\n\rClaimsRecords\x12*.evmos.claims.v1.QueryClaimsRecordsRequest\x1a+.evmos.claims.v1.QueryClaimsRecordsResponse"\'\x82\xd3\xe4\x93\x02!\x12\x1f/evmos/claims/v1/claims_records\x12\x98\x01\n\x0cClaimsRecord\x12).evmos.claims.v1.QueryClaimsRecordRequest\x1a*.evmos.claims.v1.QueryClaimsRecordResponse"1\x82\xd3\xe4\x93\x02+\x12)/evmos/claims/v1/claims_records/{address}B+Z)github.com/evmos/evmos/v13/x/claims/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'evmos.claims.v1.query_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z)github.com/evmos/evmos/v13/x/claims/types'
    _QUERYTOTALUNCLAIMEDRESPONSE.fields_by_name['coins']._options = None
    _QUERYTOTALUNCLAIMEDRESPONSE.fields_by_name['coins']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _QUERYPARAMSRESPONSE.fields_by_name['params']._options = None
    _QUERYPARAMSRESPONSE.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYCLAIMSRECORDSRESPONSE.fields_by_name['claims']._options = None
    _QUERYCLAIMSRECORDSRESPONSE.fields_by_name['claims']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYCLAIMSRECORDRESPONSE.fields_by_name['initial_claimable_amount']._options = None
    _QUERYCLAIMSRECORDRESPONSE.fields_by_name['initial_claimable_amount']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int'
    _QUERYCLAIMSRECORDRESPONSE.fields_by_name['claims']._options = None
    _QUERYCLAIMSRECORDRESPONSE.fields_by_name['claims']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERY.methods_by_name['TotalUnclaimed']._options = None
    _QUERY.methods_by_name['TotalUnclaimed']._serialized_options = b'\x82\xd3\xe4\x93\x02"\x12 /evmos/claims/v1/total_unclaimed'
    _QUERY.methods_by_name['Params']._options = None
    _QUERY.methods_by_name['Params']._serialized_options = b'\x82\xd3\xe4\x93\x02\x19\x12\x17/evmos/claims/v1/params'
    _QUERY.methods_by_name['ClaimsRecords']._options = None
    _QUERY.methods_by_name['ClaimsRecords']._serialized_options = b'\x82\xd3\xe4\x93\x02!\x12\x1f/evmos/claims/v1/claims_records'
    _QUERY.methods_by_name['ClaimsRecord']._options = None
    _QUERY.methods_by_name['ClaimsRecord']._serialized_options = b'\x82\xd3\xe4\x93\x02+\x12)/evmos/claims/v1/claims_records/{address}'
    _globals['_QUERYTOTALUNCLAIMEDREQUEST']._serialized_start = 237
    _globals['_QUERYTOTALUNCLAIMEDREQUEST']._serialized_end = 265
    _globals['_QUERYTOTALUNCLAIMEDRESPONSE']._serialized_start = 267
    _globals['_QUERYTOTALUNCLAIMEDRESPONSE']._serialized_end = 388
    _globals['_QUERYPARAMSREQUEST']._serialized_start = 390
    _globals['_QUERYPARAMSREQUEST']._serialized_end = 410
    _globals['_QUERYPARAMSRESPONSE']._serialized_start = 412
    _globals['_QUERYPARAMSRESPONSE']._serialized_end = 480
    _globals['_QUERYCLAIMSRECORDSREQUEST']._serialized_start = 482
    _globals['_QUERYCLAIMSRECORDSREQUEST']._serialized_end = 569
    _globals['_QUERYCLAIMSRECORDSRESPONSE']._serialized_start = 572
    _globals['_QUERYCLAIMSRECORDSRESPONSE']._serialized_end = 721
    _globals['_QUERYCLAIMSRECORDREQUEST']._serialized_start = 723
    _globals['_QUERYCLAIMSRECORDREQUEST']._serialized_end = 766
    _globals['_QUERYCLAIMSRECORDRESPONSE']._serialized_start = 769
    _globals['_QUERYCLAIMSRECORDRESPONSE']._serialized_end = 924
    _globals['_QUERY']._serialized_start = 927
    _globals['_QUERY']._serialized_end = 1507