# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: values/values.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13values/values.proto\x12\x11\x61utokitteh.values\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17validate/validate.proto\"\x06\n\x04None\"\x13\n\x06String\x12\t\n\x01v\x18\x01 \x01(\t\"\x14\n\x07Integer\x12\t\n\x01v\x18\x01 \x01(\x03\"\x12\n\x05\x46loat\x12\t\n\x01v\x18\x01 \x01(\x02\"\x14\n\x07\x42oolean\x12\t\n\x01v\x18\x01 \x01(\x08\";\n\x04List\x12\x33\n\x02vs\x18\x01 \x03(\x0b\x32\x18.autokitteh.values.ValueB\r\xfa\x42\n\x92\x01\x07\"\x05\x8a\x01\x02\x10\x01\":\n\x03Set\x12\x33\n\x02vs\x18\x01 \x03(\x0b\x32\x18.autokitteh.values.ValueB\r\xfa\x42\n\x92\x01\x07\"\x05\x8a\x01\x02\x10\x01\"h\n\x08\x44ictItem\x12-\n\x01k\x18\x01 \x01(\x0b\x32\x18.autokitteh.values.ValueB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\x12-\n\x01v\x18\x02 \x01(\x0b\x32\x18.autokitteh.values.ValueB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\"A\n\x04\x44ict\x12\x39\n\x05items\x18\x01 \x03(\x0b\x32\x1b.autokitteh.values.DictItemB\r\xfa\x42\n\x92\x01\x07\"\x05\x8a\x01\x02\x10\x01\"\x12\n\x05\x42ytes\x12\t\n\x01v\x18\x01 \x01(\x0c\"7\n\x04Time\x12/\n\x01t\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\xfa\x42\x05\xb2\x01\x02\x08\x01\":\n\x08\x44uration\x12.\n\x01\x64\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationB\x08\xfa\x42\x05\xb2\x01\x02\x08\x01\"\x91\x01\n\x04\x43\x61ll\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06issuer\x18\x03 \x01(\t\x12\x31\n\x05\x66lags\x18\x04 \x03(\x0b\x32\".autokitteh.values.Call.FlagsEntry\x1a,\n\nFlagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x08:\x02\x38\x01\"\xe2\x01\n\x06Struct\x12\x30\n\x04\x63tor\x18\x01 \x01(\x0b\x32\x18.autokitteh.values.ValueB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\x12]\n\x06\x66ields\x18\x02 \x03(\x0b\x32%.autokitteh.values.Struct.FieldsEntryB&\xfa\x42#\x9a\x01 \x18\x01\"\x1cr\x1a\x32\x18^[a-zA-Z_][a-zA-Z0-9_]*$\x1aG\n\x0b\x46ieldsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\'\n\x05value\x18\x02 \x01(\x0b\x32\x18.autokitteh.values.Value:\x02\x38\x01\"\xcd\x01\n\x06Module\x12\x18\n\x04name\x18\x01 \x01(\tB\n\xfa\x42\x07r\x05\x32\x03^.+\x12_\n\x07members\x18\x02 \x03(\x0b\x32&.autokitteh.values.Module.MembersEntryB&\xfa\x42#\x9a\x01 \x18\x01\"\x1cr\x1a\x32\x18^[a-zA-Z_][a-zA-Z0-9_]*$\x1aH\n\x0cMembersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\'\n\x05value\x18\x02 \x01(\x0b\x32\x18.autokitteh.values.Value:\x02\x38\x01\"\x16\n\x06Symbol\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x91\x01\n\x11\x46unctionSignature\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03\x64oc\x18\x02 \x01(\t\x12\x0e\n\x06n_args\x18\x03 \x01(\r\x12\x14\n\x0cn_kwonlyargs\x18\x04 \x01(\r\x12\x12\n\nargs_names\x18\x05 \x03(\t\x12\x13\n\x0bhas_varargs\x18\x06 \x01(\x08\x12\x12\n\nhas_kwargs\x18\x07 \x01(\x08\"\x9a\x01\n\x08\x46unction\x12%\n\x07\x66unc_id\x18\x01 \x01(\tB\x14\xfa\x42\x11r\x0f\x32\r^F[0-9a-f.]+$\x12%\n\x04lang\x18\x02 \x01(\tB\x17\xfa\x42\x14r\x12\x32\x10^[0-9a-zA-Z_-]+$\x12\r\n\x05scope\x18\x03 \x01(\t\x12\x31\n\x03sig\x18\x04 \x01(\x0b\x32$.autokitteh.values.FunctionSignature\"\xcd\x05\n\x05Value\x12\'\n\x04none\x18\x01 \x01(\x0b\x32\x17.autokitteh.values.NoneH\x00\x12+\n\x06string\x18\x02 \x01(\x0b\x32\x19.autokitteh.values.StringH\x00\x12-\n\x07integer\x18\x03 \x01(\x0b\x32\x1a.autokitteh.values.IntegerH\x00\x12-\n\x07\x62oolean\x18\x04 \x01(\x0b\x32\x1a.autokitteh.values.BooleanH\x00\x12\'\n\x04list\x18\x05 \x01(\x0b\x32\x17.autokitteh.values.ListH\x00\x12\'\n\x04\x64ict\x18\x06 \x01(\x0b\x32\x17.autokitteh.values.DictH\x00\x12)\n\x05\x66loat\x18\x07 \x01(\x0b\x32\x18.autokitteh.values.FloatH\x00\x12%\n\x03set\x18\x08 \x01(\x0b\x32\x16.autokitteh.values.SetH\x00\x12)\n\x05\x62ytes\x18\t \x01(\x0b\x32\x18.autokitteh.values.BytesH\x00\x12\'\n\x04time\x18\n \x01(\x0b\x32\x17.autokitteh.values.TimeH\x00\x12/\n\x08\x64uration\x18\x0b \x01(\x0b\x32\x1b.autokitteh.values.DurationH\x00\x12+\n\x06symbol\x18\x0c \x01(\x0b\x32\x19.autokitteh.values.SymbolH\x00\x12+\n\x06struct\x18\x32 \x01(\x0b\x32\x19.autokitteh.values.StructH\x00\x12+\n\x06module\x18\x33 \x01(\x0b\x32\x19.autokitteh.values.ModuleH\x00\x12/\n\x08\x66unction\x18\x34 \x01(\x0b\x32\x1b.autokitteh.values.FunctionH\x00\x12\'\n\x04\x63\x61ll\x18\x64 \x01(\x0b\x32\x17.autokitteh.values.CallH\x00\x42\x06\n\x04typeB!Z\x1fgo.autokitteh.dev/idl/go/valuesb\x06proto3')



_NONE = DESCRIPTOR.message_types_by_name['None']
_STRING = DESCRIPTOR.message_types_by_name['String']
_INTEGER = DESCRIPTOR.message_types_by_name['Integer']
_FLOAT = DESCRIPTOR.message_types_by_name['Float']
_BOOLEAN = DESCRIPTOR.message_types_by_name['Boolean']
_LIST = DESCRIPTOR.message_types_by_name['List']
_SET = DESCRIPTOR.message_types_by_name['Set']
_DICTITEM = DESCRIPTOR.message_types_by_name['DictItem']
_DICT = DESCRIPTOR.message_types_by_name['Dict']
_BYTES = DESCRIPTOR.message_types_by_name['Bytes']
_TIME = DESCRIPTOR.message_types_by_name['Time']
_DURATION = DESCRIPTOR.message_types_by_name['Duration']
_CALL = DESCRIPTOR.message_types_by_name['Call']
_CALL_FLAGSENTRY = _CALL.nested_types_by_name['FlagsEntry']
_STRUCT = DESCRIPTOR.message_types_by_name['Struct']
_STRUCT_FIELDSENTRY = _STRUCT.nested_types_by_name['FieldsEntry']
_MODULE = DESCRIPTOR.message_types_by_name['Module']
_MODULE_MEMBERSENTRY = _MODULE.nested_types_by_name['MembersEntry']
_SYMBOL = DESCRIPTOR.message_types_by_name['Symbol']
_FUNCTIONSIGNATURE = DESCRIPTOR.message_types_by_name['FunctionSignature']
_FUNCTION = DESCRIPTOR.message_types_by_name['Function']
_VALUE = DESCRIPTOR.message_types_by_name['Value']
globals()['None'] = _reflection.GeneratedProtocolMessageType('None', (_message.Message,), {
  'DESCRIPTOR' : _NONE,
  '__module__' : 'values.values_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.values.None)
  })
_sym_db.RegisterMessage(globals()['None'])

String = _reflection.GeneratedProtocolMessageType('String', (_message.Message,), {
  'DESCRIPTOR' : _STRING,
  '__module__' : 'values.values_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.values.String)
  })
_sym_db.RegisterMessage(String)

Integer = _reflection.GeneratedProtocolMessageType('Integer', (_message.Message,), {
  'DESCRIPTOR' : _INTEGER,
  '__module__' : 'values.values_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.values.Integer)
  })
_sym_db.RegisterMessage(Integer)

Float = _reflection.GeneratedProtocolMessageType('Float', (_message.Message,), {
  'DESCRIPTOR' : _FLOAT,
  '__module__' : 'values.values_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.values.Float)
  })
_sym_db.RegisterMessage(Float)

Boolean = _reflection.GeneratedProtocolMessageType('Boolean', (_message.Message,), {
  'DESCRIPTOR' : _BOOLEAN,
  '__module__' : 'values.values_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.values.Boolean)
  })
_sym_db.RegisterMessage(Boolean)

List = _reflection.GeneratedProtocolMessageType('List', (_message.Message,), {
  'DESCRIPTOR' : _LIST,
  '__module__' : 'values.values_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.values.List)
  })
_sym_db.RegisterMessage(List)

Set = _reflection.GeneratedProtocolMessageType('Set', (_message.Message,), {
  'DESCRIPTOR' : _SET,
  '__module__' : 'values.values_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.values.Set)
  })
_sym_db.RegisterMessage(Set)

DictItem = _reflection.GeneratedProtocolMessageType('DictItem', (_message.Message,), {
  'DESCRIPTOR' : _DICTITEM,
  '__module__' : 'values.values_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.values.DictItem)
  })
_sym_db.RegisterMessage(DictItem)

Dict = _reflection.GeneratedProtocolMessageType('Dict', (_message.Message,), {
  'DESCRIPTOR' : _DICT,
  '__module__' : 'values.values_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.values.Dict)
  })
_sym_db.RegisterMessage(Dict)

Bytes = _reflection.GeneratedProtocolMessageType('Bytes', (_message.Message,), {
  'DESCRIPTOR' : _BYTES,
  '__module__' : 'values.values_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.values.Bytes)
  })
_sym_db.RegisterMessage(Bytes)

Time = _reflection.GeneratedProtocolMessageType('Time', (_message.Message,), {
  'DESCRIPTOR' : _TIME,
  '__module__' : 'values.values_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.values.Time)
  })
_sym_db.RegisterMessage(Time)

Duration = _reflection.GeneratedProtocolMessageType('Duration', (_message.Message,), {
  'DESCRIPTOR' : _DURATION,
  '__module__' : 'values.values_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.values.Duration)
  })
_sym_db.RegisterMessage(Duration)

Call = _reflection.GeneratedProtocolMessageType('Call', (_message.Message,), {

  'FlagsEntry' : _reflection.GeneratedProtocolMessageType('FlagsEntry', (_message.Message,), {
    'DESCRIPTOR' : _CALL_FLAGSENTRY,
    '__module__' : 'values.values_pb2'
    # @@protoc_insertion_point(class_scope:autokitteh.values.Call.FlagsEntry)
    })
  ,
  'DESCRIPTOR' : _CALL,
  '__module__' : 'values.values_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.values.Call)
  })
_sym_db.RegisterMessage(Call)
_sym_db.RegisterMessage(Call.FlagsEntry)

Struct = _reflection.GeneratedProtocolMessageType('Struct', (_message.Message,), {

  'FieldsEntry' : _reflection.GeneratedProtocolMessageType('FieldsEntry', (_message.Message,), {
    'DESCRIPTOR' : _STRUCT_FIELDSENTRY,
    '__module__' : 'values.values_pb2'
    # @@protoc_insertion_point(class_scope:autokitteh.values.Struct.FieldsEntry)
    })
  ,
  'DESCRIPTOR' : _STRUCT,
  '__module__' : 'values.values_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.values.Struct)
  })
_sym_db.RegisterMessage(Struct)
_sym_db.RegisterMessage(Struct.FieldsEntry)

Module = _reflection.GeneratedProtocolMessageType('Module', (_message.Message,), {

  'MembersEntry' : _reflection.GeneratedProtocolMessageType('MembersEntry', (_message.Message,), {
    'DESCRIPTOR' : _MODULE_MEMBERSENTRY,
    '__module__' : 'values.values_pb2'
    # @@protoc_insertion_point(class_scope:autokitteh.values.Module.MembersEntry)
    })
  ,
  'DESCRIPTOR' : _MODULE,
  '__module__' : 'values.values_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.values.Module)
  })
_sym_db.RegisterMessage(Module)
_sym_db.RegisterMessage(Module.MembersEntry)

Symbol = _reflection.GeneratedProtocolMessageType('Symbol', (_message.Message,), {
  'DESCRIPTOR' : _SYMBOL,
  '__module__' : 'values.values_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.values.Symbol)
  })
_sym_db.RegisterMessage(Symbol)

FunctionSignature = _reflection.GeneratedProtocolMessageType('FunctionSignature', (_message.Message,), {
  'DESCRIPTOR' : _FUNCTIONSIGNATURE,
  '__module__' : 'values.values_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.values.FunctionSignature)
  })
_sym_db.RegisterMessage(FunctionSignature)

Function = _reflection.GeneratedProtocolMessageType('Function', (_message.Message,), {
  'DESCRIPTOR' : _FUNCTION,
  '__module__' : 'values.values_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.values.Function)
  })
_sym_db.RegisterMessage(Function)

Value = _reflection.GeneratedProtocolMessageType('Value', (_message.Message,), {
  'DESCRIPTOR' : _VALUE,
  '__module__' : 'values.values_pb2'
  # @@protoc_insertion_point(class_scope:autokitteh.values.Value)
  })
_sym_db.RegisterMessage(Value)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\037go.autokitteh.dev/idl/go/values'
  _LIST.fields_by_name['vs']._options = None
  _LIST.fields_by_name['vs']._serialized_options = b'\372B\n\222\001\007\"\005\212\001\002\020\001'
  _SET.fields_by_name['vs']._options = None
  _SET.fields_by_name['vs']._serialized_options = b'\372B\n\222\001\007\"\005\212\001\002\020\001'
  _DICTITEM.fields_by_name['k']._options = None
  _DICTITEM.fields_by_name['k']._serialized_options = b'\372B\005\212\001\002\020\001'
  _DICTITEM.fields_by_name['v']._options = None
  _DICTITEM.fields_by_name['v']._serialized_options = b'\372B\005\212\001\002\020\001'
  _DICT.fields_by_name['items']._options = None
  _DICT.fields_by_name['items']._serialized_options = b'\372B\n\222\001\007\"\005\212\001\002\020\001'
  _TIME.fields_by_name['t']._options = None
  _TIME.fields_by_name['t']._serialized_options = b'\372B\005\262\001\002\010\001'
  _DURATION.fields_by_name['d']._options = None
  _DURATION.fields_by_name['d']._serialized_options = b'\372B\005\262\001\002\010\001'
  _CALL_FLAGSENTRY._options = None
  _CALL_FLAGSENTRY._serialized_options = b'8\001'
  _STRUCT_FIELDSENTRY._options = None
  _STRUCT_FIELDSENTRY._serialized_options = b'8\001'
  _STRUCT.fields_by_name['ctor']._options = None
  _STRUCT.fields_by_name['ctor']._serialized_options = b'\372B\005\212\001\002\020\001'
  _STRUCT.fields_by_name['fields']._options = None
  _STRUCT.fields_by_name['fields']._serialized_options = b'\372B#\232\001 \030\001\"\034r\0322\030^[a-zA-Z_][a-zA-Z0-9_]*$'
  _MODULE_MEMBERSENTRY._options = None
  _MODULE_MEMBERSENTRY._serialized_options = b'8\001'
  _MODULE.fields_by_name['name']._options = None
  _MODULE.fields_by_name['name']._serialized_options = b'\372B\007r\0052\003^.+'
  _MODULE.fields_by_name['members']._options = None
  _MODULE.fields_by_name['members']._serialized_options = b'\372B#\232\001 \030\001\"\034r\0322\030^[a-zA-Z_][a-zA-Z0-9_]*$'
  _FUNCTION.fields_by_name['func_id']._options = None
  _FUNCTION.fields_by_name['func_id']._serialized_options = b'\372B\021r\0172\r^F[0-9a-f.]+$'
  _FUNCTION.fields_by_name['lang']._options = None
  _FUNCTION.fields_by_name['lang']._serialized_options = b'\372B\024r\0222\020^[0-9a-zA-Z_-]+$'
  _NONE._serialized_start=132
  _NONE._serialized_end=138
  _STRING._serialized_start=140
  _STRING._serialized_end=159
  _INTEGER._serialized_start=161
  _INTEGER._serialized_end=181
  _FLOAT._serialized_start=183
  _FLOAT._serialized_end=201
  _BOOLEAN._serialized_start=203
  _BOOLEAN._serialized_end=223
  _LIST._serialized_start=225
  _LIST._serialized_end=284
  _SET._serialized_start=286
  _SET._serialized_end=344
  _DICTITEM._serialized_start=346
  _DICTITEM._serialized_end=450
  _DICT._serialized_start=452
  _DICT._serialized_end=517
  _BYTES._serialized_start=519
  _BYTES._serialized_end=537
  _TIME._serialized_start=539
  _TIME._serialized_end=594
  _DURATION._serialized_start=596
  _DURATION._serialized_end=654
  _CALL._serialized_start=657
  _CALL._serialized_end=802
  _CALL_FLAGSENTRY._serialized_start=758
  _CALL_FLAGSENTRY._serialized_end=802
  _STRUCT._serialized_start=805
  _STRUCT._serialized_end=1031
  _STRUCT_FIELDSENTRY._serialized_start=960
  _STRUCT_FIELDSENTRY._serialized_end=1031
  _MODULE._serialized_start=1034
  _MODULE._serialized_end=1239
  _MODULE_MEMBERSENTRY._serialized_start=1167
  _MODULE_MEMBERSENTRY._serialized_end=1239
  _SYMBOL._serialized_start=1241
  _SYMBOL._serialized_end=1263
  _FUNCTIONSIGNATURE._serialized_start=1266
  _FUNCTIONSIGNATURE._serialized_end=1411
  _FUNCTION._serialized_start=1414
  _FUNCTION._serialized_end=1568
  _VALUE._serialized_start=1571
  _VALUE._serialized_end=2288
# @@protoc_insertion_point(module_scope)
