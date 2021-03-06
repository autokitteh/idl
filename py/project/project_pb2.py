# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: project/project.proto
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
from program import program_pb2 as program_dot_program__pb2
from values import values_pb2 as values_dot_values__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15project/project.proto\x12\x12\x61utokitteh.project\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17validate/validate.proto\x1a\x15program/program.proto\x1a\x13values/values.proto\"l\n\rProjectPlugin\x12J\n\tplugin_id\x18\x01 \x01(\tB7\xfa\x42\x34r220^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z][0-9a-zA-Z_-]+$\x12\x0f\n\x07\x65nabled\x18\x02 \x01(\x08\"\xc2\x03\n\x0fProjectSettings\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x65nabled\x18\x02 \x01(\x08\x12+\n\tmain_path\x18\x03 \x01(\x0b\x32\x18.autokitteh.program.Path\x12k\n\x08predecls\x18\x05 \x03(\x0b\x32\x31.autokitteh.project.ProjectSettings.PredeclsEntryB&\xfa\x42#\x9a\x01 \x18\x01\"\x1cr\x1a\x32\x18^[a-zA-Z_][a-zA-Z0-9_]*$\x12\x41\n\x07plugins\x18\x06 \x03(\x0b\x32!.autokitteh.project.ProjectPluginB\r\xfa\x42\n\x92\x01\x07\"\x05\x8a\x01\x02\x10\x01\x12;\n\x04memo\x18\x32 \x03(\x0b\x32-.autokitteh.project.ProjectSettings.MemoEntry\x1aI\n\rPredeclsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\'\n\x05value\x18\x02 \x01(\x0b\x32\x18.autokitteh.values.Value:\x02\x38\x01\x1a+\n\tMemoEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xa1\x02\n\x07Project\x12>\n\x02id\x18\x01 \x01(\tB2\xfa\x42/r-2(^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z0-9_-]+$\xd0\x01\x01\x12\x35\n\x0c\x61\x63\x63ount_name\x18\x02 \x01(\tB\x1f\xfa\x42\x1cr\x1a\x32\x18^[a-zA-Z][0-9a-zA-Z_-]+$\x12?\n\x08settings\x18\x03 \x01(\x0b\x32#.autokitteh.project.ProjectSettingsB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\x12.\n\ncreated_at\x18\x64 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x65 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\"Z go.autokitteh.dev/idl/go/projectb\x06proto3')



_PROJECTPLUGIN = DESCRIPTOR.message_types_by_name['ProjectPlugin']
_PROJECTSETTINGS = DESCRIPTOR.message_types_by_name['ProjectSettings']
_PROJECTSETTINGS_PREDECLSENTRY = _PROJECTSETTINGS.nested_types_by_name['PredeclsEntry']
_PROJECTSETTINGS_MEMOENTRY = _PROJECTSETTINGS.nested_types_by_name['MemoEntry']
_PROJECT = DESCRIPTOR.message_types_by_name['Project']
ProjectPlugin = _reflection.GeneratedProtocolMessageType('ProjectPlugin', (_message.Message,), {
  'DESCRIPTOR' : _PROJECTPLUGIN,
  '__module__' : 'project.project_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.project.ProjectPlugin)
  })
_sym_db.RegisterMessage(ProjectPlugin)

ProjectSettings = _reflection.GeneratedProtocolMessageType('ProjectSettings', (_message.Message,), {

  'PredeclsEntry' : _reflection.GeneratedProtocolMessageType('PredeclsEntry', (_message.Message,), {
    'DESCRIPTOR' : _PROJECTSETTINGS_PREDECLSENTRY,
    '__module__' : 'project.project_pb2'
    # @@protoc_insertion_point(class_scope:autokitteh.project.ProjectSettings.PredeclsEntry)
    })
  ,

  'MemoEntry' : _reflection.GeneratedProtocolMessageType('MemoEntry', (_message.Message,), {
    'DESCRIPTOR' : _PROJECTSETTINGS_MEMOENTRY,
    '__module__' : 'project.project_pb2'
    # @@protoc_insertion_point(class_scope:autokitteh.project.ProjectSettings.MemoEntry)
    })
  ,
  'DESCRIPTOR' : _PROJECTSETTINGS,
  '__module__' : 'project.project_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.project.ProjectSettings)
  })
_sym_db.RegisterMessage(ProjectSettings)
_sym_db.RegisterMessage(ProjectSettings.PredeclsEntry)
_sym_db.RegisterMessage(ProjectSettings.MemoEntry)

Project = _reflection.GeneratedProtocolMessageType('Project', (_message.Message,), {
  'DESCRIPTOR' : _PROJECT,
  '__module__' : 'project.project_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.project.Project)
  })
_sym_db.RegisterMessage(Project)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z go.autokitteh.dev/idl/go/project'
  _PROJECTPLUGIN.fields_by_name['plugin_id']._options = None
  _PROJECTPLUGIN.fields_by_name['plugin_id']._serialized_options = b'\372B4r220^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z][0-9a-zA-Z_-]+$'
  _PROJECTSETTINGS_PREDECLSENTRY._options = None
  _PROJECTSETTINGS_PREDECLSENTRY._serialized_options = b'8\001'
  _PROJECTSETTINGS_MEMOENTRY._options = None
  _PROJECTSETTINGS_MEMOENTRY._serialized_options = b'8\001'
  _PROJECTSETTINGS.fields_by_name['predecls']._options = None
  _PROJECTSETTINGS.fields_by_name['predecls']._serialized_options = b'\372B#\232\001 \030\001\"\034r\0322\030^[a-zA-Z_][a-zA-Z0-9_]*$'
  _PROJECTSETTINGS.fields_by_name['plugins']._options = None
  _PROJECTSETTINGS.fields_by_name['plugins']._serialized_options = b'\372B\n\222\001\007\"\005\212\001\002\020\001'
  _PROJECT.fields_by_name['id']._options = None
  _PROJECT.fields_by_name['id']._serialized_options = b'\372B/r-2(^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z0-9_-]+$\320\001\001'
  _PROJECT.fields_by_name['account_name']._options = None
  _PROJECT.fields_by_name['account_name']._serialized_options = b'\372B\034r\0322\030^[a-zA-Z][0-9a-zA-Z_-]+$'
  _PROJECT.fields_by_name['settings']._options = None
  _PROJECT.fields_by_name['settings']._serialized_options = b'\372B\005\212\001\002\020\001'
  _PROJECTPLUGIN._serialized_start=147
  _PROJECTPLUGIN._serialized_end=255
  _PROJECTSETTINGS._serialized_start=258
  _PROJECTSETTINGS._serialized_end=708
  _PROJECTSETTINGS_PREDECLSENTRY._serialized_start=590
  _PROJECTSETTINGS_PREDECLSENTRY._serialized_end=663
  _PROJECTSETTINGS_MEMOENTRY._serialized_start=665
  _PROJECTSETTINGS_MEMOENTRY._serialized_end=708
  _PROJECT._serialized_start=711
  _PROJECT._serialized_end=1000
# @@protoc_insertion_point(module_scope)
