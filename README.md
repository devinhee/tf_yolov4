# tf_yolov4
## Introduction

A tensorflow implementation of YOLOv4 inspired by [https://github.com/AlexeyAB/darknet](https://github.com/AlexeyAB/darknet).

Frame code from [https://github.com/YunYang1994/tensorflow-yolov3](https://github.com/YunYang1994/tensorflow-yolov3).

Used Backbone: CSPDarknet53; Neck: SPP, PAN; Head: YOLOv3; Loss: DIOU，CIOU，Focal_Loss; Other: Label_Smoothing

## Environment

Python 3.6.8

Tensorflow 1.13.1

---

## Quick Start

1. Download YOLOv4 weights from [yolov4.weights](https://drive.google.com/open?id=1cewMfusmPjYWbrnuJRuKhPMwRe_b9PaT).
2. Convert the Darknet YOLOv4 model to a tf model.
3. Run YOLOv4 detection.

```
python from_darknet_weights_to_ckpt.py
```

Running from_darknet_weights_to_ckpt.py will get tf yolov4 weight file yolov4_coco.ckpt.

```
python ckpt2pb.py
```
Running ckpt2pb.py will get tf yolov4 weight file yolov4.pb.



### Usage

Inference

```
python image_demo.py
```
---

### Reference

keras_yolov3 [https://github.com/qqwweee/keras-yolo3](https://github.com/qqwweee/keras-yolo3).

keras_yolov4 [https://github.com/Ma-Dan/keras-yolo4](https://github.com/Ma-Dan/keras-yolo4).


