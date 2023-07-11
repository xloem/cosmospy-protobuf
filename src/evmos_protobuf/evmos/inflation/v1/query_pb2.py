"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....evmos.inflation.v1 import genesis_pb2 as evmos_dot_inflation_dot_v1_dot_genesis__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1eevmos/inflation/v1/query.proto\x12\x12evmos.inflation.v1\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a evmos/inflation/v1/genesis.proto\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto"\x14\n\x12QueryPeriodRequest"%\n\x13QueryPeriodResponse\x12\x0e\n\x06period\x18\x01 \x01(\x04" \n\x1eQueryEpochMintProvisionRequest"\x92\x01\n\x1fQueryEpochMintProvisionResponse\x12o\n\x14epoch_mint_provision\x18\x01 \x01(\x0b2\x1c.cosmos.base.v1beta1.DecCoinB3\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins"\x1b\n\x19QuerySkippedEpochsRequest"4\n\x1aQuerySkippedEpochsResponse\x12\x16\n\x0eskipped_epochs\x18\x01 \x01(\x04"\x1f\n\x1dQueryCirculatingSupplyRequest"\x8f\x01\n\x1eQueryCirculatingSupplyResponse\x12m\n\x12circulating_supply\x18\x01 \x01(\x0b2\x1c.cosmos.base.v1beta1.DecCoinB3\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins"\x1b\n\x19QueryInflationRateRequest"d\n\x1aQueryInflationRateResponse\x12F\n\x0einflation_rate\x18\x01 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec"\x14\n\x12QueryParamsRequest"G\n\x13QueryParamsResponse\x120\n\x06params\x18\x01 \x01(\x0b2\x1a.evmos.inflation.v1.ParamsB\x04\xc8\xde\x1f\x002\x9e\x07\n\x05Query\x12}\n\x06Period\x12&.evmos.inflation.v1.QueryPeriodRequest\x1a\'.evmos.inflation.v1.QueryPeriodResponse""\x82\xd3\xe4\x93\x02\x1c\x12\x1a/evmos/inflation/v1/period\x12\xaf\x01\n\x12EpochMintProvision\x122.evmos.inflation.v1.QueryEpochMintProvisionRequest\x1a3.evmos.inflation.v1.QueryEpochMintProvisionResponse"0\x82\xd3\xe4\x93\x02*\x12(/evmos/inflation/v1/epoch_mint_provision\x12\x9a\x01\n\rSkippedEpochs\x12-.evmos.inflation.v1.QuerySkippedEpochsRequest\x1a..evmos.inflation.v1.QuerySkippedEpochsResponse"*\x82\xd3\xe4\x93\x02$\x12"/evmos/inflation/v1/skipped_epochs\x12\xaa\x01\n\x11CirculatingSupply\x121.evmos.inflation.v1.QueryCirculatingSupplyRequest\x1a2.evmos.inflation.v1.QueryCirculatingSupplyResponse".\x82\xd3\xe4\x93\x02(\x12&/evmos/inflation/v1/circulating_supply\x12\x9a\x01\n\rInflationRate\x12-.evmos.inflation.v1.QueryInflationRateRequest\x1a..evmos.inflation.v1.QueryInflationRateResponse"*\x82\xd3\xe4\x93\x02$\x12"/evmos/inflation/v1/inflation_rate\x12}\n\x06Params\x12&.evmos.inflation.v1.QueryParamsRequest\x1a\'.evmos.inflation.v1.QueryParamsResponse""\x82\xd3\xe4\x93\x02\x1c\x12\x1a/evmos/inflation/v1/paramsB.Z,github.com/evmos/evmos/v13/x/inflation/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'evmos.inflation.v1.query_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z,github.com/evmos/evmos/v13/x/inflation/types'
    _QUERYEPOCHMINTPROVISIONRESPONSE.fields_by_name['epoch_mint_provision']._options = None
    _QUERYEPOCHMINTPROVISIONRESPONSE.fields_by_name['epoch_mint_provision']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins'
    _QUERYCIRCULATINGSUPPLYRESPONSE.fields_by_name['circulating_supply']._options = None
    _QUERYCIRCULATINGSUPPLYRESPONSE.fields_by_name['circulating_supply']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins'
    _QUERYINFLATIONRATERESPONSE.fields_by_name['inflation_rate']._options = None
    _QUERYINFLATIONRATERESPONSE.fields_by_name['inflation_rate']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec'
    _QUERYPARAMSRESPONSE.fields_by_name['params']._options = None
    _QUERYPARAMSRESPONSE.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERY.methods_by_name['Period']._options = None
    _QUERY.methods_by_name['Period']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1c\x12\x1a/evmos/inflation/v1/period'
    _QUERY.methods_by_name['EpochMintProvision']._options = None
    _QUERY.methods_by_name['EpochMintProvision']._serialized_options = b'\x82\xd3\xe4\x93\x02*\x12(/evmos/inflation/v1/epoch_mint_provision'
    _QUERY.methods_by_name['SkippedEpochs']._options = None
    _QUERY.methods_by_name['SkippedEpochs']._serialized_options = b'\x82\xd3\xe4\x93\x02$\x12"/evmos/inflation/v1/skipped_epochs'
    _QUERY.methods_by_name['CirculatingSupply']._options = None
    _QUERY.methods_by_name['CirculatingSupply']._serialized_options = b'\x82\xd3\xe4\x93\x02(\x12&/evmos/inflation/v1/circulating_supply'
    _QUERY.methods_by_name['InflationRate']._options = None
    _QUERY.methods_by_name['InflationRate']._serialized_options = b'\x82\xd3\xe4\x93\x02$\x12"/evmos/inflation/v1/inflation_rate'
    _QUERY.methods_by_name['Params']._options = None
    _QUERY.methods_by_name['Params']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1c\x12\x1a/evmos/inflation/v1/params'
    _globals['_QUERYPERIODREQUEST']._serialized_start = 172
    _globals['_QUERYPERIODREQUEST']._serialized_end = 192
    _globals['_QUERYPERIODRESPONSE']._serialized_start = 194
    _globals['_QUERYPERIODRESPONSE']._serialized_end = 231
    _globals['_QUERYEPOCHMINTPROVISIONREQUEST']._serialized_start = 233
    _globals['_QUERYEPOCHMINTPROVISIONREQUEST']._serialized_end = 265
    _globals['_QUERYEPOCHMINTPROVISIONRESPONSE']._serialized_start = 268
    _globals['_QUERYEPOCHMINTPROVISIONRESPONSE']._serialized_end = 414
    _globals['_QUERYSKIPPEDEPOCHSREQUEST']._serialized_start = 416
    _globals['_QUERYSKIPPEDEPOCHSREQUEST']._serialized_end = 443
    _globals['_QUERYSKIPPEDEPOCHSRESPONSE']._serialized_start = 445
    _globals['_QUERYSKIPPEDEPOCHSRESPONSE']._serialized_end = 497
    _globals['_QUERYCIRCULATINGSUPPLYREQUEST']._serialized_start = 499
    _globals['_QUERYCIRCULATINGSUPPLYREQUEST']._serialized_end = 530
    _globals['_QUERYCIRCULATINGSUPPLYRESPONSE']._serialized_start = 533
    _globals['_QUERYCIRCULATINGSUPPLYRESPONSE']._serialized_end = 676
    _globals['_QUERYINFLATIONRATEREQUEST']._serialized_start = 678
    _globals['_QUERYINFLATIONRATEREQUEST']._serialized_end = 705
    _globals['_QUERYINFLATIONRATERESPONSE']._serialized_start = 707
    _globals['_QUERYINFLATIONRATERESPONSE']._serialized_end = 807
    _globals['_QUERYPARAMSREQUEST']._serialized_start = 809
    _globals['_QUERYPARAMSREQUEST']._serialized_end = 829
    _globals['_QUERYPARAMSRESPONSE']._serialized_start = 831
    _globals['_QUERYPARAMSRESPONSE']._serialized_end = 902
    _globals['_QUERY']._serialized_start = 905
    _globals['_QUERY']._serialized_end = 1831