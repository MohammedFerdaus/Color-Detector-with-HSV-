# Color Detector

A real-time color detection tool using Python and OpenCV. It identifies colors in your webcam feed and draws labeled bounding boxes around detected regions.

Detected Colors
- Red
- Green
- Blue
- White
- Black

Requirements
- Python 3.x
- OpenCV
- NumPy

Usage
Run the main script:
   python main.py

Press Q to quit.

Configuration
You can tweak detection settings in config.py:
- CAMERA_INDEX — which camera to use
- MIN_CONTOUR_AREA — minimum size of a detection
- COLORS — add or remove colors to detect
- BOX_THICKNESS / FONT_SCALE — visual settings
