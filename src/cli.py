import argparse
import cv2
import sys
import os
import time
from src.model_impl import My_CarNumber_Model
from src.logger import app_logger

def process_video(model, source, output_path):
    app_logger.info(f"Processing video: {source}")
    cap = cv2.VideoCapture(source)
    if not cap.isOpened():
        app_logger.error(f"Cannot open video: {source}")
        return
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (w, h))
    frame_count = 0
    total_time = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame_count += 1
        start = time.time()
        try:
            detections = model.detect_plates(frame)
            latency = (time.time() - start) * 1000
            total_time += latency
            for det in detections:
                x1, y1, x2, y2 = det['bbox']
                conf = det['confidence']
                label = f"Car number: {conf:.2f}"
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
                cv2.putText(frame, label, (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)
            out.write(frame)
            if frame_count % 30 == 0:
                app_logger.info(f"Frame {frame_count}, latency: {latency:.2f}ms")
        except Exception as e:
            app_logger.error(f"Error on frame {frame_count}: {e}")
    cap.release()
    out.release()
    avg_lat = total_time / frame_count if frame_count else 0
    app_logger.info(f"Finished. Avg latency: {avg_lat:.2f}ms. Output: {output_path}")
    

def process_stream(model, source):
    app_logger.info(f"Stream from: {source}")
    if source.isdigit():
        source = int(source)
    cap = cv2.VideoCapture(source)
    if not cap.isOpened():
        app_logger.error(f"Cannot open stream: {source}")
        return
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        try:
            detections = model.detect_plates(frame)
            for det in detections:
                x1, y1, x2, y2 = det['bbox']
                conf = det['confidence']
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
                cv2.putText(frame, f"Plate: {conf:.2f}", (x1, y1-10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)
            cv2.imshow('Car Number Detection', frame)
        except Exception as e:
            app_logger.error(f"Stream error: {e}")
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

def main():
    parser = argparse.ArgumentParser(description="Car Number Detection")
    parser.add_argument('--mode', choices=['video', 'stream'], required=True)
    parser.add_argument('--source', type=str, required=True)
    parser.add_argument('--output', type=str, default='./data/output/result.mp4')
    parser.add_argument('--model', type=str, default='models/best.pt')
    args = parser.parse_args()

    try:
        app_logger.info(f"Loading model from {args.model}")
        model = My_CarNumber_Model(args.model)
    except Exception as e:
        app_logger.critical(f"Model load failed: {e}")
        sys.exit(1)

    if args.mode == 'video':
        os.makedirs(os.path.dirname(args.output), exist_ok=True)
        process_video(model, args.source, args.output)
    elif args.mode == 'stream':
        process_stream(model, args.source)

if __name__ == "__main__":
    main()