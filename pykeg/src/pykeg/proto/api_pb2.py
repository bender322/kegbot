# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import models_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='api.proto',
  package='',
  serialized_pb='\n\tapi.proto\x1a\x0cmodels.proto\"3\n\x06Paging\x12\r\n\x05total\x18\x01 \x01(\r\x12\r\n\x05limit\x18\x02 \x01(\r\x12\x0b\n\x03pos\x18\x03 \x01(\r\";\n\x08\x44rinkSet\x12\x16\n\x06\x64rinks\x18\x01 \x03(\x0b\x32\x06.Drink\x12\x17\n\x06paging\x18\x02 \x01(\x0b\x32\x07.Paging\"5\n\x06KegSet\x12\x12\n\x04kegs\x18\x01 \x03(\x0b\x32\x04.Keg\x12\x17\n\x06paging\x18\x02 \x01(\x0b\x32\x07.Paging\"A\n\nSessionSet\x12\x1a\n\x08sessions\x18\x01 \x03(\x0b\x32\x08.Session\x12\x17\n\x06paging\x18\x02 \x01(\x0b\x32\x07.Paging\"G\n\x0eSystemEventSet\x12\x1c\n\x06\x65vents\x18\x01 \x03(\x0b\x32\x0c.SystemEvent\x12\x17\n\x06paging\x18\x02 \x01(\x0b\x32\x07.Paging\"S\n\x14SystemEventDetailSet\x12\"\n\x06\x65vents\x18\x01 \x03(\x0b\x32\x12.SystemEventDetail\x12\x17\n\x06paging\x18\x02 \x01(\x0b\x32\x07.Paging\"O\n\x12SystemEventHtmlSet\x12 \n\x06\x65vents\x18\x01 \x03(\x0b\x32\x10.SystemEventHtml\x12\x17\n\x06paging\x18\x02 \x01(\x0b\x32\x07.Paging\"E\n\rSoundEventSet\x12\x1b\n\x06\x65vents\x18\x01 \x03(\x0b\x32\x0b.SoundEvent\x12\x17\n\x06paging\x18\x02 \x01(\x0b\x32\x07.Paging\"A\n\x0cTapDetailSet\x12\x18\n\x04taps\x18\x01 \x03(\x0b\x32\n.TapDetail\x12\x17\n\x06paging\x18\x02 \x01(\x0b\x32\x07.Paging\"O\n\x12\x44rinkDetailHtmlSet\x12 \n\x06\x64rinks\x18\x01 \x03(\x0b\x32\x10.DrinkDetailHtml\x12\x17\n\x06paging\x18\x02 \x01(\x0b\x32\x07.Paging\"J\n\x0fThermoSensorSet\x12\x1e\n\x07sensors\x18\x01 \x03(\x0b\x32\r.ThermoSensor\x12\x17\n\x06paging\x18\x02 \x01(\x0b\x32\x07.Paging\"A\n\x0cThermoLogSet\x12\x18\n\x04logs\x18\x01 \x03(\x0b\x32\n.ThermoLog\x12\x17\n\x06paging\x18\x02 \x01(\x0b\x32\x07.Paging\"k\n\tTapDetail\x12\x14\n\x03tap\x18\x01 \x02(\x0b\x32\x07.KegTap\x12\x11\n\x03keg\x18\x02 \x01(\x0b\x32\x04.Keg\x12\x1c\n\tbeer_type\x18\x03 \x01(\x0b\x32\t.BeerType\x12\x17\n\x06\x62rewer\x18\x04 \x01(\x0b\x32\x07.Brewer\"g\n\x0b\x44rinkDetail\x12\x15\n\x05\x64rink\x18\x01 \x02(\x0b\x32\x06.Drink\x12\x13\n\x04user\x18\x02 \x01(\x0b\x32\x05.User\x12\x11\n\x03keg\x18\x03 \x01(\x0b\x32\x04.Keg\x12\x19\n\x07session\x18\x04 \x01(\x0b\x32\x08.Session\"M\n\rSessionDetail\x12\x19\n\x07session\x18\x01 \x02(\x0b\x32\x08.Session\x12\r\n\x05stats\x18\x02 \x01(\t\x12\x12\n\x04kegs\x18\x03 \x03(\x0b\x32\x04.Keg\"\x83\x01\n\tKegDetail\x12\x11\n\x03keg\x18\x01 \x02(\x0b\x32\x04.Keg\x12\x17\n\x04type\x18\x02 \x01(\x0b\x32\t.BeerType\x12\x16\n\x04size\x18\x03 \x01(\x0b\x32\x08.KegSize\x12\x16\n\x06\x64rinks\x18\x04 \x03(\x0b\x32\x06.Drink\x12\x1a\n\x08sessions\x18\x05 \x03(\x0b\x32\x08.Session\"!\n\nUserDetail\x12\x13\n\x04user\x18\x01 \x02(\x0b\x32\x05.User\"G\n\x11SystemEventDetail\x12\x1b\n\x05\x65vent\x18\x01 \x02(\x0b\x32\x0c.SystemEvent\x12\x15\n\x05image\x18\x02 \x01(\x0b\x32\x06.Image\"+\n\x0fSystemEventHtml\x12\n\n\x02id\x18\x01 \x02(\t\x12\x0c\n\x04html\x18\x02 \x01(\t\"Y\n\x12ThermoSensorDetail\x12\x1d\n\x06sensor\x18\x01 \x02(\x0b\x32\r.ThermoSensor\x12\x11\n\tlast_temp\x18\x02 \x01(\x02\x12\x11\n\tlast_time\x18\x03 \x01(\t\"/\n\x0f\x44rinkDetailHtml\x12\n\n\x02id\x18\x01 \x02(\t\x12\x10\n\x08\x62ox_html\x18\x02 \x02(\t2\x0b\n\tKegwebApiB\x12\n\x10org.kegbot.proto')




_PAGING = descriptor.Descriptor(
  name='Paging',
  full_name='Paging',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='total', full_name='Paging.total', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='limit', full_name='Paging.limit', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='pos', full_name='Paging.pos', index=2,
      number=3, type=13, cpp_type=3, label=1,
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
  extension_ranges=[],
  serialized_start=27,
  serialized_end=78,
)


_DRINKSET = descriptor.Descriptor(
  name='DrinkSet',
  full_name='DrinkSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='drinks', full_name='DrinkSet.drinks', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='paging', full_name='DrinkSet.paging', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=80,
  serialized_end=139,
)


_KEGSET = descriptor.Descriptor(
  name='KegSet',
  full_name='KegSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='kegs', full_name='KegSet.kegs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='paging', full_name='KegSet.paging', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=141,
  serialized_end=194,
)


_SESSIONSET = descriptor.Descriptor(
  name='SessionSet',
  full_name='SessionSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='sessions', full_name='SessionSet.sessions', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='paging', full_name='SessionSet.paging', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=196,
  serialized_end=261,
)


_SYSTEMEVENTSET = descriptor.Descriptor(
  name='SystemEventSet',
  full_name='SystemEventSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='events', full_name='SystemEventSet.events', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='paging', full_name='SystemEventSet.paging', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=263,
  serialized_end=334,
)


_SYSTEMEVENTDETAILSET = descriptor.Descriptor(
  name='SystemEventDetailSet',
  full_name='SystemEventDetailSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='events', full_name='SystemEventDetailSet.events', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='paging', full_name='SystemEventDetailSet.paging', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=336,
  serialized_end=419,
)


_SYSTEMEVENTHTMLSET = descriptor.Descriptor(
  name='SystemEventHtmlSet',
  full_name='SystemEventHtmlSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='events', full_name='SystemEventHtmlSet.events', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='paging', full_name='SystemEventHtmlSet.paging', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=421,
  serialized_end=500,
)


_SOUNDEVENTSET = descriptor.Descriptor(
  name='SoundEventSet',
  full_name='SoundEventSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='events', full_name='SoundEventSet.events', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='paging', full_name='SoundEventSet.paging', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=502,
  serialized_end=571,
)


_TAPDETAILSET = descriptor.Descriptor(
  name='TapDetailSet',
  full_name='TapDetailSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='taps', full_name='TapDetailSet.taps', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='paging', full_name='TapDetailSet.paging', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=573,
  serialized_end=638,
)


_DRINKDETAILHTMLSET = descriptor.Descriptor(
  name='DrinkDetailHtmlSet',
  full_name='DrinkDetailHtmlSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='drinks', full_name='DrinkDetailHtmlSet.drinks', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='paging', full_name='DrinkDetailHtmlSet.paging', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=640,
  serialized_end=719,
)


_THERMOSENSORSET = descriptor.Descriptor(
  name='ThermoSensorSet',
  full_name='ThermoSensorSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='sensors', full_name='ThermoSensorSet.sensors', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='paging', full_name='ThermoSensorSet.paging', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=721,
  serialized_end=795,
)


_THERMOLOGSET = descriptor.Descriptor(
  name='ThermoLogSet',
  full_name='ThermoLogSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='logs', full_name='ThermoLogSet.logs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='paging', full_name='ThermoLogSet.paging', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=797,
  serialized_end=862,
)


_TAPDETAIL = descriptor.Descriptor(
  name='TapDetail',
  full_name='TapDetail',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='tap', full_name='TapDetail.tap', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='keg', full_name='TapDetail.keg', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='beer_type', full_name='TapDetail.beer_type', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='brewer', full_name='TapDetail.brewer', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=864,
  serialized_end=971,
)


_DRINKDETAIL = descriptor.Descriptor(
  name='DrinkDetail',
  full_name='DrinkDetail',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='drink', full_name='DrinkDetail.drink', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='user', full_name='DrinkDetail.user', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='keg', full_name='DrinkDetail.keg', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='session', full_name='DrinkDetail.session', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=973,
  serialized_end=1076,
)


_SESSIONDETAIL = descriptor.Descriptor(
  name='SessionDetail',
  full_name='SessionDetail',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='session', full_name='SessionDetail.session', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='stats', full_name='SessionDetail.stats', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='kegs', full_name='SessionDetail.kegs', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1078,
  serialized_end=1155,
)


_KEGDETAIL = descriptor.Descriptor(
  name='KegDetail',
  full_name='KegDetail',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='keg', full_name='KegDetail.keg', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='type', full_name='KegDetail.type', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='size', full_name='KegDetail.size', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='drinks', full_name='KegDetail.drinks', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sessions', full_name='KegDetail.sessions', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1158,
  serialized_end=1289,
)


_USERDETAIL = descriptor.Descriptor(
  name='UserDetail',
  full_name='UserDetail',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='user', full_name='UserDetail.user', index=0,
      number=1, type=11, cpp_type=10, label=2,
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
  serialized_start=1291,
  serialized_end=1324,
)


_SYSTEMEVENTDETAIL = descriptor.Descriptor(
  name='SystemEventDetail',
  full_name='SystemEventDetail',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='event', full_name='SystemEventDetail.event', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='image', full_name='SystemEventDetail.image', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=1326,
  serialized_end=1397,
)


_SYSTEMEVENTHTML = descriptor.Descriptor(
  name='SystemEventHtml',
  full_name='SystemEventHtml',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='SystemEventHtml.id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='html', full_name='SystemEventHtml.html', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  serialized_start=1399,
  serialized_end=1442,
)


_THERMOSENSORDETAIL = descriptor.Descriptor(
  name='ThermoSensorDetail',
  full_name='ThermoSensorDetail',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='sensor', full_name='ThermoSensorDetail.sensor', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='last_temp', full_name='ThermoSensorDetail.last_temp', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='last_time', full_name='ThermoSensorDetail.last_time', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  serialized_start=1444,
  serialized_end=1533,
)


_DRINKDETAILHTML = descriptor.Descriptor(
  name='DrinkDetailHtml',
  full_name='DrinkDetailHtml',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='DrinkDetailHtml.id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='box_html', full_name='DrinkDetailHtml.box_html', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  serialized_start=1535,
  serialized_end=1582,
)

_DRINKSET.fields_by_name['drinks'].message_type = models_pb2._DRINK
_DRINKSET.fields_by_name['paging'].message_type = _PAGING
_KEGSET.fields_by_name['kegs'].message_type = models_pb2._KEG
_KEGSET.fields_by_name['paging'].message_type = _PAGING
_SESSIONSET.fields_by_name['sessions'].message_type = models_pb2._SESSION
_SESSIONSET.fields_by_name['paging'].message_type = _PAGING
_SYSTEMEVENTSET.fields_by_name['events'].message_type = models_pb2._SYSTEMEVENT
_SYSTEMEVENTSET.fields_by_name['paging'].message_type = _PAGING
_SYSTEMEVENTDETAILSET.fields_by_name['events'].message_type = _SYSTEMEVENTDETAIL
_SYSTEMEVENTDETAILSET.fields_by_name['paging'].message_type = _PAGING
_SYSTEMEVENTHTMLSET.fields_by_name['events'].message_type = _SYSTEMEVENTHTML
_SYSTEMEVENTHTMLSET.fields_by_name['paging'].message_type = _PAGING
_SOUNDEVENTSET.fields_by_name['events'].message_type = models_pb2._SOUNDEVENT
_SOUNDEVENTSET.fields_by_name['paging'].message_type = _PAGING
_TAPDETAILSET.fields_by_name['taps'].message_type = _TAPDETAIL
_TAPDETAILSET.fields_by_name['paging'].message_type = _PAGING
_DRINKDETAILHTMLSET.fields_by_name['drinks'].message_type = _DRINKDETAILHTML
_DRINKDETAILHTMLSET.fields_by_name['paging'].message_type = _PAGING
_THERMOSENSORSET.fields_by_name['sensors'].message_type = models_pb2._THERMOSENSOR
_THERMOSENSORSET.fields_by_name['paging'].message_type = _PAGING
_THERMOLOGSET.fields_by_name['logs'].message_type = models_pb2._THERMOLOG
_THERMOLOGSET.fields_by_name['paging'].message_type = _PAGING
_TAPDETAIL.fields_by_name['tap'].message_type = models_pb2._KEGTAP
_TAPDETAIL.fields_by_name['keg'].message_type = models_pb2._KEG
_TAPDETAIL.fields_by_name['beer_type'].message_type = models_pb2._BEERTYPE
_TAPDETAIL.fields_by_name['brewer'].message_type = models_pb2._BREWER
_DRINKDETAIL.fields_by_name['drink'].message_type = models_pb2._DRINK
_DRINKDETAIL.fields_by_name['user'].message_type = models_pb2._USER
_DRINKDETAIL.fields_by_name['keg'].message_type = models_pb2._KEG
_DRINKDETAIL.fields_by_name['session'].message_type = models_pb2._SESSION
_SESSIONDETAIL.fields_by_name['session'].message_type = models_pb2._SESSION
_SESSIONDETAIL.fields_by_name['kegs'].message_type = models_pb2._KEG
_KEGDETAIL.fields_by_name['keg'].message_type = models_pb2._KEG
_KEGDETAIL.fields_by_name['type'].message_type = models_pb2._BEERTYPE
_KEGDETAIL.fields_by_name['size'].message_type = models_pb2._KEGSIZE
_KEGDETAIL.fields_by_name['drinks'].message_type = models_pb2._DRINK
_KEGDETAIL.fields_by_name['sessions'].message_type = models_pb2._SESSION
_USERDETAIL.fields_by_name['user'].message_type = models_pb2._USER
_SYSTEMEVENTDETAIL.fields_by_name['event'].message_type = models_pb2._SYSTEMEVENT
_SYSTEMEVENTDETAIL.fields_by_name['image'].message_type = models_pb2._IMAGE
_THERMOSENSORDETAIL.fields_by_name['sensor'].message_type = models_pb2._THERMOSENSOR
DESCRIPTOR.message_types_by_name['Paging'] = _PAGING
DESCRIPTOR.message_types_by_name['DrinkSet'] = _DRINKSET
DESCRIPTOR.message_types_by_name['KegSet'] = _KEGSET
DESCRIPTOR.message_types_by_name['SessionSet'] = _SESSIONSET
DESCRIPTOR.message_types_by_name['SystemEventSet'] = _SYSTEMEVENTSET
DESCRIPTOR.message_types_by_name['SystemEventDetailSet'] = _SYSTEMEVENTDETAILSET
DESCRIPTOR.message_types_by_name['SystemEventHtmlSet'] = _SYSTEMEVENTHTMLSET
DESCRIPTOR.message_types_by_name['SoundEventSet'] = _SOUNDEVENTSET
DESCRIPTOR.message_types_by_name['TapDetailSet'] = _TAPDETAILSET
DESCRIPTOR.message_types_by_name['DrinkDetailHtmlSet'] = _DRINKDETAILHTMLSET
DESCRIPTOR.message_types_by_name['ThermoSensorSet'] = _THERMOSENSORSET
DESCRIPTOR.message_types_by_name['ThermoLogSet'] = _THERMOLOGSET
DESCRIPTOR.message_types_by_name['TapDetail'] = _TAPDETAIL
DESCRIPTOR.message_types_by_name['DrinkDetail'] = _DRINKDETAIL
DESCRIPTOR.message_types_by_name['SessionDetail'] = _SESSIONDETAIL
DESCRIPTOR.message_types_by_name['KegDetail'] = _KEGDETAIL
DESCRIPTOR.message_types_by_name['UserDetail'] = _USERDETAIL
DESCRIPTOR.message_types_by_name['SystemEventDetail'] = _SYSTEMEVENTDETAIL
DESCRIPTOR.message_types_by_name['SystemEventHtml'] = _SYSTEMEVENTHTML
DESCRIPTOR.message_types_by_name['ThermoSensorDetail'] = _THERMOSENSORDETAIL
DESCRIPTOR.message_types_by_name['DrinkDetailHtml'] = _DRINKDETAILHTML

class Paging(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PAGING
  
  # @@protoc_insertion_point(class_scope:Paging)

class DrinkSet(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DRINKSET
  
  # @@protoc_insertion_point(class_scope:DrinkSet)

class KegSet(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _KEGSET
  
  # @@protoc_insertion_point(class_scope:KegSet)

class SessionSet(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SESSIONSET
  
  # @@protoc_insertion_point(class_scope:SessionSet)

class SystemEventSet(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SYSTEMEVENTSET
  
  # @@protoc_insertion_point(class_scope:SystemEventSet)

class SystemEventDetailSet(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SYSTEMEVENTDETAILSET
  
  # @@protoc_insertion_point(class_scope:SystemEventDetailSet)

class SystemEventHtmlSet(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SYSTEMEVENTHTMLSET
  
  # @@protoc_insertion_point(class_scope:SystemEventHtmlSet)

class SoundEventSet(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SOUNDEVENTSET
  
  # @@protoc_insertion_point(class_scope:SoundEventSet)

class TapDetailSet(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TAPDETAILSET
  
  # @@protoc_insertion_point(class_scope:TapDetailSet)

class DrinkDetailHtmlSet(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DRINKDETAILHTMLSET
  
  # @@protoc_insertion_point(class_scope:DrinkDetailHtmlSet)

class ThermoSensorSet(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _THERMOSENSORSET
  
  # @@protoc_insertion_point(class_scope:ThermoSensorSet)

class ThermoLogSet(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _THERMOLOGSET
  
  # @@protoc_insertion_point(class_scope:ThermoLogSet)

class TapDetail(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TAPDETAIL
  
  # @@protoc_insertion_point(class_scope:TapDetail)

class DrinkDetail(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DRINKDETAIL
  
  # @@protoc_insertion_point(class_scope:DrinkDetail)

class SessionDetail(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SESSIONDETAIL
  
  # @@protoc_insertion_point(class_scope:SessionDetail)

class KegDetail(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _KEGDETAIL
  
  # @@protoc_insertion_point(class_scope:KegDetail)

class UserDetail(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _USERDETAIL
  
  # @@protoc_insertion_point(class_scope:UserDetail)

class SystemEventDetail(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SYSTEMEVENTDETAIL
  
  # @@protoc_insertion_point(class_scope:SystemEventDetail)

class SystemEventHtml(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SYSTEMEVENTHTML
  
  # @@protoc_insertion_point(class_scope:SystemEventHtml)

class ThermoSensorDetail(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _THERMOSENSORDETAIL
  
  # @@protoc_insertion_point(class_scope:ThermoSensorDetail)

class DrinkDetailHtml(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DRINKDETAILHTML
  
  # @@protoc_insertion_point(class_scope:DrinkDetailHtml)

# @@protoc_insertion_point(module_scope)
