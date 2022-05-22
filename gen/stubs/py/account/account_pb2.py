# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: account/account.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x61\x63\x63ount/account.proto\x12\x12\x61utokitteh.account\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17validate/validate.proto\"\x9a\x01\n\x0f\x41\x63\x63ountSettings\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12I\n\x04memo\x18\x32 \x03(\x0b\x32-.autokitteh.account.AccountSettings.MemoEntryB\x0c\xfa\x42\t\x9a\x01\x06\"\x04r\x02\x10\x01\x1a+\n\tMemoEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xcf\x01\n\x07\x41\x63\x63ount\x12-\n\x04name\x18\x01 \x01(\tB\x1f\xfa\x42\x1cr\x1a\x32\x18^[a-zA-Z][0-9a-zA-Z_-]+$\x12\x35\n\x08settings\x18\x02 \x01(\x0b\x32#.autokitteh.account.AccountSettings\x12.\n\ncreated_at\x18\x64 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x65 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x1fZ\x1dgo.autokitteh.dev/idl/accountb\x06proto3')



_ACCOUNTSETTINGS = DESCRIPTOR.message_types_by_name['AccountSettings']
_ACCOUNTSETTINGS_MEMOENTRY = _ACCOUNTSETTINGS.nested_types_by_name['MemoEntry']
_ACCOUNT = DESCRIPTOR.message_types_by_name['Account']
AccountSettings = _reflection.GeneratedProtocolMessageType('AccountSettings', (_message.Message,), {

  'MemoEntry' : _reflection.GeneratedProtocolMessageType('MemoEntry', (_message.Message,), {
    'DESCRIPTOR' : _ACCOUNTSETTINGS_MEMOENTRY,
    '__module__' : 'account.account_pb2'
    # @@protoc_insertion_point(class_scope:autokitteh.account.AccountSettings.MemoEntry)
    })
  ,
  'DESCRIPTOR' : _ACCOUNTSETTINGS,
  '__module__' : 'account.account_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.account.AccountSettings)
  })
_sym_db.RegisterMessage(AccountSettings)
_sym_db.RegisterMessage(AccountSettings.MemoEntry)

Account = _reflection.GeneratedProtocolMessageType('Account', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNT,
  '__module__' : 'account.account_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.account.Account)
  })
_sym_db.RegisterMessage(Account)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\035go.autokitteh.dev/idl/account'
  _ACCOUNTSETTINGS_MEMOENTRY._options = None
  _ACCOUNTSETTINGS_MEMOENTRY._serialized_options = b'8\001'
  _ACCOUNTSETTINGS.fields_by_name['memo']._options = None
  _ACCOUNTSETTINGS.fields_by_name['memo']._serialized_options = b'\372B\t\232\001\006\"\004r\002\020\001'
  _ACCOUNT.fields_by_name['name']._options = None
  _ACCOUNT.fields_by_name['name']._serialized_options = b'\372B\034r\0322\030^[a-zA-Z][0-9a-zA-Z_-]+$'
  _ACCOUNTSETTINGS._serialized_start=104
  _ACCOUNTSETTINGS._serialized_end=258
  _ACCOUNTSETTINGS_MEMOENTRY._serialized_start=215
  _ACCOUNTSETTINGS_MEMOENTRY._serialized_end=258
  _ACCOUNT._serialized_start=261
  _ACCOUNT._serialized_end=468
# @@protoc_insertion_point(module_scope)
