# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: projectsvc/svc.proto
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
from project import project_pb2 as project_dot_project__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14projectsvc/svc.proto\x12\x15\x61utokitteh.projectsvc\x1a\x1cgoogle/api/annotations.proto\x1a\x17validate/validate.proto\x1a\x15project/project.proto\"\xce\x01\n\x14\x43reateProjectRequest\x12\x35\n\x0c\x61\x63\x63ount_name\x18\x01 \x01(\tB\x1f\xfa\x42\x1cr\x1a\x32\x18^[a-zA-Z][0-9a-zA-Z_-]+$\x12>\n\x02id\x18\x02 \x01(\tB2\xfa\x42/r-2(^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z0-9_-]+$\xd0\x01\x01\x12?\n\x08settings\x18\x03 \x01(\x0b\x32#.autokitteh.project.ProjectSettingsB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\"T\n\x15\x43reateProjectResponse\x12;\n\x02id\x18\x01 \x01(\tB/\xfa\x42,r*2(^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z0-9_-]+$\"\x94\x01\n\x14UpdateProjectRequest\x12;\n\x02id\x18\x01 \x01(\tB/\xfa\x42,r*2(^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z0-9_-]+$\x12?\n\x08settings\x18\x02 \x01(\x0b\x32#.autokitteh.project.ProjectSettingsB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\"\x17\n\x15UpdateProjectResponse\"S\n\x14RemoveProjectRequest\x12;\n\x02id\x18\x01 \x01(\tB/\xfa\x42,r*2(^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z0-9_-]+$\"\x17\n\x15RemoveProjectResponse\"P\n\x11GetProjectRequest\x12;\n\x02id\x18\x01 \x01(\tB/\xfa\x42,r*2(^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z0-9_-]+$\"L\n\x12GetProjectResponse\x12\x36\n\x07project\x18\x01 \x01(\x0b\x32\x1b.autokitteh.project.ProjectB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\"W\n\x12GetProjectsRequest\x12\x41\n\x03ids\x18\x01 \x03(\tB4\xfa\x42\x31\x92\x01.\",r*2(^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z0-9_-]+$\"S\n\x13GetProjectsResponse\x12<\n\x08projects\x18\x01 \x03(\x0b\x32\x1b.autokitteh.project.ProjectB\r\xfa\x42\n\x92\x01\x07\"\x05\x8a\x01\x02\x10\x01\x32\xaa\x04\n\x08Projects\x12\x87\x01\n\rCreateProject\x12+.autokitteh.projectsvc.CreateProjectRequest\x1a,.autokitteh.projectsvc.CreateProjectResponse\"\x1b\x82\xd3\xe4\x93\x02\x15\"\x10/api/v1/projects:\x01*\x12\x8c\x01\n\rUpdateProject\x12+.autokitteh.projectsvc.UpdateProjectRequest\x1a,.autokitteh.projectsvc.UpdateProjectResponse\" \x82\xd3\xe4\x93\x02\x1a\"\x15/api/v1/projects/{id}:\x01*\x12\x80\x01\n\nGetProject\x12(.autokitteh.projectsvc.GetProjectRequest\x1a).autokitteh.projectsvc.GetProjectResponse\"\x1d\x82\xd3\xe4\x93\x02\x17\x12\x15/api/v1/projects/{id}\x12\x81\x01\n\x0bGetProjects\x12).autokitteh.projectsvc.GetProjectsRequest\x1a*.autokitteh.projectsvc.GetProjectsResponse\"\x1b\x82\xd3\xe4\x93\x02\x15\"\x10/api/v1/projects:\x01*B%Z#go.autokitteh.dev/idl/go/projectsvcb\x06proto3')



_CREATEPROJECTREQUEST = DESCRIPTOR.message_types_by_name['CreateProjectRequest']
_CREATEPROJECTRESPONSE = DESCRIPTOR.message_types_by_name['CreateProjectResponse']
_UPDATEPROJECTREQUEST = DESCRIPTOR.message_types_by_name['UpdateProjectRequest']
_UPDATEPROJECTRESPONSE = DESCRIPTOR.message_types_by_name['UpdateProjectResponse']
_REMOVEPROJECTREQUEST = DESCRIPTOR.message_types_by_name['RemoveProjectRequest']
_REMOVEPROJECTRESPONSE = DESCRIPTOR.message_types_by_name['RemoveProjectResponse']
_GETPROJECTREQUEST = DESCRIPTOR.message_types_by_name['GetProjectRequest']
_GETPROJECTRESPONSE = DESCRIPTOR.message_types_by_name['GetProjectResponse']
_GETPROJECTSREQUEST = DESCRIPTOR.message_types_by_name['GetProjectsRequest']
_GETPROJECTSRESPONSE = DESCRIPTOR.message_types_by_name['GetProjectsResponse']
CreateProjectRequest = _reflection.GeneratedProtocolMessageType('CreateProjectRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEPROJECTREQUEST,
  '__module__' : 'projectsvc.svc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.projectsvc.CreateProjectRequest)
  })
_sym_db.RegisterMessage(CreateProjectRequest)

CreateProjectResponse = _reflection.GeneratedProtocolMessageType('CreateProjectResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEPROJECTRESPONSE,
  '__module__' : 'projectsvc.svc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.projectsvc.CreateProjectResponse)
  })
_sym_db.RegisterMessage(CreateProjectResponse)

UpdateProjectRequest = _reflection.GeneratedProtocolMessageType('UpdateProjectRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEPROJECTREQUEST,
  '__module__' : 'projectsvc.svc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.projectsvc.UpdateProjectRequest)
  })
_sym_db.RegisterMessage(UpdateProjectRequest)

UpdateProjectResponse = _reflection.GeneratedProtocolMessageType('UpdateProjectResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEPROJECTRESPONSE,
  '__module__' : 'projectsvc.svc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.projectsvc.UpdateProjectResponse)
  })
_sym_db.RegisterMessage(UpdateProjectResponse)

RemoveProjectRequest = _reflection.GeneratedProtocolMessageType('RemoveProjectRequest', (_message.Message,), {
  'DESCRIPTOR' : _REMOVEPROJECTREQUEST,
  '__module__' : 'projectsvc.svc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.projectsvc.RemoveProjectRequest)
  })
_sym_db.RegisterMessage(RemoveProjectRequest)

RemoveProjectResponse = _reflection.GeneratedProtocolMessageType('RemoveProjectResponse', (_message.Message,), {
  'DESCRIPTOR' : _REMOVEPROJECTRESPONSE,
  '__module__' : 'projectsvc.svc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.projectsvc.RemoveProjectResponse)
  })
_sym_db.RegisterMessage(RemoveProjectResponse)

GetProjectRequest = _reflection.GeneratedProtocolMessageType('GetProjectRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETPROJECTREQUEST,
  '__module__' : 'projectsvc.svc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.projectsvc.GetProjectRequest)
  })
_sym_db.RegisterMessage(GetProjectRequest)

GetProjectResponse = _reflection.GeneratedProtocolMessageType('GetProjectResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETPROJECTRESPONSE,
  '__module__' : 'projectsvc.svc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.projectsvc.GetProjectResponse)
  })
_sym_db.RegisterMessage(GetProjectResponse)

GetProjectsRequest = _reflection.GeneratedProtocolMessageType('GetProjectsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETPROJECTSREQUEST,
  '__module__' : 'projectsvc.svc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.projectsvc.GetProjectsRequest)
  })
_sym_db.RegisterMessage(GetProjectsRequest)

GetProjectsResponse = _reflection.GeneratedProtocolMessageType('GetProjectsResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETPROJECTSRESPONSE,
  '__module__' : 'projectsvc.svc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.projectsvc.GetProjectsResponse)
  })
_sym_db.RegisterMessage(GetProjectsResponse)

_PROJECTS = DESCRIPTOR.services_by_name['Projects']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z#go.autokitteh.dev/idl/go/projectsvc'
  _CREATEPROJECTREQUEST.fields_by_name['account_name']._options = None
  _CREATEPROJECTREQUEST.fields_by_name['account_name']._serialized_options = b'\372B\034r\0322\030^[a-zA-Z][0-9a-zA-Z_-]+$'
  _CREATEPROJECTREQUEST.fields_by_name['id']._options = None
  _CREATEPROJECTREQUEST.fields_by_name['id']._serialized_options = b'\372B/r-2(^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z0-9_-]+$\320\001\001'
  _CREATEPROJECTREQUEST.fields_by_name['settings']._options = None
  _CREATEPROJECTREQUEST.fields_by_name['settings']._serialized_options = b'\372B\005\212\001\002\020\001'
  _CREATEPROJECTRESPONSE.fields_by_name['id']._options = None
  _CREATEPROJECTRESPONSE.fields_by_name['id']._serialized_options = b'\372B,r*2(^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z0-9_-]+$'
  _UPDATEPROJECTREQUEST.fields_by_name['id']._options = None
  _UPDATEPROJECTREQUEST.fields_by_name['id']._serialized_options = b'\372B,r*2(^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z0-9_-]+$'
  _UPDATEPROJECTREQUEST.fields_by_name['settings']._options = None
  _UPDATEPROJECTREQUEST.fields_by_name['settings']._serialized_options = b'\372B\005\212\001\002\020\001'
  _REMOVEPROJECTREQUEST.fields_by_name['id']._options = None
  _REMOVEPROJECTREQUEST.fields_by_name['id']._serialized_options = b'\372B,r*2(^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z0-9_-]+$'
  _GETPROJECTREQUEST.fields_by_name['id']._options = None
  _GETPROJECTREQUEST.fields_by_name['id']._serialized_options = b'\372B,r*2(^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z0-9_-]+$'
  _GETPROJECTRESPONSE.fields_by_name['project']._options = None
  _GETPROJECTRESPONSE.fields_by_name['project']._serialized_options = b'\372B\005\212\001\002\020\001'
  _GETPROJECTSREQUEST.fields_by_name['ids']._options = None
  _GETPROJECTSREQUEST.fields_by_name['ids']._serialized_options = b'\372B1\222\001.\",r*2(^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z0-9_-]+$'
  _GETPROJECTSRESPONSE.fields_by_name['projects']._options = None
  _GETPROJECTSRESPONSE.fields_by_name['projects']._serialized_options = b'\372B\n\222\001\007\"\005\212\001\002\020\001'
  _PROJECTS.methods_by_name['CreateProject']._options = None
  _PROJECTS.methods_by_name['CreateProject']._serialized_options = b'\202\323\344\223\002\025\"\020/api/v1/projects:\001*'
  _PROJECTS.methods_by_name['UpdateProject']._options = None
  _PROJECTS.methods_by_name['UpdateProject']._serialized_options = b'\202\323\344\223\002\032\"\025/api/v1/projects/{id}:\001*'
  _PROJECTS.methods_by_name['GetProject']._options = None
  _PROJECTS.methods_by_name['GetProject']._serialized_options = b'\202\323\344\223\002\027\022\025/api/v1/projects/{id}'
  _PROJECTS.methods_by_name['GetProjects']._options = None
  _PROJECTS.methods_by_name['GetProjects']._serialized_options = b'\202\323\344\223\002\025\"\020/api/v1/projects:\001*'
  _CREATEPROJECTREQUEST._serialized_start=126
  _CREATEPROJECTREQUEST._serialized_end=332
  _CREATEPROJECTRESPONSE._serialized_start=334
  _CREATEPROJECTRESPONSE._serialized_end=418
  _UPDATEPROJECTREQUEST._serialized_start=421
  _UPDATEPROJECTREQUEST._serialized_end=569
  _UPDATEPROJECTRESPONSE._serialized_start=571
  _UPDATEPROJECTRESPONSE._serialized_end=594
  _REMOVEPROJECTREQUEST._serialized_start=596
  _REMOVEPROJECTREQUEST._serialized_end=679
  _REMOVEPROJECTRESPONSE._serialized_start=681
  _REMOVEPROJECTRESPONSE._serialized_end=704
  _GETPROJECTREQUEST._serialized_start=706
  _GETPROJECTREQUEST._serialized_end=786
  _GETPROJECTRESPONSE._serialized_start=788
  _GETPROJECTRESPONSE._serialized_end=864
  _GETPROJECTSREQUEST._serialized_start=866
  _GETPROJECTSREQUEST._serialized_end=953
  _GETPROJECTSRESPONSE._serialized_start=955
  _GETPROJECTSRESPONSE._serialized_end=1038
  _PROJECTS._serialized_start=1041
  _PROJECTS._serialized_end=1595
# @@protoc_insertion_point(module_scope)
