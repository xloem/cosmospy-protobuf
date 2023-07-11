"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.cosmos/distribution/v1beta1/distribution.proto\x12\x1bcosmos.distribution.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a\x19cosmos_proto/cosmos.proto"\xbb\x02\n\x06Params\x12S\n\rcommunity_tax\x18\x01 \x01(\tB<\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xd2\xb4-\ncosmos.Dec\x12Z\n\x14base_proposer_reward\x18\x02 \x01(\tB<\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xd2\xb4-\ncosmos.Dec\x12[\n\x15bonus_proposer_reward\x18\x03 \x01(\tB<\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xd2\xb4-\ncosmos.Dec\x12\x1d\n\x15withdraw_addr_enabled\x18\x04 \x01(\x08:\x04\x98\xa0\x1f\x00"\xa9\x01\n\x1aValidatorHistoricalRewards\x12r\n\x17cumulative_reward_ratio\x18\x01 \x03(\x0b2\x1c.cosmos.base.v1beta1.DecCoinB3\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\x12\x17\n\x0freference_count\x18\x02 \x01(\r"\x8d\x01\n\x17ValidatorCurrentRewards\x12b\n\x07rewards\x18\x01 \x03(\x0b2\x1c.cosmos.base.v1beta1.DecCoinB3\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\x12\x0e\n\x06period\x18\x02 \x01(\x04"\x87\x01\n\x1eValidatorAccumulatedCommission\x12e\n\ncommission\x18\x01 \x03(\x0b2\x1c.cosmos.base.v1beta1.DecCoinB3\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins"\x81\x01\n\x1bValidatorOutstandingRewards\x12b\n\x07rewards\x18\x01 \x03(\x0b2\x1c.cosmos.base.v1beta1.DecCoinB3\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins"\x7f\n\x13ValidatorSlashEvent\x12\x18\n\x10validator_period\x18\x01 \x01(\x04\x12N\n\x08fraction\x18\x02 \x01(\tB<\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xd2\xb4-\ncosmos.Dec"t\n\x14ValidatorSlashEvents\x12V\n\x16validator_slash_events\x18\x01 \x03(\x0b20.cosmos.distribution.v1beta1.ValidatorSlashEventB\x04\xc8\xde\x1f\x00:\x04\x98\xa0\x1f\x00"t\n\x07FeePool\x12i\n\x0ecommunity_pool\x18\x01 \x03(\x0b2\x1c.cosmos.base.v1beta1.DecCoinB3\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins"\xdc\x01\n\x1aCommunityPoolSpendProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12\x11\n\trecipient\x18\x03 \x01(\t\x12[\n\x06amount\x18\x04 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins:*\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xe8\xa0\x1f\x00\xca\xb4-\x1acosmos.gov.v1beta1.Content"\xa2\x01\n\x15DelegatorStartingInfo\x12\x17\n\x0fprevious_period\x18\x01 \x01(\x04\x12K\n\x05stake\x18\x02 \x01(\tB<\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xd2\xb4-\ncosmos.Dec\x12#\n\x06height\x18\x03 \x01(\x04B\x13\xea\xde\x1f\x0fcreation_height"\xbd\x01\n\x19DelegationDelegatorReward\x123\n\x11validator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12a\n\x06reward\x18\x02 \x03(\x0b2\x1c.cosmos.base.v1beta1.DecCoinB3\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins:\x08\x88\xa0\x1f\x00\x98\xa0\x1f\x01"\xa7\x01\n%CommunityPoolSpendProposalWithDeposit\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12\x11\n\trecipient\x18\x03 \x01(\t\x12\x0e\n\x06amount\x18\x04 \x01(\t\x12\x0f\n\x07deposit\x18\x05 \x01(\t:&\x88\xa0\x1f\x00\x98\xa0\x1f\x01\xca\xb4-\x1acosmos.gov.v1beta1.ContentB7Z1github.com/cosmos/cosmos-sdk/x/distribution/types\xa8\xe2\x1e\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.distribution.v1beta1.distribution_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z1github.com/cosmos/cosmos-sdk/x/distribution/types\xa8\xe2\x1e\x01'
    _PARAMS.fields_by_name['community_tax']._options = None
    _PARAMS.fields_by_name['community_tax']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xd2\xb4-\ncosmos.Dec'
    _PARAMS.fields_by_name['base_proposer_reward']._options = None
    _PARAMS.fields_by_name['base_proposer_reward']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xd2\xb4-\ncosmos.Dec'
    _PARAMS.fields_by_name['bonus_proposer_reward']._options = None
    _PARAMS.fields_by_name['bonus_proposer_reward']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xd2\xb4-\ncosmos.Dec'
    _PARAMS._options = None
    _PARAMS._serialized_options = b'\x98\xa0\x1f\x00'
    _VALIDATORHISTORICALREWARDS.fields_by_name['cumulative_reward_ratio']._options = None
    _VALIDATORHISTORICALREWARDS.fields_by_name['cumulative_reward_ratio']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins'
    _VALIDATORCURRENTREWARDS.fields_by_name['rewards']._options = None
    _VALIDATORCURRENTREWARDS.fields_by_name['rewards']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins'
    _VALIDATORACCUMULATEDCOMMISSION.fields_by_name['commission']._options = None
    _VALIDATORACCUMULATEDCOMMISSION.fields_by_name['commission']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins'
    _VALIDATOROUTSTANDINGREWARDS.fields_by_name['rewards']._options = None
    _VALIDATOROUTSTANDINGREWARDS.fields_by_name['rewards']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins'
    _VALIDATORSLASHEVENT.fields_by_name['fraction']._options = None
    _VALIDATORSLASHEVENT.fields_by_name['fraction']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xd2\xb4-\ncosmos.Dec'
    _VALIDATORSLASHEVENTS.fields_by_name['validator_slash_events']._options = None
    _VALIDATORSLASHEVENTS.fields_by_name['validator_slash_events']._serialized_options = b'\xc8\xde\x1f\x00'
    _VALIDATORSLASHEVENTS._options = None
    _VALIDATORSLASHEVENTS._serialized_options = b'\x98\xa0\x1f\x00'
    _FEEPOOL.fields_by_name['community_pool']._options = None
    _FEEPOOL.fields_by_name['community_pool']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins'
    _COMMUNITYPOOLSPENDPROPOSAL.fields_by_name['amount']._options = None
    _COMMUNITYPOOLSPENDPROPOSAL.fields_by_name['amount']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _COMMUNITYPOOLSPENDPROPOSAL._options = None
    _COMMUNITYPOOLSPENDPROPOSAL._serialized_options = b'\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xe8\xa0\x1f\x00\xca\xb4-\x1acosmos.gov.v1beta1.Content'
    _DELEGATORSTARTINGINFO.fields_by_name['stake']._options = None
    _DELEGATORSTARTINGINFO.fields_by_name['stake']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xd2\xb4-\ncosmos.Dec'
    _DELEGATORSTARTINGINFO.fields_by_name['height']._options = None
    _DELEGATORSTARTINGINFO.fields_by_name['height']._serialized_options = b'\xea\xde\x1f\x0fcreation_height'
    _DELEGATIONDELEGATORREWARD.fields_by_name['validator_address']._options = None
    _DELEGATIONDELEGATORREWARD.fields_by_name['validator_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _DELEGATIONDELEGATORREWARD.fields_by_name['reward']._options = None
    _DELEGATIONDELEGATORREWARD.fields_by_name['reward']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins'
    _DELEGATIONDELEGATORREWARD._options = None
    _DELEGATIONDELEGATORREWARD._serialized_options = b'\x88\xa0\x1f\x00\x98\xa0\x1f\x01'
    _COMMUNITYPOOLSPENDPROPOSALWITHDEPOSIT._options = None
    _COMMUNITYPOOLSPENDPROPOSALWITHDEPOSIT._serialized_options = b'\x88\xa0\x1f\x00\x98\xa0\x1f\x01\xca\xb4-\x1acosmos.gov.v1beta1.Content'
    _globals['_PARAMS']._serialized_start = 161
    _globals['_PARAMS']._serialized_end = 476
    _globals['_VALIDATORHISTORICALREWARDS']._serialized_start = 479
    _globals['_VALIDATORHISTORICALREWARDS']._serialized_end = 648
    _globals['_VALIDATORCURRENTREWARDS']._serialized_start = 651
    _globals['_VALIDATORCURRENTREWARDS']._serialized_end = 792
    _globals['_VALIDATORACCUMULATEDCOMMISSION']._serialized_start = 795
    _globals['_VALIDATORACCUMULATEDCOMMISSION']._serialized_end = 930
    _globals['_VALIDATOROUTSTANDINGREWARDS']._serialized_start = 933
    _globals['_VALIDATOROUTSTANDINGREWARDS']._serialized_end = 1062
    _globals['_VALIDATORSLASHEVENT']._serialized_start = 1064
    _globals['_VALIDATORSLASHEVENT']._serialized_end = 1191
    _globals['_VALIDATORSLASHEVENTS']._serialized_start = 1193
    _globals['_VALIDATORSLASHEVENTS']._serialized_end = 1309
    _globals['_FEEPOOL']._serialized_start = 1311
    _globals['_FEEPOOL']._serialized_end = 1427
    _globals['_COMMUNITYPOOLSPENDPROPOSAL']._serialized_start = 1430
    _globals['_COMMUNITYPOOLSPENDPROPOSAL']._serialized_end = 1650
    _globals['_DELEGATORSTARTINGINFO']._serialized_start = 1653
    _globals['_DELEGATORSTARTINGINFO']._serialized_end = 1815
    _globals['_DELEGATIONDELEGATORREWARD']._serialized_start = 1818
    _globals['_DELEGATIONDELEGATORREWARD']._serialized_end = 2007
    _globals['_COMMUNITYPOOLSPENDPROPOSALWITHDEPOSIT']._serialized_start = 2010
    _globals['_COMMUNITYPOOLSPENDPROPOSALWITHDEPOSIT']._serialized_end = 2177