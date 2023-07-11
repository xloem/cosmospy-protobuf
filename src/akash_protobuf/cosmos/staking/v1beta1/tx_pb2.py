"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....cosmos.staking.v1beta1 import staking_pb2 as cosmos_dot_staking_dot_v1beta1_dot_staking__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fcosmos/staking/v1beta1/tx.proto\x12\x16cosmos.staking.v1beta1\x1a\x19google/protobuf/any.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x14gogoproto/gogo.proto\x1a\x19cosmos_proto/cosmos.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a$cosmos/staking/v1beta1/staking.proto"\xee\x03\n\x12MsgCreateValidator\x12>\n\x0bdescription\x18\x01 \x01(\x0b2#.cosmos.staking.v1beta1.DescriptionB\x04\xc8\xde\x1f\x00\x12A\n\ncommission\x18\x02 \x01(\x0b2\'.cosmos.staking.v1beta1.CommissionRatesB\x04\xc8\xde\x1f\x00\x12i\n\x13min_self_delegation\x18\x03 \x01(\tBL\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x1ayaml:"min_self_delegation"\x127\n\x11delegator_address\x18\x04 \x01(\tB\x1c\xf2\xde\x1f\x18yaml:"delegator_address"\x127\n\x11validator_address\x18\x05 \x01(\tB\x1c\xf2\xde\x1f\x18yaml:"validator_address"\x12>\n\x06pubkey\x18\x06 \x01(\x0b2\x14.google.protobuf.AnyB\x18\xca\xb4-\x14cosmos.crypto.PubKey\x12.\n\x05value\x18\x07 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00"\x1c\n\x1aMsgCreateValidatorResponse"\xd1\x02\n\x10MsgEditValidator\x12>\n\x0bdescription\x18\x01 \x01(\x0b2#.cosmos.staking.v1beta1.DescriptionB\x04\xc8\xde\x1f\x00\x12-\n\x11validator_address\x18\x02 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:"address"\x12]\n\x0fcommission_rate\x18\x03 \x01(\tBD\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f\x16yaml:"commission_rate"\x12e\n\x13min_self_delegation\x18\x04 \x01(\tBH\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x1ayaml:"min_self_delegation":\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00"\x1a\n\x18MsgEditValidatorResponse"\xb6\x01\n\x0bMsgDelegate\x127\n\x11delegator_address\x18\x01 \x01(\tB\x1c\xf2\xde\x1f\x18yaml:"delegator_address"\x127\n\x11validator_address\x18\x02 \x01(\tB\x1c\xf2\xde\x1f\x18yaml:"validator_address"\x12/\n\x06amount\x18\x03 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00:\x04\xe8\xa0\x1f\x00"\x15\n\x13MsgDelegateResponse"\x86\x02\n\x12MsgBeginRedelegate\x127\n\x11delegator_address\x18\x01 \x01(\tB\x1c\xf2\xde\x1f\x18yaml:"delegator_address"\x12?\n\x15validator_src_address\x18\x02 \x01(\tB \xf2\xde\x1f\x1cyaml:"validator_src_address"\x12?\n\x15validator_dst_address\x18\x03 \x01(\tB \xf2\xde\x1f\x1cyaml:"validator_dst_address"\x12/\n\x06amount\x18\x04 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00:\x04\xe8\xa0\x1f\x00"[\n\x1aMsgBeginRedelegateResponse\x12=\n\x0fcompletion_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01"\xb8\x01\n\rMsgUndelegate\x127\n\x11delegator_address\x18\x01 \x01(\tB\x1c\xf2\xde\x1f\x18yaml:"delegator_address"\x127\n\x11validator_address\x18\x02 \x01(\tB\x1c\xf2\xde\x1f\x18yaml:"validator_address"\x12/\n\x06amount\x18\x03 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00:\x04\xe8\xa0\x1f\x00"V\n\x15MsgUndelegateResponse\x12=\n\x0fcompletion_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x012\x9a\x04\n\x03Msg\x12q\n\x0fCreateValidator\x12*.cosmos.staking.v1beta1.MsgCreateValidator\x1a2.cosmos.staking.v1beta1.MsgCreateValidatorResponse\x12k\n\rEditValidator\x12(.cosmos.staking.v1beta1.MsgEditValidator\x1a0.cosmos.staking.v1beta1.MsgEditValidatorResponse\x12\\\n\x08Delegate\x12#.cosmos.staking.v1beta1.MsgDelegate\x1a+.cosmos.staking.v1beta1.MsgDelegateResponse\x12q\n\x0fBeginRedelegate\x12*.cosmos.staking.v1beta1.MsgBeginRedelegate\x1a2.cosmos.staking.v1beta1.MsgBeginRedelegateResponse\x12b\n\nUndelegate\x12%.cosmos.staking.v1beta1.MsgUndelegate\x1a-.cosmos.staking.v1beta1.MsgUndelegateResponseB.Z,github.com/cosmos/cosmos-sdk/x/staking/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.staking.v1beta1.tx_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z,github.com/cosmos/cosmos-sdk/x/staking/types'
    _MSGCREATEVALIDATOR.fields_by_name['description']._options = None
    _MSGCREATEVALIDATOR.fields_by_name['description']._serialized_options = b'\xc8\xde\x1f\x00'
    _MSGCREATEVALIDATOR.fields_by_name['commission']._options = None
    _MSGCREATEVALIDATOR.fields_by_name['commission']._serialized_options = b'\xc8\xde\x1f\x00'
    _MSGCREATEVALIDATOR.fields_by_name['min_self_delegation']._options = None
    _MSGCREATEVALIDATOR.fields_by_name['min_self_delegation']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x1ayaml:"min_self_delegation"'
    _MSGCREATEVALIDATOR.fields_by_name['delegator_address']._options = None
    _MSGCREATEVALIDATOR.fields_by_name['delegator_address']._serialized_options = b'\xf2\xde\x1f\x18yaml:"delegator_address"'
    _MSGCREATEVALIDATOR.fields_by_name['validator_address']._options = None
    _MSGCREATEVALIDATOR.fields_by_name['validator_address']._serialized_options = b'\xf2\xde\x1f\x18yaml:"validator_address"'
    _MSGCREATEVALIDATOR.fields_by_name['pubkey']._options = None
    _MSGCREATEVALIDATOR.fields_by_name['pubkey']._serialized_options = b'\xca\xb4-\x14cosmos.crypto.PubKey'
    _MSGCREATEVALIDATOR.fields_by_name['value']._options = None
    _MSGCREATEVALIDATOR.fields_by_name['value']._serialized_options = b'\xc8\xde\x1f\x00'
    _MSGCREATEVALIDATOR._options = None
    _MSGCREATEVALIDATOR._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _MSGEDITVALIDATOR.fields_by_name['description']._options = None
    _MSGEDITVALIDATOR.fields_by_name['description']._serialized_options = b'\xc8\xde\x1f\x00'
    _MSGEDITVALIDATOR.fields_by_name['validator_address']._options = None
    _MSGEDITVALIDATOR.fields_by_name['validator_address']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"address"'
    _MSGEDITVALIDATOR.fields_by_name['commission_rate']._options = None
    _MSGEDITVALIDATOR.fields_by_name['commission_rate']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f\x16yaml:"commission_rate"'
    _MSGEDITVALIDATOR.fields_by_name['min_self_delegation']._options = None
    _MSGEDITVALIDATOR.fields_by_name['min_self_delegation']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x1ayaml:"min_self_delegation"'
    _MSGEDITVALIDATOR._options = None
    _MSGEDITVALIDATOR._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _MSGDELEGATE.fields_by_name['delegator_address']._options = None
    _MSGDELEGATE.fields_by_name['delegator_address']._serialized_options = b'\xf2\xde\x1f\x18yaml:"delegator_address"'
    _MSGDELEGATE.fields_by_name['validator_address']._options = None
    _MSGDELEGATE.fields_by_name['validator_address']._serialized_options = b'\xf2\xde\x1f\x18yaml:"validator_address"'
    _MSGDELEGATE.fields_by_name['amount']._options = None
    _MSGDELEGATE.fields_by_name['amount']._serialized_options = b'\xc8\xde\x1f\x00'
    _MSGDELEGATE._options = None
    _MSGDELEGATE._serialized_options = b'\xe8\xa0\x1f\x00'
    _MSGBEGINREDELEGATE.fields_by_name['delegator_address']._options = None
    _MSGBEGINREDELEGATE.fields_by_name['delegator_address']._serialized_options = b'\xf2\xde\x1f\x18yaml:"delegator_address"'
    _MSGBEGINREDELEGATE.fields_by_name['validator_src_address']._options = None
    _MSGBEGINREDELEGATE.fields_by_name['validator_src_address']._serialized_options = b'\xf2\xde\x1f\x1cyaml:"validator_src_address"'
    _MSGBEGINREDELEGATE.fields_by_name['validator_dst_address']._options = None
    _MSGBEGINREDELEGATE.fields_by_name['validator_dst_address']._serialized_options = b'\xf2\xde\x1f\x1cyaml:"validator_dst_address"'
    _MSGBEGINREDELEGATE.fields_by_name['amount']._options = None
    _MSGBEGINREDELEGATE.fields_by_name['amount']._serialized_options = b'\xc8\xde\x1f\x00'
    _MSGBEGINREDELEGATE._options = None
    _MSGBEGINREDELEGATE._serialized_options = b'\xe8\xa0\x1f\x00'
    _MSGBEGINREDELEGATERESPONSE.fields_by_name['completion_time']._options = None
    _MSGBEGINREDELEGATERESPONSE.fields_by_name['completion_time']._serialized_options = b'\xc8\xde\x1f\x00\x90\xdf\x1f\x01'
    _MSGUNDELEGATE.fields_by_name['delegator_address']._options = None
    _MSGUNDELEGATE.fields_by_name['delegator_address']._serialized_options = b'\xf2\xde\x1f\x18yaml:"delegator_address"'
    _MSGUNDELEGATE.fields_by_name['validator_address']._options = None
    _MSGUNDELEGATE.fields_by_name['validator_address']._serialized_options = b'\xf2\xde\x1f\x18yaml:"validator_address"'
    _MSGUNDELEGATE.fields_by_name['amount']._options = None
    _MSGUNDELEGATE.fields_by_name['amount']._serialized_options = b'\xc8\xde\x1f\x00'
    _MSGUNDELEGATE._options = None
    _MSGUNDELEGATE._serialized_options = b'\xe8\xa0\x1f\x00'
    _MSGUNDELEGATERESPONSE.fields_by_name['completion_time']._options = None
    _MSGUNDELEGATERESPONSE.fields_by_name['completion_time']._serialized_options = b'\xc8\xde\x1f\x00\x90\xdf\x1f\x01'
    _globals['_MSGCREATEVALIDATOR']._serialized_start = 239
    _globals['_MSGCREATEVALIDATOR']._serialized_end = 733
    _globals['_MSGCREATEVALIDATORRESPONSE']._serialized_start = 735
    _globals['_MSGCREATEVALIDATORRESPONSE']._serialized_end = 763
    _globals['_MSGEDITVALIDATOR']._serialized_start = 766
    _globals['_MSGEDITVALIDATOR']._serialized_end = 1103
    _globals['_MSGEDITVALIDATORRESPONSE']._serialized_start = 1105
    _globals['_MSGEDITVALIDATORRESPONSE']._serialized_end = 1131
    _globals['_MSGDELEGATE']._serialized_start = 1134
    _globals['_MSGDELEGATE']._serialized_end = 1316
    _globals['_MSGDELEGATERESPONSE']._serialized_start = 1318
    _globals['_MSGDELEGATERESPONSE']._serialized_end = 1339
    _globals['_MSGBEGINREDELEGATE']._serialized_start = 1342
    _globals['_MSGBEGINREDELEGATE']._serialized_end = 1604
    _globals['_MSGBEGINREDELEGATERESPONSE']._serialized_start = 1606
    _globals['_MSGBEGINREDELEGATERESPONSE']._serialized_end = 1697
    _globals['_MSGUNDELEGATE']._serialized_start = 1700
    _globals['_MSGUNDELEGATE']._serialized_end = 1884
    _globals['_MSGUNDELEGATERESPONSE']._serialized_start = 1886
    _globals['_MSGUNDELEGATERESPONSE']._serialized_end = 1972
    _globals['_MSG']._serialized_start = 1975
    _globals['_MSG']._serialized_end = 2513