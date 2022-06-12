# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: programssvc/svc.proto
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
from program import program_pb2 as program_dot_program__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15programssvc/svc.proto\x12\x16\x61utokitteh.programssvc\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17validate/validate.proto\x1a\x15program/program.proto\"\xa0\x01\n\nGetRequest\x12\x43\n\nproject_id\x18\x01 \x01(\tB/\xfa\x42,r*2(^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z0-9_-]+$\x12&\n\x04path\x18\x02 \x01(\x0b\x32\x18.autokitteh.program.Path\x12\x10\n\x08raw_path\x18\x03 \x01(\t\x12\x13\n\x0bomit_source\x18\x04 \x01(\x08\"\x7f\n\x0bGetResponse\x12\x30\n\x04path\x18\x01 \x01(\x0b\x32\x18.autokitteh.program.PathB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\x12\x0e\n\x06source\x18\x02 \x01(\x0c\x12.\n\nfetched_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp2\x90\x01\n\x08Programs\x12\x83\x01\n\x03Get\x12\".autokitteh.programssvc.GetRequest\x1a#.autokitteh.programssvc.GetResponse\"3\x82\xd3\xe4\x93\x02-\x12+/api/v1/programs/{project_id}/{raw_path=**}B&Z$go.autokitteh.dev/idl/go/programssvcb\x06proto3')



_GETREQUEST = DESCRIPTOR.message_types_by_name['GetRequest']
_GETRESPONSE = DESCRIPTOR.message_types_by_name['GetResponse']
GetRequest = _reflection.GeneratedProtocolMessageType('GetRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETREQUEST,
  '__module__' : 'programssvc.svc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.programssvc.GetRequest)
  })
_sym_db.RegisterMessage(GetRequest)

GetResponse = _reflection.GeneratedProtocolMessageType('GetResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETRESPONSE,
  '__module__' : 'programssvc.svc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.programssvc.GetResponse)
  })
_sym_db.RegisterMessage(GetResponse)

_PROGRAMS = DESCRIPTOR.services_by_name['Programs']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z$go.autokitteh.dev/idl/go/programssvc'
  _GETREQUEST.fields_by_name['project_id']._options = None
  _GETREQUEST.fields_by_name['project_id']._serialized_options = b'\372B,r*2(^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z0-9_-]+$'
  _GETRESPONSE.fields_by_name['path']._options = None
  _GETRESPONSE.fields_by_name['path']._serialized_options = b'\372B\005\212\001\002\020\001'
  _PROGRAMS.methods_by_name['Get']._options = None
  _PROGRAMS.methods_by_name['Get']._serialized_options = b'\202\323\344\223\002-\022+/api/v1/programs/{project_id}/{raw_path=**}'
  _GETREQUEST._serialized_start=161
  _GETREQUEST._serialized_end=321
  _GETRESPONSE._serialized_start=323
  _GETRESPONSE._serialized_end=450
  _PROGRAMS._serialized_start=453
  _PROGRAMS._serialized_end=597
# @@protoc_insertion_point(module_scope)
