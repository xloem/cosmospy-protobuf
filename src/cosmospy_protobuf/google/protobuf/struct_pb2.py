# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/protobuf/struct.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cgoogle/protobuf/struct.proto\x12\x0fgoogle.protobuf\"\x84\x01\n\x06Struct\x12\x33\n\x06\x66ields\x18\x01 \x03(\x0b\x32#.google.protobuf.Struct.FieldsEntry\x1a\x45\n\x0b\x46ieldsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.google.protobuf.Value:\x02\x38\x01\"\xea\x01\n\x05Value\x12\x30\n\nnull_value\x18\x01 \x01(\x0e\x32\x1a.google.protobuf.NullValueH\x00\x12\x16\n\x0cnumber_value\x18\x02 \x01(\x01H\x00\x12\x16\n\x0cstring_value\x18\x03 \x01(\tH\x00\x12\x14\n\nbool_value\x18\x04 \x01(\x08H\x00\x12/\n\x0cstruct_value\x18\x05 \x01(\x0b\x32\x17.google.protobuf.StructH\x00\x12\x30\n\nlist_value\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.ListValueH\x00\x42\x06\n\x04kind\"3\n\tListValue\x12&\n\x06values\x18\x01 \x03(\x0b\x32\x16.google.protobuf.Value*\x1b\n\tNullValue\x12\x0e\n\nNULL_VALUE\x10\x00\x42U\n\x13\x63om.google.protobufB\x0bStructProtoP\x01Z\x05types\xf8\x01\x01\xa2\x02\x03GPB\xaa\x02\x1eGoogle.Protobuf.WellKnownTypesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.protobuf.struct_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\023com.google.protobufB\013StructProtoP\001Z\005types\370\001\001\242\002\003GPB\252\002\036Google.Protobuf.WellKnownTypes'
  _STRUCT_FIELDSENTRY._options = None
  _STRUCT_FIELDSENTRY._serialized_options = b'8\001'
  _globals['_NULLVALUE']._serialized_start=474
  _globals['_NULLVALUE']._serialized_end=501
  _globals['_STRUCT']._serialized_start=50
  _globals['_STRUCT']._serialized_end=182
  _globals['_STRUCT_FIELDSENTRY']._serialized_start=113
  _globals['_STRUCT_FIELDSENTRY']._serialized_end=182
  _globals['_VALUE']._serialized_start=185
  _globals['_VALUE']._serialized_end=419
  _globals['_LISTVALUE']._serialized_start=421
  _globals['_LISTVALUE']._serialized_end=472
# @@protoc_insertion_point(module_scope)
