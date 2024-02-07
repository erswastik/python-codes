import cv2
from pathlib import Path
from yolov5 import torch_utils, models
from yolov5.utils.general import non_max_suppression, scale_coords

def detect():
    # Load YOLOv5 model
    model = models.load('yolov8s.pt')

    # Initialize webcam
    cap = cv2.VideoCapture(0)

    while True:
        # Read frame from webcam
        ret, frame = cap.read()

        # Perform inference
        results = model(frame)

        # Non-maximum suppression
        results = non_max_suppression(results, conf_thres=0.5)

        for det in results:
            if det is not None and len(det):
                # Rescale bounding boxes to original frame size
                det[:, :4] = scale_coords(frame.shape[1:], det[:, :4], frame.shape).round()

                # Draw bounding boxes on the frame
                for *xyxy, conf, cls in reversed(det):
                    label = f'{model.names[int(cls)]} {conf:.2f}'
                    cv2.rectangle(frame, (int(xyxy[0]), int(xyxy[1])), (int(xyxy[2]), int(xyxy[3])), (0, 255, 0), 2)
                    cv2.putText(frame, label, (int(xyxy[0]), int(xyxy[1] - 5)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Display the frame with detections
        cv2.imshow('Object Detection', frame)

        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detect()
