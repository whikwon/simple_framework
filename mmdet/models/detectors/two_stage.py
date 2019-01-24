from ..registry import DETECTORS
from .base import BaseDetector

print("two_stage initilized")

@DETECTORS.register_module
class TwoStageDetector(BaseDetector):
    pass
