# -*- coding: utf-8 -*-
from easydict import EasyDict as edict


__C = edict()
# Consumers can get config by: from config import cfg
cfg = __C

# YOLO options
__C.YOLO = edict()

# Set the class name
__C.YOLO.CLASSES = "./data/classes/voc.names"
__C.YOLO.ANCHORS = "./data/anchors/voc_anchors9.txt"
__C.YOLO.MOVING_AVE_DECAY = 0.9995
__C.YOLO.STRIDES = [8, 16, 32]
__C.YOLO.ANCHOR_PER_SCALE = 3
__C.YOLO.IOU_LOSS_THRESH = 0.5
__C.YOLO.UPSAMPLE_METHOD = "resize"


# Train options
__C.TRAIN = edict()

__C.TRAIN.ANNOT_PATH = "./data/dataset/voc_train.txt"
__C.TRAIN.BATCH_SIZE = 4
__C.TRAIN.INPUT_SIZE = 512
__C.TRAIN.DATA_AUG = True
__C.TRAIN.LEARN_RATE_INIT = 0.00005  # 1e-4
__C.TRAIN.LEARN_RATE_END = 1e-6
__C.TRAIN.WARMUP_EPOCHS = 2
__C.TRAIN.FISRT_STAGE_EPOCHS = 20
__C.TRAIN.SECOND_STAGE_EPOCHS = 100
__C.TRAIN.INITIAL_WEIGHT = "./checkpoint_yolov4/yolov4_coco.ckpt"


# TEST options
__C.TEST = edict()

__C.TEST.ANNOT_PATH = "./data/dataset/voc_val.txt"
__C.TEST.BATCH_SIZE = 2
__C.TEST.INPUT_SIZE = 512
__C.TEST.DATA_AUG = False
__C.TEST.WRITE_IMAGE = True
__C.TEST.SCORE_THRESHOLD = 0.3
__C.TEST.IOU_THRESHOLD = 0.45
