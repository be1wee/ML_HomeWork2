import numpy as np
from ultralytics import YOLO
from typing import List, Dict, Any
import os

class My_CarNumber_Model:
    def __init__(self, model_path: str = 'models/best.pt'):
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model file not found at {model_path}")
        
        self.model = YOLO(model=model_path, task='detect', verbose=False)
        self.conf_threshold = 0.5

    def detect_plates(self, frame: np.ndarray) -> List[Dict[str, Any]]:
        results = self.model(frame, verbose=False)[0]
        detections = []
        if results.boxes is not None:
            boxes = results.boxes.xyxy.cpu().numpy()
            confs = results.boxes.conf.cpu().numpy()
            classes = results.boxes.cls.cpu().numpy()
            for box, conf, cls in zip(boxes, confs, classes):
                if conf >= self.conf_threshold:
                    x1, y1, x2, y2 = map(int, box)
                    detections.append({
                        'bbox': [x1, y1, x2, y2],
                        'confidence': float(conf),
                        'class': int(cls)
                    })
        return detections