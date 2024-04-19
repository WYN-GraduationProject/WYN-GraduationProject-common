from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class VideoFrame(_message.Message):
    __slots__ = ("data", "is_final", "fps", "video_id")
    DATA_FIELD_NUMBER: _ClassVar[int]
    IS_FINAL_FIELD_NUMBER: _ClassVar[int]
    FPS_FIELD_NUMBER: _ClassVar[int]
    VIDEO_ID_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    is_final: bool
    fps: float
    video_id: str
    def __init__(self, data: _Optional[bytes] = ..., is_final: bool = ..., fps: _Optional[float] = ..., video_id: _Optional[str] = ...) -> None: ...

class ProcessedVideoFrame(_message.Message):
    __slots__ = ("data", "video_path")
    DATA_FIELD_NUMBER: _ClassVar[int]
    VIDEO_PATH_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    video_path: str
    def __init__(self, data: _Optional[bytes] = ..., video_path: _Optional[str] = ...) -> None: ...
