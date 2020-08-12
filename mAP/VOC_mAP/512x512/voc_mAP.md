# voc_mAP

## Introduction

Train set: VOCtrainval_11-May-2012; 
Test set: VOCtest_06-Nov-2007; 
Weights: [yolov4_voc.pb](https://pan.baidu.com/s/1GaXn32_F_VHBtXVskHGfWg). passwd: fwkc

**GeForce GTX 1080 Ti：**

mAP: 59.77%

|         Network        | Network Size | FPS(avg) |    mAP   |   weights   |
|:----------------------:|:------------:|:--------:|:--------:|:-----------:|
| Darknet53_spp_pan_ciou |    512x512   |    28    |**[59.77%](https://raw.githubusercontent.com/devinhee/tf_yolov4/master/mAP/VOC_mAP/512x512/mAP.png)**|  [yolov4.pb](https://pan.baidu.com/s/1GaXn32_F_VHBtXVskHGfWg) fwkc  |
| Darknet53_spp_pan_ciou |    416x416   |    28    |**[55.01%](https://raw.githubusercontent.com/devinhee/tf_yolov4/master/mAP/VOC_mAP/416x416/mAP.png)**|  [yolov4.pb](https://pan.baidu.com/s/1Ud_cF9CPbBvZc_FDvV6dCA) li3p  |

![mAP_Graph](https://raw.githubusercontent.com/devinhee/tf_yolov4/master/mAP/VOC_mAP/mAP.png)

![Avg_miss_rate](https://raw.githubusercontent.com/devinhee/tf_yolov4/master/mAP/VOC_mAP/lamr.png)

![Detection_results](https://raw.githubusercontent.com/devinhee/tf_yolov4/master/mAP/VOC_mAP/detection-results-info.png)

![GT](https://raw.githubusercontent.com/devinhee/tf_yolov4/master/mAP/VOC_mAP/ground-truth-info.png)







