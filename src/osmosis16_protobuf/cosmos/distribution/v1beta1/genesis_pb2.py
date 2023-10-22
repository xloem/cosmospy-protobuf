"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....cosmos.distribution.v1beta1 import distribution_pb2 as cosmos_dot_distribution_dot_v1beta1_dot_distribution__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from ....amino import amino_pb2 as amino_dot_amino__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)cosmos/distribution/v1beta1/genesis.proto\x12\x1bcosmos.distribution.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a.cosmos/distribution/v1beta1/distribution.proto\x1a\x19cosmos_proto/cosmos.proto\x1a\x11amino/amino.proto"\x8a\x01\n\x15DelegatorWithdrawInfo\x123\n\x11delegator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x122\n\x10withdraw_address\x18\x02 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00"\xd7\x01\n!ValidatorOutstandingRewardsRecord\x123\n\x11validator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12s\n\x13outstanding_rewards\x18\x02 \x03(\x0b2\x1c.cosmos.base.v1beta1.DecCoinB8\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xa8\xe7\xb0*\x01:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00"\xc2\x01\n$ValidatorAccumulatedCommissionRecord\x123\n\x11validator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12[\n\x0baccumulated\x18\x02 \x01(\x0b2;.cosmos.distribution.v1beta1.ValidatorAccumulatedCommissionB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00"\xc6\x01\n ValidatorHistoricalRewardsRecord\x123\n\x11validator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12\x0e\n\x06period\x18\x02 \x01(\x04\x12S\n\x07rewards\x18\x03 \x01(\x0b27.cosmos.distribution.v1beta1.ValidatorHistoricalRewardsB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00"\xb0\x01\n\x1dValidatorCurrentRewardsRecord\x123\n\x11validator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12P\n\x07rewards\x18\x02 \x01(\x0b24.cosmos.distribution.v1beta1.ValidatorCurrentRewardsB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00"\xe7\x01\n\x1bDelegatorStartingInfoRecord\x123\n\x11delegator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x123\n\x11validator_address\x18\x02 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12T\n\rstarting_info\x18\x03 \x01(\x0b22.cosmos.distribution.v1beta1.DelegatorStartingInfoB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00"\xd6\x01\n\x19ValidatorSlashEventRecord\x123\n\x11validator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12\x0e\n\x06height\x18\x02 \x01(\x04\x12\x0e\n\x06period\x18\x03 \x01(\x04\x12Z\n\x15validator_slash_event\x18\x04 \x01(\x0b20.cosmos.distribution.v1beta1.ValidatorSlashEventB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00"\xb6\x07\n\x0cGenesisState\x12>\n\x06params\x18\x01 \x01(\x0b2#.cosmos.distribution.v1beta1.ParamsB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12A\n\x08fee_pool\x18\x02 \x01(\x0b2$.cosmos.distribution.v1beta1.FeePoolB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12_\n\x18delegator_withdraw_infos\x18\x03 \x03(\x0b22.cosmos.distribution.v1beta1.DelegatorWithdrawInfoB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x123\n\x11previous_proposer\x18\x04 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12f\n\x13outstanding_rewards\x18\x05 \x03(\x0b2>.cosmos.distribution.v1beta1.ValidatorOutstandingRewardsRecordB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12w\n!validator_accumulated_commissions\x18\x06 \x03(\x0b2A.cosmos.distribution.v1beta1.ValidatorAccumulatedCommissionRecordB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12n\n\x1cvalidator_historical_rewards\x18\x07 \x03(\x0b2=.cosmos.distribution.v1beta1.ValidatorHistoricalRewardsRecordB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12h\n\x19validator_current_rewards\x18\x08 \x03(\x0b2:.cosmos.distribution.v1beta1.ValidatorCurrentRewardsRecordB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12e\n\x18delegator_starting_infos\x18\t \x03(\x0b28.cosmos.distribution.v1beta1.DelegatorStartingInfoRecordB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12a\n\x16validator_slash_events\x18\n \x03(\x0b26.cosmos.distribution.v1beta1.ValidatorSlashEventRecordB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00B7Z1github.com/cosmos/cosmos-sdk/x/distribution/types\xa8\xe2\x1e\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.distribution.v1beta1.genesis_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z1github.com/cosmos/cosmos-sdk/x/distribution/types\xa8\xe2\x1e\x01'
    _DELEGATORWITHDRAWINFO.fields_by_name['delegator_address']._options = None
    _DELEGATORWITHDRAWINFO.fields_by_name['delegator_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _DELEGATORWITHDRAWINFO.fields_by_name['withdraw_address']._options = None
    _DELEGATORWITHDRAWINFO.fields_by_name['withdraw_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _DELEGATORWITHDRAWINFO._options = None
    _DELEGATORWITHDRAWINFO._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _VALIDATOROUTSTANDINGREWARDSRECORD.fields_by_name['validator_address']._options = None
    _VALIDATOROUTSTANDINGREWARDSRECORD.fields_by_name['validator_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _VALIDATOROUTSTANDINGREWARDSRECORD.fields_by_name['outstanding_rewards']._options = None
    _VALIDATOROUTSTANDINGREWARDSRECORD.fields_by_name['outstanding_rewards']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xa8\xe7\xb0*\x01'
    _VALIDATOROUTSTANDINGREWARDSRECORD._options = None
    _VALIDATOROUTSTANDINGREWARDSRECORD._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _VALIDATORACCUMULATEDCOMMISSIONRECORD.fields_by_name['validator_address']._options = None
    _VALIDATORACCUMULATEDCOMMISSIONRECORD.fields_by_name['validator_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _VALIDATORACCUMULATEDCOMMISSIONRECORD.fields_by_name['accumulated']._options = None
    _VALIDATORACCUMULATEDCOMMISSIONRECORD.fields_by_name['accumulated']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _VALIDATORACCUMULATEDCOMMISSIONRECORD._options = None
    _VALIDATORACCUMULATEDCOMMISSIONRECORD._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _VALIDATORHISTORICALREWARDSRECORD.fields_by_name['validator_address']._options = None
    _VALIDATORHISTORICALREWARDSRECORD.fields_by_name['validator_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _VALIDATORHISTORICALREWARDSRECORD.fields_by_name['rewards']._options = None
    _VALIDATORHISTORICALREWARDSRECORD.fields_by_name['rewards']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _VALIDATORHISTORICALREWARDSRECORD._options = None
    _VALIDATORHISTORICALREWARDSRECORD._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _VALIDATORCURRENTREWARDSRECORD.fields_by_name['validator_address']._options = None
    _VALIDATORCURRENTREWARDSRECORD.fields_by_name['validator_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _VALIDATORCURRENTREWARDSRECORD.fields_by_name['rewards']._options = None
    _VALIDATORCURRENTREWARDSRECORD.fields_by_name['rewards']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _VALIDATORCURRENTREWARDSRECORD._options = None
    _VALIDATORCURRENTREWARDSRECORD._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _DELEGATORSTARTINGINFORECORD.fields_by_name['delegator_address']._options = None
    _DELEGATORSTARTINGINFORECORD.fields_by_name['delegator_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _DELEGATORSTARTINGINFORECORD.fields_by_name['validator_address']._options = None
    _DELEGATORSTARTINGINFORECORD.fields_by_name['validator_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _DELEGATORSTARTINGINFORECORD.fields_by_name['starting_info']._options = None
    _DELEGATORSTARTINGINFORECORD.fields_by_name['starting_info']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _DELEGATORSTARTINGINFORECORD._options = None
    _DELEGATORSTARTINGINFORECORD._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _VALIDATORSLASHEVENTRECORD.fields_by_name['validator_address']._options = None
    _VALIDATORSLASHEVENTRECORD.fields_by_name['validator_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _VALIDATORSLASHEVENTRECORD.fields_by_name['validator_slash_event']._options = None
    _VALIDATORSLASHEVENTRECORD.fields_by_name['validator_slash_event']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _VALIDATORSLASHEVENTRECORD._options = None
    _VALIDATORSLASHEVENTRECORD._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _GENESISSTATE.fields_by_name['params']._options = None
    _GENESISSTATE.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _GENESISSTATE.fields_by_name['fee_pool']._options = None
    _GENESISSTATE.fields_by_name['fee_pool']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _GENESISSTATE.fields_by_name['delegator_withdraw_infos']._options = None
    _GENESISSTATE.fields_by_name['delegator_withdraw_infos']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _GENESISSTATE.fields_by_name['previous_proposer']._options = None
    _GENESISSTATE.fields_by_name['previous_proposer']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _GENESISSTATE.fields_by_name['outstanding_rewards']._options = None
    _GENESISSTATE.fields_by_name['outstanding_rewards']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _GENESISSTATE.fields_by_name['validator_accumulated_commissions']._options = None
    _GENESISSTATE.fields_by_name['validator_accumulated_commissions']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _GENESISSTATE.fields_by_name['validator_historical_rewards']._options = None
    _GENESISSTATE.fields_by_name['validator_historical_rewards']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _GENESISSTATE.fields_by_name['validator_current_rewards']._options = None
    _GENESISSTATE.fields_by_name['validator_current_rewards']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _GENESISSTATE.fields_by_name['delegator_starting_infos']._options = None
    _GENESISSTATE.fields_by_name['delegator_starting_infos']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _GENESISSTATE.fields_by_name['validator_slash_events']._options = None
    _GENESISSTATE.fields_by_name['validator_slash_events']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _GENESISSTATE._options = None
    _GENESISSTATE._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _globals['_DELEGATORWITHDRAWINFO']._serialized_start = 223
    _globals['_DELEGATORWITHDRAWINFO']._serialized_end = 361
    _globals['_VALIDATOROUTSTANDINGREWARDSRECORD']._serialized_start = 364
    _globals['_VALIDATOROUTSTANDINGREWARDSRECORD']._serialized_end = 579
    _globals['_VALIDATORACCUMULATEDCOMMISSIONRECORD']._serialized_start = 582
    _globals['_VALIDATORACCUMULATEDCOMMISSIONRECORD']._serialized_end = 776
    _globals['_VALIDATORHISTORICALREWARDSRECORD']._serialized_start = 779
    _globals['_VALIDATORHISTORICALREWARDSRECORD']._serialized_end = 977
    _globals['_VALIDATORCURRENTREWARDSRECORD']._serialized_start = 980
    _globals['_VALIDATORCURRENTREWARDSRECORD']._serialized_end = 1156
    _globals['_DELEGATORSTARTINGINFORECORD']._serialized_start = 1159
    _globals['_DELEGATORSTARTINGINFORECORD']._serialized_end = 1390
    _globals['_VALIDATORSLASHEVENTRECORD']._serialized_start = 1393
    _globals['_VALIDATORSLASHEVENTRECORD']._serialized_end = 1607
    _globals['_GENESISSTATE']._serialized_start = 1610
    _globals['_GENESISSTATE']._serialized_end = 2560