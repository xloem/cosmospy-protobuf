"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....evmos.incentives.v1 import genesis_pb2 as evmos_dot_incentives_dot_v1_dot_genesis__pb2
from ....evmos.incentives.v1 import incentives_pb2 as evmos_dot_incentives_dot_v1_dot_incentives__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fevmos/incentives/v1/query.proto\x12\x13evmos.incentives.v1\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a!evmos/incentives/v1/genesis.proto\x1a$evmos/incentives/v1/incentives.proto\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto"T\n\x16QueryIncentivesRequest\x12:\n\npagination\x18\x01 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\x90\x01\n\x17QueryIncentivesResponse\x128\n\nincentives\x18\x01 \x03(\x0b2\x1e.evmos.incentives.v1.IncentiveB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse")\n\x15QueryIncentiveRequest\x12\x10\n\x08contract\x18\x01 \x01(\t"Q\n\x16QueryIncentiveResponse\x127\n\tincentive\x18\x01 \x01(\x0b2\x1e.evmos.incentives.v1.IncentiveB\x04\xc8\xde\x1f\x00"e\n\x15QueryGasMetersRequest\x12\x10\n\x08contract\x18\x01 \x01(\t\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\x8e\x01\n\x16QueryGasMetersResponse\x127\n\ngas_meters\x18\x01 \x03(\x0b2\x1d.evmos.incentives.v1.GasMeterB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"=\n\x14QueryGasMeterRequest\x12\x10\n\x08contract\x18\x01 \x01(\t\x12\x13\n\x0bparticipant\x18\x02 \x01(\t"*\n\x15QueryGasMeterResponse\x12\x11\n\tgas_meter\x18\x01 \x01(\x04"Z\n\x1cQueryAllocationMetersRequest\x12:\n\npagination\x18\x01 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\xca\x01\n\x1dQueryAllocationMetersResponse\x12l\n\x11allocation_meters\x18\x01 \x03(\x0b2\x1c.cosmos.base.v1beta1.DecCoinB3\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse",\n\x1bQueryAllocationMeterRequest\x12\r\n\x05denom\x18\x01 \x01(\t"\x8b\x01\n\x1cQueryAllocationMeterResponse\x12k\n\x10allocation_meter\x18\x01 \x01(\x0b2\x1c.cosmos.base.v1beta1.DecCoinB3\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins"\x14\n\x12QueryParamsRequest"H\n\x13QueryParamsResponse\x121\n\x06params\x18\x01 \x01(\x0b2\x1b.evmos.incentives.v1.ParamsB\x04\xc8\xde\x1f\x002\xd6\x08\n\x05Query\x12\x90\x01\n\nIncentives\x12+.evmos.incentives.v1.QueryIncentivesRequest\x1a,.evmos.incentives.v1.QueryIncentivesResponse"\'\x82\xd3\xe4\x93\x02!\x12\x1f/evmos/incentives/v1/incentives\x12\x98\x01\n\tIncentive\x12*.evmos.incentives.v1.QueryIncentiveRequest\x1a+.evmos.incentives.v1.QueryIncentiveResponse"2\x82\xd3\xe4\x93\x02,\x12*/evmos/incentives/v1/incentives/{contract}\x12\x98\x01\n\tGasMeters\x12*.evmos.incentives.v1.QueryGasMetersRequest\x1a+.evmos.incentives.v1.QueryGasMetersResponse"2\x82\xd3\xe4\x93\x02,\x12*/evmos/incentives/v1/gas_meters/{contract}\x12\xa3\x01\n\x08GasMeter\x12).evmos.incentives.v1.QueryGasMeterRequest\x1a*.evmos.incentives.v1.QueryGasMeterResponse"@\x82\xd3\xe4\x93\x02:\x128/evmos/incentives/v1/gas_meters/{contract}/{participant}\x12\xa9\x01\n\x10AllocationMeters\x121.evmos.incentives.v1.QueryAllocationMetersRequest\x1a2.evmos.incentives.v1.QueryAllocationMetersResponse".\x82\xd3\xe4\x93\x02(\x12&/evmos/incentives/v1/allocation_meters\x12\xae\x01\n\x0fAllocationMeter\x120.evmos.incentives.v1.QueryAllocationMeterRequest\x1a1.evmos.incentives.v1.QueryAllocationMeterResponse"6\x82\xd3\xe4\x93\x020\x12./evmos/incentives/v1/allocation_meters/{denom}\x12\x80\x01\n\x06Params\x12\'.evmos.incentives.v1.QueryParamsRequest\x1a(.evmos.incentives.v1.QueryParamsResponse"#\x82\xd3\xe4\x93\x02\x1d\x12\x1b/evmos/incentives/v1/paramsB/Z-github.com/evmos/evmos/v13/x/incentives/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'evmos.incentives.v1.query_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z-github.com/evmos/evmos/v13/x/incentives/types'
    _QUERYINCENTIVESRESPONSE.fields_by_name['incentives']._options = None
    _QUERYINCENTIVESRESPONSE.fields_by_name['incentives']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYINCENTIVERESPONSE.fields_by_name['incentive']._options = None
    _QUERYINCENTIVERESPONSE.fields_by_name['incentive']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYGASMETERSRESPONSE.fields_by_name['gas_meters']._options = None
    _QUERYGASMETERSRESPONSE.fields_by_name['gas_meters']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYALLOCATIONMETERSRESPONSE.fields_by_name['allocation_meters']._options = None
    _QUERYALLOCATIONMETERSRESPONSE.fields_by_name['allocation_meters']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins'
    _QUERYALLOCATIONMETERRESPONSE.fields_by_name['allocation_meter']._options = None
    _QUERYALLOCATIONMETERRESPONSE.fields_by_name['allocation_meter']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins'
    _QUERYPARAMSRESPONSE.fields_by_name['params']._options = None
    _QUERYPARAMSRESPONSE.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERY.methods_by_name['Incentives']._options = None
    _QUERY.methods_by_name['Incentives']._serialized_options = b'\x82\xd3\xe4\x93\x02!\x12\x1f/evmos/incentives/v1/incentives'
    _QUERY.methods_by_name['Incentive']._options = None
    _QUERY.methods_by_name['Incentive']._serialized_options = b'\x82\xd3\xe4\x93\x02,\x12*/evmos/incentives/v1/incentives/{contract}'
    _QUERY.methods_by_name['GasMeters']._options = None
    _QUERY.methods_by_name['GasMeters']._serialized_options = b'\x82\xd3\xe4\x93\x02,\x12*/evmos/incentives/v1/gas_meters/{contract}'
    _QUERY.methods_by_name['GasMeter']._options = None
    _QUERY.methods_by_name['GasMeter']._serialized_options = b'\x82\xd3\xe4\x93\x02:\x128/evmos/incentives/v1/gas_meters/{contract}/{participant}'
    _QUERY.methods_by_name['AllocationMeters']._options = None
    _QUERY.methods_by_name['AllocationMeters']._serialized_options = b'\x82\xd3\xe4\x93\x02(\x12&/evmos/incentives/v1/allocation_meters'
    _QUERY.methods_by_name['AllocationMeter']._options = None
    _QUERY.methods_by_name['AllocationMeter']._serialized_options = b'\x82\xd3\xe4\x93\x020\x12./evmos/incentives/v1/allocation_meters/{denom}'
    _QUERY.methods_by_name['Params']._options = None
    _QUERY.methods_by_name['Params']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1d\x12\x1b/evmos/incentives/v1/params'
    _globals['_QUERYINCENTIVESREQUEST']._serialized_start = 257
    _globals['_QUERYINCENTIVESREQUEST']._serialized_end = 341
    _globals['_QUERYINCENTIVESRESPONSE']._serialized_start = 344
    _globals['_QUERYINCENTIVESRESPONSE']._serialized_end = 488
    _globals['_QUERYINCENTIVEREQUEST']._serialized_start = 490
    _globals['_QUERYINCENTIVEREQUEST']._serialized_end = 531
    _globals['_QUERYINCENTIVERESPONSE']._serialized_start = 533
    _globals['_QUERYINCENTIVERESPONSE']._serialized_end = 614
    _globals['_QUERYGASMETERSREQUEST']._serialized_start = 616
    _globals['_QUERYGASMETERSREQUEST']._serialized_end = 717
    _globals['_QUERYGASMETERSRESPONSE']._serialized_start = 720
    _globals['_QUERYGASMETERSRESPONSE']._serialized_end = 862
    _globals['_QUERYGASMETERREQUEST']._serialized_start = 864
    _globals['_QUERYGASMETERREQUEST']._serialized_end = 925
    _globals['_QUERYGASMETERRESPONSE']._serialized_start = 927
    _globals['_QUERYGASMETERRESPONSE']._serialized_end = 969
    _globals['_QUERYALLOCATIONMETERSREQUEST']._serialized_start = 971
    _globals['_QUERYALLOCATIONMETERSREQUEST']._serialized_end = 1061
    _globals['_QUERYALLOCATIONMETERSRESPONSE']._serialized_start = 1064
    _globals['_QUERYALLOCATIONMETERSRESPONSE']._serialized_end = 1266
    _globals['_QUERYALLOCATIONMETERREQUEST']._serialized_start = 1268
    _globals['_QUERYALLOCATIONMETERREQUEST']._serialized_end = 1312
    _globals['_QUERYALLOCATIONMETERRESPONSE']._serialized_start = 1315
    _globals['_QUERYALLOCATIONMETERRESPONSE']._serialized_end = 1454
    _globals['_QUERYPARAMSREQUEST']._serialized_start = 1456
    _globals['_QUERYPARAMSREQUEST']._serialized_end = 1476
    _globals['_QUERYPARAMSRESPONSE']._serialized_start = 1478
    _globals['_QUERYPARAMSRESPONSE']._serialized_end = 1550
    _globals['_QUERY']._serialized_start = 1553
    _globals['_QUERY']._serialized_end = 2663