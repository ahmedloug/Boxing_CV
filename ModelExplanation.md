Punch Detector – Model Explanation

Overview

We fine-tuned a YOLOv8 Pose model on a custom dataset of boxing moves (Hook, Straight, Uppercut, Neutral).
Unlike classic object detection, this model learns to detect keypoints of the human body (joints like shoulders, elbows, wrists) and use them to classify different punches.

⸻

Architecture

The model is based on YOLOv8 (You Only Look Once, v8), which has three main parts:
	1.	Backbone (Feature Extractor)
	•	A convolutional neural network (CNN) that processes the raw image into a compact feature map.
	•	YOLOv8 uses a CSPDarknet-like backbone with residual connections and convolutional blocks for efficiency.
	•	This part captures shapes, edges, and motion cues in the image.
	2.	Neck (Feature Aggregator)
	•	Combines information from different scales (small details like hands, big structures like body posture).
	•	Uses FPN + PAN (Feature Pyramid + Path Aggregation) to strengthen both low-level (fingers/arms) and high-level (whole body) features.
	3.	Heads (Prediction Layers)
YOLOv8 is multi-task:
	•	Bounding Box Head → predicts the box around each detected person.
	•	Keypoint Head → predicts the coordinates (x, y, visibility) for each of the 13 body keypoints we defined in the dataset.
	•	Classification Head → assigns the punch type (Hook, Straight, Uppercut, Neutral) to each detection.

⸻

How It Works (Step by Step)
	1.	Input: An image (e.g., a video frame from webcam).
	2.	Feature Extraction: The backbone converts it into feature maps.
	3.	Multi-scale Fusion: The neck merges features from different resolutions.
	4.	Prediction: The heads output:
	•	a bounding box for each detected person,
	•	13 keypoints describing the pose,
	•	a class label (which punch).
	5.	Post-processing: Non-Max Suppression (NMS) filters out duplicates, and confidence thresholds keep only the reliable detections.

⸻

Why It Works for Punches
	•	Punches are defined by arm + shoulder movement.
	•	The keypoints (wrists, elbows, shoulders) are explicitly predicted.
	•	The model learns the spatial patterns of these keypoints:
	•	Straight punch → arm extended forward, aligned shoulder–elbow–wrist.
	•	Hook punch → elbow bent, wrist arcs sideways.
	•	Uppercut → arm moves upward with bent elbow.
	•	Neutral class covers idle or transition states.

⸻

Fine-Tuning
	•	We started from pretrained weights (yolov8n-pose.pt) trained on COCO Pose (large dataset of human keypoints).
	•	Fine-tuning adapts the model to our smaller boxing dataset.
	•	Training updates mainly the heads so the network learns to map poses to boxing moves, while keeping general human pose knowledge from COCO.

⸻

Output Example

For each frame, the model produces:
	•	Bounding Box: where the person is.
	•	Keypoints: 13 joint coordinates with confidence scores.
	•	Class Label: e.g. "Straight-punch" with confidence 0.93.

This allows real-time punch recognition on images, videos, or live webcam.