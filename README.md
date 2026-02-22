# Color Detector

A real-time color detection tool using Python and OpenCV. It identifies colors in your webcam feed and draws labeled bounding boxes around detected regions.

## Detected Colors
- Red
- Green
- Blue
- White
- Black

## Requirements
- Python 3.x
- OpenCV
- NumPy

## Installation

1. Clone the repo
   git clone https://github.com/yourusername/color-detector.git
   cd color-detector

2. Install dependencies
   pip install -r requirements.txt

## Usage

Run the main script:
   python main.py

Press Q to quit.

## Configuration
You can tweak detection settings in config.py:
- CAMERA_INDEX — which camera to use
- MIN_CONTOUR_AREA — minimum size of a detection
- COLORS — add or remove colors to detect
- BOX_THICKNESS / FONT_SCALE — visual settings
```

**5. Push to GitHub**

Go to github.com, create a new empty repo (don't initialize it with a README since you already have one), then run:
```
git remote add origin https://github.com/yourusername/your-repo-name.git
git branch -M main
git push -u origin main
