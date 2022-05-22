# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: langsvc/langsvc.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from validate import validate_pb2 as validate_dot_validate__pb2
from program import program_pb2 as program_dot_program__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15langsvc/langsvc.proto\x12\x12\x61utokitteh.langsvc\x1a\x1cgoogle/api/annotations.proto\x1a\x17validate/validate.proto\x1a\x15program/program.proto\"0\n\x05\x43ycle\x12\'\n\x05paths\x18\x01 \x03(\x0b\x32\x18.autokitteh.program.Path\"\x8d\x01\n\x0c\x44\x65pendencies\x12\'\n\x05ready\x18\x01 \x03(\x0b\x32\x18.autokitteh.program.Path\x12)\n\x07missing\x18\x02 \x03(\x0b\x32\x18.autokitteh.program.Path\x12)\n\x06\x63ycles\x18\x03 \x03(\x0b\x32\x19.autokitteh.langsvc.Cycle\"T\n\x1cGetModuleDependenciesRequest\x12\x34\n\x06module\x18\x01 \x01(\x0b\x32\x1a.autokitteh.program.ModuleB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\"O\n\x1dGetModuleDependenciesResponse\x12.\n\x04\x64\x65ps\x18\x01 \x01(\x0b\x32 .autokitteh.langsvc.Dependencies\"W\n!IsCompilerVersionSupportedRequest\x12%\n\x04lang\x18\x01 \x01(\tB\x17\xfa\x42\x14r\x12\x32\x10^[0-9a-zA-Z_-]+$\x12\x0b\n\x03ver\x18\x02 \x01(\t\"7\n\"IsCompilerVersionSupportedResponse\x12\x11\n\tsupported\x18\x01 \x01(\x08\"\xc6\x01\n\x14\x43ompileModuleRequest\x12%\n\x04lang\x18\x01 \x01(\tB\x17\xfa\x42\x14r\x12\x32\x10^[0-9a-zA-Z_-]+$\x12\x36\n\x08predecls\x18\x02 \x03(\tB$\xfa\x42!\x92\x01\x1e\"\x1cr\x1a\x32\x18^[a-zA-Z_][a-zA-Z0-9_]*$\x12\x30\n\x04path\x18\x03 \x01(\x0b\x32\x18.autokitteh.program.PathB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\x12\x0b\n\x03src\x18\x04 \x01(\x0c\x12\x10\n\x08get_deps\x18\x06 \x01(\x08\"}\n\x15\x43ompileModuleResponse\x12\x34\n\x06module\x18\x01 \x01(\x0b\x32\x1a.autokitteh.program.ModuleB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\x12.\n\x04\x64\x65ps\x18\x02 \x01(\x0b\x32 .autokitteh.langsvc.Dependencies\"\x12\n\x10ListLangsRequest\"\x1b\n\x0b\x43\x61talogLang\x12\x0c\n\x04\x65xts\x18\x01 \x03(\t\"\xb3\x01\n\x11ListLangsResponse\x12O\n\x05langs\x18\x01 \x03(\x0b\x32\x30.autokitteh.langsvc.ListLangsResponse.LangsEntryB\x0e\xfa\x42\x0b\x9a\x01\x08\x18\x01\"\x04r\x02\x10\x01\x1aM\n\nLangsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12.\n\x05value\x18\x02 \x01(\x0b\x32\x1f.autokitteh.langsvc.CatalogLang:\x02\x38\x01\x32\xe4\x04\n\x04Lang\x12t\n\tListLangs\x12$.autokitteh.langsvc.ListLangsRequest\x1a%.autokitteh.langsvc.ListLangsResponse\"\x1a\x82\xd3\xe4\x93\x02\x14\x12\x12/api/v1/langs/list\x12\xb7\x01\n\x1aIsCompilerVersionSupported\x12\x35.autokitteh.langsvc.IsCompilerVersionSupportedRequest\x1a\x36.autokitteh.langsvc.IsCompilerVersionSupportedResponse\"*\x82\xd3\xe4\x93\x02$\x12\"/api/v1/langs/{lang}/{ver}/support\x12\xa2\x01\n\x15GetModuleDependencies\x12\x30.autokitteh.langsvc.GetModuleDependenciesRequest\x1a\x31.autokitteh.langsvc.GetModuleDependenciesResponse\"$\x82\xd3\xe4\x93\x02\x1e\"\x19/api/v1/langs/module-deps:\x01*\x12\x86\x01\n\rCompileModule\x12(.autokitteh.langsvc.CompileModuleRequest\x1a).autokitteh.langsvc.CompileModuleResponse\" \x82\xd3\xe4\x93\x02\x1a\"\x15/api/v1/langs/compile:\x01*B\x1fZ\x1dgo.autokitteh.dev/idl/langsvcb\x06proto3')



_CYCLE = DESCRIPTOR.message_types_by_name['Cycle']
_DEPENDENCIES = DESCRIPTOR.message_types_by_name['Dependencies']
_GETMODULEDEPENDENCIESREQUEST = DESCRIPTOR.message_types_by_name['GetModuleDependenciesRequest']
_GETMODULEDEPENDENCIESRESPONSE = DESCRIPTOR.message_types_by_name['GetModuleDependenciesResponse']
_ISCOMPILERVERSIONSUPPORTEDREQUEST = DESCRIPTOR.message_types_by_name['IsCompilerVersionSupportedRequest']
_ISCOMPILERVERSIONSUPPORTEDRESPONSE = DESCRIPTOR.message_types_by_name['IsCompilerVersionSupportedResponse']
_COMPILEMODULEREQUEST = DESCRIPTOR.message_types_by_name['CompileModuleRequest']
_COMPILEMODULERESPONSE = DESCRIPTOR.message_types_by_name['CompileModuleResponse']
_LISTLANGSREQUEST = DESCRIPTOR.message_types_by_name['ListLangsRequest']
_CATALOGLANG = DESCRIPTOR.message_types_by_name['CatalogLang']
_LISTLANGSRESPONSE = DESCRIPTOR.message_types_by_name['ListLangsResponse']
_LISTLANGSRESPONSE_LANGSENTRY = _LISTLANGSRESPONSE.nested_types_by_name['LangsEntry']
Cycle = _reflection.GeneratedProtocolMessageType('Cycle', (_message.Message,), {
  'DESCRIPTOR' : _CYCLE,
  '__module__' : 'langsvc.langsvc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.langsvc.Cycle)
  })
_sym_db.RegisterMessage(Cycle)

Dependencies = _reflection.GeneratedProtocolMessageType('Dependencies', (_message.Message,), {
  'DESCRIPTOR' : _DEPENDENCIES,
  '__module__' : 'langsvc.langsvc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.langsvc.Dependencies)
  })
_sym_db.RegisterMessage(Dependencies)

GetModuleDependenciesRequest = _reflection.GeneratedProtocolMessageType('GetModuleDependenciesRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETMODULEDEPENDENCIESREQUEST,
  '__module__' : 'langsvc.langsvc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.langsvc.GetModuleDependenciesRequest)
  })
_sym_db.RegisterMessage(GetModuleDependenciesRequest)

GetModuleDependenciesResponse = _reflection.GeneratedProtocolMessageType('GetModuleDependenciesResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETMODULEDEPENDENCIESRESPONSE,
  '__module__' : 'langsvc.langsvc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.langsvc.GetModuleDependenciesResponse)
  })
_sym_db.RegisterMessage(GetModuleDependenciesResponse)

IsCompilerVersionSupportedRequest = _reflection.GeneratedProtocolMessageType('IsCompilerVersionSupportedRequest', (_message.Message,), {
  'DESCRIPTOR' : _ISCOMPILERVERSIONSUPPORTEDREQUEST,
  '__module__' : 'langsvc.langsvc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.langsvc.IsCompilerVersionSupportedRequest)
  })
_sym_db.RegisterMessage(IsCompilerVersionSupportedRequest)

IsCompilerVersionSupportedResponse = _reflection.GeneratedProtocolMessageType('IsCompilerVersionSupportedResponse', (_message.Message,), {
  'DESCRIPTOR' : _ISCOMPILERVERSIONSUPPORTEDRESPONSE,
  '__module__' : 'langsvc.langsvc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.langsvc.IsCompilerVersionSupportedResponse)
  })
_sym_db.RegisterMessage(IsCompilerVersionSupportedResponse)

CompileModuleRequest = _reflection.GeneratedProtocolMessageType('CompileModuleRequest', (_message.Message,), {
  'DESCRIPTOR' : _COMPILEMODULEREQUEST,
  '__module__' : 'langsvc.langsvc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.langsvc.CompileModuleRequest)
  })
_sym_db.RegisterMessage(CompileModuleRequest)

CompileModuleResponse = _reflection.GeneratedProtocolMessageType('CompileModuleResponse', (_message.Message,), {
  'DESCRIPTOR' : _COMPILEMODULERESPONSE,
  '__module__' : 'langsvc.langsvc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.langsvc.CompileModuleResponse)
  })
_sym_db.RegisterMessage(CompileModuleResponse)

ListLangsRequest = _reflection.GeneratedProtocolMessageType('ListLangsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTLANGSREQUEST,
  '__module__' : 'langsvc.langsvc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.langsvc.ListLangsRequest)
  })
_sym_db.RegisterMessage(ListLangsRequest)

CatalogLang = _reflection.GeneratedProtocolMessageType('CatalogLang', (_message.Message,), {
  'DESCRIPTOR' : _CATALOGLANG,
  '__module__' : 'langsvc.langsvc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.langsvc.CatalogLang)
  })
_sym_db.RegisterMessage(CatalogLang)

ListLangsResponse = _reflection.GeneratedProtocolMessageType('ListLangsResponse', (_message.Message,), {

  'LangsEntry' : _reflection.GeneratedProtocolMessageType('LangsEntry', (_message.Message,), {
    'DESCRIPTOR' : _LISTLANGSRESPONSE_LANGSENTRY,
    '__module__' : 'langsvc.langsvc_pb2'
    # @@protoc_insertion_point(class_scope:autokitteh.langsvc.ListLangsResponse.LangsEntry)
    })
  ,
  'DESCRIPTOR' : _LISTLANGSRESPONSE,
  '__module__' : 'langsvc.langsvc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.langsvc.ListLangsResponse)
  })
_sym_db.RegisterMessage(ListLangsResponse)
_sym_db.RegisterMessage(ListLangsResponse.LangsEntry)

_LANG = DESCRIPTOR.services_by_name['Lang']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\035go.autokitteh.dev/idl/langsvc'
  _GETMODULEDEPENDENCIESREQUEST.fields_by_name['module']._options = None
  _GETMODULEDEPENDENCIESREQUEST.fields_by_name['module']._serialized_options = b'\372B\005\212\001\002\020\001'
  _ISCOMPILERVERSIONSUPPORTEDREQUEST.fields_by_name['lang']._options = None
  _ISCOMPILERVERSIONSUPPORTEDREQUEST.fields_by_name['lang']._serialized_options = b'\372B\024r\0222\020^[0-9a-zA-Z_-]+$'
  _COMPILEMODULEREQUEST.fields_by_name['lang']._options = None
  _COMPILEMODULEREQUEST.fields_by_name['lang']._serialized_options = b'\372B\024r\0222\020^[0-9a-zA-Z_-]+$'
  _COMPILEMODULEREQUEST.fields_by_name['predecls']._options = None
  _COMPILEMODULEREQUEST.fields_by_name['predecls']._serialized_options = b'\372B!\222\001\036\"\034r\0322\030^[a-zA-Z_][a-zA-Z0-9_]*$'
  _COMPILEMODULEREQUEST.fields_by_name['path']._options = None
  _COMPILEMODULEREQUEST.fields_by_name['path']._serialized_options = b'\372B\005\212\001\002\020\001'
  _COMPILEMODULERESPONSE.fields_by_name['module']._options = None
  _COMPILEMODULERESPONSE.fields_by_name['module']._serialized_options = b'\372B\005\212\001\002\020\001'
  _LISTLANGSRESPONSE_LANGSENTRY._options = None
  _LISTLANGSRESPONSE_LANGSENTRY._serialized_options = b'8\001'
  _LISTLANGSRESPONSE.fields_by_name['langs']._options = None
  _LISTLANGSRESPONSE.fields_by_name['langs']._serialized_options = b'\372B\013\232\001\010\030\001\"\004r\002\020\001'
  _LANG.methods_by_name['ListLangs']._options = None
  _LANG.methods_by_name['ListLangs']._serialized_options = b'\202\323\344\223\002\024\022\022/api/v1/langs/list'
  _LANG.methods_by_name['IsCompilerVersionSupported']._options = None
  _LANG.methods_by_name['IsCompilerVersionSupported']._serialized_options = b'\202\323\344\223\002$\022\"/api/v1/langs/{lang}/{ver}/support'
  _LANG.methods_by_name['GetModuleDependencies']._options = None
  _LANG.methods_by_name['GetModuleDependencies']._serialized_options = b'\202\323\344\223\002\036\"\031/api/v1/langs/module-deps:\001*'
  _LANG.methods_by_name['CompileModule']._options = None
  _LANG.methods_by_name['CompileModule']._serialized_options = b'\202\323\344\223\002\032\"\025/api/v1/langs/compile:\001*'
  _CYCLE._serialized_start=123
  _CYCLE._serialized_end=171
  _DEPENDENCIES._serialized_start=174
  _DEPENDENCIES._serialized_end=315
  _GETMODULEDEPENDENCIESREQUEST._serialized_start=317
  _GETMODULEDEPENDENCIESREQUEST._serialized_end=401
  _GETMODULEDEPENDENCIESRESPONSE._serialized_start=403
  _GETMODULEDEPENDENCIESRESPONSE._serialized_end=482
  _ISCOMPILERVERSIONSUPPORTEDREQUEST._serialized_start=484
  _ISCOMPILERVERSIONSUPPORTEDREQUEST._serialized_end=571
  _ISCOMPILERVERSIONSUPPORTEDRESPONSE._serialized_start=573
  _ISCOMPILERVERSIONSUPPORTEDRESPONSE._serialized_end=628
  _COMPILEMODULEREQUEST._serialized_start=631
  _COMPILEMODULEREQUEST._serialized_end=829
  _COMPILEMODULERESPONSE._serialized_start=831
  _COMPILEMODULERESPONSE._serialized_end=956
  _LISTLANGSREQUEST._serialized_start=958
  _LISTLANGSREQUEST._serialized_end=976
  _CATALOGLANG._serialized_start=978
  _CATALOGLANG._serialized_end=1005
  _LISTLANGSRESPONSE._serialized_start=1008
  _LISTLANGSRESPONSE._serialized_end=1187
  _LISTLANGSRESPONSE_LANGSENTRY._serialized_start=1110
  _LISTLANGSRESPONSE_LANGSENTRY._serialized_end=1187
  _LANG._serialized_start=1190
  _LANG._serialized_end=1802
# @@protoc_insertion_point(module_scope)
