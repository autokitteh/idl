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
from validate import validate_pb2 as validate_dot_validate__pb2
from event import project_state_pb2 as event_dot_project__state__pb2
from event import track_pb2 as event_dot_track__pb2
from values import values_pb2 as values_dot_values__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16litterboxsvc/svc.proto\x12\x14\x61utokitteh.litterbox\x1a\x1cgoogle/api/annotations.proto\x1a\x17validate/validate.proto\x1a\x19\x65vent/project_state.proto\x1a\x11\x65vent/track.proto\x1a\x13values/values.proto\"K\n\x0cSetupRequest\x12&\n\x02id\x18\x01 \x01(\tB\x1a\xfa\x42\x17r\x15\x32\x10^[a-zA-Z0-9_-]+$\xd0\x01\x01\x12\x13\n\x0b\x66iles_txtar\x18\x02 \x01(\x0c\"4\n\rSetupResponse\x12#\n\x02id\x18\x01 \x01(\tB\x17\xfa\x42\x14r\x12\x32\x10^[a-zA-Z0-9_-]+$\"1\n\nGetRequest\x12#\n\x02id\x18\x01 \x01(\tB\x17\xfa\x42\x14r\x12\x32\x10^[a-zA-Z0-9_-]+$\"\"\n\x0bGetResponse\x12\x13\n\x0b\x66iles_txtar\x18\x01 \x01(\x0c\"3\n\x0cScoopRequest\x12#\n\x02id\x18\x01 \x01(\tB\x17\xfa\x42\x14r\x12\x32\x10^[a-zA-Z0-9_-]+$\"\x0f\n\rScoopResponse\"\xa2\x02\n\x0eLitterBoxEvent\x12,\n\x03src\x18\x01 \x01(\tB\x1f\xfa\x42\x1cr\x1a\x32\x18^[a-zA-Z_][a-zA-Z0-9_]*$\x12\x0c\n\x04type\x18\x02 \x01(\t\x12h\n\x06values\x18\x03 \x03(\x0b\x32\x30.autokitteh.litterbox.LitterBoxEvent.ValuesEntryB&\xfa\x42#\x9a\x01 \x18\x01\"\x1cr\x1a\x32\x18^[a-zA-Z_][a-zA-Z0-9_]*$\x12\x0c\n\x04\x64\x61ta\x18\x04 \x01(\t\x12\x13\n\x0boriginal_id\x18\x05 \x01(\t\x1aG\n\x0bValuesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\'\n\x05value\x18\x02 \x01(\x0b\x32\x18.autokitteh.values.Value:\x02\x38\x01\"r\n\x0c\x45ventRequest\x12#\n\x02id\x18\x01 \x01(\tB\x17\xfa\x42\x14r\x12\x32\x10^[a-zA-Z0-9_-]+$\x12=\n\x05\x65vent\x18\x02 \x01(\x0b\x32$.autokitteh.litterbox.LitterBoxEventB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\"1\n\nRunRequest\x12#\n\x02id\x18\x01 \x01(\tB\x17\xfa\x42\x14r\x12\x32\x10^[a-zA-Z0-9_-]+$2\x8b\x06\n\tLitterBox\x12\xd3\x01\n\x05Setup\x12\".autokitteh.litterbox.SetupRequest\x1a#.autokitteh.litterbox.SetupResponse\"\x80\x01\x82\xd3\xe4\x93\x02z\"\x13/api/v1/litterboxes:\x0b\x66iles_txtarZ\'\"\x18/api/v1/litterboxes/{id}:\x0b\x66iles_txtarZ-\"\x1e/api/v1/litterboxes/{id}/files:\x0b\x66iles_txtar\x12\xa8\x01\n\x03Get\x12 .autokitteh.litterbox.GetRequest\x1a!.autokitteh.litterbox.GetResponse\"\\\x82\xd3\xe4\x93\x02V\x12\x18/api/v1/litterboxes/{id}Z-\x12\x1e/api/v1/litterboxes/{id}/filesb\x0b\x66iles_txtarb\x0b\x66iles_txtar\x12\x87\x01\n\x05\x45vent\x12\".autokitteh.litterbox.EventRequest\x1a(.autokitteh.event.TrackIngestEventUpdate\".\x82\xd3\xe4\x93\x02(\"\x1f/api/v1/litterboxes/{id}/events:\x05\x65vent0\x01\x12y\n\x03Run\x12 .autokitteh.litterbox.RunRequest\x1a(.autokitteh.event.TrackIngestEventUpdate\"$\x82\xd3\xe4\x93\x02\x1e\"\x1c/api/v1/litterboxes/{id}/run0\x01\x12x\n\x05Scoop\x12\".autokitteh.litterbox.ScoopRequest\x1a#.autokitteh.litterbox.ScoopResponse\"&\x82\xd3\xe4\x93\x02 \"\x1e/api/v1/litterboxes/{id}/scoopB\'Z%go.autokitteh.dev/idl/go/litterboxsvcb\x06proto3')



_SETUPREQUEST = DESCRIPTOR.message_types_by_name['SetupRequest']
_SETUPRESPONSE = DESCRIPTOR.message_types_by_name['SetupResponse']
_GETREQUEST = DESCRIPTOR.message_types_by_name['GetRequest']
_GETRESPONSE = DESCRIPTOR.message_types_by_name['GetResponse']
_SCOOPREQUEST = DESCRIPTOR.message_types_by_name['ScoopRequest']
_SCOOPRESPONSE = DESCRIPTOR.message_types_by_name['ScoopResponse']
_LITTERBOXEVENT = DESCRIPTOR.message_types_by_name['LitterBoxEvent']
_LITTERBOXEVENT_VALUESENTRY = _LITTERBOXEVENT.nested_types_by_name['ValuesEntry']
_EVENTREQUEST = DESCRIPTOR.message_types_by_name['EventRequest']
_RUNREQUEST = DESCRIPTOR.message_types_by_name['RunRequest']
SetupRequest = _reflection.GeneratedProtocolMessageType('SetupRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETUPREQUEST,
  '__module__' : 'litterboxsvc.svc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.litterbox.SetupRequest)
  })
_sym_db.RegisterMessage(SetupRequest)

SetupResponse = _reflection.GeneratedProtocolMessageType('SetupResponse', (_message.Message,), {
  'DESCRIPTOR' : _SETUPRESPONSE,
  '__module__' : 'litterboxsvc.svc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.litterbox.SetupResponse)
  })
_sym_db.RegisterMessage(SetupResponse)

GetRequest = _reflection.GeneratedProtocolMessageType('GetRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETREQUEST,
  '__module__' : 'litterboxsvc.svc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.litterbox.GetRequest)
  })
_sym_db.RegisterMessage(GetRequest)

GetResponse = _reflection.GeneratedProtocolMessageType('GetResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETRESPONSE,
  '__module__' : 'litterboxsvc.svc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.litterbox.GetResponse)
  })
_sym_db.RegisterMessage(GetResponse)

ScoopRequest = _reflection.GeneratedProtocolMessageType('ScoopRequest', (_message.Message,), {
  'DESCRIPTOR' : _SCOOPREQUEST,
  '__module__' : 'litterboxsvc.svc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.litterbox.ScoopRequest)
  })
_sym_db.RegisterMessage(ScoopRequest)

ScoopResponse = _reflection.GeneratedProtocolMessageType('ScoopResponse', (_message.Message,), {
  'DESCRIPTOR' : _SCOOPRESPONSE,
  '__module__' : 'litterboxsvc.svc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.litterbox.ScoopResponse)
  })
_sym_db.RegisterMessage(ScoopResponse)

LitterBoxEvent = _reflection.GeneratedProtocolMessageType('LitterBoxEvent', (_message.Message,), {

  'ValuesEntry' : _reflection.GeneratedProtocolMessageType('ValuesEntry', (_message.Message,), {
    'DESCRIPTOR' : _LITTERBOXEVENT_VALUESENTRY,
    '__module__' : 'litterboxsvc.svc_pb2'
    # @@protoc_insertion_point(class_scope:autokitteh.litterbox.LitterBoxEvent.ValuesEntry)
    })
  ,
  'DESCRIPTOR' : _LITTERBOXEVENT,
  '__module__' : 'litterboxsvc.svc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.litterbox.LitterBoxEvent)
  })
_sym_db.RegisterMessage(LitterBoxEvent)
_sym_db.RegisterMessage(LitterBoxEvent.ValuesEntry)

EventRequest = _reflection.GeneratedProtocolMessageType('EventRequest', (_message.Message,), {
  'DESCRIPTOR' : _EVENTREQUEST,
  '__module__' : 'litterboxsvc.svc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.litterbox.EventRequest)
  })
_sym_db.RegisterMessage(EventRequest)

RunRequest = _reflection.GeneratedProtocolMessageType('RunRequest', (_message.Message,), {
  'DESCRIPTOR' : _RUNREQUEST,
  '__module__' : 'litterboxsvc.svc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.litterbox.RunRequest)
  })
_sym_db.RegisterMessage(RunRequest)

_LITTERBOX = DESCRIPTOR.services_by_name['LitterBox']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z%go.autokitteh.dev/idl/go/litterboxsvc'
  _SETUPREQUEST.fields_by_name['id']._options = None
  _SETUPREQUEST.fields_by_name['id']._serialized_options = b'\372B\027r\0252\020^[a-zA-Z0-9_-]+$\320\001\001'
  _SETUPRESPONSE.fields_by_name['id']._options = None
  _SETUPRESPONSE.fields_by_name['id']._serialized_options = b'\372B\024r\0222\020^[a-zA-Z0-9_-]+$'
  _GETREQUEST.fields_by_name['id']._options = None
  _GETREQUEST.fields_by_name['id']._serialized_options = b'\372B\024r\0222\020^[a-zA-Z0-9_-]+$'
  _SCOOPREQUEST.fields_by_name['id']._options = None
  _SCOOPREQUEST.fields_by_name['id']._serialized_options = b'\372B\024r\0222\020^[a-zA-Z0-9_-]+$'
  _LITTERBOXEVENT_VALUESENTRY._options = None
  _LITTERBOXEVENT_VALUESENTRY._serialized_options = b'8\001'
  _LITTERBOXEVENT.fields_by_name['src']._options = None
  _LITTERBOXEVENT.fields_by_name['src']._serialized_options = b'\372B\034r\0322\030^[a-zA-Z_][a-zA-Z0-9_]*$'
  _LITTERBOXEVENT.fields_by_name['values']._options = None
  _LITTERBOXEVENT.fields_by_name['values']._serialized_options = b'\372B#\232\001 \030\001\"\034r\0322\030^[a-zA-Z_][a-zA-Z0-9_]*$'
  _EVENTREQUEST.fields_by_name['id']._options = None
  _EVENTREQUEST.fields_by_name['id']._serialized_options = b'\372B\024r\0222\020^[a-zA-Z0-9_-]+$'
  _EVENTREQUEST.fields_by_name['event']._options = None
  _EVENTREQUEST.fields_by_name['event']._serialized_options = b'\372B\005\212\001\002\020\001'
  _RUNREQUEST.fields_by_name['id']._options = None
  _RUNREQUEST.fields_by_name['id']._serialized_options = b'\372B\024r\0222\020^[a-zA-Z0-9_-]+$'
  _LITTERBOX.methods_by_name['Setup']._options = None
  _LITTERBOX.methods_by_name['Setup']._serialized_options = b'\202\323\344\223\002z\"\023/api/v1/litterboxes:\013files_txtarZ\'\"\030/api/v1/litterboxes/{id}:\013files_txtarZ-\"\036/api/v1/litterboxes/{id}/files:\013files_txtar'
  _LITTERBOX.methods_by_name['Get']._options = None
  _LITTERBOX.methods_by_name['Get']._serialized_options = b'\202\323\344\223\002V\022\030/api/v1/litterboxes/{id}Z-\022\036/api/v1/litterboxes/{id}/filesb\013files_txtarb\013files_txtar'
  _LITTERBOX.methods_by_name['Event']._options = None
  _LITTERBOX.methods_by_name['Event']._serialized_options = b'\202\323\344\223\002(\"\037/api/v1/litterboxes/{id}/events:\005event'
  _LITTERBOX.methods_by_name['Run']._options = None
  _LITTERBOX.methods_by_name['Run']._serialized_options = b'\202\323\344\223\002\036\"\034/api/v1/litterboxes/{id}/run'
  _LITTERBOX.methods_by_name['Scoop']._options = None
  _LITTERBOX.methods_by_name['Scoop']._serialized_options = b'\202\323\344\223\002 \"\036/api/v1/litterboxes/{id}/scoop'
  _SETUPREQUEST._serialized_start=170
  _SETUPREQUEST._serialized_end=245
  _SETUPRESPONSE._serialized_start=247
  _SETUPRESPONSE._serialized_end=299
  _GETREQUEST._serialized_start=301
  _GETREQUEST._serialized_end=350
  _GETRESPONSE._serialized_start=352
  _GETRESPONSE._serialized_end=386
  _SCOOPREQUEST._serialized_start=388
  _SCOOPREQUEST._serialized_end=439
  _SCOOPRESPONSE._serialized_start=441
  _SCOOPRESPONSE._serialized_end=456
  _LITTERBOXEVENT._serialized_start=459
  _LITTERBOXEVENT._serialized_end=749
  _LITTERBOXEVENT_VALUESENTRY._serialized_start=678
  _LITTERBOXEVENT_VALUESENTRY._serialized_end=749
  _EVENTREQUEST._serialized_start=751
  _EVENTREQUEST._serialized_end=865
  _RUNREQUEST._serialized_start=867
  _RUNREQUEST._serialized_end=916
  _LITTERBOX._serialized_start=919
  _LITTERBOX._serialized_end=1698
# @@protoc_insertion_point(module_scope)
