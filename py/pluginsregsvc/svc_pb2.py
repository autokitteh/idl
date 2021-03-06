# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pluginsregsvc/svc.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from plugin import plugin_pb2 as plugin_dot_plugin__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17pluginsregsvc/svc.proto\x12\x18\x61utokitteh.pluginsregsvc\x1a\x13plugin/plugin.proto\x1a\x17validate/validate.proto\"\x95\x01\n\x0fRegisterRequest\x12\x43\n\x02id\x18\x01 \x01(\tB7\xfa\x42\x34r220^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z][0-9a-zA-Z_-]+$\x12=\n\x08settings\x18\x02 \x01(\x0b\x32!.autokitteh.plugin.PluginSettingsB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\"\x12\n\x10RegisterResponse\"G\n\x0bListRequest\x12\x38\n\x0c\x61\x63\x63ount_name\x18\x01 \x01(\tB\"\xfa\x42\x1fr\x1d\x32\x18^[a-zA-Z][0-9a-zA-Z_-]+$\xd0\x01\x01\"Y\n\x0cListResponse\x12I\n\x03ids\x18\x01 \x03(\tB<\xfa\x42\x39\x92\x01\x36\"4r220^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z][0-9a-zA-Z_-]+$\"Q\n\nGetRequest\x12\x43\n\x02id\x18\x01 \x01(\tB7\xfa\x42\x34r220^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z][0-9a-zA-Z_-]+$\"B\n\x0bGetResponse\x12\x33\n\x06plugin\x18\x01 \x01(\x0b\x32\x19.autokitteh.plugin.PluginB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\x32\x9f\x02\n\x0fPluginsRegistry\x12U\n\x04List\x12%.autokitteh.pluginsregsvc.ListRequest\x1a&.autokitteh.pluginsregsvc.ListResponse\x12R\n\x03Get\x12$.autokitteh.pluginsregsvc.GetRequest\x1a%.autokitteh.pluginsregsvc.GetResponse\x12\x61\n\x08Register\x12).autokitteh.pluginsregsvc.RegisterRequest\x1a*.autokitteh.pluginsregsvc.RegisterResponseB(Z&go.autokitteh.dev/idl/go/pluginsregsvcb\x06proto3')



_REGISTERREQUEST = DESCRIPTOR.message_types_by_name['RegisterRequest']
_REGISTERRESPONSE = DESCRIPTOR.message_types_by_name['RegisterResponse']
_LISTREQUEST = DESCRIPTOR.message_types_by_name['ListRequest']
_LISTRESPONSE = DESCRIPTOR.message_types_by_name['ListResponse']
_GETREQUEST = DESCRIPTOR.message_types_by_name['GetRequest']
_GETRESPONSE = DESCRIPTOR.message_types_by_name['GetResponse']
RegisterRequest = _reflection.GeneratedProtocolMessageType('RegisterRequest', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERREQUEST,
  '__module__' : 'pluginsregsvc.svc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.pluginsregsvc.RegisterRequest)
  })
_sym_db.RegisterMessage(RegisterRequest)

RegisterResponse = _reflection.GeneratedProtocolMessageType('RegisterResponse', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERRESPONSE,
  '__module__' : 'pluginsregsvc.svc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.pluginsregsvc.RegisterResponse)
  })
_sym_db.RegisterMessage(RegisterResponse)

ListRequest = _reflection.GeneratedProtocolMessageType('ListRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTREQUEST,
  '__module__' : 'pluginsregsvc.svc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.pluginsregsvc.ListRequest)
  })
_sym_db.RegisterMessage(ListRequest)

ListResponse = _reflection.GeneratedProtocolMessageType('ListResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTRESPONSE,
  '__module__' : 'pluginsregsvc.svc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.pluginsregsvc.ListResponse)
  })
_sym_db.RegisterMessage(ListResponse)

GetRequest = _reflection.GeneratedProtocolMessageType('GetRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETREQUEST,
  '__module__' : 'pluginsregsvc.svc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.pluginsregsvc.GetRequest)
  })
_sym_db.RegisterMessage(GetRequest)

GetResponse = _reflection.GeneratedProtocolMessageType('GetResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETRESPONSE,
  '__module__' : 'pluginsregsvc.svc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.pluginsregsvc.GetResponse)
  })
_sym_db.RegisterMessage(GetResponse)

_PLUGINSREGISTRY = DESCRIPTOR.services_by_name['PluginsRegistry']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z&go.autokitteh.dev/idl/go/pluginsregsvc'
  _REGISTERREQUEST.fields_by_name['id']._options = None
  _REGISTERREQUEST.fields_by_name['id']._serialized_options = b'\372B4r220^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z][0-9a-zA-Z_-]+$'
  _REGISTERREQUEST.fields_by_name['settings']._options = None
  _REGISTERREQUEST.fields_by_name['settings']._serialized_options = b'\372B\005\212\001\002\020\001'
  _LISTREQUEST.fields_by_name['account_name']._options = None
  _LISTREQUEST.fields_by_name['account_name']._serialized_options = b'\372B\037r\0352\030^[a-zA-Z][0-9a-zA-Z_-]+$\320\001\001'
  _LISTRESPONSE.fields_by_name['ids']._options = None
  _LISTRESPONSE.fields_by_name['ids']._serialized_options = b'\372B9\222\0016\"4r220^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z][0-9a-zA-Z_-]+$'
  _GETREQUEST.fields_by_name['id']._options = None
  _GETREQUEST.fields_by_name['id']._serialized_options = b'\372B4r220^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z][0-9a-zA-Z_-]+$'
  _GETRESPONSE.fields_by_name['plugin']._options = None
  _GETRESPONSE.fields_by_name['plugin']._serialized_options = b'\372B\005\212\001\002\020\001'
  _REGISTERREQUEST._serialized_start=100
  _REGISTERREQUEST._serialized_end=249
  _REGISTERRESPONSE._serialized_start=251
  _REGISTERRESPONSE._serialized_end=269
  _LISTREQUEST._serialized_start=271
  _LISTREQUEST._serialized_end=342
  _LISTRESPONSE._serialized_start=344
  _LISTRESPONSE._serialized_end=433
  _GETREQUEST._serialized_start=435
  _GETREQUEST._serialized_end=516
  _GETRESPONSE._serialized_start=518
  _GETRESPONSE._serialized_end=584
  _PLUGINSREGISTRY._serialized_start=587
  _PLUGINSREGISTRY._serialized_end=874
# @@protoc_insertion_point(module_scope)
