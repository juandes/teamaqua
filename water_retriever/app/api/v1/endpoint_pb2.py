# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: endpoint.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='endpoint.proto',
  package='api',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0e\x65ndpoint.proto\x12\x03\x61pi\x1a\x1fgoogle/protobuf/timestamp.proto\".\n\x11LogSplashResponse\x12\n\n\x02ok\x18\x01 \x01(\x08\x12\r\n\x05\x65rror\x18\x02 \x01(\t\"@\n\x06Splash\x12&\n\x02ts\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x05\x32>\n\nDrinkWater\x12\x30\n\tLogSplash\x12\x0b.api.Splash\x1a\x16.api.LogSplashResponseb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_LOGSPLASHRESPONSE = _descriptor.Descriptor(
  name='LogSplashResponse',
  full_name='api.LogSplashResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ok', full_name='api.LogSplashResponse.ok', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='api.LogSplashResponse.error', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=56,
  serialized_end=102,
)


_SPLASH = _descriptor.Descriptor(
  name='Splash',
  full_name='api.Splash',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ts', full_name='api.Splash.ts', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='api.Splash.amount', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=104,
  serialized_end=168,
)

_SPLASH.fields_by_name['ts'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['LogSplashResponse'] = _LOGSPLASHRESPONSE
DESCRIPTOR.message_types_by_name['Splash'] = _SPLASH
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LogSplashResponse = _reflection.GeneratedProtocolMessageType('LogSplashResponse', (_message.Message,), {
  'DESCRIPTOR' : _LOGSPLASHRESPONSE,
  '__module__' : 'endpoint_pb2'
  # @@protoc_insertion_point(class_scope:api.LogSplashResponse)
  })
_sym_db.RegisterMessage(LogSplashResponse)

Splash = _reflection.GeneratedProtocolMessageType('Splash', (_message.Message,), {
  'DESCRIPTOR' : _SPLASH,
  '__module__' : 'endpoint_pb2'
  # @@protoc_insertion_point(class_scope:api.Splash)
  })
_sym_db.RegisterMessage(Splash)



_DRINKWATER = _descriptor.ServiceDescriptor(
  name='DrinkWater',
  full_name='api.DrinkWater',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=170,
  serialized_end=232,
  methods=[
  _descriptor.MethodDescriptor(
    name='LogSplash',
    full_name='api.DrinkWater.LogSplash',
    index=0,
    containing_service=None,
    input_type=_SPLASH,
    output_type=_LOGSPLASHRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_DRINKWATER)

DESCRIPTOR.services_by_name['DrinkWater'] = _DRINKWATER

# @@protoc_insertion_point(module_scope)
