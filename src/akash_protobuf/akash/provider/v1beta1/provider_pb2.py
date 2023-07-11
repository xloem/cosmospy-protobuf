"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....akash.base.v1beta1 import attribute_pb2 as akash_dot_base_dot_v1beta1_dot_attribute__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%akash/provider/v1beta1/provider.proto\x12\x16akash.provider.v1beta1\x1a\x14gogoproto/gogo.proto\x1a"akash/base/v1beta1/attribute.proto"q\n\x0cProviderInfo\x121\n\x05email\x18\x01 \x01(\tB"\xe2\xde\x1f\x05EMail\xea\xde\x1f\x05email\xf2\xde\x1f\x0cyaml:"email"\x12.\n\x07website\x18\x02 \x01(\tB\x1d\xea\xde\x1f\x07website\xf2\xde\x1f\x0eyaml:"website""\xf6\x02\n\x11MsgCreateProvider\x12(\n\x05owner\x18\x01 \x01(\tB\x19\xea\xde\x1f\x05owner\xf2\xde\x1f\x0cyaml:"owner"\x12<\n\x08host_uri\x18\x02 \x01(\tB*\xe2\xde\x1f\x07HostURI\xea\xde\x1f\x08host_uri\xf2\xde\x1f\x0fyaml:"host_uri"\x12\xa1\x01\n\nattributes\x18\x03 \x03(\x0b2\x1d.akash.base.v1beta1.AttributeBn\xc8\xde\x1f\x00\xea\xde\x1f\nattributes\xf2\xde\x1f\x11yaml:"attributes"\xaa\xdf\x1fCgithub.com/akash-network/akash-api/go/node/types/v1beta1.Attributes\x12O\n\x04info\x18\x04 \x01(\x0b2$.akash.provider.v1beta1.ProviderInfoB\x1b\xc8\xde\x1f\x00\xea\xde\x1f\x04info\xf2\xde\x1f\x0byaml:"info":\x04\xe8\xa0\x1f\x00"\x1b\n\x19MsgCreateProviderResponse"\xf6\x02\n\x11MsgUpdateProvider\x12(\n\x05owner\x18\x01 \x01(\tB\x19\xea\xde\x1f\x05owner\xf2\xde\x1f\x0cyaml:"owner"\x12<\n\x08host_uri\x18\x02 \x01(\tB*\xe2\xde\x1f\x07HostURI\xea\xde\x1f\x08host_uri\xf2\xde\x1f\x0fyaml:"host_uri"\x12\xa1\x01\n\nattributes\x18\x03 \x03(\x0b2\x1d.akash.base.v1beta1.AttributeBn\xc8\xde\x1f\x00\xea\xde\x1f\nattributes\xf2\xde\x1f\x11yaml:"attributes"\xaa\xdf\x1fCgithub.com/akash-network/akash-api/go/node/types/v1beta1.Attributes\x12O\n\x04info\x18\x04 \x01(\x0b2$.akash.provider.v1beta1.ProviderInfoB\x1b\xc8\xde\x1f\x00\xea\xde\x1f\x04info\xf2\xde\x1f\x0byaml:"info":\x04\xe8\xa0\x1f\x00"\x1b\n\x19MsgUpdateProviderResponse"C\n\x11MsgDeleteProvider\x12(\n\x05owner\x18\x01 \x01(\tB\x19\xea\xde\x1f\x05owner\xf2\xde\x1f\x0cyaml:"owner":\x04\xe8\xa0\x1f\x00"\x1b\n\x19MsgDeleteProviderResponse"\xf1\x02\n\x08Provider\x12(\n\x05owner\x18\x01 \x01(\tB\x19\xea\xde\x1f\x05owner\xf2\xde\x1f\x0cyaml:"owner"\x12<\n\x08host_uri\x18\x02 \x01(\tB*\xe2\xde\x1f\x07HostURI\xea\xde\x1f\x08host_uri\xf2\xde\x1f\x0fyaml:"host_uri"\x12\xa1\x01\n\nattributes\x18\x03 \x03(\x0b2\x1d.akash.base.v1beta1.AttributeBn\xc8\xde\x1f\x00\xea\xde\x1f\nattributes\xf2\xde\x1f\x11yaml:"attributes"\xaa\xdf\x1fCgithub.com/akash-network/akash-api/go/node/types/v1beta1.Attributes\x12O\n\x04info\x18\x04 \x01(\x0b2$.akash.provider.v1beta1.ProviderInfoB\x1b\xc8\xde\x1f\x00\xea\xde\x1f\x04info\xf2\xde\x1f\x0byaml:"info":\x08\x98\xa0\x1f\x00\xe8\xa0\x1f\x002\xd5\x02\n\x03Msg\x12n\n\x0eCreateProvider\x12).akash.provider.v1beta1.MsgCreateProvider\x1a1.akash.provider.v1beta1.MsgCreateProviderResponse\x12n\n\x0eUpdateProvider\x12).akash.provider.v1beta1.MsgUpdateProvider\x1a1.akash.provider.v1beta1.MsgUpdateProviderResponse\x12n\n\x0eDeleteProvider\x12).akash.provider.v1beta1.MsgDeleteProvider\x1a1.akash.provider.v1beta1.MsgDeleteProviderResponseB=Z;github.com/akash-network/akash-api/go/node/provider/v1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'akash.provider.v1beta1.provider_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z;github.com/akash-network/akash-api/go/node/provider/v1beta1'
    _PROVIDERINFO.fields_by_name['email']._options = None
    _PROVIDERINFO.fields_by_name['email']._serialized_options = b'\xe2\xde\x1f\x05EMail\xea\xde\x1f\x05email\xf2\xde\x1f\x0cyaml:"email"'
    _PROVIDERINFO.fields_by_name['website']._options = None
    _PROVIDERINFO.fields_by_name['website']._serialized_options = b'\xea\xde\x1f\x07website\xf2\xde\x1f\x0eyaml:"website"'
    _MSGCREATEPROVIDER.fields_by_name['owner']._options = None
    _MSGCREATEPROVIDER.fields_by_name['owner']._serialized_options = b'\xea\xde\x1f\x05owner\xf2\xde\x1f\x0cyaml:"owner"'
    _MSGCREATEPROVIDER.fields_by_name['host_uri']._options = None
    _MSGCREATEPROVIDER.fields_by_name['host_uri']._serialized_options = b'\xe2\xde\x1f\x07HostURI\xea\xde\x1f\x08host_uri\xf2\xde\x1f\x0fyaml:"host_uri"'
    _MSGCREATEPROVIDER.fields_by_name['attributes']._options = None
    _MSGCREATEPROVIDER.fields_by_name['attributes']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\nattributes\xf2\xde\x1f\x11yaml:"attributes"\xaa\xdf\x1fCgithub.com/akash-network/akash-api/go/node/types/v1beta1.Attributes'
    _MSGCREATEPROVIDER.fields_by_name['info']._options = None
    _MSGCREATEPROVIDER.fields_by_name['info']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x04info\xf2\xde\x1f\x0byaml:"info"'
    _MSGCREATEPROVIDER._options = None
    _MSGCREATEPROVIDER._serialized_options = b'\xe8\xa0\x1f\x00'
    _MSGUPDATEPROVIDER.fields_by_name['owner']._options = None
    _MSGUPDATEPROVIDER.fields_by_name['owner']._serialized_options = b'\xea\xde\x1f\x05owner\xf2\xde\x1f\x0cyaml:"owner"'
    _MSGUPDATEPROVIDER.fields_by_name['host_uri']._options = None
    _MSGUPDATEPROVIDER.fields_by_name['host_uri']._serialized_options = b'\xe2\xde\x1f\x07HostURI\xea\xde\x1f\x08host_uri\xf2\xde\x1f\x0fyaml:"host_uri"'
    _MSGUPDATEPROVIDER.fields_by_name['attributes']._options = None
    _MSGUPDATEPROVIDER.fields_by_name['attributes']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\nattributes\xf2\xde\x1f\x11yaml:"attributes"\xaa\xdf\x1fCgithub.com/akash-network/akash-api/go/node/types/v1beta1.Attributes'
    _MSGUPDATEPROVIDER.fields_by_name['info']._options = None
    _MSGUPDATEPROVIDER.fields_by_name['info']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x04info\xf2\xde\x1f\x0byaml:"info"'
    _MSGUPDATEPROVIDER._options = None
    _MSGUPDATEPROVIDER._serialized_options = b'\xe8\xa0\x1f\x00'
    _MSGDELETEPROVIDER.fields_by_name['owner']._options = None
    _MSGDELETEPROVIDER.fields_by_name['owner']._serialized_options = b'\xea\xde\x1f\x05owner\xf2\xde\x1f\x0cyaml:"owner"'
    _MSGDELETEPROVIDER._options = None
    _MSGDELETEPROVIDER._serialized_options = b'\xe8\xa0\x1f\x00'
    _PROVIDER.fields_by_name['owner']._options = None
    _PROVIDER.fields_by_name['owner']._serialized_options = b'\xea\xde\x1f\x05owner\xf2\xde\x1f\x0cyaml:"owner"'
    _PROVIDER.fields_by_name['host_uri']._options = None
    _PROVIDER.fields_by_name['host_uri']._serialized_options = b'\xe2\xde\x1f\x07HostURI\xea\xde\x1f\x08host_uri\xf2\xde\x1f\x0fyaml:"host_uri"'
    _PROVIDER.fields_by_name['attributes']._options = None
    _PROVIDER.fields_by_name['attributes']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\nattributes\xf2\xde\x1f\x11yaml:"attributes"\xaa\xdf\x1fCgithub.com/akash-network/akash-api/go/node/types/v1beta1.Attributes'
    _PROVIDER.fields_by_name['info']._options = None
    _PROVIDER.fields_by_name['info']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x04info\xf2\xde\x1f\x0byaml:"info"'
    _PROVIDER._options = None
    _PROVIDER._serialized_options = b'\x98\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _globals['_PROVIDERINFO']._serialized_start = 123
    _globals['_PROVIDERINFO']._serialized_end = 236
    _globals['_MSGCREATEPROVIDER']._serialized_start = 239
    _globals['_MSGCREATEPROVIDER']._serialized_end = 613
    _globals['_MSGCREATEPROVIDERRESPONSE']._serialized_start = 615
    _globals['_MSGCREATEPROVIDERRESPONSE']._serialized_end = 642
    _globals['_MSGUPDATEPROVIDER']._serialized_start = 645
    _globals['_MSGUPDATEPROVIDER']._serialized_end = 1019
    _globals['_MSGUPDATEPROVIDERRESPONSE']._serialized_start = 1021
    _globals['_MSGUPDATEPROVIDERRESPONSE']._serialized_end = 1048
    _globals['_MSGDELETEPROVIDER']._serialized_start = 1050
    _globals['_MSGDELETEPROVIDER']._serialized_end = 1117
    _globals['_MSGDELETEPROVIDERRESPONSE']._serialized_start = 1119
    _globals['_MSGDELETEPROVIDERRESPONSE']._serialized_end = 1146
    _globals['_PROVIDER']._serialized_start = 1149
    _globals['_PROVIDER']._serialized_end = 1518
    _globals['_MSG']._serialized_start = 1521
    _globals['_MSG']._serialized_end = 1862