# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/download_item_templates_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.settings.master import avatar_customization_settings_pb2 as pogoprotos_dot_settings_dot_master_dot_avatar__customization__settings__pb2
from pogoprotos.settings.master import badge_settings_pb2 as pogoprotos_dot_settings_dot_master_dot_badge__settings__pb2
from pogoprotos.settings.master import camera_settings_pb2 as pogoprotos_dot_settings_dot_master_dot_camera__settings__pb2
from pogoprotos.settings.master import encounter_settings_pb2 as pogoprotos_dot_settings_dot_master_dot_encounter__settings__pb2
from pogoprotos.settings.master import equipped_badge_settings_pb2 as pogoprotos_dot_settings_dot_master_dot_equipped__badge__settings__pb2
from pogoprotos.settings.master import form_settings_pb2 as pogoprotos_dot_settings_dot_master_dot_form__settings__pb2
from pogoprotos.settings.master import gym_battle_settings_pb2 as pogoprotos_dot_settings_dot_master_dot_gym__battle__settings__pb2
from pogoprotos.settings.master import gym_level_settings_pb2 as pogoprotos_dot_settings_dot_master_dot_gym__level__settings__pb2
from pogoprotos.settings.master import iap_item_display_pb2 as pogoprotos_dot_settings_dot_master_dot_iap__item__display__pb2
from pogoprotos.settings.master import iap_settings_pb2 as pogoprotos_dot_settings_dot_master_dot_iap__settings__pb2
from pogoprotos.settings.master import item_settings_pb2 as pogoprotos_dot_settings_dot_master_dot_item__settings__pb2
from pogoprotos.settings.master import move_sequence_settings_pb2 as pogoprotos_dot_settings_dot_master_dot_move__sequence__settings__pb2
from pogoprotos.settings.master import move_settings_pb2 as pogoprotos_dot_settings_dot_master_dot_move__settings__pb2
from pogoprotos.settings.master import player_level_settings_pb2 as pogoprotos_dot_settings_dot_master_dot_player__level__settings__pb2
from pogoprotos.settings.master import pokemon_settings_pb2 as pogoprotos_dot_settings_dot_master_dot_pokemon__settings__pb2
from pogoprotos.settings.master import pokemon_upgrade_settings_pb2 as pogoprotos_dot_settings_dot_master_dot_pokemon__upgrade__settings__pb2
from pogoprotos.settings.master import quest_settings_pb2 as pogoprotos_dot_settings_dot_master_dot_quest__settings__pb2
from pogoprotos.settings.master import type_effective_settings_pb2 as pogoprotos_dot_settings_dot_master_dot_type__effective__settings__pb2
from pogoprotos.settings.master import gender_settings_pb2 as pogoprotos_dot_settings_dot_master_dot_gender__settings__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/download_item_templates_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_pb=_b('\nFpogoprotos/networking/responses/download_item_templates_response.proto\x12\x1fpogoprotos.networking.responses\x1a>pogoprotos/settings/master/avatar_customization_settings.proto\x1a/pogoprotos/settings/master/badge_settings.proto\x1a\x30pogoprotos/settings/master/camera_settings.proto\x1a\x33pogoprotos/settings/master/encounter_settings.proto\x1a\x38pogoprotos/settings/master/equipped_badge_settings.proto\x1a.pogoprotos/settings/master/form_settings.proto\x1a\x34pogoprotos/settings/master/gym_battle_settings.proto\x1a\x33pogoprotos/settings/master/gym_level_settings.proto\x1a\x31pogoprotos/settings/master/iap_item_display.proto\x1a-pogoprotos/settings/master/iap_settings.proto\x1a.pogoprotos/settings/master/item_settings.proto\x1a\x37pogoprotos/settings/master/move_sequence_settings.proto\x1a.pogoprotos/settings/master/move_settings.proto\x1a\x36pogoprotos/settings/master/player_level_settings.proto\x1a\x31pogoprotos/settings/master/pokemon_settings.proto\x1a\x39pogoprotos/settings/master/pokemon_upgrade_settings.proto\x1a/pogoprotos/settings/master/quest_settings.proto\x1a\x38pogoprotos/settings/master/type_effective_settings.proto\x1a\x30pogoprotos/settings/master/gender_settings.proto\"\xa2\r\n\x1d\x44ownloadItemTemplatesResponse\x12U\n\x06result\x18\x01 \x01(\x0e\x32\x45.pogoprotos.networking.responses.DownloadItemTemplatesResponse.Result\x12\x63\n\x0eitem_templates\x18\x02 \x03(\x0b\x32K.pogoprotos.networking.responses.DownloadItemTemplatesResponse.ItemTemplate\x12\x14\n\x0ctimestamp_ms\x18\x03 \x01(\x04\x12\x13\n\x0bpage_offset\x18\x04 \x01(\x05\x1a\xe2\n\n\x0cItemTemplate\x12\x13\n\x0btemplate_id\x18\x01 \x01(\t\x12\x45\n\x10pokemon_settings\x18\x02 \x01(\x0b\x32+.pogoprotos.settings.master.PokemonSettings\x12?\n\ritem_settings\x18\x03 \x01(\x0b\x32(.pogoprotos.settings.master.ItemSettings\x12?\n\rmove_settings\x18\x04 \x01(\x0b\x32(.pogoprotos.settings.master.MoveSettings\x12P\n\x16move_sequence_settings\x18\x05 \x01(\x0b\x32\x30.pogoprotos.settings.master.MoveSequenceSettings\x12I\n\x0etype_effective\x18\x08 \x01(\x0b\x32\x31.pogoprotos.settings.master.TypeEffectiveSettings\x12\x41\n\x0e\x62\x61\x64ge_settings\x18\n \x01(\x0b\x32).pogoprotos.settings.master.BadgeSettings\x12:\n\x06\x63\x61mera\x18\x0b \x01(\x0b\x32*.pogoprotos.settings.master.CameraSettings\x12\x45\n\x0cplayer_level\x18\x0c \x01(\x0b\x32/.pogoprotos.settings.master.PlayerLevelSettings\x12?\n\tgym_level\x18\r \x01(\x0b\x32,.pogoprotos.settings.master.GymLevelSettings\x12\x46\n\x0f\x62\x61ttle_settings\x18\x0e \x01(\x0b\x32-.pogoprotos.settings.master.GymBattleSettings\x12I\n\x12\x65ncounter_settings\x18\x0f \x01(\x0b\x32-.pogoprotos.settings.master.EncounterSettings\x12\x44\n\x10iap_item_display\x18\x10 \x01(\x0b\x32*.pogoprotos.settings.master.IapItemDisplay\x12=\n\x0ciap_settings\x18\x11 \x01(\x0b\x32\'.pogoprotos.settings.master.IapSettings\x12L\n\x10pokemon_upgrades\x18\x12 \x01(\x0b\x32\x32.pogoprotos.settings.master.PokemonUpgradeSettings\x12J\n\x0f\x65quipped_badges\x18\x13 \x01(\x0b\x32\x31.pogoprotos.settings.master.EquippedBadgeSettings\x12\x41\n\x0equest_settings\x18\x14 \x01(\x0b\x32).pogoprotos.settings.master.QuestSettings\x12U\n\x14\x61vatar_customization\x18\x15 \x01(\x0b\x32\x37.pogoprotos.settings.master.AvatarCustomizationSettings\x12?\n\rform_settings\x18\x16 \x01(\x0b\x32(.pogoprotos.settings.master.FormSettings\x12\x43\n\x0fgender_settings\x18\x17 \x01(\x0b\x32*.pogoprotos.settings.master.GenderSettings\"5\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x08\n\x04PAGE\x10\x02\x12\t\n\x05RETRY\x10\x03\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_settings_dot_master_dot_avatar__customization__settings__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_master_dot_badge__settings__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_master_dot_camera__settings__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_master_dot_encounter__settings__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_master_dot_equipped__badge__settings__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_master_dot_form__settings__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_master_dot_gym__battle__settings__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_master_dot_gym__level__settings__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_master_dot_iap__item__display__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_master_dot_iap__settings__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_master_dot_item__settings__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_master_dot_move__sequence__settings__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_master_dot_move__settings__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_master_dot_player__level__settings__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_master_dot_pokemon__settings__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_master_dot_pokemon__upgrade__settings__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_master_dot_quest__settings__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_master_dot_type__effective__settings__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_master_dot_gender__settings__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_DOWNLOADITEMTEMPLATESRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.responses.DownloadItemTemplatesResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PAGE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RETRY', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=2756,
  serialized_end=2809,
)
_sym_db.RegisterEnumDescriptor(_DOWNLOADITEMTEMPLATESRESPONSE_RESULT)


_DOWNLOADITEMTEMPLATESRESPONSE_ITEMTEMPLATE = _descriptor.Descriptor(
  name='ItemTemplate',
  full_name='pogoprotos.networking.responses.DownloadItemTemplatesResponse.ItemTemplate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='template_id', full_name='pogoprotos.networking.responses.DownloadItemTemplatesResponse.ItemTemplate.template_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokemon_settings', full_name='pogoprotos.networking.responses.DownloadItemTemplatesResponse.ItemTemplate.pokemon_settings', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item_settings', full_name='pogoprotos.networking.responses.DownloadItemTemplatesResponse.ItemTemplate.item_settings', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='move_settings', full_name='pogoprotos.networking.responses.DownloadItemTemplatesResponse.ItemTemplate.move_settings', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='move_sequence_settings', full_name='pogoprotos.networking.responses.DownloadItemTemplatesResponse.ItemTemplate.move_sequence_settings', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type_effective', full_name='pogoprotos.networking.responses.DownloadItemTemplatesResponse.ItemTemplate.type_effective', index=5,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='badge_settings', full_name='pogoprotos.networking.responses.DownloadItemTemplatesResponse.ItemTemplate.badge_settings', index=6,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='camera', full_name='pogoprotos.networking.responses.DownloadItemTemplatesResponse.ItemTemplate.camera', index=7,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='player_level', full_name='pogoprotos.networking.responses.DownloadItemTemplatesResponse.ItemTemplate.player_level', index=8,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gym_level', full_name='pogoprotos.networking.responses.DownloadItemTemplatesResponse.ItemTemplate.gym_level', index=9,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battle_settings', full_name='pogoprotos.networking.responses.DownloadItemTemplatesResponse.ItemTemplate.battle_settings', index=10,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='encounter_settings', full_name='pogoprotos.networking.responses.DownloadItemTemplatesResponse.ItemTemplate.encounter_settings', index=11,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iap_item_display', full_name='pogoprotos.networking.responses.DownloadItemTemplatesResponse.ItemTemplate.iap_item_display', index=12,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iap_settings', full_name='pogoprotos.networking.responses.DownloadItemTemplatesResponse.ItemTemplate.iap_settings', index=13,
      number=17, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokemon_upgrades', full_name='pogoprotos.networking.responses.DownloadItemTemplatesResponse.ItemTemplate.pokemon_upgrades', index=14,
      number=18, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='equipped_badges', full_name='pogoprotos.networking.responses.DownloadItemTemplatesResponse.ItemTemplate.equipped_badges', index=15,
      number=19, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='quest_settings', full_name='pogoprotos.networking.responses.DownloadItemTemplatesResponse.ItemTemplate.quest_settings', index=16,
      number=20, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='avatar_customization', full_name='pogoprotos.networking.responses.DownloadItemTemplatesResponse.ItemTemplate.avatar_customization', index=17,
      number=21, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='form_settings', full_name='pogoprotos.networking.responses.DownloadItemTemplatesResponse.ItemTemplate.form_settings', index=18,
      number=22, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gender_settings', full_name='pogoprotos.networking.responses.DownloadItemTemplatesResponse.ItemTemplate.gender_settings', index=19,
      number=23, type=11, cpp_type=10, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1376,
  serialized_end=2754,
)

_DOWNLOADITEMTEMPLATESRESPONSE = _descriptor.Descriptor(
  name='DownloadItemTemplatesResponse',
  full_name='pogoprotos.networking.responses.DownloadItemTemplatesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.DownloadItemTemplatesResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item_templates', full_name='pogoprotos.networking.responses.DownloadItemTemplatesResponse.item_templates', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp_ms', full_name='pogoprotos.networking.responses.DownloadItemTemplatesResponse.timestamp_ms', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_offset', full_name='pogoprotos.networking.responses.DownloadItemTemplatesResponse.page_offset', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_DOWNLOADITEMTEMPLATESRESPONSE_ITEMTEMPLATE, ],
  enum_types=[
    _DOWNLOADITEMTEMPLATESRESPONSE_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1111,
  serialized_end=2809,
)

_DOWNLOADITEMTEMPLATESRESPONSE_ITEMTEMPLATE.fields_by_name['pokemon_settings'].message_type = pogoprotos_dot_settings_dot_master_dot_pokemon__settings__pb2._POKEMONSETTINGS
_DOWNLOADITEMTEMPLATESRESPONSE_ITEMTEMPLATE.fields_by_name['item_settings'].message_type = pogoprotos_dot_settings_dot_master_dot_item__settings__pb2._ITEMSETTINGS
_DOWNLOADITEMTEMPLATESRESPONSE_ITEMTEMPLATE.fields_by_name['move_settings'].message_type = pogoprotos_dot_settings_dot_master_dot_move__settings__pb2._MOVESETTINGS
_DOWNLOADITEMTEMPLATESRESPONSE_ITEMTEMPLATE.fields_by_name['move_sequence_settings'].message_type = pogoprotos_dot_settings_dot_master_dot_move__sequence__settings__pb2._MOVESEQUENCESETTINGS
_DOWNLOADITEMTEMPLATESRESPONSE_ITEMTEMPLATE.fields_by_name['type_effective'].message_type = pogoprotos_dot_settings_dot_master_dot_type__effective__settings__pb2._TYPEEFFECTIVESETTINGS
_DOWNLOADITEMTEMPLATESRESPONSE_ITEMTEMPLATE.fields_by_name['badge_settings'].message_type = pogoprotos_dot_settings_dot_master_dot_badge__settings__pb2._BADGESETTINGS
_DOWNLOADITEMTEMPLATESRESPONSE_ITEMTEMPLATE.fields_by_name['camera'].message_type = pogoprotos_dot_settings_dot_master_dot_camera__settings__pb2._CAMERASETTINGS
_DOWNLOADITEMTEMPLATESRESPONSE_ITEMTEMPLATE.fields_by_name['player_level'].message_type = pogoprotos_dot_settings_dot_master_dot_player__level__settings__pb2._PLAYERLEVELSETTINGS
_DOWNLOADITEMTEMPLATESRESPONSE_ITEMTEMPLATE.fields_by_name['gym_level'].message_type = pogoprotos_dot_settings_dot_master_dot_gym__level__settings__pb2._GYMLEVELSETTINGS
_DOWNLOADITEMTEMPLATESRESPONSE_ITEMTEMPLATE.fields_by_name['battle_settings'].message_type = pogoprotos_dot_settings_dot_master_dot_gym__battle__settings__pb2._GYMBATTLESETTINGS
_DOWNLOADITEMTEMPLATESRESPONSE_ITEMTEMPLATE.fields_by_name['encounter_settings'].message_type = pogoprotos_dot_settings_dot_master_dot_encounter__settings__pb2._ENCOUNTERSETTINGS
_DOWNLOADITEMTEMPLATESRESPONSE_ITEMTEMPLATE.fields_by_name['iap_item_display'].message_type = pogoprotos_dot_settings_dot_master_dot_iap__item__display__pb2._IAPITEMDISPLAY
_DOWNLOADITEMTEMPLATESRESPONSE_ITEMTEMPLATE.fields_by_name['iap_settings'].message_type = pogoprotos_dot_settings_dot_master_dot_iap__settings__pb2._IAPSETTINGS
_DOWNLOADITEMTEMPLATESRESPONSE_ITEMTEMPLATE.fields_by_name['pokemon_upgrades'].message_type = pogoprotos_dot_settings_dot_master_dot_pokemon__upgrade__settings__pb2._POKEMONUPGRADESETTINGS
_DOWNLOADITEMTEMPLATESRESPONSE_ITEMTEMPLATE.fields_by_name['equipped_badges'].message_type = pogoprotos_dot_settings_dot_master_dot_equipped__badge__settings__pb2._EQUIPPEDBADGESETTINGS
_DOWNLOADITEMTEMPLATESRESPONSE_ITEMTEMPLATE.fields_by_name['quest_settings'].message_type = pogoprotos_dot_settings_dot_master_dot_quest__settings__pb2._QUESTSETTINGS
_DOWNLOADITEMTEMPLATESRESPONSE_ITEMTEMPLATE.fields_by_name['avatar_customization'].message_type = pogoprotos_dot_settings_dot_master_dot_avatar__customization__settings__pb2._AVATARCUSTOMIZATIONSETTINGS
_DOWNLOADITEMTEMPLATESRESPONSE_ITEMTEMPLATE.fields_by_name['form_settings'].message_type = pogoprotos_dot_settings_dot_master_dot_form__settings__pb2._FORMSETTINGS
_DOWNLOADITEMTEMPLATESRESPONSE_ITEMTEMPLATE.fields_by_name['gender_settings'].message_type = pogoprotos_dot_settings_dot_master_dot_gender__settings__pb2._GENDERSETTINGS
_DOWNLOADITEMTEMPLATESRESPONSE_ITEMTEMPLATE.containing_type = _DOWNLOADITEMTEMPLATESRESPONSE
_DOWNLOADITEMTEMPLATESRESPONSE.fields_by_name['result'].enum_type = _DOWNLOADITEMTEMPLATESRESPONSE_RESULT
_DOWNLOADITEMTEMPLATESRESPONSE.fields_by_name['item_templates'].message_type = _DOWNLOADITEMTEMPLATESRESPONSE_ITEMTEMPLATE
_DOWNLOADITEMTEMPLATESRESPONSE_RESULT.containing_type = _DOWNLOADITEMTEMPLATESRESPONSE
DESCRIPTOR.message_types_by_name['DownloadItemTemplatesResponse'] = _DOWNLOADITEMTEMPLATESRESPONSE

DownloadItemTemplatesResponse = _reflection.GeneratedProtocolMessageType('DownloadItemTemplatesResponse', (_message.Message,), dict(

  ItemTemplate = _reflection.GeneratedProtocolMessageType('ItemTemplate', (_message.Message,), dict(
    DESCRIPTOR = _DOWNLOADITEMTEMPLATESRESPONSE_ITEMTEMPLATE,
    __module__ = 'pogoprotos.networking.responses.download_item_templates_response_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.DownloadItemTemplatesResponse.ItemTemplate)
    ))
  ,
  DESCRIPTOR = _DOWNLOADITEMTEMPLATESRESPONSE,
  __module__ = 'pogoprotos.networking.responses.download_item_templates_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.DownloadItemTemplatesResponse)
  ))
_sym_db.RegisterMessage(DownloadItemTemplatesResponse)
_sym_db.RegisterMessage(DownloadItemTemplatesResponse.ItemTemplate)


# @@protoc_insertion_point(module_scope)
