"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from ....cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n cosmos/feegrant/v1beta1/tx.proto\x12\x17cosmos.feegrant.v1beta1\x1a\x19google/protobuf/any.proto\x1a\x19cosmos_proto/cosmos.proto\x1a\x17cosmos/msg/v1/msg.proto"\xb3\x01\n\x11MsgGrantAllowance\x12)\n\x07granter\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12)\n\x07grantee\x18\x02 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12:\n\tallowance\x18\x03 \x01(\x0b2\x14.google.protobuf.AnyB\x11\xca\xb4-\rFeeAllowanceI:\x0c\x82\xe7\xb0*\x07granter"\x1b\n\x19MsgGrantAllowanceResponse"x\n\x12MsgRevokeAllowance\x12)\n\x07granter\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12)\n\x07grantee\x18\x02 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString:\x0c\x82\xe7\xb0*\x07granter"\x1c\n\x1aMsgRevokeAllowanceResponse2\xec\x01\n\x03Msg\x12p\n\x0eGrantAllowance\x12*.cosmos.feegrant.v1beta1.MsgGrantAllowance\x1a2.cosmos.feegrant.v1beta1.MsgGrantAllowanceResponse\x12s\n\x0fRevokeAllowance\x12+.cosmos.feegrant.v1beta1.MsgRevokeAllowance\x1a3.cosmos.feegrant.v1beta1.MsgRevokeAllowanceResponseB)Z\'github.com/cosmos/cosmos-sdk/x/feegrantb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.feegrant.v1beta1.tx_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"Z'github.com/cosmos/cosmos-sdk/x/feegrant"
    _MSGGRANTALLOWANCE.fields_by_name['granter']._options = None
    _MSGGRANTALLOWANCE.fields_by_name['granter']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGGRANTALLOWANCE.fields_by_name['grantee']._options = None
    _MSGGRANTALLOWANCE.fields_by_name['grantee']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGGRANTALLOWANCE.fields_by_name['allowance']._options = None
    _MSGGRANTALLOWANCE.fields_by_name['allowance']._serialized_options = b'\xca\xb4-\rFeeAllowanceI'
    _MSGGRANTALLOWANCE._options = None
    _MSGGRANTALLOWANCE._serialized_options = b'\x82\xe7\xb0*\x07granter'
    _MSGREVOKEALLOWANCE.fields_by_name['granter']._options = None
    _MSGREVOKEALLOWANCE.fields_by_name['granter']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGREVOKEALLOWANCE.fields_by_name['grantee']._options = None
    _MSGREVOKEALLOWANCE.fields_by_name['grantee']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGREVOKEALLOWANCE._options = None
    _MSGREVOKEALLOWANCE._serialized_options = b'\x82\xe7\xb0*\x07granter'
    _globals['_MSGGRANTALLOWANCE']._serialized_start = 141
    _globals['_MSGGRANTALLOWANCE']._serialized_end = 320
    _globals['_MSGGRANTALLOWANCERESPONSE']._serialized_start = 322
    _globals['_MSGGRANTALLOWANCERESPONSE']._serialized_end = 349
    _globals['_MSGREVOKEALLOWANCE']._serialized_start = 351
    _globals['_MSGREVOKEALLOWANCE']._serialized_end = 471
    _globals['_MSGREVOKEALLOWANCERESPONSE']._serialized_start = 473
    _globals['_MSGREVOKEALLOWANCERESPONSE']._serialized_end = 501
    _globals['_MSG']._serialized_start = 504
    _globals['_MSG']._serialized_end = 740