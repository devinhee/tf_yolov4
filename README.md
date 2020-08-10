# tf_yolov4

[![license](https://img.shields.io/github/license/mashape/apistatus.svg)](LICENSE)

## Introduction

A tensorflow implementation of YOLOv4 inspired by [https://github.com/AlexeyAB/darknet](https://github.com/AlexeyAB/darknet).

Frame code from [https://github.com/YunYang1994/tensorflow-yolov3](https://github.com/YunYang1994/tensorflow-yolov3).

Backbone: CSPDarknet53[[1]](https://arxiv.org/pdf/1911.11929.pdf), Mish[[2]](https://arxiv.org/abs/1908.08681); 

Neck: SPP[[3]](https://arxiv.org/abs/1406.4729), PAN[[4]](https://arxiv.org/abs/1803.01534); 

Head: YOLOv3(Leaky_ReLU)[[10]](https://arxiv.org/abs/1804.02767); 

Loss: DIOU CIOU[[5]](https://arxiv.org/pdf/1911.08287v1.pdf), Focal_Loss[[6]](https://arxiv.org/abs/1708.02002);  Other: Label_Smoothing[[7]](https://arxiv.org/pdf/1906.02629.pdf);

---
**[Eval: VOC, 512x512, mAP=59.77%](https://github.com/devinhee/tf_yolov4/blob/master/mAP/VOC_mAP/voc_mAP.md)**

---

## Environment

Python 3.6.8

Tensorflow 1.13.1

---

## Quick Start

1. Download YOLOv4 weights from [yolov4.weights](https://drive.google.com/open?id=1cewMfusmPjYWbrnuJRuKhPMwRe_b9PaT).
2. Convert the Darknet YOLOv4 model to a tf model.
3. Run YOLOv4 detection.

Running from_darknet_weights_to_ckpt.py will get tf yolov4 weight file yolov4_coco.ckpt.

```
python from_darknet_weights_to_ckpt.py
```

Running ckpt2pb.py will get tf yolov4 weight file yolov4.pb.

```
python ckpt2pb.py
```

Or running from_darknet_weights_to_pb.py directly.

```
python from_darknet_weights_to_pb.py
```



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

[[1] Cross Stage Partial Network (CSPNet)](https://arxiv.org/pdf/1911.11929.pdf)

[[2] A Self Regularized Non-Monotonic Neural Activation Function](https://arxiv.org/abs/1908.08681)

[[3] Spatial Pyramid Pooling in Deep Convolutional Networks for Visual Recognition](https://arxiv.org/abs/1406.4729)

[[4] Path Aggregation Network for Instance Segmentation](https://arxiv.org/abs/1803.01534)

[[5] Distance-IoU Loss: Faster and Better Learning for Bounding Box Regression](https://arxiv.org/pdf/1911.08287v1.pdf)

[[6] Focal Loss for Dense Object Detection](https://arxiv.org/abs/1708.02002)

[[7] When Does Label Smoothing Help?](https://arxiv.org/pdf/1906.02629.pdf)

[[8] Convolutional Block Attention Module](https://arxiv.org/abs/1807.06521)

[[9] YOLOv4: Optimal Speed and Accuracy of Object Detection](https://arxiv.org/abs/2004.10934)

[[10] YOLOv3: An Incremental Improvement](https://arxiv.org/abs/1804.02767)

[[11] Aggregated Residual Transformations for Deep Neural Networks](https://arxiv.org/abs/1611.05431)

### Acknowledgment

keras_yolov3 [https://github.com/qqwweee/keras-yolo3](https://github.com/qqwweee/keras-yolo3).



