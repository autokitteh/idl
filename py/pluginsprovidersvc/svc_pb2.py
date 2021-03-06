# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pluginsprovidersvc/svc.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from validate import validate_pb2 as validate_dot_validate__pb2
from plugin import desc_pb2 as plugin_dot_desc__pb2
from values import values_pb2 as values_dot_values__pb2
from program import error_pb2 as program_dot_error__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cpluginsprovidersvc/svc.proto\x12\x1d\x61utokitteh.pluginsprovidersvc\x1a\x17validate/validate.proto\x1a\x11plugin/desc.proto\x1a\x13values/values.proto\x1a\x13program/error.proto\"\r\n\x0bListRequest\"Y\n\x0cListResponse\x12I\n\x03ids\x18\x01 \x03(\tB<\xfa\x42\x39\x92\x01\x36\"4r220^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z][0-9a-zA-Z_-]+$\"V\n\x0f\x44\x65scribeRequest\x12\x43\n\x02id\x18\x01 \x01(\tB7\xfa\x42\x34r220^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z][0-9a-zA-Z_-]+$\"I\n\x10\x44\x65scribeResponse\x12\x35\n\x04\x64\x65sc\x18\x01 \x01(\x0b\x32\x1d.autokitteh.plugin.PluginDescB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\"\x8c\x01\n\x10GetValuesRequest\x12\x43\n\x02id\x18\x01 \x01(\tB7\xfa\x42\x34r220^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z][0-9a-zA-Z_-]+$\x12\x33\n\x05names\x18\x02 \x03(\tB$\xfa\x42!\x92\x01\x1e\"\x1cr\x1a\x32\x18^[a-zA-Z_][a-zA-Z0-9_]*$\"\xd2\x01\n\x11GetValuesResponse\x12t\n\x06values\x18\x01 \x03(\x0b\x32<.autokitteh.pluginsprovidersvc.GetValuesResponse.ValuesEntryB&\xfa\x42#\x9a\x01 \x18\x01\"\x1cr\x1a\x32\x18^[a-zA-Z_][a-zA-Z0-9_]*$\x1aG\n\x0bValuesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\'\n\x05value\x18\x02 \x01(\x0b\x32\x18.autokitteh.values.Value:\x02\x38\x01\"\xff\x02\n\x10\x43\x61llValueRequest\x12\x43\n\x02id\x18\x01 \x01(\tB7\xfa\x42\x34r220^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z][0-9a-zA-Z_-]+$\x12\x31\n\x05value\x18\x02 \x01(\x0b\x32\x18.autokitteh.values.ValueB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\x12\x35\n\x04\x61rgs\x18\x03 \x03(\x0b\x32\x18.autokitteh.values.ValueB\r\xfa\x42\n\x92\x01\x07\"\x05\x8a\x01\x02\x10\x01\x12s\n\x06kwargs\x18\x04 \x03(\x0b\x32;.autokitteh.pluginsprovidersvc.CallValueRequest.KwargsEntryB&\xfa\x42#\x9a\x01 \x18\x01\"\x1cr\x1a\x32\x18^[a-zA-Z_][a-zA-Z0-9_]*$\x1aG\n\x0bKwargsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\'\n\x05value\x18\x02 \x01(\x0b\x32\x18.autokitteh.values.Value:\x02\x38\x01\"r\n\x11\x43\x61llValueResponse\x12*\n\x06retval\x18\x01 \x01(\x0b\x32\x18.autokitteh.values.ValueH\x00\x12*\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x19.autokitteh.program.ErrorH\x00\x42\x05\n\x03ret2\xbf\x03\n\x0fPluginsProvider\x12_\n\x04List\x12*.autokitteh.pluginsprovidersvc.ListRequest\x1a+.autokitteh.pluginsprovidersvc.ListResponse\x12k\n\x08\x44\x65scribe\x12..autokitteh.pluginsprovidersvc.DescribeRequest\x1a/.autokitteh.pluginsprovidersvc.DescribeResponse\x12n\n\tGetValues\x12/.autokitteh.pluginsprovidersvc.GetValuesRequest\x1a\x30.autokitteh.pluginsprovidersvc.GetValuesResponse\x12n\n\tCallValue\x12/.autokitteh.pluginsprovidersvc.CallValueRequest\x1a\x30.autokitteh.pluginsprovidersvc.CallValueResponseB-Z+go.autokitteh.dev/idl/go/pluginsprovidersvcb\x06proto3')



_LISTREQUEST = DESCRIPTOR.message_types_by_name['ListRequest']
_LISTRESPONSE = DESCRIPTOR.message_types_by_name['ListResponse']
_DESCRIBEREQUEST = DESCRIPTOR.message_types_by_name['DescribeRequest']
_DESCRIBERESPONSE = DESCRIPTOR.message_types_by_name['DescribeResponse']
_GETVALUESREQUEST = DESCRIPTOR.message_types_by_name['GetValuesRequest']
_GETVALUESRESPONSE = DESCRIPTOR.message_types_by_name['GetValuesResponse']
_GETVALUESRESPONSE_VALUESENTRY = _GETVALUESRESPONSE.nested_types_by_name['ValuesEntry']
_CALLVALUEREQUEST = DESCRIPTOR.message_types_by_name['CallValueRequest']
_CALLVALUEREQUEST_KWARGSENTRY = _CALLVALUEREQUEST.nested_types_by_name['KwargsEntry']
_CALLVALUERESPONSE = DESCRIPTOR.message_types_by_name['CallValueResponse']
ListRequest = _reflection.GeneratedProtocolMessageType('ListRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTREQUEST,
  '__module__' : 'pluginsprovidersvc.svc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.pluginsprovidersvc.ListRequest)
  })
_sym_db.RegisterMessage(ListRequest)

ListResponse = _reflection.GeneratedProtocolMessageType('ListResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTRESPONSE,
  '__module__' : 'pluginsprovidersvc.svc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.pluginsprovidersvc.ListResponse)
  })
_sym_db.RegisterMessage(ListResponse)

DescribeRequest = _reflection.GeneratedProtocolMessageType('DescribeRequest', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEREQUEST,
  '__module__' : 'pluginsprovidersvc.svc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.pluginsprovidersvc.DescribeRequest)
  })
_sym_db.RegisterMessage(DescribeRequest)

DescribeResponse = _reflection.GeneratedProtocolMessageType('DescribeResponse', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBERESPONSE,
  '__module__' : 'pluginsprovidersvc.svc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.pluginsprovidersvc.DescribeResponse)
  })
_sym_db.RegisterMessage(DescribeResponse)

GetValuesRequest = _reflection.GeneratedProtocolMessageType('GetValuesRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETVALUESREQUEST,
  '__module__' : 'pluginsprovidersvc.svc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.pluginsprovidersvc.GetValuesRequest)
  })
_sym_db.RegisterMessage(GetValuesRequest)

GetValuesResponse = _reflection.GeneratedProtocolMessageType('GetValuesResponse', (_message.Message,), {

  'ValuesEntry' : _reflection.GeneratedProtocolMessageType('ValuesEntry', (_message.Message,), {
    'DESCRIPTOR' : _GETVALUESRESPONSE_VALUESENTRY,
    '__module__' : 'pluginsprovidersvc.svc_pb2'
    # @@protoc_insertion_point(class_scope:autokitteh.pluginsprovidersvc.GetValuesResponse.ValuesEntry)
    })
  ,
  'DESCRIPTOR' : _GETVALUESRESPONSE,
  '__module__' : 'pluginsprovidersvc.svc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.pluginsprovidersvc.GetValuesResponse)
  })
_sym_db.RegisterMessage(GetValuesResponse)
_sym_db.RegisterMessage(GetValuesResponse.ValuesEntry)

CallValueRequest = _reflection.GeneratedProtocolMessageType('CallValueRequest', (_message.Message,), {

  'KwargsEntry' : _reflection.GeneratedProtocolMessageType('KwargsEntry', (_message.Message,), {
    'DESCRIPTOR' : _CALLVALUEREQUEST_KWARGSENTRY,
    '__module__' : 'pluginsprovidersvc.svc_pb2'
    # @@protoc_insertion_point(class_scope:autokitteh.pluginsprovidersvc.CallValueRequest.KwargsEntry)
    })
  ,
  'DESCRIPTOR' : _CALLVALUEREQUEST,
  '__module__' : 'pluginsprovidersvc.svc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.pluginsprovidersvc.CallValueRequest)
  })
_sym_db.RegisterMessage(CallValueRequest)
_sym_db.RegisterMessage(CallValueRequest.KwargsEntry)

CallValueResponse = _reflection.GeneratedProtocolMessageType('CallValueResponse', (_message.Message,), {
  'DESCRIPTOR' : _CALLVALUERESPONSE,
  '__module__' : 'pluginsprovidersvc.svc_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.pluginsprovidersvc.CallValueResponse)
  })
_sym_db.RegisterMessage(CallValueResponse)

_PLUGINSPROVIDER = DESCRIPTOR.services_by_name['PluginsProvider']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z+go.autokitteh.dev/idl/go/pluginsprovidersvc'
  _LISTRESPONSE.fields_by_name['ids']._options = None
  _LISTRESPONSE.fields_by_name['ids']._serialized_options = b'\372B9\222\0016\"4r220^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z][0-9a-zA-Z_-]+$'
  _DESCRIBEREQUEST.fields_by_name['id']._options = None
  _DESCRIBEREQUEST.fields_by_name['id']._serialized_options = b'\372B4r220^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z][0-9a-zA-Z_-]+$'
  _DESCRIBERESPONSE.fields_by_name['desc']._options = None
  _DESCRIBERESPONSE.fields_by_name['desc']._serialized_options = b'\372B\005\212\001\002\020\001'
  _GETVALUESREQUEST.fields_by_name['id']._options = None
  _GETVALUESREQUEST.fields_by_name['id']._serialized_options = b'\372B4r220^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z][0-9a-zA-Z_-]+$'
  _GETVALUESREQUEST.fields_by_name['names']._options = None
  _GETVALUESREQUEST.fields_by_name['names']._serialized_options = b'\372B!\222\001\036\"\034r\0322\030^[a-zA-Z_][a-zA-Z0-9_]*$'
  _GETVALUESRESPONSE_VALUESENTRY._options = None
  _GETVALUESRESPONSE_VALUESENTRY._serialized_options = b'8\001'
  _GETVALUESRESPONSE.fields_by_name['values']._options = None
  _GETVALUESRESPONSE.fields_by_name['values']._serialized_options = b'\372B#\232\001 \030\001\"\034r\0322\030^[a-zA-Z_][a-zA-Z0-9_]*$'
  _CALLVALUEREQUEST_KWARGSENTRY._options = None
  _CALLVALUEREQUEST_KWARGSENTRY._serialized_options = b'8\001'
  _CALLVALUEREQUEST.fields_by_name['id']._options = None
  _CALLVALUEREQUEST.fields_by_name['id']._serialized_options = b'\372B4r220^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z][0-9a-zA-Z_-]+$'
  _CALLVALUEREQUEST.fields_by_name['value']._options = None
  _CALLVALUEREQUEST.fields_by_name['value']._serialized_options = b'\372B\005\212\001\002\020\001'
  _CALLVALUEREQUEST.fields_by_name['args']._options = None
  _CALLVALUEREQUEST.fields_by_name['args']._serialized_options = b'\372B\n\222\001\007\"\005\212\001\002\020\001'
  _CALLVALUEREQUEST.fields_by_name['kwargs']._options = None
  _CALLVALUEREQUEST.fields_by_name['kwargs']._serialized_options = b'\372B#\232\001 \030\001\"\034r\0322\030^[a-zA-Z_][a-zA-Z0-9_]*$'
  _LISTREQUEST._serialized_start=149
  _LISTREQUEST._serialized_end=162
  _LISTRESPONSE._serialized_start=164
  _LISTRESPONSE._serialized_end=253
  _DESCRIBEREQUEST._serialized_start=255
  _DESCRIBEREQUEST._serialized_end=341
  _DESCRIBERESPONSE._serialized_start=343
  _DESCRIBERESPONSE._serialized_end=416
  _GETVALUESREQUEST._serialized_start=419
  _GETVALUESREQUEST._serialized_end=559
  _GETVALUESRESPONSE._serialized_start=562
  _GETVALUESRESPONSE._serialized_end=772
  _GETVALUESRESPONSE_VALUESENTRY._serialized_start=701
  _GETVALUESRESPONSE_VALUESENTRY._serialized_end=772
  _CALLVALUEREQUEST._serialized_start=775
  _CALLVALUEREQUEST._serialized_end=1158
  _CALLVALUEREQUEST_KWARGSENTRY._serialized_start=1087
  _CALLVALUEREQUEST_KWARGSENTRY._serialized_end=1158
  _CALLVALUERESPONSE._serialized_start=1160
  _CALLVALUERESPONSE._serialized_end=1274
  _PLUGINSPROVIDER._serialized_start=1277
  _PLUGINSPROVIDER._serialized_end=1724
# @@protoc_insertion_point(module_scope)
