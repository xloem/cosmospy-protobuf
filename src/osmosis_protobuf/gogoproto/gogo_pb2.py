"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14gogoproto/gogo.proto\x12\tgogoproto\x1a google/protobuf/descriptor.proto:;\n\x13goproto_enum_prefix\x12\x1c.google.protobuf.EnumOptions\x18\xb1\xe4\x03 \x01(\x08:=\n\x15goproto_enum_stringer\x12\x1c.google.protobuf.EnumOptions\x18\xc5\xe4\x03 \x01(\x08:5\n\renum_stringer\x12\x1c.google.protobuf.EnumOptions\x18\xc6\xe4\x03 \x01(\x08:7\n\x0fenum_customname\x12\x1c.google.protobuf.EnumOptions\x18\xc7\xe4\x03 \x01(\t:0\n\x08enumdecl\x12\x1c.google.protobuf.EnumOptions\x18\xc8\xe4\x03 \x01(\x08:A\n\x14enumvalue_customname\x12!.google.protobuf.EnumValueOptions\x18\xd1\x83\x04 \x01(\t:;\n\x13goproto_getters_all\x12\x1c.google.protobuf.FileOptions\x18\x99\xec\x03 \x01(\x08:?\n\x17goproto_enum_prefix_all\x12\x1c.google.protobuf.FileOptions\x18\x9a\xec\x03 \x01(\x08:<\n\x14goproto_stringer_all\x12\x1c.google.protobuf.FileOptions\x18\x9b\xec\x03 \x01(\x08:9\n\x11verbose_equal_all\x12\x1c.google.protobuf.FileOptions\x18\x9c\xec\x03 \x01(\x08:0\n\x08face_all\x12\x1c.google.protobuf.FileOptions\x18\x9d\xec\x03 \x01(\x08:4\n\x0cgostring_all\x12\x1c.google.protobuf.FileOptions\x18\x9e\xec\x03 \x01(\x08:4\n\x0cpopulate_all\x12\x1c.google.protobuf.FileOptions\x18\x9f\xec\x03 \x01(\x08:4\n\x0cstringer_all\x12\x1c.google.protobuf.FileOptions\x18\xa0\xec\x03 \x01(\x08:3\n\x0bonlyone_all\x12\x1c.google.protobuf.FileOptions\x18\xa1\xec\x03 \x01(\x08:1\n\tequal_all\x12\x1c.google.protobuf.FileOptions\x18\xa5\xec\x03 \x01(\x08:7\n\x0fdescription_all\x12\x1c.google.protobuf.FileOptions\x18\xa6\xec\x03 \x01(\x08:3\n\x0btestgen_all\x12\x1c.google.protobuf.FileOptions\x18\xa7\xec\x03 \x01(\x08:4\n\x0cbenchgen_all\x12\x1c.google.protobuf.FileOptions\x18\xa8\xec\x03 \x01(\x08:5\n\rmarshaler_all\x12\x1c.google.protobuf.FileOptions\x18\xa9\xec\x03 \x01(\x08:7\n\x0funmarshaler_all\x12\x1c.google.protobuf.FileOptions\x18\xaa\xec\x03 \x01(\x08:<\n\x14stable_marshaler_all\x12\x1c.google.protobuf.FileOptions\x18\xab\xec\x03 \x01(\x08:1\n\tsizer_all\x12\x1c.google.protobuf.FileOptions\x18\xac\xec\x03 \x01(\x08:A\n\x19goproto_enum_stringer_all\x12\x1c.google.protobuf.FileOptions\x18\xad\xec\x03 \x01(\x08:9\n\x11enum_stringer_all\x12\x1c.google.protobuf.FileOptions\x18\xae\xec\x03 \x01(\x08:<\n\x14unsafe_marshaler_all\x12\x1c.google.protobuf.FileOptions\x18\xaf\xec\x03 \x01(\x08:>\n\x16unsafe_unmarshaler_all\x12\x1c.google.protobuf.FileOptions\x18\xb0\xec\x03 \x01(\x08:B\n\x1agoproto_extensions_map_all\x12\x1c.google.protobuf.FileOptions\x18\xb1\xec\x03 \x01(\x08:@\n\x18goproto_unrecognized_all\x12\x1c.google.protobuf.FileOptions\x18\xb2\xec\x03 \x01(\x08:8\n\x10gogoproto_import\x12\x1c.google.protobuf.FileOptions\x18\xb3\xec\x03 \x01(\x08:6\n\x0eprotosizer_all\x12\x1c.google.protobuf.FileOptions\x18\xb4\xec\x03 \x01(\x08:3\n\x0bcompare_all\x12\x1c.google.protobuf.FileOptions\x18\xb5\xec\x03 \x01(\x08:4\n\x0ctypedecl_all\x12\x1c.google.protobuf.FileOptions\x18\xb6\xec\x03 \x01(\x08:4\n\x0cenumdecl_all\x12\x1c.google.protobuf.FileOptions\x18\xb7\xec\x03 \x01(\x08:<\n\x14goproto_registration\x12\x1c.google.protobuf.FileOptions\x18\xb8\xec\x03 \x01(\x08:7\n\x0fmessagename_all\x12\x1c.google.protobuf.FileOptions\x18\xb9\xec\x03 \x01(\x08:=\n\x15goproto_sizecache_all\x12\x1c.google.protobuf.FileOptions\x18\xba\xec\x03 \x01(\x08:;\n\x13goproto_unkeyed_all\x12\x1c.google.protobuf.FileOptions\x18\xbb\xec\x03 \x01(\x08::\n\x0fgoproto_getters\x12\x1f.google.protobuf.MessageOptions\x18\x81\xf4\x03 \x01(\x08:;\n\x10goproto_stringer\x12\x1f.google.protobuf.MessageOptions\x18\x83\xf4\x03 \x01(\x08:8\n\rverbose_equal\x12\x1f.google.protobuf.MessageOptions\x18\x84\xf4\x03 \x01(\x08:/\n\x04face\x12\x1f.google.protobuf.MessageOptions\x18\x85\xf4\x03 \x01(\x08:3\n\x08gostring\x12\x1f.google.protobuf.MessageOptions\x18\x86\xf4\x03 \x01(\x08:3\n\x08populate\x12\x1f.google.protobuf.MessageOptions\x18\x87\xf4\x03 \x01(\x08:3\n\x08stringer\x12\x1f.google.protobuf.MessageOptions\x18\xc0\x8b\x04 \x01(\x08:2\n\x07onlyone\x12\x1f.google.protobuf.MessageOptions\x18\x89\xf4\x03 \x01(\x08:0\n\x05equal\x12\x1f.google.protobuf.MessageOptions\x18\x8d\xf4\x03 \x01(\x08:6\n\x0bdescription\x12\x1f.google.protobuf.MessageOptions\x18\x8e\xf4\x03 \x01(\x08:2\n\x07testgen\x12\x1f.google.protobuf.MessageOptions\x18\x8f\xf4\x03 \x01(\x08:3\n\x08benchgen\x12\x1f.google.protobuf.MessageOptions\x18\x90\xf4\x03 \x01(\x08:4\n\tmarshaler\x12\x1f.google.protobuf.MessageOptions\x18\x91\xf4\x03 \x01(\x08:6\n\x0bunmarshaler\x12\x1f.google.protobuf.MessageOptions\x18\x92\xf4\x03 \x01(\x08:;\n\x10stable_marshaler\x12\x1f.google.protobuf.MessageOptions\x18\x93\xf4\x03 \x01(\x08:0\n\x05sizer\x12\x1f.google.protobuf.MessageOptions\x18\x94\xf4\x03 \x01(\x08:;\n\x10unsafe_marshaler\x12\x1f.google.protobuf.MessageOptions\x18\x97\xf4\x03 \x01(\x08:=\n\x12unsafe_unmarshaler\x12\x1f.google.protobuf.MessageOptions\x18\x98\xf4\x03 \x01(\x08:A\n\x16goproto_extensions_map\x12\x1f.google.protobuf.MessageOptions\x18\x99\xf4\x03 \x01(\x08:?\n\x14goproto_unrecognized\x12\x1f.google.protobuf.MessageOptions\x18\x9a\xf4\x03 \x01(\x08:5\n\nprotosizer\x12\x1f.google.protobuf.MessageOptions\x18\x9c\xf4\x03 \x01(\x08:2\n\x07compare\x12\x1f.google.protobuf.MessageOptions\x18\x9d\xf4\x03 \x01(\x08:3\n\x08typedecl\x12\x1f.google.protobuf.MessageOptions\x18\x9e\xf4\x03 \x01(\x08:6\n\x0bmessagename\x12\x1f.google.protobuf.MessageOptions\x18\xa1\xf4\x03 \x01(\x08:<\n\x11goproto_sizecache\x12\x1f.google.protobuf.MessageOptions\x18\xa2\xf4\x03 \x01(\x08::\n\x0fgoproto_unkeyed\x12\x1f.google.protobuf.MessageOptions\x18\xa3\xf4\x03 \x01(\x08:1\n\x08nullable\x12\x1d.google.protobuf.FieldOptions\x18\xe9\xfb\x03 \x01(\x08:.\n\x05embed\x12\x1d.google.protobuf.FieldOptions\x18\xea\xfb\x03 \x01(\x08:3\n\ncustomtype\x12\x1d.google.protobuf.FieldOptions\x18\xeb\xfb\x03 \x01(\t:3\n\ncustomname\x12\x1d.google.protobuf.FieldOptions\x18\xec\xfb\x03 \x01(\t:0\n\x07jsontag\x12\x1d.google.protobuf.FieldOptions\x18\xed\xfb\x03 \x01(\t:1\n\x08moretags\x12\x1d.google.protobuf.FieldOptions\x18\xee\xfb\x03 \x01(\t:1\n\x08casttype\x12\x1d.google.protobuf.FieldOptions\x18\xef\xfb\x03 \x01(\t:0\n\x07castkey\x12\x1d.google.protobuf.FieldOptions\x18\xf0\xfb\x03 \x01(\t:2\n\tcastvalue\x12\x1d.google.protobuf.FieldOptions\x18\xf1\xfb\x03 \x01(\t:0\n\x07stdtime\x12\x1d.google.protobuf.FieldOptions\x18\xf2\xfb\x03 \x01(\x08:4\n\x0bstdduration\x12\x1d.google.protobuf.FieldOptions\x18\xf3\xfb\x03 \x01(\x08:3\n\nwktpointer\x12\x1d.google.protobuf.FieldOptions\x18\xf4\xfb\x03 \x01(\x08:5\n\x0ccastrepeated\x12\x1d.google.protobuf.FieldOptions\x18\xf5\xfb\x03 \x01(\tBH\n\x13com.google.protobufB\nGoGoProtosZ%github.com/cosmos/gogoproto/gogoproto')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gogoproto.gogo_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    google_dot_protobuf_dot_descriptor__pb2.EnumOptions.RegisterExtension(goproto_enum_prefix)
    google_dot_protobuf_dot_descriptor__pb2.EnumOptions.RegisterExtension(goproto_enum_stringer)
    google_dot_protobuf_dot_descriptor__pb2.EnumOptions.RegisterExtension(enum_stringer)
    google_dot_protobuf_dot_descriptor__pb2.EnumOptions.RegisterExtension(enum_customname)
    google_dot_protobuf_dot_descriptor__pb2.EnumOptions.RegisterExtension(enumdecl)
    google_dot_protobuf_dot_descriptor__pb2.EnumValueOptions.RegisterExtension(enumvalue_customname)
    google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(goproto_getters_all)
    google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(goproto_enum_prefix_all)
    google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(goproto_stringer_all)
    google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(verbose_equal_all)
    google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(face_all)
    google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(gostring_all)
    google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(populate_all)
    google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(stringer_all)
    google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(onlyone_all)
    google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(equal_all)
    google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(description_all)
    google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(testgen_all)
    google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(benchgen_all)
    google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(marshaler_all)
    google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(unmarshaler_all)
    google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(stable_marshaler_all)
    google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(sizer_all)
    google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(goproto_enum_stringer_all)
    google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(enum_stringer_all)
    google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(unsafe_marshaler_all)
    google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(unsafe_unmarshaler_all)
    google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(goproto_extensions_map_all)
    google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(goproto_unrecognized_all)
    google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(gogoproto_import)
    google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(protosizer_all)
    google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(compare_all)
    google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(typedecl_all)
    google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(enumdecl_all)
    google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(goproto_registration)
    google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(messagename_all)
    google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(goproto_sizecache_all)
    google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(goproto_unkeyed_all)
    google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(goproto_getters)
    google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(goproto_stringer)
    google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(verbose_equal)
    google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(face)
    google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(gostring)
    google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(populate)
    google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(stringer)
    google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(onlyone)
    google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(equal)
    google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(description)
    google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(testgen)
    google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(benchgen)
    google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(marshaler)
    google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(unmarshaler)
    google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(stable_marshaler)
    google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(sizer)
    google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(unsafe_marshaler)
    google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(unsafe_unmarshaler)
    google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(goproto_extensions_map)
    google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(goproto_unrecognized)
    google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(protosizer)
    google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(compare)
    google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(typedecl)
    google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(messagename)
    google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(goproto_sizecache)
    google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(goproto_unkeyed)
    google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(nullable)
    google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(embed)
    google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(customtype)
    google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(customname)
    google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(jsontag)
    google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(moretags)
    google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(casttype)
    google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(castkey)
    google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(castvalue)
    google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(stdtime)
    google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(stdduration)
    google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(wktpointer)
    google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(castrepeated)
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\x13com.google.protobufB\nGoGoProtosZ%github.com/cosmos/gogoproto/gogoproto'