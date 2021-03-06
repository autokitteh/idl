# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: eventsrc/src.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12\x65ventsrc/src.proto\x12\x13\x61utokitteh.eventsrc\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17validate/validate.proto\"5\n\x13\x45ventSourceSettings\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12\r\n\x05types\x18\x02 \x03(\t\"\xee\x01\n\x0b\x45ventSource\x12\x43\n\x02id\x18\x01 \x01(\tB7\xfa\x42\x34r220^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z][0-9a-zA-Z_-]+$\x12:\n\x08settings\x18\x03 \x01(\x0b\x32(.autokitteh.eventsrc.EventSourceSettings\x12.\n\ncreated_at\x18\x64 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x65 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"4\n!EventSourceProjectBindingSettings\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\"\xc9\x03\n\x19\x45ventSourceProjectBinding\x12G\n\x06src_id\x18\x01 \x01(\tB7\xfa\x42\x34r220^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z][0-9a-zA-Z_-]+$\x12\x43\n\nproject_id\x18\x02 \x01(\tB/\xfa\x42,r*2(^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z0-9_-]+$\x12\x30\n\x04name\x18\x03 \x01(\tB\"\xfa\x42\x1fr\x1d\x32\x18^[a-zA-Z_][a-zA-Z0-9_]*$\xd0\x01\x01\x12\x19\n\x11\x61ssociation_token\x18\x04 \x01(\t\x12\x15\n\rsource_config\x18\x05 \x01(\t\x12\x10\n\x08\x61pproved\x18\x06 \x01(\x08\x12H\n\x08settings\x18\n \x01(\x0b\x32\x36.autokitteh.eventsrc.EventSourceProjectBindingSettings\x12.\n\ncreated_at\x18\x64 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x65 \x01(\x0b\x32\x1a.google.protobuf.TimestampB#Z!go.autokitteh.dev/idl/go/eventsrcb\x06proto3')



_EVENTSOURCESETTINGS = DESCRIPTOR.message_types_by_name['EventSourceSettings']
_EVENTSOURCE = DESCRIPTOR.message_types_by_name['EventSource']
_EVENTSOURCEPROJECTBINDINGSETTINGS = DESCRIPTOR.message_types_by_name['EventSourceProjectBindingSettings']
_EVENTSOURCEPROJECTBINDING = DESCRIPTOR.message_types_by_name['EventSourceProjectBinding']
EventSourceSettings = _reflection.GeneratedProtocolMessageType('EventSourceSettings', (_message.Message,), {
  'DESCRIPTOR' : _EVENTSOURCESETTINGS,
  '__module__' : 'eventsrc.src_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.eventsrc.EventSourceSettings)
  })
_sym_db.RegisterMessage(EventSourceSettings)

EventSource = _reflection.GeneratedProtocolMessageType('EventSource', (_message.Message,), {
  'DESCRIPTOR' : _EVENTSOURCE,
  '__module__' : 'eventsrc.src_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.eventsrc.EventSource)
  })
_sym_db.RegisterMessage(EventSource)

EventSourceProjectBindingSettings = _reflection.GeneratedProtocolMessageType('EventSourceProjectBindingSettings', (_message.Message,), {
  'DESCRIPTOR' : _EVENTSOURCEPROJECTBINDINGSETTINGS,
  '__module__' : 'eventsrc.src_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.eventsrc.EventSourceProjectBindingSettings)
  })
_sym_db.RegisterMessage(EventSourceProjectBindingSettings)

EventSourceProjectBinding = _reflection.GeneratedProtocolMessageType('EventSourceProjectBinding', (_message.Message,), {
  'DESCRIPTOR' : _EVENTSOURCEPROJECTBINDING,
  '__module__' : 'eventsrc.src_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.eventsrc.EventSourceProjectBinding)
  })
_sym_db.RegisterMessage(EventSourceProjectBinding)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z!go.autokitteh.dev/idl/go/eventsrc'
  _EVENTSOURCE.fields_by_name['id']._options = None
  _EVENTSOURCE.fields_by_name['id']._serialized_options = b'\372B4r220^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z][0-9a-zA-Z_-]+$'
  _EVENTSOURCEPROJECTBINDING.fields_by_name['src_id']._options = None
  _EVENTSOURCEPROJECTBINDING.fields_by_name['src_id']._serialized_options = b'\372B4r220^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z][0-9a-zA-Z_-]+$'
  _EVENTSOURCEPROJECTBINDING.fields_by_name['project_id']._options = None
  _EVENTSOURCEPROJECTBINDING.fields_by_name['project_id']._serialized_options = b'\372B,r*2(^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z0-9_-]+$'
  _EVENTSOURCEPROJECTBINDING.fields_by_name['name']._options = None
  _EVENTSOURCEPROJECTBINDING.fields_by_name['name']._serialized_options = b'\372B\037r\0352\030^[a-zA-Z_][a-zA-Z0-9_]*$\320\001\001'
  _EVENTSOURCESETTINGS._serialized_start=101
  _EVENTSOURCESETTINGS._serialized_end=154
  _EVENTSOURCE._serialized_start=157
  _EVENTSOURCE._serialized_end=395
  _EVENTSOURCEPROJECTBINDINGSETTINGS._serialized_start=397
  _EVENTSOURCEPROJECTBINDINGSETTINGS._serialized_end=449
  _EVENTSOURCEPROJECTBINDING._serialized_start=452
  _EVENTSOURCEPROJECTBINDING._serialized_end=909
# @@protoc_insertion_point(module_scope)
