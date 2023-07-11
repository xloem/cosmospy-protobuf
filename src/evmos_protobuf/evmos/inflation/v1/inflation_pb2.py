"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"evmos/inflation/v1/inflation.proto\x12\x12evmos.inflation.v1\x1a\x14gogoproto/gogo.proto"\xf2\x01\n\x15InflationDistribution\x12G\n\x0fstaking_rewards\x18\x01 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\x12H\n\x10usage_incentives\x18\x02 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\x12F\n\x0ecommunity_pool\x18\x03 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec"\xd7\x02\n\x16ExponentialCalculation\x129\n\x01a\x18\x01 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\x129\n\x01r\x18\x02 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\x129\n\x01c\x18\x03 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\x12F\n\x0ebonding_target\x18\x04 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\x12D\n\x0cmax_variance\x18\x05 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.DecB.Z,github.com/evmos/evmos/v13/x/inflation/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'evmos.inflation.v1.inflation_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z,github.com/evmos/evmos/v13/x/inflation/types'
    _INFLATIONDISTRIBUTION.fields_by_name['staking_rewards']._options = None
    _INFLATIONDISTRIBUTION.fields_by_name['staking_rewards']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec'
    _INFLATIONDISTRIBUTION.fields_by_name['usage_incentives']._options = None
    _INFLATIONDISTRIBUTION.fields_by_name['usage_incentives']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec'
    _INFLATIONDISTRIBUTION.fields_by_name['community_pool']._options = None
    _INFLATIONDISTRIBUTION.fields_by_name['community_pool']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec'
    _EXPONENTIALCALCULATION.fields_by_name['a']._options = None
    _EXPONENTIALCALCULATION.fields_by_name['a']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec'
    _EXPONENTIALCALCULATION.fields_by_name['r']._options = None
    _EXPONENTIALCALCULATION.fields_by_name['r']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec'
    _EXPONENTIALCALCULATION.fields_by_name['c']._options = None
    _EXPONENTIALCALCULATION.fields_by_name['c']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec'
    _EXPONENTIALCALCULATION.fields_by_name['bonding_target']._options = None
    _EXPONENTIALCALCULATION.fields_by_name['bonding_target']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec'
    _EXPONENTIALCALCULATION.fields_by_name['max_variance']._options = None
    _EXPONENTIALCALCULATION.fields_by_name['max_variance']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec'
    _globals['_INFLATIONDISTRIBUTION']._serialized_start = 81
    _globals['_INFLATIONDISTRIBUTION']._serialized_end = 323
    _globals['_EXPONENTIALCALCULATION']._serialized_start = 326
    _globals['_EXPONENTIALCALCULATION']._serialized_end = 669