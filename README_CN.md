# tf_yolov4

[![license](https://img.shields.io/github/license/mashape/apistatus.svg)](LICENSE)

## 介绍

构建YOLOV4模型受启发于 [https://github.com/AlexeyAB/darknet](https://github.com/AlexeyAB/darknet).

模型主结构来源于 [https://github.com/YunYang1994/tensorflow-yolov3](https://github.com/YunYang1994/tensorflow-yolov3).

Backbone: CSPDarknet53[[1]](https://arxiv.org/pdf/1911.11929.pdf), Mish[[2]](https://arxiv.org/abs/1908.08681); 

Neck: SPP[[3]](https://arxiv.org/abs/1406.4729), PAN[[4]](https://arxiv.org/abs/1803.01534); 

Head: YOLOv3(Leaky_ReLU)[[10]](https://arxiv.org/abs/1804.02767); 

Loss函数: DIOU CIOU[[5]](https://arxiv.org/pdf/1911.08287v1.pdf), Focal_Loss[[6]](https://arxiv.org/abs/1708.02002);  Other: Label_Smoothing[[7]](https://arxiv.org/pdf/1906.02629.pdf);

---
## **模型评估**

**GeForce GTX 1080 Ti：**

训练验证集: VOCtrainval_11-May-2012; 
测试集: VOCtest_06-Nov-2007;

|         Network        |     Size     | FPS(avg) |    mAP   |   weights   |
|:----------------------:|:------------:|:--------:|:--------:|:-----------:|
| Darknet53_spp_pan_ciou |    608x608   |    23    |**[62.52%](https://raw.githubusercontent.com/devinhee/tf_yolov4/master/mAP/VOC_mAP/608x608/mAP.png)**|  [yolov4.pb](https://pan.baidu.com/s/1d9N2eE3Hu_A4Rww4MLQAGA) kvn3  |
| Darknet53_spp_pan_ciou |    512x512   |    29    |**[59.77%](https://raw.githubusercontent.com/devinhee/tf_yolov4/master/mAP/VOC_mAP/512x512/mAP.png)**|  [yolov4.pb](https://pan.baidu.com/s/1GaXn32_F_VHBtXVskHGfWg) fwkc  |
| Darknet53_spp_pan_ciou |    416x416   |    36    |**[55.01%](https://raw.githubusercontent.com/devinhee/tf_yolov4/master/mAP/VOC_mAP/416x416/mAP.png)**|  [yolov4.pb](https://pan.baidu.com/s/1Ud_cF9CPbBvZc_FDvV6dCA) li3p  |

---

## 运行环境

Python 3.6.8

Tensorflow 1.13.1

---

## 快速开始

1. 从这里 [yolov4.weights](https://drive.google.com/open?id=1cewMfusmPjYWbrnuJRuKhPMwRe_b9PaT) 下载预训练的权重.
2. 将权重文件转换为tf模型.
3. 运行 YOLOv4 进行检测.

运行 from_darknet_weights_to_ckpt.py 就会得到yolov4 tf模型的.ckpt权重文件 yolov4_coco.ckpt.

```
python from_darknet_weights_to_ckpt.py
```

再运行 ckpt2pb.py 就会得到yolov4 tf模型的.pb权重文件 yolov4.pb.

```
python ckpt2pb.py
```

或者直接运行 from_darknet_weights_to_pb.py 得到.pd权重文件.

```
python from_darknet_weights_to_pb.py
```



### Usage

模型demo展示

```
python image_demo.py
```

### 训练

进入 yolov4/config.py 脚本添加你自己的相关路径.

```
python train.py
```

---

### 参考文章

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

### 致谢！

keras_yolov3 [https://github.com/qqwweee/keras-yolo3](https://github.com/qqwweee/keras-yolo3).



