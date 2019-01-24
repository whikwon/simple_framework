from .two_stage import TwoStageDetector
from ..registry import DETECTORS
from mmdet.core import anchor_target

print("faster_rcnn loaded")

@DETECTORS.register_module
class FasterRCNN(TwoStageDetector):

    def __init__(self):
        super(FasterRCNN, self).__init__()

    def generate_anchor(self):
        anchor_target()
