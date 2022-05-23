# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: litterboxsvc/svc.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from validate import validate_pb2 as validate_dot_validate__pb2
from lang import run_pb2 as lang_dot_run__pb2
from values import values_pb2 as values_dot_values__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16litterboxsvc/svc.proto\x12\x14\x61utokitteh.litterbox\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17validate/validate.proto\x1a\x0elang/run.proto\x1a\x13values/values.proto\"\xa2\x03\n\x0eSyntheticEvent\x12G\n\x06src_id\x18\x01 \x01(\tB7\xfa\x42\x34r220^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z][0-9a-zA-Z_-]+$\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x64\n\x04\x64\x61ta\x18\x03 \x03(\x0b\x32..autokitteh.litterbox.SyntheticEvent.DataEntryB&\xfa\x42#\x9a\x01 \x18\x01\"\x1cr\x1a\x32\x18^[a-zA-Z_][a-zA-Z0-9_]*$\x12\x13\n\x0boriginal_id\x18\x04 \x01(\t\x12J\n\x04memo\x18\x32 \x03(\x0b\x32..autokitteh.litterbox.SyntheticEvent.MemoEntryB\x0c\xfa\x42\t\x9a\x01\x06\"\x04r\x02\x10\x01\x1a\x45\n\tDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\'\n\x05value\x18\x02 \x01(\x0b\x32\x18.autokitteh.values.Value:\x02\x38\x01\x1a+\n\tMemoEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"[\n\nRunRequest\x12\x0e\n\x06source\x18\x01 \x01(\t\x12=\n\x05\x65vent\x18\x02 \x01(\x0b\x32$.autokitteh.litterbox.SyntheticEventB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\"p\n\tRunUpdate\x12/\n\x01t\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\xfa\x42\x05\xb2\x01\x02\x08\x01\x12\x32\n\x05state\x18\x02 \x01(\x0b\x32\x19.autokitteh.lang.RunStateB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\x32y\n\tLitterBox\x12l\n\x03Run\x12 .autokitteh.litterbox.RunRequest\x1a\x1f.autokitteh.litterbox.RunUpdate\" \x82\xd3\xe4\x93\x02\x1a\"\x15/api/v1/litterbox/run:\x01*0\x01\x42\'Z%go.autokitteh.dev/idl/go/litterboxsvcb\x06proto3')



_SYNTHETICEVENT = DESCRIPTOR.message_types_by_name['SyntheticEvent']
_SYNTHETICEVENT_DATAENTRY = _SYNTHETICEVENT.nested_types_by_name['DataEntry']
_SYNTHETICEVENT_MEMOENTRY = _SYNTHETICEVENT.nested_types_by_name['MemoEntry']
_RUNREQUEST = DESCRIPTOR.message_types_by_name['RunRequest']
_RUNUPDATE = DESCRIPTOR.message_types_by_name['RunUpdate']
SyntheticEvent = _reflection.GeneratedProtocolMessageType('SyntheticEvent', (_message.Message,), {

  'DataEntry' : _reflection.GeneratedProtocolMessageType('DataEntry', (_message.Message,), {
    'DESCRIPTOR' : _SYNTHETICEVENT_DATAENTRY,
    '__module__' : 'litterboxsvc.svc_pb2'
    # @@protoc_insertion_point(class_scope:autokitteh.litterbox.SyntheticEvent.DataEntry)
    })
  ,

  'MemoEntry' : _reflection.GeneratedProtocolMessageType('MemoEntry', (_message.Message,), {
    'DESCRIPTOR' : _SYNTHETICEVENT_MEMOENTRY,
    '__module__' : 'litterboxsvc.svc_pb2'
    # @@protoc_insertion_point(class_scope:autokitteh.litterbox.SyntheticEvent.MemoEntry)
    })
  ,
  'DESCRIPTOR' : _SYNTHETICEVENT,
  '__module__' : 'litterboxsvc.svc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.litterbox.SyntheticEvent)
  })
_sym_db.RegisterMessage(SyntheticEvent)
_sym_db.RegisterMessage(SyntheticEvent.DataEntry)
_sym_db.RegisterMessage(SyntheticEvent.MemoEntry)

RunRequest = _reflection.GeneratedProtocolMessageType('RunRequest', (_message.Message,), {
  'DESCRIPTOR' : _RUNREQUEST,
  '__module__' : 'litterboxsvc.svc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.litterbox.RunRequest)
  })
_sym_db.RegisterMessage(RunRequest)

RunUpdate = _reflection.GeneratedProtocolMessageType('RunUpdate', (_message.Message,), {
  'DESCRIPTOR' : _RUNUPDATE,
  '__module__' : 'litterboxsvc.svc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.litterbox.RunUpdate)
  })
_sym_db.RegisterMessage(RunUpdate)

_LITTERBOX = DESCRIPTOR.services_by_name['LitterBox']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z%go.autokitteh.dev/idl/go/litterboxsvc'
  _SYNTHETICEVENT_DATAENTRY._options = None
  _SYNTHETICEVENT_DATAENTRY._serialized_options = b'8\001'
  _SYNTHETICEVENT_MEMOENTRY._options = None
  _SYNTHETICEVENT_MEMOENTRY._serialized_options = b'8\001'
  _SYNTHETICEVENT.fields_by_name['src_id']._options = None
  _SYNTHETICEVENT.fields_by_name['src_id']._serialized_options = b'\372B4r220^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z][0-9a-zA-Z_-]+$'
  _SYNTHETICEVENT.fields_by_name['data']._options = None
  _SYNTHETICEVENT.fields_by_name['data']._serialized_options = b'\372B#\232\001 \030\001\"\034r\0322\030^[a-zA-Z_][a-zA-Z0-9_]*$'
  _SYNTHETICEVENT.fields_by_name['memo']._options = None
  _SYNTHETICEVENT.fields_by_name['memo']._serialized_options = b'\372B\t\232\001\006\"\004r\002\020\001'
  _RUNREQUEST.fields_by_name['event']._options = None
  _RUNREQUEST.fields_by_name['event']._serialized_options = b'\372B\005\212\001\002\020\001'
  _RUNUPDATE.fields_by_name['t']._options = None
  _RUNUPDATE.fields_by_name['t']._serialized_options = b'\372B\005\262\001\002\010\001'
  _RUNUPDATE.fields_by_name['state']._options = None
  _RUNUPDATE.fields_by_name['state']._serialized_options = b'\372B\005\212\001\002\020\001'
  _LITTERBOX.methods_by_name['Run']._options = None
  _LITTERBOX.methods_by_name['Run']._serialized_options = b'\202\323\344\223\002\032\"\025/api/v1/litterbox/run:\001*'
  _SYNTHETICEVENT._serialized_start=174
  _SYNTHETICEVENT._serialized_end=592
  _SYNTHETICEVENT_DATAENTRY._serialized_start=478
  _SYNTHETICEVENT_DATAENTRY._serialized_end=547
  _SYNTHETICEVENT_MEMOENTRY._serialized_start=549
  _SYNTHETICEVENT_MEMOENTRY._serialized_end=592
  _RUNREQUEST._serialized_start=594
  _RUNREQUEST._serialized_end=685
  _RUNUPDATE._serialized_start=687
  _RUNUPDATE._serialized_end=799
  _LITTERBOX._serialized_start=801
  _LITTERBOX._serialized_end=922
# @@protoc_insertion_point(module_scope)
