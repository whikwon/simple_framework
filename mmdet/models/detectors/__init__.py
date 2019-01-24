from .faster_rcnn import FasterRCNN
from .retinanet import RetinaNet
from .two_stage import TwoStageDetector
from .base import BaseDetector

print("detector initialized")

__all__ = ["BaseDetector", "TwoStageDetector", "FasterRCNN", "RetinaNet"]
