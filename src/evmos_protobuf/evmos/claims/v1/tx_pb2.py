"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from ....evmos.claims.v1 import genesis_pb2 as evmos_dot_claims_dot_v1_dot_genesis__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18evmos/claims/v1/tx.proto\x12\x0fevmos.claims.v1\x1a\x17cosmos/msg/v1/msg.proto\x1a\x19cosmos_proto/cosmos.proto\x1a\x1devmos/claims/v1/genesis.proto\x1a\x14gogoproto/gogo.proto"}\n\x0fMsgUpdateParams\x12+\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12-\n\x06params\x18\x02 \x01(\x0b2\x17.evmos.claims.v1.ParamsB\x04\xc8\xde\x1f\x00:\x0e\x82\xe7\xb0*\tauthority"\x19\n\x17MsgUpdateParamsResponse2a\n\x03Msg\x12Z\n\x0cUpdateParams\x12 .evmos.claims.v1.MsgUpdateParams\x1a(.evmos.claims.v1.MsgUpdateParamsResponseB+Z)github.com/evmos/evmos/v13/x/claims/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'evmos.claims.v1.tx_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z)github.com/evmos/evmos/v13/x/claims/types'
    _MSGUPDATEPARAMS.fields_by_name['authority']._options = None
    _MSGUPDATEPARAMS.fields_by_name['authority']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGUPDATEPARAMS.fields_by_name['params']._options = None
    _MSGUPDATEPARAMS.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _MSGUPDATEPARAMS._options = None
    _MSGUPDATEPARAMS._serialized_options = b'\x82\xe7\xb0*\tauthority'
    _globals['_MSGUPDATEPARAMS']._serialized_start = 150
    _globals['_MSGUPDATEPARAMS']._serialized_end = 275
    _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_start = 277
    _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_end = 302
    _globals['_MSG']._serialized_start = 304
    _globals['_MSG']._serialized_end = 401