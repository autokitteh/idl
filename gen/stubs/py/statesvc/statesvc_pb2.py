# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: statesvc/statesvc.proto
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
from values import values_pb2 as values_dot_values__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17statesvc/statesvc.proto\x12\x13\x61utokitteh.statesvc\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17validate/validate.proto\x1a\x13values/values.proto\"\xa9\x01\n\nSetRequest\x12\x43\n\nproject_id\x18\x01 \x01(\tB/\xfa\x42,r*2(^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z0-9_-]+$\x12-\n\x04name\x18\x02 \x01(\tB\x1f\xfa\x42\x1cr\x1a\x32\x18^[a-zA-Z_][a-zA-Z0-9_]*$\x12\'\n\x05value\x18\x03 \x01(\x0b\x32\x18.autokitteh.values.Value\"\r\n\x0bSetResponse\"?\n\rValueMetadata\x12.\n\nupdated_at\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xb6\x01\n\nGetRequest\x12\x43\n\nproject_id\x18\x01 \x01(\tB/\xfa\x42,r*2(^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z0-9_-]+$\x12-\n\x04name\x18\x02 \x01(\tB\x1f\xfa\x42\x1cr\x1a\x32\x18^[a-zA-Z_][a-zA-Z0-9_]*$\x12\x34\n\x08metadata\x18\x03 \x01(\x0b\x32\".autokitteh.statesvc.ValueMetadata\"v\n\x0bGetResponse\x12\x31\n\x05value\x18\x01 \x01(\x0b\x32\x18.autokitteh.values.ValueB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\x12\x34\n\x08metadata\x18\x02 \x01(\x0b\x32\".autokitteh.statesvc.ValueMetadata\"R\n\x0bListRequest\x12\x43\n\nproject_id\x18\x01 \x01(\tB/\xfa\x42,r*2(^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z0-9_-]+$\"\x1d\n\x0cListResponse\x12\r\n\x05names\x18\x01 \x03(\t2\xe8\x02\n\x05State\x12w\n\x03Set\x12\x1f.autokitteh.statesvc.SetRequest\x1a .autokitteh.statesvc.SetResponse\"-\x82\xd3\xe4\x93\x02\'\"\"/api/v1/states/{project_id}/{name}:\x01*\x12t\n\x03Get\x12\x1f.autokitteh.statesvc.GetRequest\x1a .autokitteh.statesvc.GetResponse\"*\x82\xd3\xe4\x93\x02$\x12\"/api/v1/states/{project_id}/{name}\x12p\n\x04List\x12 .autokitteh.statesvc.ListRequest\x1a!.autokitteh.statesvc.ListResponse\"#\x82\xd3\xe4\x93\x02\x1d\x12\x1b/api/v1/states/{project_id}B Z\x1ego.autokitteh.dev/idl/statesvcb\x06proto3')



_SETREQUEST = DESCRIPTOR.message_types_by_name['SetRequest']
_SETRESPONSE = DESCRIPTOR.message_types_by_name['SetResponse']
_VALUEMETADATA = DESCRIPTOR.message_types_by_name['ValueMetadata']
_GETREQUEST = DESCRIPTOR.message_types_by_name['GetRequest']
_GETRESPONSE = DESCRIPTOR.message_types_by_name['GetResponse']
_LISTREQUEST = DESCRIPTOR.message_types_by_name['ListRequest']
_LISTRESPONSE = DESCRIPTOR.message_types_by_name['ListResponse']
SetRequest = _reflection.GeneratedProtocolMessageType('SetRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETREQUEST,
  '__module__' : 'statesvc.statesvc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.statesvc.SetRequest)
  })
_sym_db.RegisterMessage(SetRequest)

SetResponse = _reflection.GeneratedProtocolMessageType('SetResponse', (_message.Message,), {
  'DESCRIPTOR' : _SETRESPONSE,
  '__module__' : 'statesvc.statesvc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.statesvc.SetResponse)
  })
_sym_db.RegisterMessage(SetResponse)

ValueMetadata = _reflection.GeneratedProtocolMessageType('ValueMetadata', (_message.Message,), {
  'DESCRIPTOR' : _VALUEMETADATA,
  '__module__' : 'statesvc.statesvc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.statesvc.ValueMetadata)
  })
_sym_db.RegisterMessage(ValueMetadata)

GetRequest = _reflection.GeneratedProtocolMessageType('GetRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETREQUEST,
  '__module__' : 'statesvc.statesvc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.statesvc.GetRequest)
  })
_sym_db.RegisterMessage(GetRequest)

GetResponse = _reflection.GeneratedProtocolMessageType('GetResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETRESPONSE,
  '__module__' : 'statesvc.statesvc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.statesvc.GetResponse)
  })
_sym_db.RegisterMessage(GetResponse)

ListRequest = _reflection.GeneratedProtocolMessageType('ListRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTREQUEST,
  '__module__' : 'statesvc.statesvc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.statesvc.ListRequest)
  })
_sym_db.RegisterMessage(ListRequest)

ListResponse = _reflection.GeneratedProtocolMessageType('ListResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTRESPONSE,
  '__module__' : 'statesvc.statesvc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.statesvc.ListResponse)
  })
_sym_db.RegisterMessage(ListResponse)

_STATE = DESCRIPTOR.services_by_name['State']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\036go.autokitteh.dev/idl/statesvc'
  _SETREQUEST.fields_by_name['project_id']._options = None
  _SETREQUEST.fields_by_name['project_id']._serialized_options = b'\372B,r*2(^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z0-9_-]+$'
  _SETREQUEST.fields_by_name['name']._options = None
  _SETREQUEST.fields_by_name['name']._serialized_options = b'\372B\034r\0322\030^[a-zA-Z_][a-zA-Z0-9_]*$'
  _GETREQUEST.fields_by_name['project_id']._options = None
  _GETREQUEST.fields_by_name['project_id']._serialized_options = b'\372B,r*2(^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z0-9_-]+$'
  _GETREQUEST.fields_by_name['name']._options = None
  _GETREQUEST.fields_by_name['name']._serialized_options = b'\372B\034r\0322\030^[a-zA-Z_][a-zA-Z0-9_]*$'
  _GETRESPONSE.fields_by_name['value']._options = None
  _GETRESPONSE.fields_by_name['value']._serialized_options = b'\372B\005\212\001\002\020\001'
  _LISTREQUEST.fields_by_name['project_id']._options = None
  _LISTREQUEST.fields_by_name['project_id']._serialized_options = b'\372B,r*2(^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z0-9_-]+$'
  _STATE.methods_by_name['Set']._options = None
  _STATE.methods_by_name['Set']._serialized_options = b'\202\323\344\223\002\'\"\"/api/v1/states/{project_id}/{name}:\001*'
  _STATE.methods_by_name['Get']._options = None
  _STATE.methods_by_name['Get']._serialized_options = b'\202\323\344\223\002$\022\"/api/v1/states/{project_id}/{name}'
  _STATE.methods_by_name['List']._options = None
  _STATE.methods_by_name['List']._serialized_options = b'\202\323\344\223\002\035\022\033/api/v1/states/{project_id}'
  _SETREQUEST._serialized_start=158
  _SETREQUEST._serialized_end=327
  _SETRESPONSE._serialized_start=329
  _SETRESPONSE._serialized_end=342
  _VALUEMETADATA._serialized_start=344
  _VALUEMETADATA._serialized_end=407
  _GETREQUEST._serialized_start=410
  _GETREQUEST._serialized_end=592
  _GETRESPONSE._serialized_start=594
  _GETRESPONSE._serialized_end=712
  _LISTREQUEST._serialized_start=714
  _LISTREQUEST._serialized_end=796
  _LISTRESPONSE._serialized_start=798
  _LISTRESPONSE._serialized_end=827
  _STATE._serialized_start=830
  _STATE._serialized_end=1190
# @@protoc_insertion_point(module_scope)
