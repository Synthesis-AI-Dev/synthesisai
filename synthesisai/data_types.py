from enum import Enum
from typing import Dict, Tuple

import numpy as np

Item = dict
InstanceId = int
LandmarkId = int
Landmark_2D = Tuple[float, float]
Landmark_3D = Tuple[float, float, float]


class OutOfFrameLandmarkStrategy(Enum):
    IGNORE = "ignore"
    CLIP = "clip"

    @staticmethod
    def clip_landmarks_(
        landmarks: Dict[LandmarkId, Landmark_2D], height: int, width: int
    ) -> Dict[LandmarkId, Landmark_2D]:
        clipped_landmarks: Dict[LandmarkId, Landmark_2D] = {}
        for name, (x, y) in landmarks.items():
            xx = np.clip(x, 0, width - 1)
            yy = np.clip(y, 0, height - 1)
            clipped_landmarks[name] = (float(xx), float(yy))
        return clipped_landmarks
