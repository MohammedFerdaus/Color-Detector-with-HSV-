import numpy as np
import cv2

def get_limits(bgr_color):
    # Convert the BGR color to HSV so we can work with hue ranges
    color = np.uint8([[bgr_color]])
    hsv_color = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)[0][0]
    hue = hsv_color[0]

    # White has very low saturation and high brightness, so we match on those instead of hue
    if bgr_color[0] > 200 and bgr_color[1] > 200 and bgr_color[2] > 200:
        lower1 = np.array([0, 0, 200], dtype=np.uint8)
        upper1 = np.array([179, 40, 255], dtype=np.uint8)
        return [(lower1, upper1)]

    # Black has very low brightness regardless of hue or saturation
    # We use a tight value ceiling of 30 to avoid matching dark tones
    if bgr_color[0] < 50 and bgr_color[1] < 50 and bgr_color[2] < 50:
        lower1 = np.array([0, 0, 0], dtype=np.uint8)
        upper1 = np.array([179, 255, 30], dtype=np.uint8)
        return [(lower1, upper1)]

    # Red wraps around the HSV hue circle, appearing at both 0-10 and 170-179
    # We return two ranges and combine them in main.py to catch both ends
    # Saturation is set to a minimum of 150 to avoid matching tones
    if hue < 10:
        lower1 = np.array([0, 150, 100], dtype=np.uint8)
        upper1 = np.array([10, 255, 255], dtype=np.uint8)
        lower2 = np.array([170, 150, 100], dtype=np.uint8)
        upper2 = np.array([179, 255, 255], dtype=np.uint8)
        return [(lower1, upper1), (lower2, upper2)]

    # For all other colors, build a hue range of +/-10 around the target hue
    lower1 = np.array([hue - 10, 100, 100], dtype=np.uint8)
    upper1 = np.array([hue + 10, 255, 255], dtype=np.uint8)
    return [(lower1, upper1)]
