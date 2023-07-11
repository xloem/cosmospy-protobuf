"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....akash.base.v1beta2 import attribute_pb2 as akash_dot_base_dot_v1beta2_dot_attribute__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fakash/audit/v1beta2/audit.proto\x12\x13akash.audit.v1beta2\x1a\x14gogoproto/gogo.proto\x1a"akash/base/v1beta2/attribute.proto"\x88\x02\n\x08Provider\x12(\n\x05owner\x18\x01 \x01(\tB\x19\xea\xde\x1f\x05owner\xf2\xde\x1f\x0cyaml:"owner"\x12.\n\x07auditor\x18\x02 \x01(\tB\x1d\xea\xde\x1f\x07auditor\xf2\xde\x1f\x0eyaml:"auditor"\x12\xa1\x01\n\nattributes\x18\x04 \x03(\x0b2\x1d.akash.base.v1beta2.AttributeBn\xc8\xde\x1f\x00\xea\xde\x1f\nattributes\xf2\xde\x1f\x11yaml:"attributes"\xaa\xdf\x1fCgithub.com/akash-network/akash-api/go/node/types/v1beta2.Attributes"\x9b\x02\n\x11AuditedAttributes\x12(\n\x05owner\x18\x01 \x01(\tB\x19\xea\xde\x1f\x05owner\xf2\xde\x1f\x0cyaml:"owner"\x12.\n\x07auditor\x18\x02 \x01(\tB\x1d\xea\xde\x1f\x07auditor\xf2\xde\x1f\x0eyaml:"auditor"\x12\xa1\x01\n\nattributes\x18\x03 \x03(\x0b2\x1d.akash.base.v1beta2.AttributeBn\xc8\xde\x1f\x00\xea\xde\x1f\nattributes\xf2\xde\x1f\x11yaml:"attributes"\xaa\xdf\x1fCgithub.com/akash-network/akash-api/go/node/types/v1beta2.Attributes:\x08\x98\xa0\x1f\x01\xe8\xa0\x1f\x00"\x83\x01\n\x12AttributesResponse\x12c\n\nattributes\x18\x01 \x03(\x0b2&.akash.audit.v1beta2.AuditedAttributesB\'\xc8\xde\x1f\x00\xea\xde\x1f\nattributes\xf2\xde\x1f\x11yaml:"attributes":\x08\x98\xa0\x1f\x01\xe8\xa0\x1f\x00"}\n\x11AttributesFilters\x121\n\x08auditors\x18\x01 \x03(\tB\x1f\xea\xde\x1f\x08auditors\xf2\xde\x1f\x0fyaml:"auditors"\x12+\n\x06owners\x18\x02 \x03(\tB\x1b\xea\xde\x1f\x06owners\xf2\xde\x1f\ryaml:"owners":\x08\x98\xa0\x1f\x01\xe8\xa0\x1f\x00"\x9f\x02\n\x19MsgSignProviderAttributes\x12(\n\x05owner\x18\x01 \x01(\tB\x19\xea\xde\x1f\x05owner\xf2\xde\x1f\x0cyaml:"owner"\x12.\n\x07auditor\x18\x02 \x01(\tB\x1d\xea\xde\x1f\x07auditor\xf2\xde\x1f\x0eyaml:"auditor"\x12\xa1\x01\n\nattributes\x18\x03 \x03(\x0b2\x1d.akash.base.v1beta2.AttributeBn\xc8\xde\x1f\x00\xea\xde\x1f\nattributes\xf2\xde\x1f\x11yaml:"attributes"\xaa\xdf\x1fCgithub.com/akash-network/akash-api/go/node/types/v1beta2.Attributes:\x04\xe8\xa0\x1f\x00"#\n!MsgSignProviderAttributesResponse"\xa4\x01\n\x1bMsgDeleteProviderAttributes\x12(\n\x05owner\x18\x01 \x01(\tB\x19\xea\xde\x1f\x05owner\xf2\xde\x1f\x0cyaml:"owner"\x12.\n\x07auditor\x18\x02 \x01(\tB\x1d\xea\xde\x1f\x07auditor\xf2\xde\x1f\x0eyaml:"auditor"\x12%\n\x04keys\x18\x03 \x03(\tB\x17\xea\xde\x1f\x04keys\xf2\xde\x1f\x0byaml:"keys":\x04\xe8\xa0\x1f\x00"%\n#MsgDeleteProviderAttributesResponse2\x91\x02\n\x03Msg\x12\x80\x01\n\x16SignProviderAttributes\x12..akash.audit.v1beta2.MsgSignProviderAttributes\x1a6.akash.audit.v1beta2.MsgSignProviderAttributesResponse\x12\x86\x01\n\x18DeleteProviderAttributes\x120.akash.audit.v1beta2.MsgDeleteProviderAttributes\x1a8.akash.audit.v1beta2.MsgDeleteProviderAttributesResponseB:Z8github.com/akash-network/akash-api/go/node/audit/v1beta2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'akash.audit.v1beta2.audit_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z8github.com/akash-network/akash-api/go/node/audit/v1beta2'
    _PROVIDER.fields_by_name['owner']._options = None
    _PROVIDER.fields_by_name['owner']._serialized_options = b'\xea\xde\x1f\x05owner\xf2\xde\x1f\x0cyaml:"owner"'
    _PROVIDER.fields_by_name['auditor']._options = None
    _PROVIDER.fields_by_name['auditor']._serialized_options = b'\xea\xde\x1f\x07auditor\xf2\xde\x1f\x0eyaml:"auditor"'
    _PROVIDER.fields_by_name['attributes']._options = None
    _PROVIDER.fields_by_name['attributes']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\nattributes\xf2\xde\x1f\x11yaml:"attributes"\xaa\xdf\x1fCgithub.com/akash-network/akash-api/go/node/types/v1beta2.Attributes'
    _AUDITEDATTRIBUTES.fields_by_name['owner']._options = None
    _AUDITEDATTRIBUTES.fields_by_name['owner']._serialized_options = b'\xea\xde\x1f\x05owner\xf2\xde\x1f\x0cyaml:"owner"'
    _AUDITEDATTRIBUTES.fields_by_name['auditor']._options = None
    _AUDITEDATTRIBUTES.fields_by_name['auditor']._serialized_options = b'\xea\xde\x1f\x07auditor\xf2\xde\x1f\x0eyaml:"auditor"'
    _AUDITEDATTRIBUTES.fields_by_name['attributes']._options = None
    _AUDITEDATTRIBUTES.fields_by_name['attributes']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\nattributes\xf2\xde\x1f\x11yaml:"attributes"\xaa\xdf\x1fCgithub.com/akash-network/akash-api/go/node/types/v1beta2.Attributes'
    _AUDITEDATTRIBUTES._options = None
    _AUDITEDATTRIBUTES._serialized_options = b'\x98\xa0\x1f\x01\xe8\xa0\x1f\x00'
    _ATTRIBUTESRESPONSE.fields_by_name['attributes']._options = None
    _ATTRIBUTESRESPONSE.fields_by_name['attributes']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\nattributes\xf2\xde\x1f\x11yaml:"attributes"'
    _ATTRIBUTESRESPONSE._options = None
    _ATTRIBUTESRESPONSE._serialized_options = b'\x98\xa0\x1f\x01\xe8\xa0\x1f\x00'
    _ATTRIBUTESFILTERS.fields_by_name['auditors']._options = None
    _ATTRIBUTESFILTERS.fields_by_name['auditors']._serialized_options = b'\xea\xde\x1f\x08auditors\xf2\xde\x1f\x0fyaml:"auditors"'
    _ATTRIBUTESFILTERS.fields_by_name['owners']._options = None
    _ATTRIBUTESFILTERS.fields_by_name['owners']._serialized_options = b'\xea\xde\x1f\x06owners\xf2\xde\x1f\ryaml:"owners"'
    _ATTRIBUTESFILTERS._options = None
    _ATTRIBUTESFILTERS._serialized_options = b'\x98\xa0\x1f\x01\xe8\xa0\x1f\x00'
    _MSGSIGNPROVIDERATTRIBUTES.fields_by_name['owner']._options = None
    _MSGSIGNPROVIDERATTRIBUTES.fields_by_name['owner']._serialized_options = b'\xea\xde\x1f\x05owner\xf2\xde\x1f\x0cyaml:"owner"'
    _MSGSIGNPROVIDERATTRIBUTES.fields_by_name['auditor']._options = None
    _MSGSIGNPROVIDERATTRIBUTES.fields_by_name['auditor']._serialized_options = b'\xea\xde\x1f\x07auditor\xf2\xde\x1f\x0eyaml:"auditor"'
    _MSGSIGNPROVIDERATTRIBUTES.fields_by_name['attributes']._options = None
    _MSGSIGNPROVIDERATTRIBUTES.fields_by_name['attributes']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\nattributes\xf2\xde\x1f\x11yaml:"attributes"\xaa\xdf\x1fCgithub.com/akash-network/akash-api/go/node/types/v1beta2.Attributes'
    _MSGSIGNPROVIDERATTRIBUTES._options = None
    _MSGSIGNPROVIDERATTRIBUTES._serialized_options = b'\xe8\xa0\x1f\x00'
    _MSGDELETEPROVIDERATTRIBUTES.fields_by_name['owner']._options = None
    _MSGDELETEPROVIDERATTRIBUTES.fields_by_name['owner']._serialized_options = b'\xea\xde\x1f\x05owner\xf2\xde\x1f\x0cyaml:"owner"'
    _MSGDELETEPROVIDERATTRIBUTES.fields_by_name['auditor']._options = None
    _MSGDELETEPROVIDERATTRIBUTES.fields_by_name['auditor']._serialized_options = b'\xea\xde\x1f\x07auditor\xf2\xde\x1f\x0eyaml:"auditor"'
    _MSGDELETEPROVIDERATTRIBUTES.fields_by_name['keys']._options = None
    _MSGDELETEPROVIDERATTRIBUTES.fields_by_name['keys']._serialized_options = b'\xea\xde\x1f\x04keys\xf2\xde\x1f\x0byaml:"keys"'
    _MSGDELETEPROVIDERATTRIBUTES._options = None
    _MSGDELETEPROVIDERATTRIBUTES._serialized_options = b'\xe8\xa0\x1f\x00'
    _globals['_PROVIDER']._serialized_start = 115
    _globals['_PROVIDER']._serialized_end = 379
    _globals['_AUDITEDATTRIBUTES']._serialized_start = 382
    _globals['_AUDITEDATTRIBUTES']._serialized_end = 665
    _globals['_ATTRIBUTESRESPONSE']._serialized_start = 668
    _globals['_ATTRIBUTESRESPONSE']._serialized_end = 799
    _globals['_ATTRIBUTESFILTERS']._serialized_start = 801
    _globals['_ATTRIBUTESFILTERS']._serialized_end = 926
    _globals['_MSGSIGNPROVIDERATTRIBUTES']._serialized_start = 929
    _globals['_MSGSIGNPROVIDERATTRIBUTES']._serialized_end = 1216
    _globals['_MSGSIGNPROVIDERATTRIBUTESRESPONSE']._serialized_start = 1218
    _globals['_MSGSIGNPROVIDERATTRIBUTESRESPONSE']._serialized_end = 1253
    _globals['_MSGDELETEPROVIDERATTRIBUTES']._serialized_start = 1256
    _globals['_MSGDELETEPROVIDERATTRIBUTES']._serialized_end = 1420
    _globals['_MSGDELETEPROVIDERATTRIBUTESRESPONSE']._serialized_start = 1422
    _globals['_MSGDELETEPROVIDERATTRIBUTESRESPONSE']._serialized_end = 1459
    _globals['_MSG']._serialized_start = 1462
    _globals['_MSG']._serialized_end = 1735