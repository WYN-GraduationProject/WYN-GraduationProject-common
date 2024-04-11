import os
import uuid
from typing import List, Optional
from utils.tools.LoggingFormatter import LoggerManager
from fastapi import UploadFile
import cv2 as cv
import numpy as np

logger = LoggerManager(logger_name="VideoModel").get_logger()


class VideoModel:
    """
    视频实体类
    """
    fps: int = 30
    """视频帧率"""
    path: Optional[str] = None
    """视频保存路径"""
    filename: Optional[str] = None
    """视频文件名"""
    data: Optional[List[bytes]] = None
    """视频数据"""
    id: Optional[str] = None
    """视频唯一ID"""

    def __init__(self, path: str, filename: str, id: str, data: List[bytes], fps: int = 30):
        """
        初始化视频实体
        :param path: 视频保存路径
        :param filename: 视频文件名
        :param id: 视频唯一ID
        :param data: 视频数据
        :param fps: 视频帧率
        """
        self.path = path
        self.filename = filename
        self.id = id
        self.data = data
        self.fps = fps

    @staticmethod
    async def http_video_save(video: UploadFile) -> 'VideoModel':
        """
        保存上传的视频
        :param video: 上传的视频
        :return: 视频实体
        """
        video_id = str(uuid.uuid4())
        video_filename = f"{video_id}.mp4"
        video_save_path = f"video_data/original/"
        video_model = VideoModel(video_save_path, video_filename, video_id, [], 30)
        # 创建保存视频的目录
        os.makedirs(video_save_path, exist_ok=True)
        # 保存上传的视频到文件
        filepath = os.path.join(video_save_path, video_filename)
        with open(filepath, "wb") as f:
            f.write(await video.read())
        # 打印文件路径和视频文件名
        logger.info(f"Saved video to {filepath}")
        return video_model

    async def save(self):
        """
        保存视频到本地
        :return: None
        """
        if not self.data:
            logger.error(f"视频保存失败：{self.filename}，没有数据")
            return
        os.makedirs(self.path, exist_ok=True)
        filepath = os.path.join(self.path, self.filename)

        first_frame = np.frombuffer(self.data[0], dtype=np.uint8)
        first_frame = cv.imdecode(first_frame, cv.IMREAD_COLOR)
        height, width, _ = first_frame.shape

        fourcc = cv.VideoWriter.fourcc(*'mp4v')
        out = cv.VideoWriter(filepath, fourcc, self.fps, (width, height))

        for frame_bytes in self.data:
            frame = np.frombuffer(frame_bytes, dtype=np.uint8)
            frame = cv.imdecode(frame, cv.IMREAD_COLOR)
            if frame is not None:
                out.write(frame)

        out.release()
        logger.info(f"视频保存成功：{self.path}/{self.filename}")
