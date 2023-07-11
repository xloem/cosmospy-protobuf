"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15test_proto/test.proto\x12\ntest_proto"&\n\x06GoEnum\x12\x1c\n\x03foo\x18\x01 \x02(\x0e2\x0f.test_proto.FOO"*\n\x0bGoTestField\x12\r\n\x05Label\x18\x01 \x02(\t\x12\x0c\n\x04Type\x18\x02 \x02(\t"\xe3\x16\n\x06GoTest\x12%\n\x04Kind\x18\x01 \x02(\x0e2\x17.test_proto.GoTest.KIND\x12\r\n\x05Table\x18\x02 \x01(\t\x12\r\n\x05Param\x18\x03 \x01(\x05\x12.\n\rRequiredField\x18\x04 \x02(\x0b2\x17.test_proto.GoTestField\x12.\n\rRepeatedField\x18\x05 \x03(\x0b2\x17.test_proto.GoTestField\x12.\n\rOptionalField\x18\x06 \x01(\x0b2\x17.test_proto.GoTestField\x12\x17\n\x0fF_Bool_required\x18\n \x02(\x08\x12\x18\n\x10F_Int32_required\x18\x0b \x02(\x05\x12\x18\n\x10F_Int64_required\x18\x0c \x02(\x03\x12\x1a\n\x12F_Fixed32_required\x18\r \x02(\x07\x12\x1a\n\x12F_Fixed64_required\x18\x0e \x02(\x06\x12\x19\n\x11F_Uint32_required\x18\x0f \x02(\r\x12\x19\n\x11F_Uint64_required\x18\x10 \x02(\x04\x12\x18\n\x10F_Float_required\x18\x11 \x02(\x02\x12\x19\n\x11F_Double_required\x18\x12 \x02(\x01\x12\x19\n\x11F_String_required\x18\x13 \x02(\t\x12\x18\n\x10F_Bytes_required\x18e \x02(\x0c\x12\x19\n\x11F_Sint32_required\x18f \x02(\x11\x12\x19\n\x11F_Sint64_required\x18g \x02(\x12\x12\x1b\n\x13F_Sfixed32_required\x18h \x02(\x0f\x12\x1b\n\x13F_Sfixed64_required\x18i \x02(\x10\x12\x17\n\x0fF_Bool_repeated\x18\x14 \x03(\x08\x12\x18\n\x10F_Int32_repeated\x18\x15 \x03(\x05\x12\x18\n\x10F_Int64_repeated\x18\x16 \x03(\x03\x12\x1a\n\x12F_Fixed32_repeated\x18\x17 \x03(\x07\x12\x1a\n\x12F_Fixed64_repeated\x18\x18 \x03(\x06\x12\x19\n\x11F_Uint32_repeated\x18\x19 \x03(\r\x12\x19\n\x11F_Uint64_repeated\x18\x1a \x03(\x04\x12\x18\n\x10F_Float_repeated\x18\x1b \x03(\x02\x12\x19\n\x11F_Double_repeated\x18\x1c \x03(\x01\x12\x19\n\x11F_String_repeated\x18\x1d \x03(\t\x12\x19\n\x10F_Bytes_repeated\x18\xc9\x01 \x03(\x0c\x12\x1a\n\x11F_Sint32_repeated\x18\xca\x01 \x03(\x11\x12\x1a\n\x11F_Sint64_repeated\x18\xcb\x01 \x03(\x12\x12\x1c\n\x13F_Sfixed32_repeated\x18\xcc\x01 \x03(\x0f\x12\x1c\n\x13F_Sfixed64_repeated\x18\xcd\x01 \x03(\x10\x12\x17\n\x0fF_Bool_optional\x18\x1e \x01(\x08\x12\x18\n\x10F_Int32_optional\x18\x1f \x01(\x05\x12\x18\n\x10F_Int64_optional\x18  \x01(\x03\x12\x1a\n\x12F_Fixed32_optional\x18! \x01(\x07\x12\x1a\n\x12F_Fixed64_optional\x18" \x01(\x06\x12\x19\n\x11F_Uint32_optional\x18# \x01(\r\x12\x19\n\x11F_Uint64_optional\x18$ \x01(\x04\x12\x18\n\x10F_Float_optional\x18% \x01(\x02\x12\x19\n\x11F_Double_optional\x18& \x01(\x01\x12\x19\n\x11F_String_optional\x18\' \x01(\t\x12\x19\n\x10F_Bytes_optional\x18\xad\x02 \x01(\x0c\x12\x1a\n\x11F_Sint32_optional\x18\xae\x02 \x01(\x11\x12\x1a\n\x11F_Sint64_optional\x18\xaf\x02 \x01(\x12\x12\x1c\n\x13F_Sfixed32_optional\x18\xb0\x02 \x01(\x0f\x12\x1c\n\x13F_Sfixed64_optional\x18\xb1\x02 \x01(\x10\x12\x1e\n\x10F_Bool_defaulted\x18( \x01(\x08:\x04true\x12\x1d\n\x11F_Int32_defaulted\x18) \x01(\x05:\x0232\x12\x1d\n\x11F_Int64_defaulted\x18* \x01(\x03:\x0264\x12 \n\x13F_Fixed32_defaulted\x18+ \x01(\x07:\x03320\x12 \n\x13F_Fixed64_defaulted\x18, \x01(\x06:\x03640\x12 \n\x12F_Uint32_defaulted\x18- \x01(\r:\x043200\x12 \n\x12F_Uint64_defaulted\x18. \x01(\x04:\x046400\x12!\n\x11F_Float_defaulted\x18/ \x01(\x02:\x06314159\x12"\n\x12F_Double_defaulted\x180 \x01(\x01:\x06271828\x12,\n\x12F_String_defaulted\x181 \x01(\t:\x10hello, "world!"\n\x12#\n\x11F_Bytes_defaulted\x18\x91\x03 \x01(\x0c:\x07Bignose\x12 \n\x12F_Sint32_defaulted\x18\x92\x03 \x01(\x11:\x03-32\x12 \n\x12F_Sint64_defaulted\x18\x93\x03 \x01(\x12:\x03-64\x12"\n\x14F_Sfixed32_defaulted\x18\x94\x03 \x01(\x0f:\x03-32\x12"\n\x14F_Sfixed64_defaulted\x18\x95\x03 \x01(\x10:\x03-64\x12"\n\x16F_Bool_repeated_packed\x182 \x03(\x08B\x02\x10\x01\x12#\n\x17F_Int32_repeated_packed\x183 \x03(\x05B\x02\x10\x01\x12#\n\x17F_Int64_repeated_packed\x184 \x03(\x03B\x02\x10\x01\x12%\n\x19F_Fixed32_repeated_packed\x185 \x03(\x07B\x02\x10\x01\x12%\n\x19F_Fixed64_repeated_packed\x186 \x03(\x06B\x02\x10\x01\x12$\n\x18F_Uint32_repeated_packed\x187 \x03(\rB\x02\x10\x01\x12$\n\x18F_Uint64_repeated_packed\x188 \x03(\x04B\x02\x10\x01\x12#\n\x17F_Float_repeated_packed\x189 \x03(\x02B\x02\x10\x01\x12$\n\x18F_Double_repeated_packed\x18: \x03(\x01B\x02\x10\x01\x12%\n\x18F_Sint32_repeated_packed\x18\xf6\x03 \x03(\x11B\x02\x10\x01\x12%\n\x18F_Sint64_repeated_packed\x18\xf7\x03 \x03(\x12B\x02\x10\x01\x12\'\n\x1aF_Sfixed32_repeated_packed\x18\xf8\x03 \x03(\x0fB\x02\x10\x01\x12\'\n\x1aF_Sfixed64_repeated_packed\x18\xf9\x03 \x03(\x10B\x02\x10\x01\x127\n\rrequiredgroup\x18F \x02(\n2 .test_proto.GoTest.RequiredGroup\x127\n\rrepeatedgroup\x18P \x03(\n2 .test_proto.GoTest.RepeatedGroup\x127\n\roptionalgroup\x18Z \x01(\n2 .test_proto.GoTest.OptionalGroup\x1a&\n\rRequiredGroup\x12\x15\n\rRequiredField\x18G \x02(\t\x1a&\n\rRepeatedGroup\x12\x15\n\rRequiredField\x18Q \x02(\t\x1a&\n\rOptionalGroup\x12\x15\n\rRequiredField\x18[ \x02(\t"\x98\x01\n\x04KIND\x12\x08\n\x04VOID\x10\x00\x12\x08\n\x04BOOL\x10\x01\x12\t\n\x05BYTES\x10\x02\x12\x0f\n\x0bFINGERPRINT\x10\x03\x12\t\n\x05FLOAT\x10\x04\x12\x07\n\x03INT\x10\x05\x12\n\n\x06STRING\x10\x06\x12\x08\n\x04TIME\x10\x07\x12\t\n\x05TUPLE\x10\x08\x12\t\n\x05ARRAY\x10\t\x12\x07\n\x03MAP\x10\n\x12\t\n\x05TABLE\x10\x0b\x12\x0c\n\x08FUNCTION\x10\x0c"m\n\x18GoTestRequiredGroupField\x129\n\x05group\x18\x01 \x02(\n2*.test_proto.GoTestRequiredGroupField.Group\x1a\x16\n\x05Group\x12\r\n\x05Field\x18\x02 \x02(\x05"\xce\x01\n\nGoSkipTest\x12\x12\n\nskip_int32\x18\x0b \x02(\x05\x12\x14\n\x0cskip_fixed32\x18\x0c \x02(\x07\x12\x14\n\x0cskip_fixed64\x18\r \x02(\x06\x12\x13\n\x0bskip_string\x18\x0e \x02(\t\x123\n\tskipgroup\x18\x0f \x02(\n2 .test_proto.GoSkipTest.SkipGroup\x1a6\n\tSkipGroup\x12\x13\n\x0bgroup_int32\x18\x10 \x02(\x05\x12\x14\n\x0cgroup_string\x18\x11 \x02(\t"\x1a\n\rNonPackedTest\x12\t\n\x01a\x18\x01 \x03(\x05"\x1b\n\nPackedTest\x12\r\n\x01b\x18\x01 \x03(\x05B\x02\x10\x01" \n\x06MaxTag\x12\x16\n\nlast_field\x18\xff\xff\xff\xff\x01 \x01(\t"`\n\nOldMessage\x12-\n\x06nested\x18\x01 \x01(\x0b2\x1d.test_proto.OldMessage.Nested\x12\x0b\n\x03num\x18\x02 \x01(\x05\x1a\x16\n\x06Nested\x12\x0c\n\x04name\x18\x01 \x01(\t"t\n\nNewMessage\x12-\n\x06nested\x18\x01 \x01(\x0b2\x1d.test_proto.NewMessage.Nested\x12\x0b\n\x03num\x18\x02 \x01(\x03\x1a*\n\x06Nested\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nfood_group\x18\x02 \x01(\t"C\n\x0cInnerMessage\x12\x0c\n\x04host\x18\x01 \x02(\t\x12\x12\n\x04port\x18\x02 \x01(\x05:\x044000\x12\x11\n\tconnected\x18\x03 \x01(\x08"m\n\x0cOtherMessage\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12\r\n\x05value\x18\x02 \x01(\x0c\x12\x0e\n\x06weight\x18\x03 \x01(\x02\x12\'\n\x05inner\x18\x04 \x01(\x0b2\x18.test_proto.InnerMessage*\x08\x08d\x10\x80\x80\x80\x80\x02"R\n\x14RequiredInnerMessage\x12:\n\x18leo_finally_won_an_oscar\x18\x01 \x02(\x0b2\x18.test_proto.InnerMessage"\xdc\x03\n\tMyMessage\x12\r\n\x05count\x18\x01 \x02(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05quote\x18\x03 \x01(\t\x12\x0b\n\x03pet\x18\x04 \x03(\t\x12\'\n\x05inner\x18\x05 \x01(\x0b2\x18.test_proto.InnerMessage\x12(\n\x06others\x18\x06 \x03(\x0b2\x18.test_proto.OtherMessage\x12;\n\x11we_must_go_deeper\x18\r \x01(\x0b2 .test_proto.RequiredInnerMessage\x12+\n\trep_inner\x18\x0c \x03(\x0b2\x18.test_proto.InnerMessage\x12-\n\x08bikeshed\x18\x07 \x01(\x0e2\x1b.test_proto.MyMessage.Color\x122\n\tsomegroup\x18\x08 \x01(\n2\x1f.test_proto.MyMessage.SomeGroup\x12\x11\n\trep_bytes\x18\n \x03(\x0c\x12\x10\n\x08bigfloat\x18\x0b \x01(\x01\x1a \n\tSomeGroup\x12\x13\n\x0bgroup_field\x18\t \x01(\x05"%\n\x05Color\x12\x07\n\x03RED\x10\x00\x12\t\n\x05GREEN\x10\x01\x12\x08\n\x04BLUE\x10\x02*\x08\x08d\x10\x80\x80\x80\x80\x02"\xf8\x01\n\x03Ext\x12\x0c\n\x04data\x18\x01 \x01(\t\x120\n\tmap_field\x18\x02 \x03(\x0b2\x1d.test_proto.Ext.MapFieldEntry\x1a/\n\rMapFieldEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x05:\x028\x0124\n\x04more\x12\x15.test_proto.MyMessage\x18g \x01(\x0b2\x0f.test_proto.Ext2#\n\x04text\x12\x15.test_proto.MyMessage\x18h \x01(\t2%\n\x06number\x12\x15.test_proto.MyMessage\x18i \x01(\x05"@\n\x10ComplexExtension\x12\r\n\x05first\x18\x01 \x01(\x05\x12\x0e\n\x06second\x18\x02 \x01(\x05\x12\r\n\x05third\x18\x03 \x03(\x05"G\n\x0fDefaultsMessage"*\n\x0cDefaultsEnum\x12\x08\n\x04ZERO\x10\x00\x12\x07\n\x03ONE\x10\x01\x12\x07\n\x03TWO\x10\x02*\x08\x08d\x10\x80\x80\x80\x80\x02"\x1c\n\x0cMyMessageSet*\x08\x08d\x10\xff\xff\xff\xff\x07:\x02\x08\x01"\x07\n\x05Empty"g\n\x0bMessageList\x120\n\x07message\x18\x01 \x03(\n2\x1f.test_proto.MessageList.Message\x1a&\n\x07Message\x12\x0c\n\x04name\x18\x02 \x02(\t\x12\r\n\x05count\x18\x03 \x02(\x05"4\n\x07Strings\x12\x14\n\x0cstring_field\x18\x01 \x01(\t\x12\x13\n\x0bbytes_field\x18\x02 \x01(\x0c"\x9c\x04\n\x08Defaults\x12\x14\n\x06F_Bool\x18\x01 \x01(\x08:\x04true\x12\x13\n\x07F_Int32\x18\x02 \x01(\x05:\x0232\x12\x13\n\x07F_Int64\x18\x03 \x01(\x03:\x0264\x12\x16\n\tF_Fixed32\x18\x04 \x01(\x07:\x03320\x12\x16\n\tF_Fixed64\x18\x05 \x01(\x06:\x03640\x12\x16\n\x08F_Uint32\x18\x06 \x01(\r:\x043200\x12\x16\n\x08F_Uint64\x18\x07 \x01(\x04:\x046400\x12\x17\n\x07F_Float\x18\x08 \x01(\x02:\x06314159\x12\x18\n\x08F_Double\x18\t \x01(\x01:\x06271828\x12"\n\x08F_String\x18\n \x01(\t:\x10hello, "world!"\n\x12\x18\n\x07F_Bytes\x18\x0b \x01(\x0c:\x07Bignose\x12\x15\n\x08F_Sint32\x18\x0c \x01(\x11:\x03-32\x12\x15\n\x08F_Sint64\x18\r \x01(\x12:\x03-64\x121\n\x06F_Enum\x18\x0e \x01(\x0e2\x1a.test_proto.Defaults.Color:\x05GREEN\x12\x13\n\x06F_Pinf\x18\x0f \x01(\x02:\x03inf\x12\x14\n\x06F_Ninf\x18\x10 \x01(\x02:\x04-inf\x12\x12\n\x05F_Nan\x18\x11 \x01(\x02:\x03nan\x12$\n\x03sub\x18\x12 \x01(\x0b2\x17.test_proto.SubDefaults\x12\x12\n\x08str_zero\x18\x13 \x01(\t:\x00"%\n\x05Color\x12\x07\n\x03RED\x10\x00\x12\t\n\x05GREEN\x10\x01\x12\x08\n\x04BLUE\x10\x02"\x1b\n\x0bSubDefaults\x12\x0c\n\x01n\x18\x01 \x01(\x03:\x017"O\n\x0cRepeatedEnum\x12-\n\x05color\x18\x01 \x03(\x0e2\x1e.test_proto.RepeatedEnum.Color"\x10\n\x05Color\x12\x07\n\x03RED\x10\x01"\x9a\x01\n\x0cMoreRepeated\x12\r\n\x05bools\x18\x01 \x03(\x08\x12\x18\n\x0cbools_packed\x18\x02 \x03(\x08B\x02\x10\x01\x12\x0c\n\x04ints\x18\x03 \x03(\x05\x12\x17\n\x0bints_packed\x18\x04 \x03(\x05B\x02\x10\x01\x12\x19\n\rint64s_packed\x18\x07 \x03(\x03B\x02\x10\x01\x12\x0f\n\x07strings\x18\x05 \x03(\t\x12\x0e\n\x06fixeds\x18\x06 \x03(\x07"=\n\x08GroupOld\x12!\n\x01g\x18e \x01(\n2\x16.test_proto.GroupOld.G\x1a\x0e\n\x01G\x12\t\n\x01x\x18\x02 \x01(\x05"H\n\x08GroupNew\x12!\n\x01g\x18e \x01(\n2\x16.test_proto.GroupNew.G\x1a\x19\n\x01G\x12\t\n\x01x\x18\x02 \x01(\x05\x12\t\n\x01y\x18\x03 \x01(\x05")\n\rFloatingPoint\x12\t\n\x01f\x18\x01 \x02(\x01\x12\r\n\x05exact\x18\x02 \x01(\x08"\xfc\x03\n\x0eMessageWithMap\x12A\n\x0cname_mapping\x18\x01 \x03(\x0b2+.test_proto.MessageWithMap.NameMappingEntry\x12?\n\x0bmsg_mapping\x18\x02 \x03(\x0b2*.test_proto.MessageWithMap.MsgMappingEntry\x12A\n\x0cbyte_mapping\x18\x03 \x03(\x0b2+.test_proto.MessageWithMap.ByteMappingEntry\x12<\n\nstr_to_str\x18\x04 \x03(\x0b2(.test_proto.MessageWithMap.StrToStrEntry\x1a2\n\x10NameMappingEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1aL\n\x0fMsgMappingEntry\x12\x0b\n\x03key\x18\x01 \x01(\x12\x12(\n\x05value\x18\x02 \x01(\x0b2\x19.test_proto.FloatingPoint:\x028\x01\x1a2\n\x10ByteMappingEntry\x12\x0b\n\x03key\x18\x01 \x01(\x08\x12\r\n\x05value\x18\x02 \x01(\x0c:\x028\x01\x1a/\n\rStrToStrEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\xea\x03\n\x05Oneof\x12\x10\n\x06F_Bool\x18\x01 \x01(\x08H\x00\x12\x11\n\x07F_Int32\x18\x02 \x01(\x05H\x00\x12\x11\n\x07F_Int64\x18\x03 \x01(\x03H\x00\x12\x13\n\tF_Fixed32\x18\x04 \x01(\x07H\x00\x12\x13\n\tF_Fixed64\x18\x05 \x01(\x06H\x00\x12\x12\n\x08F_Uint32\x18\x06 \x01(\rH\x00\x12\x12\n\x08F_Uint64\x18\x07 \x01(\x04H\x00\x12\x11\n\x07F_Float\x18\x08 \x01(\x02H\x00\x12\x12\n\x08F_Double\x18\t \x01(\x01H\x00\x12\x12\n\x08F_String\x18\n \x01(\tH\x00\x12\x11\n\x07F_Bytes\x18\x0b \x01(\x0cH\x00\x12\x12\n\x08F_Sint32\x18\x0c \x01(\x11H\x00\x12\x12\n\x08F_Sint64\x18\r \x01(\x12H\x00\x12-\n\x06F_Enum\x18\x0e \x01(\x0e2\x1b.test_proto.MyMessage.ColorH\x00\x12,\n\tF_Message\x18\x0f \x01(\x0b2\x17.test_proto.GoTestFieldH\x00\x12,\n\x07f_group\x18\x10 \x01(\n2\x19.test_proto.Oneof.F_GroupH\x00\x12\x1b\n\rF_Largest_Tag\x18\xff\xff\xff\xff\x01 \x01(\x05H\x00\x12\x0f\n\x05value\x18d \x01(\x05H\x01\x1a\x14\n\x07F_Group\x12\t\n\x01x\x18\x11 \x01(\x05B\x07\n\x05unionB\t\n\x07tormato"\xbe\x01\n\nCommunique\x12\x13\n\x0bmake_me_cry\x18\x01 \x01(\x08\x12\x10\n\x06number\x18\x05 \x01(\x05H\x00\x12\x0e\n\x04name\x18\x06 \x01(\tH\x00\x12\x0e\n\x04data\x18\x07 \x01(\x0cH\x00\x12\x10\n\x06temp_c\x18\x08 \x01(\x01H\x00\x12*\n\x03col\x18\t \x01(\x0e2\x1b.test_proto.MyMessage.ColorH\x00\x12"\n\x03msg\x18\n \x01(\x0b2\x13.test_proto.StringsH\x00B\x07\n\x05union"\x8e\x02\n\x08TestUTF8\x12\x0e\n\x06scalar\x18\x01 \x01(\t\x12\x0e\n\x06vector\x18\x02 \x03(\t\x12\x0f\n\x05field\x18\x03 \x01(\tH\x00\x121\n\x07map_key\x18\x04 \x03(\x0b2 .test_proto.TestUTF8.MapKeyEntry\x125\n\tmap_value\x18\x05 \x03(\x0b2".test_proto.TestUTF8.MapValueEntry\x1a-\n\x0bMapKeyEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x03:\x028\x01\x1a/\n\rMapValueEntry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01B\x07\n\x05oneof*\x0f\n\x03FOO\x12\x08\n\x04FOO1\x10\x01:\'\n\x08greeting\x12\x15.test_proto.MyMessage\x18j \x03(\t:H\n\x07complex\x12\x18.test_proto.OtherMessage\x18\xc8\x01 \x01(\x0b2\x1c.test_proto.ComplexExtension:J\n\tr_complex\x12\x18.test_proto.OtherMessage\x18\xc9\x01 \x03(\x0b2\x1c.test_proto.ComplexExtension:6\n\x11no_default_double\x12\x1b.test_proto.DefaultsMessage\x18e \x01(\x01:5\n\x10no_default_float\x12\x1b.test_proto.DefaultsMessage\x18f \x01(\x02:5\n\x10no_default_int32\x12\x1b.test_proto.DefaultsMessage\x18g \x01(\x05:5\n\x10no_default_int64\x12\x1b.test_proto.DefaultsMessage\x18h \x01(\x03:6\n\x11no_default_uint32\x12\x1b.test_proto.DefaultsMessage\x18i \x01(\r:6\n\x11no_default_uint64\x12\x1b.test_proto.DefaultsMessage\x18j \x01(\x04:6\n\x11no_default_sint32\x12\x1b.test_proto.DefaultsMessage\x18k \x01(\x11:6\n\x11no_default_sint64\x12\x1b.test_proto.DefaultsMessage\x18l \x01(\x12:7\n\x12no_default_fixed32\x12\x1b.test_proto.DefaultsMessage\x18m \x01(\x07:7\n\x12no_default_fixed64\x12\x1b.test_proto.DefaultsMessage\x18n \x01(\x06:8\n\x13no_default_sfixed32\x12\x1b.test_proto.DefaultsMessage\x18o \x01(\x0f:8\n\x13no_default_sfixed64\x12\x1b.test_proto.DefaultsMessage\x18p \x01(\x10:4\n\x0fno_default_bool\x12\x1b.test_proto.DefaultsMessage\x18q \x01(\x08:6\n\x11no_default_string\x12\x1b.test_proto.DefaultsMessage\x18r \x01(\t:5\n\x10no_default_bytes\x12\x1b.test_proto.DefaultsMessage\x18s \x01(\x0c:^\n\x0fno_default_enum\x12\x1b.test_proto.DefaultsMessage\x18t \x01(\x0e2(.test_proto.DefaultsMessage.DefaultsEnum:<\n\x0edefault_double\x12\x1b.test_proto.DefaultsMessage\x18\xc9\x01 \x01(\x01:\x063.1415:9\n\rdefault_float\x12\x1b.test_proto.DefaultsMessage\x18\xca\x01 \x01(\x02:\x043.14:7\n\rdefault_int32\x12\x1b.test_proto.DefaultsMessage\x18\xcb\x01 \x01(\x05:\x0242:7\n\rdefault_int64\x12\x1b.test_proto.DefaultsMessage\x18\xcc\x01 \x01(\x03:\x0243:8\n\x0edefault_uint32\x12\x1b.test_proto.DefaultsMessage\x18\xcd\x01 \x01(\r:\x0244:8\n\x0edefault_uint64\x12\x1b.test_proto.DefaultsMessage\x18\xce\x01 \x01(\x04:\x0245:8\n\x0edefault_sint32\x12\x1b.test_proto.DefaultsMessage\x18\xcf\x01 \x01(\x11:\x0246:8\n\x0edefault_sint64\x12\x1b.test_proto.DefaultsMessage\x18\xd0\x01 \x01(\x12:\x0247:9\n\x0fdefault_fixed32\x12\x1b.test_proto.DefaultsMessage\x18\xd1\x01 \x01(\x07:\x0248:9\n\x0fdefault_fixed64\x12\x1b.test_proto.DefaultsMessage\x18\xd2\x01 \x01(\x06:\x0249::\n\x10default_sfixed32\x12\x1b.test_proto.DefaultsMessage\x18\xd3\x01 \x01(\x0f:\x0250::\n\x10default_sfixed64\x12\x1b.test_proto.DefaultsMessage\x18\xd4\x01 \x01(\x10:\x0251:8\n\x0cdefault_bool\x12\x1b.test_proto.DefaultsMessage\x18\xd5\x01 \x01(\x08:\x04true:K\n\x0edefault_string\x12\x1b.test_proto.DefaultsMessage\x18\xd6\x01 \x01(\t:\x15Hello, string,def=foo:A\n\rdefault_bytes\x12\x1b.test_proto.DefaultsMessage\x18\xd7\x01 \x01(\x0c:\x0cHello, bytes:a\n\x0cdefault_enum\x12\x1b.test_proto.DefaultsMessage\x18\xd8\x01 \x01(\x0e2(.test_proto.DefaultsMessage.DefaultsEnum:\x03ONE::\n\x04x201\x12\x18.test_proto.MyMessageSet\x18\xc9\x01 \x01(\x0b2\x11.test_proto.Empty::\n\x04x202\x12\x18.test_proto.MyMessageSet\x18\xca\x01 \x01(\x0b2\x11.test_proto.Empty::\n\x04x203\x12\x18.test_proto.MyMessageSet\x18\xcb\x01 \x01(\x0b2\x11.test_proto.Empty::\n\x04x204\x12\x18.test_proto.MyMessageSet\x18\xcc\x01 \x01(\x0b2\x11.test_proto.Empty::\n\x04x205\x12\x18.test_proto.MyMessageSet\x18\xcd\x01 \x01(\x0b2\x11.test_proto.Empty::\n\x04x206\x12\x18.test_proto.MyMessageSet\x18\xce\x01 \x01(\x0b2\x11.test_proto.Empty::\n\x04x207\x12\x18.test_proto.MyMessageSet\x18\xcf\x01 \x01(\x0b2\x11.test_proto.Empty::\n\x04x208\x12\x18.test_proto.MyMessageSet\x18\xd0\x01 \x01(\x0b2\x11.test_proto.Empty::\n\x04x209\x12\x18.test_proto.MyMessageSet\x18\xd1\x01 \x01(\x0b2\x11.test_proto.Empty::\n\x04x210\x12\x18.test_proto.MyMessageSet\x18\xd2\x01 \x01(\x0b2\x11.test_proto.Empty::\n\x04x211\x12\x18.test_proto.MyMessageSet\x18\xd3\x01 \x01(\x0b2\x11.test_proto.Empty::\n\x04x212\x12\x18.test_proto.MyMessageSet\x18\xd4\x01 \x01(\x0b2\x11.test_proto.Empty::\n\x04x213\x12\x18.test_proto.MyMessageSet\x18\xd5\x01 \x01(\x0b2\x11.test_proto.Empty::\n\x04x214\x12\x18.test_proto.MyMessageSet\x18\xd6\x01 \x01(\x0b2\x11.test_proto.Empty::\n\x04x215\x12\x18.test_proto.MyMessageSet\x18\xd7\x01 \x01(\x0b2\x11.test_proto.Empty::\n\x04x216\x12\x18.test_proto.MyMessageSet\x18\xd8\x01 \x01(\x0b2\x11.test_proto.Empty::\n\x04x217\x12\x18.test_proto.MyMessageSet\x18\xd9\x01 \x01(\x0b2\x11.test_proto.Empty::\n\x04x218\x12\x18.test_proto.MyMessageSet\x18\xda\x01 \x01(\x0b2\x11.test_proto.Empty::\n\x04x219\x12\x18.test_proto.MyMessageSet\x18\xdb\x01 \x01(\x0b2\x11.test_proto.Empty::\n\x04x220\x12\x18.test_proto.MyMessageSet\x18\xdc\x01 \x01(\x0b2\x11.test_proto.Empty::\n\x04x221\x12\x18.test_proto.MyMessageSet\x18\xdd\x01 \x01(\x0b2\x11.test_proto.Empty::\n\x04x222\x12\x18.test_proto.MyMessageSet\x18\xde\x01 \x01(\x0b2\x11.test_proto.Empty::\n\x04x223\x12\x18.test_proto.MyMessageSet\x18\xdf\x01 \x01(\x0b2\x11.test_proto.Empty::\n\x04x224\x12\x18.test_proto.MyMessageSet\x18\xe0\x01 \x01(\x0b2\x11.test_proto.Empty::\n\x04x225\x12\x18.test_proto.MyMessageSet\x18\xe1\x01 \x01(\x0b2\x11.test_proto.Empty::\n\x04x226\x12\x18.test_proto.MyMessageSet\x18\xe2\x01 \x01(\x0b2\x11.test_proto.Empty::\n\x04x227\x12\x18.test_proto.MyMessageSet\x18\xe3\x01 \x01(\x0b2\x11.test_proto.Empty::\n\x04x228\x12\x18.test_proto.MyMessageSet\x18\xe4\x01 \x01(\x0b2\x11.test_proto.Empty::\n\x04x229\x12\x18.test_proto.MyMessageSet\x18\xe5\x01 \x01(\x0b2\x11.test_proto.Empty::\n\x04x230\x12\x18.test_proto.MyMessageSet\x18\xe6\x01 \x01(\x0b2\x11.test_proto.Empty::\n\x04x231\x12\x18.test_proto.MyMessageSet\x18\xe7\x01 \x01(\x0b2\x11.test_proto.Empty::\n\x04x232\x12\x18.test_proto.MyMessageSet\x18\xe8\x01 \x01(\x0b2\x11.test_proto.Empty::\n\x04x233\x12\x18.test_proto.MyMessageSet\x18\xe9\x01 \x01(\x0b2\x11.test_proto.Empty::\n\x04x234\x12\x18.test_proto.MyMessageSet\x18\xea\x01 \x01(\x0b2\x11.test_proto.Empty::\n\x04x235\x12\x18.test_proto.MyMessageSet\x18\xeb\x01 \x01(\x0b2\x11.test_proto.Empty::\n\x04x236\x12\x18.test_proto.MyMessageSet\x18\xec\x01 \x01(\x0b2\x11.test_proto.Empty::\n\x04x237\x12\x18.test_proto.MyMessageSet\x18\xed\x01 \x01(\x0b2\x11.test_proto.Empty::\n\x04x238\x12\x18.test_proto.MyMessageSet\x18\xee\x01 \x01(\x0b2\x11.test_proto.Empty::\n\x04x239\x12\x18.test_proto.MyMessageSet\x18\xef\x01 \x01(\x0b2\x11.test_proto.Empty::\n\x04x240\x12\x18.test_proto.MyMessageSet\x18\xf0\x01 \x01(\x0b2\x11.test_proto.Empty::\n\x04x241\x12\x18.test_proto.MyMessageSet\x18\xf1\x01 \x01(\x0b2\x11.test_proto.Empty::\n\x04x242\x12\x18.test_proto.MyMessageSet\x18\xf2\x01 \x01(\x0b2\x11.test_proto.Empty::\n\x04x243\x12\x18.test_proto.MyMessageSet\x18\xf3\x01 \x01(\x0b2\x11.test_proto.Empty::\n\x04x244\x12\x18.test_proto.MyMessageSet\x18\xf4\x01 \x01(\x0b2\x11.test_proto.Empty::\n\x04x245\x12\x18.test_proto.MyMessageSet\x18\xf5\x01 \x01(\x0b2\x11.test_proto.Empty::\n\x04x246\x12\x18.test_proto.MyMessageSet\x18\xf6\x01 \x01(\x0b2\x11.test_proto.Empty::\n\x04x247\x12\x18.test_proto.MyMessageSet\x18\xf7\x01 \x01(\x0b2\x11.test_proto.Empty::\n\x04x248\x12\x18.test_proto.MyMessageSet\x18\xf8\x01 \x01(\x0b2\x11.test_proto.Empty::\n\x04x249\x12\x18.test_proto.MyMessageSet\x18\xf9\x01 \x01(\x0b2\x11.test_proto.Empty::\n\x04x250\x12\x18.test_proto.MyMessageSet\x18\xfa\x01 \x01(\x0b2\x11.test_proto.EmptyB+Z)github.com/gogo/protobuf/proto/test_proto')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'test_proto.test_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    MyMessage.RegisterExtension(greeting)
    OtherMessage.RegisterExtension(complex)
    OtherMessage.RegisterExtension(r_complex)
    DefaultsMessage.RegisterExtension(no_default_double)
    DefaultsMessage.RegisterExtension(no_default_float)
    DefaultsMessage.RegisterExtension(no_default_int32)
    DefaultsMessage.RegisterExtension(no_default_int64)
    DefaultsMessage.RegisterExtension(no_default_uint32)
    DefaultsMessage.RegisterExtension(no_default_uint64)
    DefaultsMessage.RegisterExtension(no_default_sint32)
    DefaultsMessage.RegisterExtension(no_default_sint64)
    DefaultsMessage.RegisterExtension(no_default_fixed32)
    DefaultsMessage.RegisterExtension(no_default_fixed64)
    DefaultsMessage.RegisterExtension(no_default_sfixed32)
    DefaultsMessage.RegisterExtension(no_default_sfixed64)
    DefaultsMessage.RegisterExtension(no_default_bool)
    DefaultsMessage.RegisterExtension(no_default_string)
    DefaultsMessage.RegisterExtension(no_default_bytes)
    DefaultsMessage.RegisterExtension(no_default_enum)
    DefaultsMessage.RegisterExtension(default_double)
    DefaultsMessage.RegisterExtension(default_float)
    DefaultsMessage.RegisterExtension(default_int32)
    DefaultsMessage.RegisterExtension(default_int64)
    DefaultsMessage.RegisterExtension(default_uint32)
    DefaultsMessage.RegisterExtension(default_uint64)
    DefaultsMessage.RegisterExtension(default_sint32)
    DefaultsMessage.RegisterExtension(default_sint64)
    DefaultsMessage.RegisterExtension(default_fixed32)
    DefaultsMessage.RegisterExtension(default_fixed64)
    DefaultsMessage.RegisterExtension(default_sfixed32)
    DefaultsMessage.RegisterExtension(default_sfixed64)
    DefaultsMessage.RegisterExtension(default_bool)
    DefaultsMessage.RegisterExtension(default_string)
    DefaultsMessage.RegisterExtension(default_bytes)
    DefaultsMessage.RegisterExtension(default_enum)
    MyMessageSet.RegisterExtension(x201)
    MyMessageSet.RegisterExtension(x202)
    MyMessageSet.RegisterExtension(x203)
    MyMessageSet.RegisterExtension(x204)
    MyMessageSet.RegisterExtension(x205)
    MyMessageSet.RegisterExtension(x206)
    MyMessageSet.RegisterExtension(x207)
    MyMessageSet.RegisterExtension(x208)
    MyMessageSet.RegisterExtension(x209)
    MyMessageSet.RegisterExtension(x210)
    MyMessageSet.RegisterExtension(x211)
    MyMessageSet.RegisterExtension(x212)
    MyMessageSet.RegisterExtension(x213)
    MyMessageSet.RegisterExtension(x214)
    MyMessageSet.RegisterExtension(x215)
    MyMessageSet.RegisterExtension(x216)
    MyMessageSet.RegisterExtension(x217)
    MyMessageSet.RegisterExtension(x218)
    MyMessageSet.RegisterExtension(x219)
    MyMessageSet.RegisterExtension(x220)
    MyMessageSet.RegisterExtension(x221)
    MyMessageSet.RegisterExtension(x222)
    MyMessageSet.RegisterExtension(x223)
    MyMessageSet.RegisterExtension(x224)
    MyMessageSet.RegisterExtension(x225)
    MyMessageSet.RegisterExtension(x226)
    MyMessageSet.RegisterExtension(x227)
    MyMessageSet.RegisterExtension(x228)
    MyMessageSet.RegisterExtension(x229)
    MyMessageSet.RegisterExtension(x230)
    MyMessageSet.RegisterExtension(x231)
    MyMessageSet.RegisterExtension(x232)
    MyMessageSet.RegisterExtension(x233)
    MyMessageSet.RegisterExtension(x234)
    MyMessageSet.RegisterExtension(x235)
    MyMessageSet.RegisterExtension(x236)
    MyMessageSet.RegisterExtension(x237)
    MyMessageSet.RegisterExtension(x238)
    MyMessageSet.RegisterExtension(x239)
    MyMessageSet.RegisterExtension(x240)
    MyMessageSet.RegisterExtension(x241)
    MyMessageSet.RegisterExtension(x242)
    MyMessageSet.RegisterExtension(x243)
    MyMessageSet.RegisterExtension(x244)
    MyMessageSet.RegisterExtension(x245)
    MyMessageSet.RegisterExtension(x246)
    MyMessageSet.RegisterExtension(x247)
    MyMessageSet.RegisterExtension(x248)
    MyMessageSet.RegisterExtension(x249)
    MyMessageSet.RegisterExtension(x250)
    MyMessage.RegisterExtension(_EXT.extensions_by_name['more'])
    MyMessage.RegisterExtension(_EXT.extensions_by_name['text'])
    MyMessage.RegisterExtension(_EXT.extensions_by_name['number'])
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z)github.com/gogo/protobuf/proto/test_proto'
    _GOTEST.fields_by_name['F_Bool_repeated_packed']._options = None
    _GOTEST.fields_by_name['F_Bool_repeated_packed']._serialized_options = b'\x10\x01'
    _GOTEST.fields_by_name['F_Int32_repeated_packed']._options = None
    _GOTEST.fields_by_name['F_Int32_repeated_packed']._serialized_options = b'\x10\x01'
    _GOTEST.fields_by_name['F_Int64_repeated_packed']._options = None
    _GOTEST.fields_by_name['F_Int64_repeated_packed']._serialized_options = b'\x10\x01'
    _GOTEST.fields_by_name['F_Fixed32_repeated_packed']._options = None
    _GOTEST.fields_by_name['F_Fixed32_repeated_packed']._serialized_options = b'\x10\x01'
    _GOTEST.fields_by_name['F_Fixed64_repeated_packed']._options = None
    _GOTEST.fields_by_name['F_Fixed64_repeated_packed']._serialized_options = b'\x10\x01'
    _GOTEST.fields_by_name['F_Uint32_repeated_packed']._options = None
    _GOTEST.fields_by_name['F_Uint32_repeated_packed']._serialized_options = b'\x10\x01'
    _GOTEST.fields_by_name['F_Uint64_repeated_packed']._options = None
    _GOTEST.fields_by_name['F_Uint64_repeated_packed']._serialized_options = b'\x10\x01'
    _GOTEST.fields_by_name['F_Float_repeated_packed']._options = None
    _GOTEST.fields_by_name['F_Float_repeated_packed']._serialized_options = b'\x10\x01'
    _GOTEST.fields_by_name['F_Double_repeated_packed']._options = None
    _GOTEST.fields_by_name['F_Double_repeated_packed']._serialized_options = b'\x10\x01'
    _GOTEST.fields_by_name['F_Sint32_repeated_packed']._options = None
    _GOTEST.fields_by_name['F_Sint32_repeated_packed']._serialized_options = b'\x10\x01'
    _GOTEST.fields_by_name['F_Sint64_repeated_packed']._options = None
    _GOTEST.fields_by_name['F_Sint64_repeated_packed']._serialized_options = b'\x10\x01'
    _GOTEST.fields_by_name['F_Sfixed32_repeated_packed']._options = None
    _GOTEST.fields_by_name['F_Sfixed32_repeated_packed']._serialized_options = b'\x10\x01'
    _GOTEST.fields_by_name['F_Sfixed64_repeated_packed']._options = None
    _GOTEST.fields_by_name['F_Sfixed64_repeated_packed']._serialized_options = b'\x10\x01'
    _PACKEDTEST.fields_by_name['b']._options = None
    _PACKEDTEST.fields_by_name['b']._serialized_options = b'\x10\x01'
    _EXT_MAPFIELDENTRY._options = None
    _EXT_MAPFIELDENTRY._serialized_options = b'8\x01'
    _MYMESSAGESET._options = None
    _MYMESSAGESET._serialized_options = b'\x08\x01'
    _MOREREPEATED.fields_by_name['bools_packed']._options = None
    _MOREREPEATED.fields_by_name['bools_packed']._serialized_options = b'\x10\x01'
    _MOREREPEATED.fields_by_name['ints_packed']._options = None
    _MOREREPEATED.fields_by_name['ints_packed']._serialized_options = b'\x10\x01'
    _MOREREPEATED.fields_by_name['int64s_packed']._options = None
    _MOREREPEATED.fields_by_name['int64s_packed']._serialized_options = b'\x10\x01'
    _MESSAGEWITHMAP_NAMEMAPPINGENTRY._options = None
    _MESSAGEWITHMAP_NAMEMAPPINGENTRY._serialized_options = b'8\x01'
    _MESSAGEWITHMAP_MSGMAPPINGENTRY._options = None
    _MESSAGEWITHMAP_MSGMAPPINGENTRY._serialized_options = b'8\x01'
    _MESSAGEWITHMAP_BYTEMAPPINGENTRY._options = None
    _MESSAGEWITHMAP_BYTEMAPPINGENTRY._serialized_options = b'8\x01'
    _MESSAGEWITHMAP_STRTOSTRENTRY._options = None
    _MESSAGEWITHMAP_STRTOSTRENTRY._serialized_options = b'8\x01'
    _TESTUTF8_MAPKEYENTRY._options = None
    _TESTUTF8_MAPKEYENTRY._serialized_options = b'8\x01'
    _TESTUTF8_MAPVALUEENTRY._options = None
    _TESTUTF8_MAPVALUEENTRY._serialized_options = b'8\x01'
    _globals['_FOO']._serialized_start = 7457
    _globals['_FOO']._serialized_end = 7472
    _globals['_GOENUM']._serialized_start = 37
    _globals['_GOENUM']._serialized_end = 75
    _globals['_GOTESTFIELD']._serialized_start = 77
    _globals['_GOTESTFIELD']._serialized_end = 119
    _globals['_GOTEST']._serialized_start = 122
    _globals['_GOTEST']._serialized_end = 3037
    _globals['_GOTEST_REQUIREDGROUP']._serialized_start = 2764
    _globals['_GOTEST_REQUIREDGROUP']._serialized_end = 2802
    _globals['_GOTEST_REPEATEDGROUP']._serialized_start = 2804
    _globals['_GOTEST_REPEATEDGROUP']._serialized_end = 2842
    _globals['_GOTEST_OPTIONALGROUP']._serialized_start = 2844
    _globals['_GOTEST_OPTIONALGROUP']._serialized_end = 2882
    _globals['_GOTEST_KIND']._serialized_start = 2885
    _globals['_GOTEST_KIND']._serialized_end = 3037
    _globals['_GOTESTREQUIREDGROUPFIELD']._serialized_start = 3039
    _globals['_GOTESTREQUIREDGROUPFIELD']._serialized_end = 3148
    _globals['_GOTESTREQUIREDGROUPFIELD_GROUP']._serialized_start = 3126
    _globals['_GOTESTREQUIREDGROUPFIELD_GROUP']._serialized_end = 3148
    _globals['_GOSKIPTEST']._serialized_start = 3151
    _globals['_GOSKIPTEST']._serialized_end = 3357
    _globals['_GOSKIPTEST_SKIPGROUP']._serialized_start = 3303
    _globals['_GOSKIPTEST_SKIPGROUP']._serialized_end = 3357
    _globals['_NONPACKEDTEST']._serialized_start = 3359
    _globals['_NONPACKEDTEST']._serialized_end = 3385
    _globals['_PACKEDTEST']._serialized_start = 3387
    _globals['_PACKEDTEST']._serialized_end = 3414
    _globals['_MAXTAG']._serialized_start = 3416
    _globals['_MAXTAG']._serialized_end = 3448
    _globals['_OLDMESSAGE']._serialized_start = 3450
    _globals['_OLDMESSAGE']._serialized_end = 3546
    _globals['_OLDMESSAGE_NESTED']._serialized_start = 3524
    _globals['_OLDMESSAGE_NESTED']._serialized_end = 3546
    _globals['_NEWMESSAGE']._serialized_start = 3548
    _globals['_NEWMESSAGE']._serialized_end = 3664
    _globals['_NEWMESSAGE_NESTED']._serialized_start = 3622
    _globals['_NEWMESSAGE_NESTED']._serialized_end = 3664
    _globals['_INNERMESSAGE']._serialized_start = 3666
    _globals['_INNERMESSAGE']._serialized_end = 3733
    _globals['_OTHERMESSAGE']._serialized_start = 3735
    _globals['_OTHERMESSAGE']._serialized_end = 3844
    _globals['_REQUIREDINNERMESSAGE']._serialized_start = 3846
    _globals['_REQUIREDINNERMESSAGE']._serialized_end = 3928
    _globals['_MYMESSAGE']._serialized_start = 3931
    _globals['_MYMESSAGE']._serialized_end = 4407
    _globals['_MYMESSAGE_SOMEGROUP']._serialized_start = 4326
    _globals['_MYMESSAGE_SOMEGROUP']._serialized_end = 4358
    _globals['_MYMESSAGE_COLOR']._serialized_start = 4360
    _globals['_MYMESSAGE_COLOR']._serialized_end = 4397
    _globals['_EXT']._serialized_start = 4410
    _globals['_EXT']._serialized_end = 4658
    _globals['_EXT_MAPFIELDENTRY']._serialized_start = 4481
    _globals['_EXT_MAPFIELDENTRY']._serialized_end = 4528
    _globals['_COMPLEXEXTENSION']._serialized_start = 4660
    _globals['_COMPLEXEXTENSION']._serialized_end = 4724
    _globals['_DEFAULTSMESSAGE']._serialized_start = 4726
    _globals['_DEFAULTSMESSAGE']._serialized_end = 4797
    _globals['_DEFAULTSMESSAGE_DEFAULTSENUM']._serialized_start = 4745
    _globals['_DEFAULTSMESSAGE_DEFAULTSENUM']._serialized_end = 4787
    _globals['_MYMESSAGESET']._serialized_start = 4799
    _globals['_MYMESSAGESET']._serialized_end = 4827
    _globals['_EMPTY']._serialized_start = 4829
    _globals['_EMPTY']._serialized_end = 4836
    _globals['_MESSAGELIST']._serialized_start = 4838
    _globals['_MESSAGELIST']._serialized_end = 4941
    _globals['_MESSAGELIST_MESSAGE']._serialized_start = 4903
    _globals['_MESSAGELIST_MESSAGE']._serialized_end = 4941
    _globals['_STRINGS']._serialized_start = 4943
    _globals['_STRINGS']._serialized_end = 4995
    _globals['_DEFAULTS']._serialized_start = 4998
    _globals['_DEFAULTS']._serialized_end = 5538
    _globals['_DEFAULTS_COLOR']._serialized_start = 4360
    _globals['_DEFAULTS_COLOR']._serialized_end = 4397
    _globals['_SUBDEFAULTS']._serialized_start = 5540
    _globals['_SUBDEFAULTS']._serialized_end = 5567
    _globals['_REPEATEDENUM']._serialized_start = 5569
    _globals['_REPEATEDENUM']._serialized_end = 5648
    _globals['_REPEATEDENUM_COLOR']._serialized_start = 5632
    _globals['_REPEATEDENUM_COLOR']._serialized_end = 5648
    _globals['_MOREREPEATED']._serialized_start = 5651
    _globals['_MOREREPEATED']._serialized_end = 5805
    _globals['_GROUPOLD']._serialized_start = 5807
    _globals['_GROUPOLD']._serialized_end = 5868
    _globals['_GROUPOLD_G']._serialized_start = 5854
    _globals['_GROUPOLD_G']._serialized_end = 5868
    _globals['_GROUPNEW']._serialized_start = 5870
    _globals['_GROUPNEW']._serialized_end = 5942
    _globals['_GROUPNEW_G']._serialized_start = 5917
    _globals['_GROUPNEW_G']._serialized_end = 5942
    _globals['_FLOATINGPOINT']._serialized_start = 5944
    _globals['_FLOATINGPOINT']._serialized_end = 5985
    _globals['_MESSAGEWITHMAP']._serialized_start = 5988
    _globals['_MESSAGEWITHMAP']._serialized_end = 6496
    _globals['_MESSAGEWITHMAP_NAMEMAPPINGENTRY']._serialized_start = 6267
    _globals['_MESSAGEWITHMAP_NAMEMAPPINGENTRY']._serialized_end = 6317
    _globals['_MESSAGEWITHMAP_MSGMAPPINGENTRY']._serialized_start = 6319
    _globals['_MESSAGEWITHMAP_MSGMAPPINGENTRY']._serialized_end = 6395
    _globals['_MESSAGEWITHMAP_BYTEMAPPINGENTRY']._serialized_start = 6397
    _globals['_MESSAGEWITHMAP_BYTEMAPPINGENTRY']._serialized_end = 6447
    _globals['_MESSAGEWITHMAP_STRTOSTRENTRY']._serialized_start = 6449
    _globals['_MESSAGEWITHMAP_STRTOSTRENTRY']._serialized_end = 6496
    _globals['_ONEOF']._serialized_start = 6499
    _globals['_ONEOF']._serialized_end = 6989
    _globals['_ONEOF_F_GROUP']._serialized_start = 6949
    _globals['_ONEOF_F_GROUP']._serialized_end = 6969
    _globals['_COMMUNIQUE']._serialized_start = 6992
    _globals['_COMMUNIQUE']._serialized_end = 7182
    _globals['_TESTUTF8']._serialized_start = 7185
    _globals['_TESTUTF8']._serialized_end = 7455
    _globals['_TESTUTF8_MAPKEYENTRY']._serialized_start = 7352
    _globals['_TESTUTF8_MAPKEYENTRY']._serialized_end = 7397
    _globals['_TESTUTF8_MAPVALUEENTRY']._serialized_start = 7399
    _globals['_TESTUTF8_MAPVALUEENTRY']._serialized_end = 7446