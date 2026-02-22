# Camera index — 0 uses the default system webcam
CAMERA_INDEX = 0

# Minimum contour area in pixels to count as a valid detection, filters out small noise
MIN_CONTOUR_AREA = 250

# Colors to detect, defined in BGR format as used by OpenCV
COLORS = {
    "RED":   [0, 0, 255],
    "GREEN": [0, 255, 0],
    "BLUE":  [255, 0, 0],
    "WHITE": [255, 255, 255],
    "BLACK": [0, 0, 0]
}

# Thickness of the bounding box rectangle drawn around detected colors
BOX_THICKNESS = 2

# Font scale for the color name label drawn above each bounding box
FONT_SCALE = 0.7
