# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: slackeventsrc/src.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17slackeventsrc/src.proto\x12\x18\x61utokitteh.slackeventsrc\x1a\x1cgoogle/api/annotations.proto\x1a\x17validate/validate.proto\"\x9b\x01\n\x0b\x42indRequest\x12\x43\n\nproject_id\x18\x01 \x01(\tB/\xfa\x42,r*2(^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z0-9_-]+$\x12-\n\x04name\x18\x02 \x01(\tB\x1f\xfa\x42\x1cr\x1a\x32\x18^[a-zA-Z_][a-zA-Z0-9_]*$\x12\x18\n\x07team_id\x18\x03 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01\"\x0e\n\x0c\x42indResponse\"\x83\x01\n\rUnbindRequest\x12\x43\n\nproject_id\x18\x01 \x01(\tB/\xfa\x42,r*2(^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z0-9_-]+$\x12-\n\x04name\x18\x02 \x01(\tB\x1f\xfa\x42\x1cr\x1a\x32\x18^[a-zA-Z_][a-zA-Z0-9_]*$\"\x10\n\x0eUnbindResponse2\x8c\x02\n\x10SlackEventSource\x12w\n\x04\x42ind\x12%.autokitteh.slackeventsrc.BindRequest\x1a&.autokitteh.slackeventsrc.BindResponse\" \x82\xd3\xe4\x93\x02\x1a\"\x15/api/v1/slacksrc/bind:\x01*\x12\x7f\n\x06Unbind\x12\'.autokitteh.slackeventsrc.UnbindRequest\x1a(.autokitteh.slackeventsrc.UnbindResponse\"\"\x82\xd3\xe4\x93\x02\x1c\"\x17/api/v1/slacksrc/unbind:\x01*B%Z#go.autokitteh.dev/idl/slackeventsrcb\x06proto3')



_BINDREQUEST = DESCRIPTOR.message_types_by_name['BindRequest']
_BINDRESPONSE = DESCRIPTOR.message_types_by_name['BindResponse']
_UNBINDREQUEST = DESCRIPTOR.message_types_by_name['UnbindRequest']
_UNBINDRESPONSE = DESCRIPTOR.message_types_by_name['UnbindResponse']
BindRequest = _reflection.GeneratedProtocolMessageType('BindRequest', (_message.Message,), {
  'DESCRIPTOR' : _BINDREQUEST,
  '__module__' : 'slackeventsrc.src_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.slackeventsrc.BindRequest)
  })
_sym_db.RegisterMessage(BindRequest)

BindResponse = _reflection.GeneratedProtocolMessageType('BindResponse', (_message.Message,), {
  'DESCRIPTOR' : _BINDRESPONSE,
  '__module__' : 'slackeventsrc.src_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.slackeventsrc.BindResponse)
  })
_sym_db.RegisterMessage(BindResponse)

UnbindRequest = _reflection.GeneratedProtocolMessageType('UnbindRequest', (_message.Message,), {
  'DESCRIPTOR' : _UNBINDREQUEST,
  '__module__' : 'slackeventsrc.src_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.slackeventsrc.UnbindRequest)
  })
_sym_db.RegisterMessage(UnbindRequest)

UnbindResponse = _reflection.GeneratedProtocolMessageType('UnbindResponse', (_message.Message,), {
  'DESCRIPTOR' : _UNBINDRESPONSE,
  '__module__' : 'slackeventsrc.src_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.slackeventsrc.UnbindResponse)
  })
_sym_db.RegisterMessage(UnbindResponse)

_SLACKEVENTSOURCE = DESCRIPTOR.services_by_name['SlackEventSource']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z#go.autokitteh.dev/idl/slackeventsrc'
  _BINDREQUEST.fields_by_name['project_id']._options = None
  _BINDREQUEST.fields_by_name['project_id']._serialized_options = b'\372B,r*2(^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z0-9_-]+$'
  _BINDREQUEST.fields_by_name['name']._options = None
  _BINDREQUEST.fields_by_name['name']._serialized_options = b'\372B\034r\0322\030^[a-zA-Z_][a-zA-Z0-9_]*$'
  _BINDREQUEST.fields_by_name['team_id']._options = None
  _BINDREQUEST.fields_by_name['team_id']._serialized_options = b'\372B\004r\002\020\001'
  _UNBINDREQUEST.fields_by_name['project_id']._options = None
  _UNBINDREQUEST.fields_by_name['project_id']._serialized_options = b'\372B,r*2(^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z0-9_-]+$'
  _UNBINDREQUEST.fields_by_name['name']._options = None
  _UNBINDREQUEST.fields_by_name['name']._serialized_options = b'\372B\034r\0322\030^[a-zA-Z_][a-zA-Z0-9_]*$'
  _SLACKEVENTSOURCE.methods_by_name['Bind']._options = None
  _SLACKEVENTSOURCE.methods_by_name['Bind']._serialized_options = b'\202\323\344\223\002\032\"\025/api/v1/slacksrc/bind:\001*'
  _SLACKEVENTSOURCE.methods_by_name['Unbind']._options = None
  _SLACKEVENTSOURCE.methods_by_name['Unbind']._serialized_options = b'\202\323\344\223\002\034\"\027/api/v1/slacksrc/unbind:\001*'
  _BINDREQUEST._serialized_start=109
  _BINDREQUEST._serialized_end=264
  _BINDRESPONSE._serialized_start=266
  _BINDRESPONSE._serialized_end=280
  _UNBINDREQUEST._serialized_start=283
  _UNBINDREQUEST._serialized_end=414
  _UNBINDRESPONSE._serialized_start=416
  _UNBINDRESPONSE._serialized_end=432
  _SLACKEVENTSOURCE._serialized_start=435
  _SLACKEVENTSOURCE._serialized_end=703
# @@protoc_insertion_point(module_scope)
