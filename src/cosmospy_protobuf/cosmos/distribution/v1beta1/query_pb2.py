"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....cosmos.distribution.v1beta1 import distribution_pb2 as cosmos_dot_distribution_dot_v1beta1_dot_distribution__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'cosmos/distribution/v1beta1/query.proto\x12\x1bcosmos.distribution.v1beta1\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a.cosmos/distribution/v1beta1/distribution.proto"\x14\n\x12QueryParamsRequest"P\n\x13QueryParamsResponse\x129\n\x06params\x18\x01 \x01(\x0b2#.cosmos.distribution.v1beta1.ParamsB\x04\xc8\xde\x1f\x00"D\n\'QueryValidatorOutstandingRewardsRequest\x12\x19\n\x11validator_address\x18\x01 \x01(\t"{\n(QueryValidatorOutstandingRewardsResponse\x12O\n\x07rewards\x18\x01 \x01(\x0b28.cosmos.distribution.v1beta1.ValidatorOutstandingRewardsB\x04\xc8\xde\x1f\x00"<\n\x1fQueryValidatorCommissionRequest\x12\x19\n\x11validator_address\x18\x01 \x01(\t"y\n QueryValidatorCommissionResponse\x12U\n\ncommission\x18\x01 \x01(\x0b2;.cosmos.distribution.v1beta1.ValidatorAccumulatedCommissionB\x04\xc8\xde\x1f\x00"\xaf\x01\n\x1cQueryValidatorSlashesRequest\x12\x19\n\x11validator_address\x18\x01 \x01(\t\x12\x17\n\x0fstarting_height\x18\x02 \x01(\x04\x12\x15\n\rending_height\x18\x03 \x01(\x04\x12:\n\npagination\x18\x04 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest:\x08\x88\xa0\x1f\x00\x98\xa0\x1f\x01"\xa5\x01\n\x1dQueryValidatorSlashesResponse\x12G\n\x07slashes\x18\x01 \x03(\x0b20.cosmos.distribution.v1beta1.ValidatorSlashEventB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"_\n\x1dQueryDelegationRewardsRequest\x12\x19\n\x11delegator_address\x18\x01 \x01(\t\x12\x19\n\x11validator_address\x18\x02 \x01(\t:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00"\x84\x01\n\x1eQueryDelegationRewardsResponse\x12b\n\x07rewards\x18\x01 \x03(\x0b2\x1c.cosmos.base.v1beta1.DecCoinB3\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins"I\n"QueryDelegationTotalRewardsRequest\x12\x19\n\x11delegator_address\x18\x01 \x01(\t:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00"\xd6\x01\n#QueryDelegationTotalRewardsResponse\x12M\n\x07rewards\x18\x01 \x03(\x0b26.cosmos.distribution.v1beta1.DelegationDelegatorRewardB\x04\xc8\xde\x1f\x00\x12`\n\x05total\x18\x02 \x03(\x0b2\x1c.cosmos.base.v1beta1.DecCoinB3\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins"F\n\x1fQueryDelegatorValidatorsRequest\x12\x19\n\x11delegator_address\x18\x01 \x01(\t:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00"@\n QueryDelegatorValidatorsResponse\x12\x12\n\nvalidators\x18\x01 \x03(\t:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00"K\n$QueryDelegatorWithdrawAddressRequest\x12\x19\n\x11delegator_address\x18\x01 \x01(\t:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00"K\n%QueryDelegatorWithdrawAddressResponse\x12\x18\n\x10withdraw_address\x18\x01 \x01(\t:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00"\x1b\n\x19QueryCommunityPoolRequest"}\n\x1aQueryCommunityPoolResponse\x12_\n\x04pool\x18\x01 \x03(\x0b2\x1c.cosmos.base.v1beta1.DecCoinB3\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins"b\n%QueryTokenizeShareRecordRewardRequest\x12/\n\rowner_address\x18\x01 \x01(\tB\x18\xf2\xde\x1f\x14yaml:"owner_address":\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00"\xd9\x01\n&QueryTokenizeShareRecordRewardResponse\x12M\n\x07rewards\x18\x01 \x03(\x0b26.cosmos.distribution.v1beta1.TokenizeShareRecordRewardB\x04\xc8\xde\x1f\x00\x12`\n\x05total\x18\x02 \x03(\x0b2\x1c.cosmos.base.v1beta1.DecCoinB3\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins2\xd3\x11\n\x05Query\x12\x98\x01\n\x06Params\x12/.cosmos.distribution.v1beta1.QueryParamsRequest\x1a0.cosmos.distribution.v1beta1.QueryParamsResponse"+\x82\xd3\xe4\x93\x02%\x12#/cosmos/distribution/v1beta1/params\x12\x83\x02\n\x1bValidatorOutstandingRewards\x12D.cosmos.distribution.v1beta1.QueryValidatorOutstandingRewardsRequest\x1aE.cosmos.distribution.v1beta1.QueryValidatorOutstandingRewardsResponse"W\x82\xd3\xe4\x93\x02Q\x12O/cosmos/distribution/v1beta1/validators/{validator_address}/outstanding_rewards\x12\xe2\x01\n\x13ValidatorCommission\x12<.cosmos.distribution.v1beta1.QueryValidatorCommissionRequest\x1a=.cosmos.distribution.v1beta1.QueryValidatorCommissionResponse"N\x82\xd3\xe4\x93\x02H\x12F/cosmos/distribution/v1beta1/validators/{validator_address}/commission\x12\xd6\x01\n\x10ValidatorSlashes\x129.cosmos.distribution.v1beta1.QueryValidatorSlashesRequest\x1a:.cosmos.distribution.v1beta1.QueryValidatorSlashesResponse"K\x82\xd3\xe4\x93\x02E\x12C/cosmos/distribution/v1beta1/validators/{validator_address}/slashes\x12\xed\x01\n\x11DelegationRewards\x12:.cosmos.distribution.v1beta1.QueryDelegationRewardsRequest\x1a;.cosmos.distribution.v1beta1.QueryDelegationRewardsResponse"_\x82\xd3\xe4\x93\x02Y\x12W/cosmos/distribution/v1beta1/delegators/{delegator_address}/rewards/{validator_address}\x12\xe8\x01\n\x16DelegationTotalRewards\x12?.cosmos.distribution.v1beta1.QueryDelegationTotalRewardsRequest\x1a@.cosmos.distribution.v1beta1.QueryDelegationTotalRewardsResponse"K\x82\xd3\xe4\x93\x02E\x12C/cosmos/distribution/v1beta1/delegators/{delegator_address}/rewards\x12\xe2\x01\n\x13DelegatorValidators\x12<.cosmos.distribution.v1beta1.QueryDelegatorValidatorsRequest\x1a=.cosmos.distribution.v1beta1.QueryDelegatorValidatorsResponse"N\x82\xd3\xe4\x93\x02H\x12F/cosmos/distribution/v1beta1/delegators/{delegator_address}/validators\x12\xf7\x01\n\x18DelegatorWithdrawAddress\x12A.cosmos.distribution.v1beta1.QueryDelegatorWithdrawAddressRequest\x1aB.cosmos.distribution.v1beta1.QueryDelegatorWithdrawAddressResponse"T\x82\xd3\xe4\x93\x02N\x12L/cosmos/distribution/v1beta1/delegators/{delegator_address}/withdraw_address\x12\xb5\x01\n\rCommunityPool\x126.cosmos.distribution.v1beta1.QueryCommunityPoolRequest\x1a7.cosmos.distribution.v1beta1.QueryCommunityPoolResponse"3\x82\xd3\xe4\x93\x02-\x12+/cosmos/distribution/v1beta1/community_pool\x12\xf8\x01\n\x19TokenizeShareRecordReward\x12B.cosmos.distribution.v1beta1.QueryTokenizeShareRecordRewardRequest\x1aC.cosmos.distribution.v1beta1.QueryTokenizeShareRecordRewardResponse"R\x82\xd3\xe4\x93\x02L\x12J/cosmos/distribution/v1beta1/{owner_address}/tokenize_share_record_rewardsB3Z1github.com/cosmos/cosmos-sdk/x/distribution/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.distribution.v1beta1.query_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z1github.com/cosmos/cosmos-sdk/x/distribution/types'
    _QUERYPARAMSRESPONSE.fields_by_name['params']._options = None
    _QUERYPARAMSRESPONSE.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYVALIDATOROUTSTANDINGREWARDSRESPONSE.fields_by_name['rewards']._options = None
    _QUERYVALIDATOROUTSTANDINGREWARDSRESPONSE.fields_by_name['rewards']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYVALIDATORCOMMISSIONRESPONSE.fields_by_name['commission']._options = None
    _QUERYVALIDATORCOMMISSIONRESPONSE.fields_by_name['commission']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYVALIDATORSLASHESREQUEST._options = None
    _QUERYVALIDATORSLASHESREQUEST._serialized_options = b'\x88\xa0\x1f\x00\x98\xa0\x1f\x01'
    _QUERYVALIDATORSLASHESRESPONSE.fields_by_name['slashes']._options = None
    _QUERYVALIDATORSLASHESRESPONSE.fields_by_name['slashes']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYDELEGATIONREWARDSREQUEST._options = None
    _QUERYDELEGATIONREWARDSREQUEST._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _QUERYDELEGATIONREWARDSRESPONSE.fields_by_name['rewards']._options = None
    _QUERYDELEGATIONREWARDSRESPONSE.fields_by_name['rewards']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins'
    _QUERYDELEGATIONTOTALREWARDSREQUEST._options = None
    _QUERYDELEGATIONTOTALREWARDSREQUEST._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _QUERYDELEGATIONTOTALREWARDSRESPONSE.fields_by_name['rewards']._options = None
    _QUERYDELEGATIONTOTALREWARDSRESPONSE.fields_by_name['rewards']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYDELEGATIONTOTALREWARDSRESPONSE.fields_by_name['total']._options = None
    _QUERYDELEGATIONTOTALREWARDSRESPONSE.fields_by_name['total']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins'
    _QUERYDELEGATORVALIDATORSREQUEST._options = None
    _QUERYDELEGATORVALIDATORSREQUEST._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _QUERYDELEGATORVALIDATORSRESPONSE._options = None
    _QUERYDELEGATORVALIDATORSRESPONSE._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _QUERYDELEGATORWITHDRAWADDRESSREQUEST._options = None
    _QUERYDELEGATORWITHDRAWADDRESSREQUEST._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _QUERYDELEGATORWITHDRAWADDRESSRESPONSE._options = None
    _QUERYDELEGATORWITHDRAWADDRESSRESPONSE._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _QUERYCOMMUNITYPOOLRESPONSE.fields_by_name['pool']._options = None
    _QUERYCOMMUNITYPOOLRESPONSE.fields_by_name['pool']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins'
    _QUERYTOKENIZESHARERECORDREWARDREQUEST.fields_by_name['owner_address']._options = None
    _QUERYTOKENIZESHARERECORDREWARDREQUEST.fields_by_name['owner_address']._serialized_options = b'\xf2\xde\x1f\x14yaml:"owner_address"'
    _QUERYTOKENIZESHARERECORDREWARDREQUEST._options = None
    _QUERYTOKENIZESHARERECORDREWARDREQUEST._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _QUERYTOKENIZESHARERECORDREWARDRESPONSE.fields_by_name['rewards']._options = None
    _QUERYTOKENIZESHARERECORDREWARDRESPONSE.fields_by_name['rewards']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYTOKENIZESHARERECORDREWARDRESPONSE.fields_by_name['total']._options = None
    _QUERYTOKENIZESHARERECORDREWARDRESPONSE.fields_by_name['total']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins'
    _QUERY.methods_by_name['Params']._options = None
    _QUERY.methods_by_name['Params']._serialized_options = b'\x82\xd3\xe4\x93\x02%\x12#/cosmos/distribution/v1beta1/params'
    _QUERY.methods_by_name['ValidatorOutstandingRewards']._options = None
    _QUERY.methods_by_name['ValidatorOutstandingRewards']._serialized_options = b'\x82\xd3\xe4\x93\x02Q\x12O/cosmos/distribution/v1beta1/validators/{validator_address}/outstanding_rewards'
    _QUERY.methods_by_name['ValidatorCommission']._options = None
    _QUERY.methods_by_name['ValidatorCommission']._serialized_options = b'\x82\xd3\xe4\x93\x02H\x12F/cosmos/distribution/v1beta1/validators/{validator_address}/commission'
    _QUERY.methods_by_name['ValidatorSlashes']._options = None
    _QUERY.methods_by_name['ValidatorSlashes']._serialized_options = b'\x82\xd3\xe4\x93\x02E\x12C/cosmos/distribution/v1beta1/validators/{validator_address}/slashes'
    _QUERY.methods_by_name['DelegationRewards']._options = None
    _QUERY.methods_by_name['DelegationRewards']._serialized_options = b'\x82\xd3\xe4\x93\x02Y\x12W/cosmos/distribution/v1beta1/delegators/{delegator_address}/rewards/{validator_address}'
    _QUERY.methods_by_name['DelegationTotalRewards']._options = None
    _QUERY.methods_by_name['DelegationTotalRewards']._serialized_options = b'\x82\xd3\xe4\x93\x02E\x12C/cosmos/distribution/v1beta1/delegators/{delegator_address}/rewards'
    _QUERY.methods_by_name['DelegatorValidators']._options = None
    _QUERY.methods_by_name['DelegatorValidators']._serialized_options = b'\x82\xd3\xe4\x93\x02H\x12F/cosmos/distribution/v1beta1/delegators/{delegator_address}/validators'
    _QUERY.methods_by_name['DelegatorWithdrawAddress']._options = None
    _QUERY.methods_by_name['DelegatorWithdrawAddress']._serialized_options = b'\x82\xd3\xe4\x93\x02N\x12L/cosmos/distribution/v1beta1/delegators/{delegator_address}/withdraw_address'
    _QUERY.methods_by_name['CommunityPool']._options = None
    _QUERY.methods_by_name['CommunityPool']._serialized_options = b'\x82\xd3\xe4\x93\x02-\x12+/cosmos/distribution/v1beta1/community_pool'
    _QUERY.methods_by_name['TokenizeShareRecordReward']._options = None
    _QUERY.methods_by_name['TokenizeShareRecordReward']._serialized_options = b'\x82\xd3\xe4\x93\x02L\x12J/cosmos/distribution/v1beta1/{owner_address}/tokenize_share_record_rewards'
    _globals['_QUERYPARAMSREQUEST']._serialized_start = 248
    _globals['_QUERYPARAMSREQUEST']._serialized_end = 268
    _globals['_QUERYPARAMSRESPONSE']._serialized_start = 270
    _globals['_QUERYPARAMSRESPONSE']._serialized_end = 350
    _globals['_QUERYVALIDATOROUTSTANDINGREWARDSREQUEST']._serialized_start = 352
    _globals['_QUERYVALIDATOROUTSTANDINGREWARDSREQUEST']._serialized_end = 420
    _globals['_QUERYVALIDATOROUTSTANDINGREWARDSRESPONSE']._serialized_start = 422
    _globals['_QUERYVALIDATOROUTSTANDINGREWARDSRESPONSE']._serialized_end = 545
    _globals['_QUERYVALIDATORCOMMISSIONREQUEST']._serialized_start = 547
    _globals['_QUERYVALIDATORCOMMISSIONREQUEST']._serialized_end = 607
    _globals['_QUERYVALIDATORCOMMISSIONRESPONSE']._serialized_start = 609
    _globals['_QUERYVALIDATORCOMMISSIONRESPONSE']._serialized_end = 730
    _globals['_QUERYVALIDATORSLASHESREQUEST']._serialized_start = 733
    _globals['_QUERYVALIDATORSLASHESREQUEST']._serialized_end = 908
    _globals['_QUERYVALIDATORSLASHESRESPONSE']._serialized_start = 911
    _globals['_QUERYVALIDATORSLASHESRESPONSE']._serialized_end = 1076
    _globals['_QUERYDELEGATIONREWARDSREQUEST']._serialized_start = 1078
    _globals['_QUERYDELEGATIONREWARDSREQUEST']._serialized_end = 1173
    _globals['_QUERYDELEGATIONREWARDSRESPONSE']._serialized_start = 1176
    _globals['_QUERYDELEGATIONREWARDSRESPONSE']._serialized_end = 1308
    _globals['_QUERYDELEGATIONTOTALREWARDSREQUEST']._serialized_start = 1310
    _globals['_QUERYDELEGATIONTOTALREWARDSREQUEST']._serialized_end = 1383
    _globals['_QUERYDELEGATIONTOTALREWARDSRESPONSE']._serialized_start = 1386
    _globals['_QUERYDELEGATIONTOTALREWARDSRESPONSE']._serialized_end = 1600
    _globals['_QUERYDELEGATORVALIDATORSREQUEST']._serialized_start = 1602
    _globals['_QUERYDELEGATORVALIDATORSREQUEST']._serialized_end = 1672
    _globals['_QUERYDELEGATORVALIDATORSRESPONSE']._serialized_start = 1674
    _globals['_QUERYDELEGATORVALIDATORSRESPONSE']._serialized_end = 1738
    _globals['_QUERYDELEGATORWITHDRAWADDRESSREQUEST']._serialized_start = 1740
    _globals['_QUERYDELEGATORWITHDRAWADDRESSREQUEST']._serialized_end = 1815
    _globals['_QUERYDELEGATORWITHDRAWADDRESSRESPONSE']._serialized_start = 1817
    _globals['_QUERYDELEGATORWITHDRAWADDRESSRESPONSE']._serialized_end = 1892
    _globals['_QUERYCOMMUNITYPOOLREQUEST']._serialized_start = 1894
    _globals['_QUERYCOMMUNITYPOOLREQUEST']._serialized_end = 1921
    _globals['_QUERYCOMMUNITYPOOLRESPONSE']._serialized_start = 1923
    _globals['_QUERYCOMMUNITYPOOLRESPONSE']._serialized_end = 2048
    _globals['_QUERYTOKENIZESHARERECORDREWARDREQUEST']._serialized_start = 2050
    _globals['_QUERYTOKENIZESHARERECORDREWARDREQUEST']._serialized_end = 2148
    _globals['_QUERYTOKENIZESHARERECORDREWARDRESPONSE']._serialized_start = 2151
    _globals['_QUERYTOKENIZESHARERECORDREWARDRESPONSE']._serialized_end = 2368
    _globals['_QUERY']._serialized_start = 2371
    _globals['_QUERY']._serialized_end = 4630