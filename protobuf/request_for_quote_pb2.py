# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: request_for_quote.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='request_for_quote.proto',
  package='protobuf',
  syntax='proto2',
  serialized_pb=_b('\n\x17request_for_quote.proto\x12\x08protobuf\x1a\x1fgoogle/protobuf/timestamp.proto\"\"\n\tClient_pb\x12\x15\n\rbusiness_name\x18\x01 \x02(\t\"j\n\nProduct_pb\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\r\n\x05price\x18\x02 \x02(\x02\x12\'\n\x08\x63\x61tegory\x18\x03 \x02(\x0b\x32\x15.protobuf.Category_pb\x12\x16\n\x0eproduct_number\x18\x04 \x01(\x05\"\x1b\n\x0b\x43\x61tegory_pb\x12\x0c\n\x04name\x18\x01 \x02(\t\"\xa2\x01\n\x06RFQ_pb\x12\x10\n\x08quantity\x18\x01 \x02(\x05\x12\'\n\naccount_id\x18\x02 \x02(\x0b\x32\x13.protobuf.Client_pb\x12,\n\x0eproduct_number\x18\x03 \x02(\x0b\x32\x14.protobuf.Product_pb\x12/\n\x10product_category\x18\x04 \x02(\x0b\x32\x15.protobuf.Category_pb\"\xa6\x01\n\x06RFP_pb\x12 \n\x06RFQ_id\x18\x01 \x02(\x0b\x32\x10.protobuf.RFQ_pb\x12\x12\n\nunit_price\x18\x02 \x02(\x02\x12\x30\n\x0c\x64\x61te_created\x18\x03 \x02(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x34\n\x10price_expiration\x18\x04 \x02(\x0b\x32\x1a.google.protobuf.Timestamp')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_CLIENT_PB = _descriptor.Descriptor(
  name='Client_pb',
  full_name='protobuf.Client_pb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='business_name', full_name='protobuf.Client_pb.business_name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=70,
  serialized_end=104,
)


_PRODUCT_PB = _descriptor.Descriptor(
  name='Product_pb',
  full_name='protobuf.Product_pb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='protobuf.Product_pb.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='price', full_name='protobuf.Product_pb.price', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='category', full_name='protobuf.Product_pb.category', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='product_number', full_name='protobuf.Product_pb.product_number', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=106,
  serialized_end=212,
)


_CATEGORY_PB = _descriptor.Descriptor(
  name='Category_pb',
  full_name='protobuf.Category_pb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='protobuf.Category_pb.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=214,
  serialized_end=241,
)


_RFQ_PB = _descriptor.Descriptor(
  name='RFQ_pb',
  full_name='protobuf.RFQ_pb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='quantity', full_name='protobuf.RFQ_pb.quantity', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='account_id', full_name='protobuf.RFQ_pb.account_id', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='product_number', full_name='protobuf.RFQ_pb.product_number', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='product_category', full_name='protobuf.RFQ_pb.product_category', index=3,
      number=4, type=11, cpp_type=10, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=244,
  serialized_end=406,
)


_RFP_PB = _descriptor.Descriptor(
  name='RFP_pb',
  full_name='protobuf.RFP_pb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='RFQ_id', full_name='protobuf.RFP_pb.RFQ_id', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unit_price', full_name='protobuf.RFP_pb.unit_price', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='date_created', full_name='protobuf.RFP_pb.date_created', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='price_expiration', full_name='protobuf.RFP_pb.price_expiration', index=3,
      number=4, type=11, cpp_type=10, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=409,
  serialized_end=575,
)

_PRODUCT_PB.fields_by_name['category'].message_type = _CATEGORY_PB
_RFQ_PB.fields_by_name['account_id'].message_type = _CLIENT_PB
_RFQ_PB.fields_by_name['product_number'].message_type = _PRODUCT_PB
_RFQ_PB.fields_by_name['product_category'].message_type = _CATEGORY_PB
_RFP_PB.fields_by_name['RFQ_id'].message_type = _RFQ_PB
_RFP_PB.fields_by_name['date_created'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_RFP_PB.fields_by_name['price_expiration'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['Client_pb'] = _CLIENT_PB
DESCRIPTOR.message_types_by_name['Product_pb'] = _PRODUCT_PB
DESCRIPTOR.message_types_by_name['Category_pb'] = _CATEGORY_PB
DESCRIPTOR.message_types_by_name['RFQ_pb'] = _RFQ_PB
DESCRIPTOR.message_types_by_name['RFP_pb'] = _RFP_PB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Client_pb = _reflection.GeneratedProtocolMessageType('Client_pb', (_message.Message,), dict(
  DESCRIPTOR = _CLIENT_PB,
  __module__ = 'request_for_quote_pb2'
  # @@protoc_insertion_point(class_scope:protobuf.Client_pb)
  ))
_sym_db.RegisterMessage(Client_pb)

Product_pb = _reflection.GeneratedProtocolMessageType('Product_pb', (_message.Message,), dict(
  DESCRIPTOR = _PRODUCT_PB,
  __module__ = 'request_for_quote_pb2'
  # @@protoc_insertion_point(class_scope:protobuf.Product_pb)
  ))
_sym_db.RegisterMessage(Product_pb)

Category_pb = _reflection.GeneratedProtocolMessageType('Category_pb', (_message.Message,), dict(
  DESCRIPTOR = _CATEGORY_PB,
  __module__ = 'request_for_quote_pb2'
  # @@protoc_insertion_point(class_scope:protobuf.Category_pb)
  ))
_sym_db.RegisterMessage(Category_pb)

RFQ_pb = _reflection.GeneratedProtocolMessageType('RFQ_pb', (_message.Message,), dict(
  DESCRIPTOR = _RFQ_PB,
  __module__ = 'request_for_quote_pb2'
  # @@protoc_insertion_point(class_scope:protobuf.RFQ_pb)
  ))
_sym_db.RegisterMessage(RFQ_pb)

RFP_pb = _reflection.GeneratedProtocolMessageType('RFP_pb', (_message.Message,), dict(
  DESCRIPTOR = _RFP_PB,
  __module__ = 'request_for_quote_pb2'
  # @@protoc_insertion_point(class_scope:protobuf.RFP_pb)
  ))
_sym_db.RegisterMessage(RFP_pb)


# @@protoc_insertion_point(module_scope)
