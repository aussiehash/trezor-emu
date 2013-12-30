# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: storage.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import types_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='storage.proto',
  package='',
  serialized_pb='\n\rstorage.proto\x1a\x0btypes.proto\"\xbd\x01\n\x07Storage\x12\x0f\n\x07version\x18\x01 \x02(\r\x12\x19\n\x04node\x18\x02 \x01(\x0b\x32\x0b.HDNodeType\x12\x16\n\x08mnemonic\x18\x03 \x01(\x0c\x42\x04\x88\xb5\x18\x01\x12\x1d\n\x15passphrase_protection\x18\x04 \x01(\x08\x12\x1b\n\x13pin_failed_attempts\x18\x05 \x01(\r\x12\x0b\n\x03pin\x18\x06 \x01(\x0c\x12\x10\n\x08language\x18\x07 \x01(\x0c\x12\x13\n\x05label\x18\x08 \x01(\x0c\x42\x04\x88\xb5\x18\x01\"W\n\x07Session\x12\x18\n\npassphrase\x18\x01 \x01(\x0c\x42\x04\x88\xb5\x18\x01\x12\x17\n\x04\x63oin\x18\x02 \x01(\x0b\x32\t.CoinType\x12\x19\n\x04node\x18\x03 \x01(\x0b\x32\x0b.HDNodeType')




_STORAGE = _descriptor.Descriptor(
  name='Storage',
  full_name='Storage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='Storage.version', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='node', full_name='Storage.node', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mnemonic', full_name='Storage.mnemonic', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\210\265\030\001')),
    _descriptor.FieldDescriptor(
      name='passphrase_protection', full_name='Storage.passphrase_protection', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pin_failed_attempts', full_name='Storage.pin_failed_attempts', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pin', full_name='Storage.pin', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='language', full_name='Storage.language', index=6,
      number=7, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='label', full_name='Storage.label', index=7,
      number=8, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\210\265\030\001')),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=31,
  serialized_end=220,
)


_SESSION = _descriptor.Descriptor(
  name='Session',
  full_name='Session',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='passphrase', full_name='Session.passphrase', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\210\265\030\001')),
    _descriptor.FieldDescriptor(
      name='coin', full_name='Session.coin', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='node', full_name='Session.node', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=222,
  serialized_end=309,
)

_STORAGE.fields_by_name['node'].message_type = types_pb2._HDNODETYPE
_SESSION.fields_by_name['coin'].message_type = types_pb2._COINTYPE
_SESSION.fields_by_name['node'].message_type = types_pb2._HDNODETYPE
DESCRIPTOR.message_types_by_name['Storage'] = _STORAGE
DESCRIPTOR.message_types_by_name['Session'] = _SESSION

class Storage(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _STORAGE

  # @@protoc_insertion_point(class_scope:Storage)

class Session(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SESSION

  # @@protoc_insertion_point(class_scope:Session)


_STORAGE.fields_by_name['mnemonic'].has_options = True
_STORAGE.fields_by_name['mnemonic']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\210\265\030\001')
_STORAGE.fields_by_name['label'].has_options = True
_STORAGE.fields_by_name['label']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\210\265\030\001')
_SESSION.fields_by_name['passphrase'].has_options = True
_SESSION.fields_by_name['passphrase']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\210\265\030\001')
# @@protoc_insertion_point(module_scope)
