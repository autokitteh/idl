# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: event/event.proto
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
from values import values_pb2 as values_dot_values__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x65vent/event.proto\x12\x10\x61utokitteh.event\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17validate/validate.proto\x1a\x13values/values.proto\"\xf5\x03\n\x05\x45vent\x12/\n\x01t\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\xfa\x42\x05\xb2\x01\x02\x08\x01\x12\x1f\n\x02id\x18\x02 \x01(\tB\x13\xfa\x42\x10r\x0e\x32\x0c^E[0-9a-f]+$\x12G\n\x06src_id\x18\x03 \x01(\tB7\xfa\x42\x34r220^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z][0-9a-zA-Z_-]+$\x12\x19\n\x11\x61ssociation_token\x18\x04 \x01(\t\x12\x13\n\x0boriginal_id\x18\x05 \x01(\t\x12\x15\n\x04type\x18\x06 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01\x12W\n\x04\x64\x61ta\x18\x07 \x03(\x0b\x32!.autokitteh.event.Event.DataEntryB&\xfa\x42#\x9a\x01 \x18\x01\"\x1cr\x1a\x32\x18^[a-zA-Z_][a-zA-Z0-9_]*$\x12=\n\x04memo\x18\x08 \x03(\x0b\x32!.autokitteh.event.Event.MemoEntryB\x0c\xfa\x42\t\x9a\x01\x06\"\x04r\x02\x10\x01\x1a\x45\n\tDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\'\n\x05value\x18\x02 \x01(\x0b\x32\x18.autokitteh.values.Value:\x02\x38\x01\x1a+\n\tMemoEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42 Z\x1ego.autokitteh.dev/idl/go/eventb\x06proto3')



_EVENT = DESCRIPTOR.message_types_by_name['Event']
_EVENT_DATAENTRY = _EVENT.nested_types_by_name['DataEntry']
_EVENT_MEMOENTRY = _EVENT.nested_types_by_name['MemoEntry']
Event = _reflection.GeneratedProtocolMessageType('Event', (_message.Message,), {

  'DataEntry' : _reflection.GeneratedProtocolMessageType('DataEntry', (_message.Message,), {
    'DESCRIPTOR' : _EVENT_DATAENTRY,
    '__module__' : 'event.event_pb2'
    # @@protoc_insertion_point(class_scope:autokitteh.event.Event.DataEntry)
    })
  ,

  'MemoEntry' : _reflection.GeneratedProtocolMessageType('MemoEntry', (_message.Message,), {
    'DESCRIPTOR' : _EVENT_MEMOENTRY,
    '__module__' : 'event.event_pb2'
    # @@protoc_insertion_point(class_scope:autokitteh.event.Event.MemoEntry)
    })
  ,
  'DESCRIPTOR' : _EVENT,
  '__module__' : 'event.event_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.event.Event)
  })
_sym_db.RegisterMessage(Event)
_sym_db.RegisterMessage(Event.DataEntry)
_sym_db.RegisterMessage(Event.MemoEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\036go.autokitteh.dev/idl/go/event'
  _EVENT_DATAENTRY._options = None
  _EVENT_DATAENTRY._serialized_options = b'8\001'
  _EVENT_MEMOENTRY._options = None
  _EVENT_MEMOENTRY._serialized_options = b'8\001'
  _EVENT.fields_by_name['t']._options = None
  _EVENT.fields_by_name['t']._serialized_options = b'\372B\005\262\001\002\010\001'
  _EVENT.fields_by_name['id']._options = None
  _EVENT.fields_by_name['id']._serialized_options = b'\372B\020r\0162\014^E[0-9a-f]+$'
  _EVENT.fields_by_name['src_id']._options = None
  _EVENT.fields_by_name['src_id']._serialized_options = b'\372B4r220^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z][0-9a-zA-Z_-]+$'
  _EVENT.fields_by_name['type']._options = None
  _EVENT.fields_by_name['type']._serialized_options = b'\372B\004r\002\020\001'
  _EVENT.fields_by_name['data']._options = None
  _EVENT.fields_by_name['data']._serialized_options = b'\372B#\232\001 \030\001\"\034r\0322\030^[a-zA-Z_][a-zA-Z0-9_]*$'
  _EVENT.fields_by_name['memo']._options = None
  _EVENT.fields_by_name['memo']._serialized_options = b'\372B\t\232\001\006\"\004r\002\020\001'
  _EVENT._serialized_start=119
  _EVENT._serialized_end=620
  _EVENT_DATAENTRY._serialized_start=506
  _EVENT_DATAENTRY._serialized_end=575
  _EVENT_MEMOENTRY._serialized_start=577
  _EVENT_MEMOENTRY._serialized_end=620
# @@protoc_insertion_point(module_scope)
