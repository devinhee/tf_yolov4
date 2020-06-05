# tf_yolov4

[![license](https://img.shields.io/github/license/mashape/apistatus.svg)](LICENSE)

## Introduction

A tensorflow implementation of YOLOv4 inspired by [https://github.com/AlexeyAB/darknet](https://github.com/AlexeyAB/darknet).

Frame code from [https://github.com/YunYang1994/tensorflow-yolov3](https://github.com/YunYang1994/tensorflow-yolov3).

Backbone: [CSPDarknet53](https://arxiv.org/pdf/1911.11929.pdf), [Mish](https://arxiv.org/abs/1908.08681); 

Neck: [SPP](https://arxiv.org/abs/1406.4729), [PAN](https://arxiv.org/abs/1803.01534); 

Head: YOLOv3(Leaky_ReLU); 

Loss: [DIOU CIOU](https://arxiv.org/pdf/1911.08287v1.pdf), [Focal_Loss](https://arxiv.org/abs/1708.02002);  Other: [Label_Smoothing](https://arxiv.org/pdf/1906.02629.pdf);

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

### train

to yolov4/config.py add your own path.

```
python train.py
```

---

### Reference

keras_yolov3 [https://github.com/qqwweee/keras-yolo3](https://github.com/qqwweee/keras-yolo3).

keras_yolov4 [https://github.com/Ma-Dan/keras-yolo4](https://github.com/Ma-Dan/keras-yolo4).


