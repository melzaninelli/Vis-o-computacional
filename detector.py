from ultralytics import YOLO

class DetectorPose:

    def __init__(self):
        self.model = YOLO("yolo11n-pose.pt")

    def detectar(self, frame):
        return self.model(frame, verbose=False)