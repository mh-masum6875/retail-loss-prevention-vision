# Retail Loss Prevention Vision

[![Vision Transformer](https://img.shields.io/badge/Architecture-Vision%20Transformer%20(ViT)-76B900)](https://github.com/mh-masum6875/smart-retail-loss-prevention-ai)
[![Action Recognition](https://img.shields.io/badge/Task-Action%20Recognition-orange)](https://github.com/mh-masum6875/smart-retail-loss-prevention-ai)
[![YOLOv8 Pose](https://img.shields.io/badge/Pose-YOLO--Pose-00FFFF)](https://ultralytics.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An advanced computer vision framework for retail shrinkage prevention, self-checkout scanning verification, unauthorized photography detection, and temporal action recognition leveraging Vision Transformers.

---

## System Architecture

```mermaid
graph TD
    Camera["CCTV / Self-Checkout Video Feed"] --> Detection["YOLOE Person & Item Segmentation"]
    Detection --> HandTracker["Hand & Object Interaction Detector (Faster R-CNN)"]
    Detection --> Pose["YOLO-Pose Keypoint Extractor (Wrists, Hips)"]
    
    HandTracker --> StateMachine["Temporal Action State Machine"]
    Pose --> StateMachine
    
    StateMachine --> SC["Self-Checkout Scanning Verification<br/>(Item crossing alert line without scan)"]
    StateMachine --> Shoplift["Shoplifting Detection<br/>(Shelf reach -> conceal in pocket)"]
    StateMachine --> Photo["Unauthorized Photography<br/>(50°-150° phone orientation angle)"]
    
    SC --> AlertEngine["Real-time Alert Engine & VMS Dispatch"]
    Shoplift --> AlertEngine
    Photo --> AlertEngine
```

---

## Core Modules

### 1. Self-Checkout Unscanned Item Detector (`self_checkout_tracker.py`)
- **Multi-Model Fusion**: Integrates person segmentation, Faster R-CNN hand-object interaction detection, and wrist/fingertip trajectory state machines.
- **Scanning Zone Logic**: Defines virtual scanner polygons and alert boundaries. Immediately flags items moved into bagging areas without entering the active scanner sequence ($0.3\text{s}$ threshold).
- **False Alarm Suppression**: Phone handling detection suppresses false alerts when customers reach for mobile payments.

### 2. Shoplifting Action Recognition
- **Temporal Action Sequence**:
  $$\text{Idle} \longrightarrow \text{Hand in Shelf} \longrightarrow \text{Took Object} \longrightarrow \text{Hand to Pocket} \longrightarrow \text{Concealment Alert}$$
- **Pose & Wrist Geometry**: Tracks distance from wrist to shelf line ($<80\text{px}$) and wrist to hip pocket ($<15\text{px}$).
- **Research direction**: a graph-based skeleton tokenizer with a spatial-temporal transformer to model multi-frame theft behaviour, explored on the public PoseLift dataset.

### 3. Unauthorized Mobile Photography (`unauthorized_photo_detector.py`)
- **Phone Aspect Angle Calculation**: Classifies phone orientation angles between $50^\circ$ and $150^\circ$ as active camera holding positions.
- **Face & Chest Proximity**: Verifies phone elevation in the upper 60% of the torso bounding box.

---

## Quickstart

```bash
git clone https://github.com/mh-masum6875/smart-retail-loss-prevention-ai.git
cd smart-retail-loss-prevention-ai
pip install -r requirements.txt

# Run Self-Checkout Tracker Demo
python src/self_checkout_tracker.py --source sample_checkout.mp4

# Run Shoplifting Action Sequence Detector
python src/shoplifting_action_detector.py --source sample_retail.mp4
```

---

## License
This project is licensed under the MIT License.
