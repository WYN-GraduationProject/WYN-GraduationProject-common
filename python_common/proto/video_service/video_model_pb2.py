# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/video_service/video_model.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%proto/video_service/video_model.proto\x12\rvideo_service\"K\n\nVideoFrame\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x12\x10\n\x08is_final\x18\x02 \x01(\x08\x12\x0b\n\x03\x66ps\x18\x03 \x01(\x02\x12\x10\n\x08video_id\x18\x04 \x01(\t\"7\n\x13ProcessedVideoFrame\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x12\x12\n\nvideo_path\x18\x02 \x01(\tb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.video_service.video_model_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_VIDEOFRAME']._serialized_start=56
  _globals['_VIDEOFRAME']._serialized_end=131
  _globals['_PROCESSEDVIDEOFRAME']._serialized_start=133
  _globals['_PROCESSEDVIDEOFRAME']._serialized_end=188
# @@protoc_insertion_point(module_scope)
