"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$evmos/incentives/v1/incentives.proto\x12\x13evmos.incentives.v1\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a\x14gogoproto/gogo.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xe2\x01\n\tIncentive\x12\x10\n\x08contract\x18\x01 \x01(\t\x12f\n\x0ballocations\x18\x02 \x03(\x0b2\x1c.cosmos.base.v1beta1.DecCoinB3\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\x12\x0e\n\x06epochs\x18\x03 \x01(\r\x128\n\nstart_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01\x12\x11\n\ttotal_gas\x18\x05 \x01(\x04"I\n\x08GasMeter\x12\x10\n\x08contract\x18\x01 \x01(\t\x12\x13\n\x0bparticipant\x18\x02 \x01(\t\x12\x16\n\x0ecumulative_gas\x18\x03 \x01(\x04"\xcf\x01\n\x19RegisterIncentiveProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12\x10\n\x08contract\x18\x03 \x01(\t\x12f\n\x0ballocations\x18\x04 \x03(\x0b2\x1c.cosmos.base.v1beta1.DecCoinB3\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\x12\x0e\n\x06epochs\x18\x05 \x01(\r:\x04\xe8\xa0\x1f\x00"U\n\x17CancelIncentiveProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12\x10\n\x08contract\x18\x03 \x01(\t:\x04\xe8\xa0\x1f\x00B/Z-github.com/evmos/evmos/v13/x/incentives/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'evmos.incentives.v1.incentives_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z-github.com/evmos/evmos/v13/x/incentives/types'
    _INCENTIVE.fields_by_name['allocations']._options = None
    _INCENTIVE.fields_by_name['allocations']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins'
    _INCENTIVE.fields_by_name['start_time']._options = None
    _INCENTIVE.fields_by_name['start_time']._serialized_options = b'\xc8\xde\x1f\x00\x90\xdf\x1f\x01'
    _REGISTERINCENTIVEPROPOSAL.fields_by_name['allocations']._options = None
    _REGISTERINCENTIVEPROPOSAL.fields_by_name['allocations']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins'
    _REGISTERINCENTIVEPROPOSAL._options = None
    _REGISTERINCENTIVEPROPOSAL._serialized_options = b'\xe8\xa0\x1f\x00'
    _CANCELINCENTIVEPROPOSAL._options = None
    _CANCELINCENTIVEPROPOSAL._serialized_options = b'\xe8\xa0\x1f\x00'
    _globals['_INCENTIVE']._serialized_start = 149
    _globals['_INCENTIVE']._serialized_end = 375
    _globals['_GASMETER']._serialized_start = 377
    _globals['_GASMETER']._serialized_end = 450
    _globals['_REGISTERINCENTIVEPROPOSAL']._serialized_start = 453
    _globals['_REGISTERINCENTIVEPROPOSAL']._serialized_end = 660
    _globals['_CANCELINCENTIVEPROPOSAL']._serialized_start = 662
    _globals['_CANCELINCENTIVEPROPOSAL']._serialized_end = 747