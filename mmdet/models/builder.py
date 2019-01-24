from .registry import DETECTORS

print("builder initialized")

def build_detector():
    print("build completed")
    return DETECTORS
