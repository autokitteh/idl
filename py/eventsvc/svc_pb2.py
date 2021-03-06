# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: eventsvc/svc.proto
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
from event import event_pb2 as event_dot_event__pb2
from event import event_state_pb2 as event_dot_event__state__pb2
from event import project_state_pb2 as event_dot_project__state__pb2
from event import track_pb2 as event_dot_track__pb2
from values import values_pb2 as values_dot_values__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12\x65ventsvc/svc.proto\x12\x13\x61utokitteh.eventsvc\x1a\x1cgoogle/api/annotations.proto\x1a\x17validate/validate.proto\x1a\x11\x65vent/event.proto\x1a\x17\x65vent/event_state.proto\x1a\x19\x65vent/project_state.proto\x1a\x11\x65vent/track.proto\x1a\x13values/values.proto\"\xd9\x03\n\x12IngestEventRequest\x12\x10\n\x08\x65vent_id\x18\x01 \x01(\t\x12G\n\x06src_id\x18\x02 \x01(\tB7\xfa\x42\x34r220^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z][0-9a-zA-Z_-]+$\x12\x19\n\x11\x61ssociation_token\x18\x03 \x01(\t\x12\x0c\n\x04type\x18\x04 \x01(\t\x12g\n\x04\x64\x61ta\x18\x05 \x03(\x0b\x32\x31.autokitteh.eventsvc.IngestEventRequest.DataEntryB&\xfa\x42#\x9a\x01 \x18\x01\"\x1cr\x1a\x32\x18^[a-zA-Z_][a-zA-Z0-9_]*$\x12\x13\n\x0boriginal_id\x18\x06 \x01(\t\x12M\n\x04memo\x18\x32 \x03(\x0b\x32\x31.autokitteh.eventsvc.IngestEventRequest.MemoEntryB\x0c\xfa\x42\t\x9a\x01\x06\"\x04r\x02\x10\x01\x1a\x45\n\tDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\'\n\x05value\x18\x02 \x01(\x0b\x32\x18.autokitteh.values.Value:\x02\x38\x01\x1a+\n\tMemoEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"6\n\x13IngestEventResponse\x12\x1f\n\x02id\x18\x01 \x01(\tB\x13\xfa\x42\x10r\x0e\x32\x0c^E[0-9a-f]+$\"2\n\x0fGetEventRequest\x12\x1f\n\x02id\x18\x01 \x01(\tB\x13\xfa\x42\x10r\x0e\x32\x0c^E[0-9a-f]+$\"D\n\x10GetEventResponse\x12\x30\n\x05\x65vent\x18\x01 \x01(\x0b\x32\x17.autokitteh.event.EventB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\"7\n\x14GetEventStateRequest\x12\x1f\n\x02id\x18\x01 \x01(\tB\x13\xfa\x42\x10r\x0e\x32\x0c^E[0-9a-f]+$\"W\n\x15GetEventStateResponse\x12>\n\x03log\x18\x01 \x03(\x0b\x32\".autokitteh.event.EventStateRecordB\r\xfa\x42\n\x92\x01\x07\"\x05\x8a\x01\x02\x10\x01\"\x86\x01\n\x1eGetEventStateForProjectRequest\x12\x1f\n\x02id\x18\x01 \x01(\tB\x13\xfa\x42\x10r\x0e\x32\x0c^E[0-9a-f]+$\x12\x43\n\nproject_id\x18\x02 \x01(\tB/\xfa\x42,r*2(^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z0-9_-]+$\"h\n\x1fGetEventStateForProjectResponse\x12\x45\n\x03log\x18\x01 \x03(\x0b\x32).autokitteh.event.ProjectEventStateRecordB\r\xfa\x42\n\x92\x01\x07\"\x05\x8a\x01\x02\x10\x01\"q\n\x17UpdateEventStateRequest\x12\x1f\n\x02id\x18\x01 \x01(\tB\x13\xfa\x42\x10r\x0e\x32\x0c^E[0-9a-f]+$\x12\x35\n\x05state\x18\x02 \x01(\x0b\x32\x1c.autokitteh.event.EventStateB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\"\x1a\n\x18UpdateEventStateResponse\"\xc7\x01\n!UpdateEventStateForProjectRequest\x12\x1f\n\x02id\x18\x01 \x01(\tB\x13\xfa\x42\x10r\x0e\x32\x0c^E[0-9a-f]+$\x12\x43\n\nproject_id\x18\x02 \x01(\tB/\xfa\x42,r*2(^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z0-9_-]+$\x12<\n\x05state\x18\x03 \x01(\x0b\x32#.autokitteh.event.ProjectEventStateB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\"$\n\"UpdateEventStateForProjectResponse\"A\n\x11ListEventsRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x0b\n\x03ofs\x18\x02 \x01(\r\x12\x0b\n\x03len\x18\x03 \x01(\r\"\x86\x01\n\x0fListEventRecord\x12\x30\n\x05\x65vent\x18\x01 \x01(\x0b\x32\x17.autokitteh.event.EventB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\x12\x41\n\x06states\x18\x02 \x03(\x0b\x32\".autokitteh.event.EventStateRecordB\r\xfa\x42\n\x92\x01\x07\"\x05\x8a\x01\x02\x10\x01\"Z\n\x12ListEventsResponse\x12\x44\n\x07records\x18\x01 \x03(\x0b\x32$.autokitteh.eventsvc.ListEventRecordB\r\xfa\x42\n\x92\x01\x07\"\x05\x8a\x01\x02\x10\x01\"h\n\x1eGetProjectWaitingEventsRequest\x12\x46\n\nproject_id\x18\x01 \x01(\tB2\xfa\x42/r-2(^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z0-9_-]+$\xd0\x01\x01\"N\n\x1fGetProjectWaitingEventsResponse\x12+\n\tevent_ids\x18\x01 \x03(\tB\x18\xfa\x42\x15\x92\x01\x12\"\x10r\x0e\x32\x0c^E[0-9a-f]+$\"b\n\x1bMonitorProjectEventsRequest\x12\x43\n\nproject_id\x18\x01 \x01(\tB/\xfa\x42,r*2(^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z0-9_-]+$2\xb5\x0c\n\x06\x45vents\x12{\n\x0bIngestEvent\x12\'.autokitteh.eventsvc.IngestEventRequest\x1a(.autokitteh.eventsvc.IngestEventResponse\"\x19\x82\xd3\xe4\x93\x02\x13\"\x0e/api/v1/events:\x01*\x12\x8a\x01\n\x10TrackIngestEvent\x12\'.autokitteh.eventsvc.IngestEventRequest\x1a(.autokitteh.event.TrackIngestEventUpdate\"!\x82\xd3\xe4\x93\x02\x1b\"\x16/api/v1/tracked-events:\x01*0\x01\x12\xaa\x01\n\x14MonitorProjectEvents\x12\x30.autokitteh.eventsvc.MonitorProjectEventsRequest\x1a(.autokitteh.event.TrackIngestEventUpdate\"4\x82\xd3\xe4\x93\x02.\x12,/api/v1/projects/{project_id}/monitor-events0\x01\x12t\n\x08GetEvent\x12$.autokitteh.eventsvc.GetEventRequest\x1a%.autokitteh.eventsvc.GetEventResponse\"\x1b\x82\xd3\xe4\x93\x02\x15\x12\x13/api/v1/events/{id}\x12\x89\x01\n\rGetEventState\x12).autokitteh.eventsvc.GetEventStateRequest\x1a*.autokitteh.eventsvc.GetEventStateResponse\"!\x82\xd3\xe4\x93\x02\x1b\x12\x19/api/v1/events/{id}/state\x12\x92\x01\n\x10UpdateEventState\x12,.autokitteh.eventsvc.UpdateEventStateRequest\x1a-.autokitteh.eventsvc.UpdateEventStateResponse\"!\x82\xd3\xe4\x93\x02\x1b\"\x19/api/v1/events/{id}/state\x12\x9d\x01\n\nListEvents\x12&.autokitteh.eventsvc.ListEventsRequest\x1a\'.autokitteh.eventsvc.ListEventsResponse\">\x82\xd3\xe4\x93\x02\x38\x12\x0e/api/v1/eventsZ&\x12$/api/v1/projects/{project_id}/events\x12\xbd\x01\n\x17GetEventStateForProject\x12\x33.autokitteh.eventsvc.GetEventStateForProjectRequest\x1a\x34.autokitteh.eventsvc.GetEventStateForProjectResponse\"7\x82\xd3\xe4\x93\x02\x31\x12//api/v1/events/{id}/projects/{project_id}/state\x12\xc6\x01\n\x1aUpdateEventStateForProject\x12\x36.autokitteh.eventsvc.UpdateEventStateForProjectRequest\x1a\x37.autokitteh.eventsvc.UpdateEventStateForProjectResponse\"7\x82\xd3\xe4\x93\x02\x31\"//api/v1/events/{id}/projects/{project_id}/state\x12\xb3\x01\n\x17GetProjectWaitingEvents\x12\x33.autokitteh.eventsvc.GetProjectWaitingEventsRequest\x1a\x34.autokitteh.eventsvc.GetProjectWaitingEventsResponse\"-\x82\xd3\xe4\x93\x02\'\x12%/api/v1/projects/{project_id}/waitingB#Z!go.autokitteh.dev/idl/go/eventsvcb\x06proto3')



_INGESTEVENTREQUEST = DESCRIPTOR.message_types_by_name['IngestEventRequest']
_INGESTEVENTREQUEST_DATAENTRY = _INGESTEVENTREQUEST.nested_types_by_name['DataEntry']
_INGESTEVENTREQUEST_MEMOENTRY = _INGESTEVENTREQUEST.nested_types_by_name['MemoEntry']
_INGESTEVENTRESPONSE = DESCRIPTOR.message_types_by_name['IngestEventResponse']
_GETEVENTREQUEST = DESCRIPTOR.message_types_by_name['GetEventRequest']
_GETEVENTRESPONSE = DESCRIPTOR.message_types_by_name['GetEventResponse']
_GETEVENTSTATEREQUEST = DESCRIPTOR.message_types_by_name['GetEventStateRequest']
_GETEVENTSTATERESPONSE = DESCRIPTOR.message_types_by_name['GetEventStateResponse']
_GETEVENTSTATEFORPROJECTREQUEST = DESCRIPTOR.message_types_by_name['GetEventStateForProjectRequest']
_GETEVENTSTATEFORPROJECTRESPONSE = DESCRIPTOR.message_types_by_name['GetEventStateForProjectResponse']
_UPDATEEVENTSTATEREQUEST = DESCRIPTOR.message_types_by_name['UpdateEventStateRequest']
_UPDATEEVENTSTATERESPONSE = DESCRIPTOR.message_types_by_name['UpdateEventStateResponse']
_UPDATEEVENTSTATEFORPROJECTREQUEST = DESCRIPTOR.message_types_by_name['UpdateEventStateForProjectRequest']
_UPDATEEVENTSTATEFORPROJECTRESPONSE = DESCRIPTOR.message_types_by_name['UpdateEventStateForProjectResponse']
_LISTEVENTSREQUEST = DESCRIPTOR.message_types_by_name['ListEventsRequest']
_LISTEVENTRECORD = DESCRIPTOR.message_types_by_name['ListEventRecord']
_LISTEVENTSRESPONSE = DESCRIPTOR.message_types_by_name['ListEventsResponse']
_GETPROJECTWAITINGEVENTSREQUEST = DESCRIPTOR.message_types_by_name['GetProjectWaitingEventsRequest']
_GETPROJECTWAITINGEVENTSRESPONSE = DESCRIPTOR.message_types_by_name['GetProjectWaitingEventsResponse']
_MONITORPROJECTEVENTSREQUEST = DESCRIPTOR.message_types_by_name['MonitorProjectEventsRequest']
IngestEventRequest = _reflection.GeneratedProtocolMessageType('IngestEventRequest', (_message.Message,), {

  'DataEntry' : _reflection.GeneratedProtocolMessageType('DataEntry', (_message.Message,), {
    'DESCRIPTOR' : _INGESTEVENTREQUEST_DATAENTRY,
    '__module__' : 'eventsvc.svc_pb2'
    # @@protoc_insertion_point(class_scope:autokitteh.eventsvc.IngestEventRequest.DataEntry)
    })
  ,

  'MemoEntry' : _reflection.GeneratedProtocolMessageType('MemoEntry', (_message.Message,), {
    'DESCRIPTOR' : _INGESTEVENTREQUEST_MEMOENTRY,
    '__module__' : 'eventsvc.svc_pb2'
    # @@protoc_insertion_point(class_scope:autokitteh.eventsvc.IngestEventRequest.MemoEntry)
    })
  ,
  'DESCRIPTOR' : _INGESTEVENTREQUEST,
  '__module__' : 'eventsvc.svc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.eventsvc.IngestEventRequest)
  })
_sym_db.RegisterMessage(IngestEventRequest)
_sym_db.RegisterMessage(IngestEventRequest.DataEntry)
_sym_db.RegisterMessage(IngestEventRequest.MemoEntry)

IngestEventResponse = _reflection.GeneratedProtocolMessageType('IngestEventResponse', (_message.Message,), {
  'DESCRIPTOR' : _INGESTEVENTRESPONSE,
  '__module__' : 'eventsvc.svc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.eventsvc.IngestEventResponse)
  })
_sym_db.RegisterMessage(IngestEventResponse)

GetEventRequest = _reflection.GeneratedProtocolMessageType('GetEventRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETEVENTREQUEST,
  '__module__' : 'eventsvc.svc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.eventsvc.GetEventRequest)
  })
_sym_db.RegisterMessage(GetEventRequest)

GetEventResponse = _reflection.GeneratedProtocolMessageType('GetEventResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETEVENTRESPONSE,
  '__module__' : 'eventsvc.svc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.eventsvc.GetEventResponse)
  })
_sym_db.RegisterMessage(GetEventResponse)

GetEventStateRequest = _reflection.GeneratedProtocolMessageType('GetEventStateRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETEVENTSTATEREQUEST,
  '__module__' : 'eventsvc.svc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.eventsvc.GetEventStateRequest)
  })
_sym_db.RegisterMessage(GetEventStateRequest)

GetEventStateResponse = _reflection.GeneratedProtocolMessageType('GetEventStateResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETEVENTSTATERESPONSE,
  '__module__' : 'eventsvc.svc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.eventsvc.GetEventStateResponse)
  })
_sym_db.RegisterMessage(GetEventStateResponse)

GetEventStateForProjectRequest = _reflection.GeneratedProtocolMessageType('GetEventStateForProjectRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETEVENTSTATEFORPROJECTREQUEST,
  '__module__' : 'eventsvc.svc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.eventsvc.GetEventStateForProjectRequest)
  })
_sym_db.RegisterMessage(GetEventStateForProjectRequest)

GetEventStateForProjectResponse = _reflection.GeneratedProtocolMessageType('GetEventStateForProjectResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETEVENTSTATEFORPROJECTRESPONSE,
  '__module__' : 'eventsvc.svc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.eventsvc.GetEventStateForProjectResponse)
  })
_sym_db.RegisterMessage(GetEventStateForProjectResponse)

UpdateEventStateRequest = _reflection.GeneratedProtocolMessageType('UpdateEventStateRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEEVENTSTATEREQUEST,
  '__module__' : 'eventsvc.svc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.eventsvc.UpdateEventStateRequest)
  })
_sym_db.RegisterMessage(UpdateEventStateRequest)

UpdateEventStateResponse = _reflection.GeneratedProtocolMessageType('UpdateEventStateResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEEVENTSTATERESPONSE,
  '__module__' : 'eventsvc.svc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.eventsvc.UpdateEventStateResponse)
  })
_sym_db.RegisterMessage(UpdateEventStateResponse)

UpdateEventStateForProjectRequest = _reflection.GeneratedProtocolMessageType('UpdateEventStateForProjectRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEEVENTSTATEFORPROJECTREQUEST,
  '__module__' : 'eventsvc.svc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.eventsvc.UpdateEventStateForProjectRequest)
  })
_sym_db.RegisterMessage(UpdateEventStateForProjectRequest)

UpdateEventStateForProjectResponse = _reflection.GeneratedProtocolMessageType('UpdateEventStateForProjectResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEEVENTSTATEFORPROJECTRESPONSE,
  '__module__' : 'eventsvc.svc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.eventsvc.UpdateEventStateForProjectResponse)
  })
_sym_db.RegisterMessage(UpdateEventStateForProjectResponse)

ListEventsRequest = _reflection.GeneratedProtocolMessageType('ListEventsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTEVENTSREQUEST,
  '__module__' : 'eventsvc.svc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.eventsvc.ListEventsRequest)
  })
_sym_db.RegisterMessage(ListEventsRequest)

ListEventRecord = _reflection.GeneratedProtocolMessageType('ListEventRecord', (_message.Message,), {
  'DESCRIPTOR' : _LISTEVENTRECORD,
  '__module__' : 'eventsvc.svc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.eventsvc.ListEventRecord)
  })
_sym_db.RegisterMessage(ListEventRecord)

ListEventsResponse = _reflection.GeneratedProtocolMessageType('ListEventsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTEVENTSRESPONSE,
  '__module__' : 'eventsvc.svc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.eventsvc.ListEventsResponse)
  })
_sym_db.RegisterMessage(ListEventsResponse)

GetProjectWaitingEventsRequest = _reflection.GeneratedProtocolMessageType('GetProjectWaitingEventsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETPROJECTWAITINGEVENTSREQUEST,
  '__module__' : 'eventsvc.svc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.eventsvc.GetProjectWaitingEventsRequest)
  })
_sym_db.RegisterMessage(GetProjectWaitingEventsRequest)

GetProjectWaitingEventsResponse = _reflection.GeneratedProtocolMessageType('GetProjectWaitingEventsResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETPROJECTWAITINGEVENTSRESPONSE,
  '__module__' : 'eventsvc.svc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.eventsvc.GetProjectWaitingEventsResponse)
  })
_sym_db.RegisterMessage(GetProjectWaitingEventsResponse)

MonitorProjectEventsRequest = _reflection.GeneratedProtocolMessageType('MonitorProjectEventsRequest', (_message.Message,), {
  'DESCRIPTOR' : _MONITORPROJECTEVENTSREQUEST,
  '__module__' : 'eventsvc.svc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.eventsvc.MonitorProjectEventsRequest)
  })
_sym_db.RegisterMessage(MonitorProjectEventsRequest)

_EVENTS = DESCRIPTOR.services_by_name['Events']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z!go.autokitteh.dev/idl/go/eventsvc'
  _INGESTEVENTREQUEST_DATAENTRY._options = None
  _INGESTEVENTREQUEST_DATAENTRY._serialized_options = b'8\001'
  _INGESTEVENTREQUEST_MEMOENTRY._options = None
  _INGESTEVENTREQUEST_MEMOENTRY._serialized_options = b'8\001'
  _INGESTEVENTREQUEST.fields_by_name['src_id']._options = None
  _INGESTEVENTREQUEST.fields_by_name['src_id']._serialized_options = b'\372B4r220^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z][0-9a-zA-Z_-]+$'
  _INGESTEVENTREQUEST.fields_by_name['data']._options = None
  _INGESTEVENTREQUEST.fields_by_name['data']._serialized_options = b'\372B#\232\001 \030\001\"\034r\0322\030^[a-zA-Z_][a-zA-Z0-9_]*$'
  _INGESTEVENTREQUEST.fields_by_name['memo']._options = None
  _INGESTEVENTREQUEST.fields_by_name['memo']._serialized_options = b'\372B\t\232\001\006\"\004r\002\020\001'
  _INGESTEVENTRESPONSE.fields_by_name['id']._options = None
  _INGESTEVENTRESPONSE.fields_by_name['id']._serialized_options = b'\372B\020r\0162\014^E[0-9a-f]+$'
  _GETEVENTREQUEST.fields_by_name['id']._options = None
  _GETEVENTREQUEST.fields_by_name['id']._serialized_options = b'\372B\020r\0162\014^E[0-9a-f]+$'
  _GETEVENTRESPONSE.fields_by_name['event']._options = None
  _GETEVENTRESPONSE.fields_by_name['event']._serialized_options = b'\372B\005\212\001\002\020\001'
  _GETEVENTSTATEREQUEST.fields_by_name['id']._options = None
  _GETEVENTSTATEREQUEST.fields_by_name['id']._serialized_options = b'\372B\020r\0162\014^E[0-9a-f]+$'
  _GETEVENTSTATERESPONSE.fields_by_name['log']._options = None
  _GETEVENTSTATERESPONSE.fields_by_name['log']._serialized_options = b'\372B\n\222\001\007\"\005\212\001\002\020\001'
  _GETEVENTSTATEFORPROJECTREQUEST.fields_by_name['id']._options = None
  _GETEVENTSTATEFORPROJECTREQUEST.fields_by_name['id']._serialized_options = b'\372B\020r\0162\014^E[0-9a-f]+$'
  _GETEVENTSTATEFORPROJECTREQUEST.fields_by_name['project_id']._options = None
  _GETEVENTSTATEFORPROJECTREQUEST.fields_by_name['project_id']._serialized_options = b'\372B,r*2(^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z0-9_-]+$'
  _GETEVENTSTATEFORPROJECTRESPONSE.fields_by_name['log']._options = None
  _GETEVENTSTATEFORPROJECTRESPONSE.fields_by_name['log']._serialized_options = b'\372B\n\222\001\007\"\005\212\001\002\020\001'
  _UPDATEEVENTSTATEREQUEST.fields_by_name['id']._options = None
  _UPDATEEVENTSTATEREQUEST.fields_by_name['id']._serialized_options = b'\372B\020r\0162\014^E[0-9a-f]+$'
  _UPDATEEVENTSTATEREQUEST.fields_by_name['state']._options = None
  _UPDATEEVENTSTATEREQUEST.fields_by_name['state']._serialized_options = b'\372B\005\212\001\002\020\001'
  _UPDATEEVENTSTATEFORPROJECTREQUEST.fields_by_name['id']._options = None
  _UPDATEEVENTSTATEFORPROJECTREQUEST.fields_by_name['id']._serialized_options = b'\372B\020r\0162\014^E[0-9a-f]+$'
  _UPDATEEVENTSTATEFORPROJECTREQUEST.fields_by_name['project_id']._options = None
  _UPDATEEVENTSTATEFORPROJECTREQUEST.fields_by_name['project_id']._serialized_options = b'\372B,r*2(^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z0-9_-]+$'
  _UPDATEEVENTSTATEFORPROJECTREQUEST.fields_by_name['state']._options = None
  _UPDATEEVENTSTATEFORPROJECTREQUEST.fields_by_name['state']._serialized_options = b'\372B\005\212\001\002\020\001'
  _LISTEVENTRECORD.fields_by_name['event']._options = None
  _LISTEVENTRECORD.fields_by_name['event']._serialized_options = b'\372B\005\212\001\002\020\001'
  _LISTEVENTRECORD.fields_by_name['states']._options = None
  _LISTEVENTRECORD.fields_by_name['states']._serialized_options = b'\372B\n\222\001\007\"\005\212\001\002\020\001'
  _LISTEVENTSRESPONSE.fields_by_name['records']._options = None
  _LISTEVENTSRESPONSE.fields_by_name['records']._serialized_options = b'\372B\n\222\001\007\"\005\212\001\002\020\001'
  _GETPROJECTWAITINGEVENTSREQUEST.fields_by_name['project_id']._options = None
  _GETPROJECTWAITINGEVENTSREQUEST.fields_by_name['project_id']._serialized_options = b'\372B/r-2(^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z0-9_-]+$\320\001\001'
  _GETPROJECTWAITINGEVENTSRESPONSE.fields_by_name['event_ids']._options = None
  _GETPROJECTWAITINGEVENTSRESPONSE.fields_by_name['event_ids']._serialized_options = b'\372B\025\222\001\022\"\020r\0162\014^E[0-9a-f]+$'
  _MONITORPROJECTEVENTSREQUEST.fields_by_name['project_id']._options = None
  _MONITORPROJECTEVENTSREQUEST.fields_by_name['project_id']._serialized_options = b'\372B,r*2(^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z0-9_-]+$'
  _EVENTS.methods_by_name['IngestEvent']._options = None
  _EVENTS.methods_by_name['IngestEvent']._serialized_options = b'\202\323\344\223\002\023\"\016/api/v1/events:\001*'
  _EVENTS.methods_by_name['TrackIngestEvent']._options = None
  _EVENTS.methods_by_name['TrackIngestEvent']._serialized_options = b'\202\323\344\223\002\033\"\026/api/v1/tracked-events:\001*'
  _EVENTS.methods_by_name['MonitorProjectEvents']._options = None
  _EVENTS.methods_by_name['MonitorProjectEvents']._serialized_options = b'\202\323\344\223\002.\022,/api/v1/projects/{project_id}/monitor-events'
  _EVENTS.methods_by_name['GetEvent']._options = None
  _EVENTS.methods_by_name['GetEvent']._serialized_options = b'\202\323\344\223\002\025\022\023/api/v1/events/{id}'
  _EVENTS.methods_by_name['GetEventState']._options = None
  _EVENTS.methods_by_name['GetEventState']._serialized_options = b'\202\323\344\223\002\033\022\031/api/v1/events/{id}/state'
  _EVENTS.methods_by_name['UpdateEventState']._options = None
  _EVENTS.methods_by_name['UpdateEventState']._serialized_options = b'\202\323\344\223\002\033\"\031/api/v1/events/{id}/state'
  _EVENTS.methods_by_name['ListEvents']._options = None
  _EVENTS.methods_by_name['ListEvents']._serialized_options = b'\202\323\344\223\0028\022\016/api/v1/eventsZ&\022$/api/v1/projects/{project_id}/events'
  _EVENTS.methods_by_name['GetEventStateForProject']._options = None
  _EVENTS.methods_by_name['GetEventStateForProject']._serialized_options = b'\202\323\344\223\0021\022//api/v1/events/{id}/projects/{project_id}/state'
  _EVENTS.methods_by_name['UpdateEventStateForProject']._options = None
  _EVENTS.methods_by_name['UpdateEventStateForProject']._serialized_options = b'\202\323\344\223\0021\"//api/v1/events/{id}/projects/{project_id}/state'
  _EVENTS.methods_by_name['GetProjectWaitingEvents']._options = None
  _EVENTS.methods_by_name['GetProjectWaitingEvents']._serialized_options = b'\202\323\344\223\002\'\022%/api/v1/projects/{project_id}/waiting'
  _INGESTEVENTREQUEST._serialized_start=210
  _INGESTEVENTREQUEST._serialized_end=683
  _INGESTEVENTREQUEST_DATAENTRY._serialized_start=569
  _INGESTEVENTREQUEST_DATAENTRY._serialized_end=638
  _INGESTEVENTREQUEST_MEMOENTRY._serialized_start=640
  _INGESTEVENTREQUEST_MEMOENTRY._serialized_end=683
  _INGESTEVENTRESPONSE._serialized_start=685
  _INGESTEVENTRESPONSE._serialized_end=739
  _GETEVENTREQUEST._serialized_start=741
  _GETEVENTREQUEST._serialized_end=791
  _GETEVENTRESPONSE._serialized_start=793
  _GETEVENTRESPONSE._serialized_end=861
  _GETEVENTSTATEREQUEST._serialized_start=863
  _GETEVENTSTATEREQUEST._serialized_end=918
  _GETEVENTSTATERESPONSE._serialized_start=920
  _GETEVENTSTATERESPONSE._serialized_end=1007
  _GETEVENTSTATEFORPROJECTREQUEST._serialized_start=1010
  _GETEVENTSTATEFORPROJECTREQUEST._serialized_end=1144
  _GETEVENTSTATEFORPROJECTRESPONSE._serialized_start=1146
  _GETEVENTSTATEFORPROJECTRESPONSE._serialized_end=1250
  _UPDATEEVENTSTATEREQUEST._serialized_start=1252
  _UPDATEEVENTSTATEREQUEST._serialized_end=1365
  _UPDATEEVENTSTATERESPONSE._serialized_start=1367
  _UPDATEEVENTSTATERESPONSE._serialized_end=1393
  _UPDATEEVENTSTATEFORPROJECTREQUEST._serialized_start=1396
  _UPDATEEVENTSTATEFORPROJECTREQUEST._serialized_end=1595
  _UPDATEEVENTSTATEFORPROJECTRESPONSE._serialized_start=1597
  _UPDATEEVENTSTATEFORPROJECTRESPONSE._serialized_end=1633
  _LISTEVENTSREQUEST._serialized_start=1635
  _LISTEVENTSREQUEST._serialized_end=1700
  _LISTEVENTRECORD._serialized_start=1703
  _LISTEVENTRECORD._serialized_end=1837
  _LISTEVENTSRESPONSE._serialized_start=1839
  _LISTEVENTSRESPONSE._serialized_end=1929
  _GETPROJECTWAITINGEVENTSREQUEST._serialized_start=1931
  _GETPROJECTWAITINGEVENTSREQUEST._serialized_end=2035
  _GETPROJECTWAITINGEVENTSRESPONSE._serialized_start=2037
  _GETPROJECTWAITINGEVENTSRESPONSE._serialized_end=2115
  _MONITORPROJECTEVENTSREQUEST._serialized_start=2117
  _MONITORPROJECTEVENTSREQUEST._serialized_end=2215
  _EVENTS._serialized_start=2218
  _EVENTS._serialized_end=3807
# @@protoc_insertion_point(module_scope)
