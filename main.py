import cv2
import numpy as np
from util import get_limits
import config

def boxes_overlap(box1, box2):
    # Check if two bounding boxes intersect by testing if they are separated on either axis
    x1, y1, w1, h1 = box1
    x2, y2, w2, h2 = box2
    return not (x1 + w1 < x2 or x2 + w2 < x1 or y1 + h1 < y2 or y2 + h2 < y1)

cap = cv2.VideoCapture(config.CAMERA_INDEX)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to HSV color space for color range matching
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Collect all valid detections as (area, name, bgr, box) before drawing anything
    detections = []

    for name, bgr in config.COLORS.items():
        ranges = get_limits(bgr)

        # Start with an empty mask and OR in each HSV range for this color
        mask = np.zeros(hsv.shape[:2], dtype=np.uint8)
        for lower, upper in ranges:
            mask = cv2.bitwise_or(mask, cv2.inRange(hsv, lower, upper))

        # Smooth the mask to reduce noise and fill small gaps
        mask = cv2.medianBlur(mask, 5)

        # Find contours in the mask to locate regions of this color
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if contours:
            # Only keep the largest contour to avoid noise detections
            largest = max(contours, key=cv2.contourArea)
            area = cv2.contourArea(largest)

            # Ignore detections smaller than the configured minimum area
            if area > config.MIN_CONTOUR_AREA:
                box = cv2.boundingRect(largest)
                detections.append((area, name, bgr, box))

    # Sort detections largest first so bigger regions take priority in overlap resolution
    detections.sort(key=lambda d: d[0], reverse=True)

    # Walk through detections and discard any that overlap with an already kept detection
    kept = []
    for det in detections:
        if not any(boxes_overlap(det[3], k[3]) for k in kept):
            kept.append(det)

    # Draw bounding boxes and labels only for the final kept detections
    for area, name, bgr, (x, y, w, h) in kept:
        color_tuple = tuple(bgr)
        cv2.rectangle(frame, (x, y), (x + w, y + h), color_tuple, config.BOX_THICKNESS)
        cv2.putText(frame, name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, config.FONT_SCALE, color_tuple, 2)

    cv2.imshow("Color Detection", frame)

    # Press Q to quit the detection loop
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
