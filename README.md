# Boxing CV - Punch Detection System

A real-time boxing punch detection system using YOLOv8 Pose estimation to classify different boxing moves.

## Overview

This project uses a fine-tuned YOLOv8 model to detect and classify boxing punches in real-time from webcam input or video files. The model can identify:
- **Hook Punch**
- **Straight Punch** 
- **Uppercut**
- **Neutral** (idle/transition states)

## Features

- Real-time webcam punch detection
- Video file analysis
- Keypoint-based pose estimation (13 body joints)
- Confidence scoring for predictions

## Quick Start

### Requirements

pip install ultralytics opencv-python

## Usage 

### Live webcam detection 

python boxing_test/test_webcam.py

### Video File Analysis:

python boxing_test/test.py

## Model Details 

Sorry for any frustration. Here is your complete README in one clean, copyable Markdown block:

```markdown
# Boxing CV - Punch Detection System

A real-time boxing punch detection system using YOLOv8 Pose estimation to classify different boxing moves.

## Overview

This project uses a fine-tuned YOLOv8 model to detect and classify boxing punches in real-time from webcam input or video files. The model can identify:
- **Hook Punch**
- **Straight Punch** 
- **Uppercut**
- **Neutral** (idle/transition states)

## Features

- Real-time webcam punch detection
- Video file analysis
- Keypoint-based pose estimation (13 body joints)
- Confidence scoring for predictions

## Quick Start

### Requirements
```bash
pip install ultralytics opencv-python
```

### Usage

**Live Webcam Detection:**
```bash
python boxing_test/test_webcam.py
```

**Video File Analysis:**
```bash
python boxing_test/test.py
```

## Model Details

- **Architecture**: YOLOv8 Pose
- **Input**: 640x640 images
- **Confidence Threshold**: 0.35
- **Keypoints**: 13 body joints (shoulders, elbows, wrists, etc.)

The model analyzes spatial patterns of arm and shoulder movements to classify punch types based on keypoint positions.

## Dataset

Training data sourced from [Roboflow Punch Detector Dataset](https://universe.roboflow.com/westminster-zpvgi/punch-detector/dataset/2)

## Controls

- Press `q` or `Esc` to quit webcam mode
- Annotated videos are saved to `runs/pose/predict*`

---

*For detailed model architecture explanation, see ModelExplanation.md*
```

You can copy and paste this entire block into your `README.md` file.
You can copy and paste this entire block into your `README.md` file.
