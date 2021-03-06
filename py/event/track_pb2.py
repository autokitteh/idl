# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: event/track.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from validate import validate_pb2 as validate_dot_validate__pb2
from event import event_state_pb2 as event_dot_event__state__pb2
from event import project_state_pb2 as event_dot_project__state__pb2
from lang import run_pb2 as lang_dot_run__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x65vent/track.proto\x12\x10\x61utokitteh.event\x1a\x17validate/validate.proto\x1a\x17\x65vent/event_state.proto\x1a\x19\x65vent/project_state.proto\x1a\x0elang/run.proto\"\xc4\x02\n\x16TrackIngestEventUpdate\x12%\n\x08\x65vent_id\x18\x01 \x01(\tB\x13\xfa\x42\x10r\x0e\x32\x0c^E[0-9a-f]+$\x12\x37\n\x0b\x65vent_state\x18\x02 \x01(\x0b\x32\".autokitteh.event.EventStateRecord\x12\x46\n\nproject_id\x18\x03 \x01(\tB2\xfa\x42/r-2(^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z0-9_-]+$\xd0\x01\x01\x12\x46\n\x13project_event_state\x18\x04 \x01(\x0b\x32).autokitteh.event.ProjectEventStateRecord\x12:\n\x15\x66lattened_run_summary\x18\x05 \x01(\x0b\x32\x1b.autokitteh.lang.RunSummaryB Z\x1ego.autokitteh.dev/idl/go/eventb\x06proto3')



_TRACKINGESTEVENTUPDATE = DESCRIPTOR.message_types_by_name['TrackIngestEventUpdate']
TrackIngestEventUpdate = _reflection.GeneratedProtocolMessageType('TrackIngestEventUpdate', (_message.Message,), {
  'DESCRIPTOR' : _TRACKINGESTEVENTUPDATE,
  '__module__' : 'event.track_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.event.TrackIngestEventUpdate)
  })
_sym_db.RegisterMessage(TrackIngestEventUpdate)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\036go.autokitteh.dev/idl/go/event'
  _TRACKINGESTEVENTUPDATE.fields_by_name['event_id']._options = None
  _TRACKINGESTEVENTUPDATE.fields_by_name['event_id']._serialized_options = b'\372B\020r\0162\014^E[0-9a-f]+$'
  _TRACKINGESTEVENTUPDATE.fields_by_name['project_id']._options = None
  _TRACKINGESTEVENTUPDATE.fields_by_name['project_id']._serialized_options = b'\372B/r-2(^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z0-9_-]+$\320\001\001'
  _TRACKINGESTEVENTUPDATE._serialized_start=133
  _TRACKINGESTEVENTUPDATE._serialized_end=457
# @@protoc_insertion_point(module_scope)
