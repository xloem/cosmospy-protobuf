"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....akash.manifest.v2beta1 import serviceexpose_pb2 as akash_dot_manifest_dot_v2beta1_dot_serviceexpose__pb2
from ....akash.base.v1beta2 import resourceunits_pb2 as akash_dot_base_dot_v1beta2_dot_resourceunits__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$akash/manifest/v2beta1/service.proto\x12\x16akash.manifest.v2beta1\x1a\x14gogoproto/gogo.proto\x1a*akash/manifest/v2beta1/serviceexpose.proto\x1a&akash/base/v1beta2/resourceunits.proto"\x94\x01\n\rStorageParams\x12%\n\x04name\x18\x01 \x01(\tB\x17\xea\xde\x1f\x04name\xf2\xde\x1f\x0byaml:"name"\x12(\n\x05mount\x18\x02 \x01(\tB\x19\xea\xde\x1f\x05mount\xf2\xde\x1f\x0cyaml:"mount"\x122\n\tread_only\x18\x03 \x01(\x08B\x1f\xea\xde\x1f\x08readOnly\xf2\xde\x1f\x0fyaml:"readOnly""j\n\rServiceParams\x12Y\n\x07storage\x18\x01 \x03(\x0b2%.akash.manifest.v2beta1.StorageParamsB!\xc8\xde\x1f\x00\xea\xde\x1f\x07storage\xf2\xde\x1f\x0eyaml:"storage""\x90\x04\n\x07Service\x12%\n\x04name\x18\x01 \x01(\tB\x17\xea\xde\x1f\x04name\xf2\xde\x1f\x0byaml:"name"\x12(\n\x05image\x18\x02 \x01(\tB\x19\xea\xde\x1f\x05image\xf2\xde\x1f\x0cyaml:"image"\x12.\n\x07command\x18\x03 \x03(\tB\x1d\xea\xde\x1f\x07command\xf2\xde\x1f\x0eyaml:"command"\x12%\n\x04args\x18\x04 \x03(\tB\x17\xea\xde\x1f\x04args\xf2\xde\x1f\x0byaml:"args"\x12&\n\x03env\x18\x05 \x03(\tB\x19\xc8\xde\x1f\x01\xea\xde\x1f\x03env\xf2\xde\x1f\nyaml:"env"\x12[\n\tresources\x18\x06 \x01(\x0b2!.akash.base.v1beta2.ResourceUnitsB%\xc8\xde\x1f\x00\xea\xde\x1f\tresources\xf2\xde\x1f\x10yaml:"resources"\x12(\n\x05count\x18\x07 \x01(\rB\x19\xea\xde\x1f\x05count\xf2\xde\x1f\x0cyaml:"count"\x12V\n\x06expose\x18\x08 \x03(\x0b2%.akash.manifest.v2beta1.ServiceExposeB\x1f\xc8\xde\x1f\x00\xea\xde\x1f\x06expose\xf2\xde\x1f\ryaml:"expose"\x12V\n\x06params\x18\t \x01(\x0b2%.akash.manifest.v2beta1.ServiceParamsB\x1f\xc8\xde\x1f\x01\xea\xde\x1f\x06params\xf2\xde\x1f\ryaml:"params"B@Z6github.com/akash-network/akash-api/go/manifest/v2beta1\xd8\xe1\x1e\x00\x80\xe2\x1e\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'akash.manifest.v2beta1.service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z6github.com/akash-network/akash-api/go/manifest/v2beta1\xd8\xe1\x1e\x00\x80\xe2\x1e\x01'
    _STORAGEPARAMS.fields_by_name['name']._options = None
    _STORAGEPARAMS.fields_by_name['name']._serialized_options = b'\xea\xde\x1f\x04name\xf2\xde\x1f\x0byaml:"name"'
    _STORAGEPARAMS.fields_by_name['mount']._options = None
    _STORAGEPARAMS.fields_by_name['mount']._serialized_options = b'\xea\xde\x1f\x05mount\xf2\xde\x1f\x0cyaml:"mount"'
    _STORAGEPARAMS.fields_by_name['read_only']._options = None
    _STORAGEPARAMS.fields_by_name['read_only']._serialized_options = b'\xea\xde\x1f\x08readOnly\xf2\xde\x1f\x0fyaml:"readOnly"'
    _SERVICEPARAMS.fields_by_name['storage']._options = None
    _SERVICEPARAMS.fields_by_name['storage']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x07storage\xf2\xde\x1f\x0eyaml:"storage"'
    _SERVICE.fields_by_name['name']._options = None
    _SERVICE.fields_by_name['name']._serialized_options = b'\xea\xde\x1f\x04name\xf2\xde\x1f\x0byaml:"name"'
    _SERVICE.fields_by_name['image']._options = None
    _SERVICE.fields_by_name['image']._serialized_options = b'\xea\xde\x1f\x05image\xf2\xde\x1f\x0cyaml:"image"'
    _SERVICE.fields_by_name['command']._options = None
    _SERVICE.fields_by_name['command']._serialized_options = b'\xea\xde\x1f\x07command\xf2\xde\x1f\x0eyaml:"command"'
    _SERVICE.fields_by_name['args']._options = None
    _SERVICE.fields_by_name['args']._serialized_options = b'\xea\xde\x1f\x04args\xf2\xde\x1f\x0byaml:"args"'
    _SERVICE.fields_by_name['env']._options = None
    _SERVICE.fields_by_name['env']._serialized_options = b'\xc8\xde\x1f\x01\xea\xde\x1f\x03env\xf2\xde\x1f\nyaml:"env"'
    _SERVICE.fields_by_name['resources']._options = None
    _SERVICE.fields_by_name['resources']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\tresources\xf2\xde\x1f\x10yaml:"resources"'
    _SERVICE.fields_by_name['count']._options = None
    _SERVICE.fields_by_name['count']._serialized_options = b'\xea\xde\x1f\x05count\xf2\xde\x1f\x0cyaml:"count"'
    _SERVICE.fields_by_name['expose']._options = None
    _SERVICE.fields_by_name['expose']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x06expose\xf2\xde\x1f\ryaml:"expose"'
    _SERVICE.fields_by_name['params']._options = None
    _SERVICE.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x01\xea\xde\x1f\x06params\xf2\xde\x1f\ryaml:"params"'
    _globals['_STORAGEPARAMS']._serialized_start = 171
    _globals['_STORAGEPARAMS']._serialized_end = 319
    _globals['_SERVICEPARAMS']._serialized_start = 321
    _globals['_SERVICEPARAMS']._serialized_end = 427
    _globals['_SERVICE']._serialized_start = 430
    _globals['_SERVICE']._serialized_end = 958