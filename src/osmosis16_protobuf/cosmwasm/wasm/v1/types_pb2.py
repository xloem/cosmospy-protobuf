"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1ccosmwasm/wasm/v1/types.proto\x12\x10cosmwasm.wasm.v1\x1a\x19cosmos_proto/cosmos.proto\x1a\x14gogoproto/gogo.proto\x1a\x19google/protobuf/any.proto"V\n\x0fAccessTypeParam\x12=\n\x05value\x18\x01 \x01(\x0e2\x1c.cosmwasm.wasm.v1.AccessTypeB\x10\xf2\xde\x1f\x0cyaml:"value":\x04\x98\xa0\x1f\x01"\xab\x01\n\x0cAccessConfig\x12G\n\npermission\x18\x01 \x01(\x0e2\x1c.cosmwasm.wasm.v1.AccessTypeB\x15\xf2\xde\x1f\x11yaml:"permission"\x12#\n\x07address\x18\x02 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:"address"\x12\'\n\taddresses\x18\x03 \x03(\tB\x14\xf2\xde\x1f\x10yaml:"addresses":\x04\x98\xa0\x1f\x01"\xde\x01\n\x06Params\x12]\n\x12code_upload_access\x18\x01 \x01(\x0b2\x1e.cosmwasm.wasm.v1.AccessConfigB!\xc8\xde\x1f\x00\xf2\xde\x1f\x19yaml:"code_upload_access"\x12o\n\x1einstantiate_default_permission\x18\x02 \x01(\x0e2\x1c.cosmwasm.wasm.v1.AccessTypeB)\xf2\xde\x1f%yaml:"instantiate_default_permission":\x04\x98\xa0\x1f\x00"|\n\x08CodeInfo\x12\x11\n\tcode_hash\x18\x01 \x01(\x0c\x12\x0f\n\x07creator\x18\x02 \x01(\t\x12@\n\x12instantiate_config\x18\x05 \x01(\x0b2\x1e.cosmwasm.wasm.v1.AccessConfigB\x04\xc8\xde\x1f\x00J\x04\x08\x03\x10\x04J\x04\x08\x04\x10\x05"\x90\x02\n\x0cContractInfo\x12\x1b\n\x07code_id\x18\x01 \x01(\x04B\n\xe2\xde\x1f\x06CodeID\x12\x0f\n\x07creator\x18\x02 \x01(\t\x12\r\n\x05admin\x18\x03 \x01(\t\x12\r\n\x05label\x18\x04 \x01(\t\x125\n\x07created\x18\x05 \x01(\x0b2$.cosmwasm.wasm.v1.AbsoluteTxPosition\x12"\n\x0bibc_port_id\x18\x06 \x01(\tB\r\xe2\xde\x1f\tIBCPortID\x12S\n\textension\x18\x07 \x01(\x0b2\x14.google.protobuf.AnyB*\xca\xb4-&cosmwasm.wasm.v1.ContractInfoExtension:\x04\xe8\xa0\x1f\x01"\xda\x01\n\x18ContractCodeHistoryEntry\x12E\n\toperation\x18\x01 \x01(\x0e22.cosmwasm.wasm.v1.ContractCodeHistoryOperationType\x12\x1b\n\x07code_id\x18\x02 \x01(\x04B\n\xe2\xde\x1f\x06CodeID\x125\n\x07updated\x18\x03 \x01(\x0b2$.cosmwasm.wasm.v1.AbsoluteTxPosition\x12#\n\x03msg\x18\x04 \x01(\x0cB\x16\xfa\xde\x1f\x12RawContractMessage"<\n\x12AbsoluteTxPosition\x12\x14\n\x0cblock_height\x18\x01 \x01(\x04\x12\x10\n\x08tx_index\x18\x02 \x01(\x04"]\n\x05Model\x12E\n\x03key\x18\x01 \x01(\x0cB8\xfa\xde\x1f4github.com/tendermint/tendermint/libs/bytes.HexBytes\x12\r\n\x05value\x18\x02 \x01(\x0c*\xa9\x02\n\nAccessType\x126\n\x17ACCESS_TYPE_UNSPECIFIED\x10\x00\x1a\x19\x8a\x9d \x15AccessTypeUnspecified\x12,\n\x12ACCESS_TYPE_NOBODY\x10\x01\x1a\x14\x8a\x9d \x10AccessTypeNobody\x127\n\x18ACCESS_TYPE_ONLY_ADDRESS\x10\x02\x1a\x19\x8a\x9d \x15AccessTypeOnlyAddress\x122\n\x15ACCESS_TYPE_EVERYBODY\x10\x03\x1a\x17\x8a\x9d \x13AccessTypeEverybody\x12>\n\x1cACCESS_TYPE_ANY_OF_ADDRESSES\x10\x04\x1a\x1c\x8a\x9d \x18AccessTypeAnyOfAddresses\x1a\x08\x88\xa3\x1e\x00\xa8\xa4\x1e\x00*\xa6\x03\n ContractCodeHistoryOperationType\x12e\n0CONTRACT_CODE_HISTORY_OPERATION_TYPE_UNSPECIFIED\x10\x00\x1a/\x8a\x9d +ContractCodeHistoryOperationTypeUnspecified\x12W\n)CONTRACT_CODE_HISTORY_OPERATION_TYPE_INIT\x10\x01\x1a(\x8a\x9d $ContractCodeHistoryOperationTypeInit\x12]\n,CONTRACT_CODE_HISTORY_OPERATION_TYPE_MIGRATE\x10\x02\x1a+\x8a\x9d \'ContractCodeHistoryOperationTypeMigrate\x12]\n,CONTRACT_CODE_HISTORY_OPERATION_TYPE_GENESIS\x10\x03\x1a+\x8a\x9d \'ContractCodeHistoryOperationTypeGenesis\x1a\x04\x88\xa3\x1e\x00B0Z&github.com/CosmWasm/wasmd/x/wasm/types\xc8\xe1\x1e\x00\xa8\xe2\x1e\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmwasm.wasm.v1.types_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z&github.com/CosmWasm/wasmd/x/wasm/types\xc8\xe1\x1e\x00\xa8\xe2\x1e\x01'
    _ACCESSTYPE._options = None
    _ACCESSTYPE._serialized_options = b'\x88\xa3\x1e\x00\xa8\xa4\x1e\x00'
    _ACCESSTYPE.values_by_name['ACCESS_TYPE_UNSPECIFIED']._options = None
    _ACCESSTYPE.values_by_name['ACCESS_TYPE_UNSPECIFIED']._serialized_options = b'\x8a\x9d \x15AccessTypeUnspecified'
    _ACCESSTYPE.values_by_name['ACCESS_TYPE_NOBODY']._options = None
    _ACCESSTYPE.values_by_name['ACCESS_TYPE_NOBODY']._serialized_options = b'\x8a\x9d \x10AccessTypeNobody'
    _ACCESSTYPE.values_by_name['ACCESS_TYPE_ONLY_ADDRESS']._options = None
    _ACCESSTYPE.values_by_name['ACCESS_TYPE_ONLY_ADDRESS']._serialized_options = b'\x8a\x9d \x15AccessTypeOnlyAddress'
    _ACCESSTYPE.values_by_name['ACCESS_TYPE_EVERYBODY']._options = None
    _ACCESSTYPE.values_by_name['ACCESS_TYPE_EVERYBODY']._serialized_options = b'\x8a\x9d \x13AccessTypeEverybody'
    _ACCESSTYPE.values_by_name['ACCESS_TYPE_ANY_OF_ADDRESSES']._options = None
    _ACCESSTYPE.values_by_name['ACCESS_TYPE_ANY_OF_ADDRESSES']._serialized_options = b'\x8a\x9d \x18AccessTypeAnyOfAddresses'
    _CONTRACTCODEHISTORYOPERATIONTYPE._options = None
    _CONTRACTCODEHISTORYOPERATIONTYPE._serialized_options = b'\x88\xa3\x1e\x00'
    _CONTRACTCODEHISTORYOPERATIONTYPE.values_by_name['CONTRACT_CODE_HISTORY_OPERATION_TYPE_UNSPECIFIED']._options = None
    _CONTRACTCODEHISTORYOPERATIONTYPE.values_by_name['CONTRACT_CODE_HISTORY_OPERATION_TYPE_UNSPECIFIED']._serialized_options = b'\x8a\x9d +ContractCodeHistoryOperationTypeUnspecified'
    _CONTRACTCODEHISTORYOPERATIONTYPE.values_by_name['CONTRACT_CODE_HISTORY_OPERATION_TYPE_INIT']._options = None
    _CONTRACTCODEHISTORYOPERATIONTYPE.values_by_name['CONTRACT_CODE_HISTORY_OPERATION_TYPE_INIT']._serialized_options = b'\x8a\x9d $ContractCodeHistoryOperationTypeInit'
    _CONTRACTCODEHISTORYOPERATIONTYPE.values_by_name['CONTRACT_CODE_HISTORY_OPERATION_TYPE_MIGRATE']._options = None
    _CONTRACTCODEHISTORYOPERATIONTYPE.values_by_name['CONTRACT_CODE_HISTORY_OPERATION_TYPE_MIGRATE']._serialized_options = b"\x8a\x9d 'ContractCodeHistoryOperationTypeMigrate"
    _CONTRACTCODEHISTORYOPERATIONTYPE.values_by_name['CONTRACT_CODE_HISTORY_OPERATION_TYPE_GENESIS']._options = None
    _CONTRACTCODEHISTORYOPERATIONTYPE.values_by_name['CONTRACT_CODE_HISTORY_OPERATION_TYPE_GENESIS']._serialized_options = b"\x8a\x9d 'ContractCodeHistoryOperationTypeGenesis"
    _ACCESSTYPEPARAM.fields_by_name['value']._options = None
    _ACCESSTYPEPARAM.fields_by_name['value']._serialized_options = b'\xf2\xde\x1f\x0cyaml:"value"'
    _ACCESSTYPEPARAM._options = None
    _ACCESSTYPEPARAM._serialized_options = b'\x98\xa0\x1f\x01'
    _ACCESSCONFIG.fields_by_name['permission']._options = None
    _ACCESSCONFIG.fields_by_name['permission']._serialized_options = b'\xf2\xde\x1f\x11yaml:"permission"'
    _ACCESSCONFIG.fields_by_name['address']._options = None
    _ACCESSCONFIG.fields_by_name['address']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"address"'
    _ACCESSCONFIG.fields_by_name['addresses']._options = None
    _ACCESSCONFIG.fields_by_name['addresses']._serialized_options = b'\xf2\xde\x1f\x10yaml:"addresses"'
    _ACCESSCONFIG._options = None
    _ACCESSCONFIG._serialized_options = b'\x98\xa0\x1f\x01'
    _PARAMS.fields_by_name['code_upload_access']._options = None
    _PARAMS.fields_by_name['code_upload_access']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x19yaml:"code_upload_access"'
    _PARAMS.fields_by_name['instantiate_default_permission']._options = None
    _PARAMS.fields_by_name['instantiate_default_permission']._serialized_options = b'\xf2\xde\x1f%yaml:"instantiate_default_permission"'
    _PARAMS._options = None
    _PARAMS._serialized_options = b'\x98\xa0\x1f\x00'
    _CODEINFO.fields_by_name['instantiate_config']._options = None
    _CODEINFO.fields_by_name['instantiate_config']._serialized_options = b'\xc8\xde\x1f\x00'
    _CONTRACTINFO.fields_by_name['code_id']._options = None
    _CONTRACTINFO.fields_by_name['code_id']._serialized_options = b'\xe2\xde\x1f\x06CodeID'
    _CONTRACTINFO.fields_by_name['ibc_port_id']._options = None
    _CONTRACTINFO.fields_by_name['ibc_port_id']._serialized_options = b'\xe2\xde\x1f\tIBCPortID'
    _CONTRACTINFO.fields_by_name['extension']._options = None
    _CONTRACTINFO.fields_by_name['extension']._serialized_options = b'\xca\xb4-&cosmwasm.wasm.v1.ContractInfoExtension'
    _CONTRACTINFO._options = None
    _CONTRACTINFO._serialized_options = b'\xe8\xa0\x1f\x01'
    _CONTRACTCODEHISTORYENTRY.fields_by_name['code_id']._options = None
    _CONTRACTCODEHISTORYENTRY.fields_by_name['code_id']._serialized_options = b'\xe2\xde\x1f\x06CodeID'
    _CONTRACTCODEHISTORYENTRY.fields_by_name['msg']._options = None
    _CONTRACTCODEHISTORYENTRY.fields_by_name['msg']._serialized_options = b'\xfa\xde\x1f\x12RawContractMessage'
    _MODEL.fields_by_name['key']._options = None
    _MODEL.fields_by_name['key']._serialized_options = b'\xfa\xde\x1f4github.com/tendermint/tendermint/libs/bytes.HexBytes'
    _globals['_ACCESSTYPE']._serialized_start = 1393
    _globals['_ACCESSTYPE']._serialized_end = 1690
    _globals['_CONTRACTCODEHISTORYOPERATIONTYPE']._serialized_start = 1693
    _globals['_CONTRACTCODEHISTORYOPERATIONTYPE']._serialized_end = 2115
    _globals['_ACCESSTYPEPARAM']._serialized_start = 126
    _globals['_ACCESSTYPEPARAM']._serialized_end = 212
    _globals['_ACCESSCONFIG']._serialized_start = 215
    _globals['_ACCESSCONFIG']._serialized_end = 386
    _globals['_PARAMS']._serialized_start = 389
    _globals['_PARAMS']._serialized_end = 611
    _globals['_CODEINFO']._serialized_start = 613
    _globals['_CODEINFO']._serialized_end = 737
    _globals['_CONTRACTINFO']._serialized_start = 740
    _globals['_CONTRACTINFO']._serialized_end = 1012
    _globals['_CONTRACTCODEHISTORYENTRY']._serialized_start = 1015
    _globals['_CONTRACTCODEHISTORYENTRY']._serialized_end = 1233
    _globals['_ABSOLUTETXPOSITION']._serialized_start = 1235
    _globals['_ABSOLUTETXPOSITION']._serialized_end = 1295
    _globals['_MODEL']._serialized_start = 1297
    _globals['_MODEL']._serialized_end = 1390