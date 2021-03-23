#!/usr/bin/env python3

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'    # Suppress TensorFlow logging (1)
import pathlib
import tensorflow as tf

tf.get_logger().setLevel('ERROR')           # Suppress TensorFlow logging (2)

# Enable GPU dynamic memory allocation
gpus = tf.config.experimental.list_physical_devices('GPU')
for gpu in gpus:
    tf.config.experimental.set_memory_growth(gpu, True)


import time
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as viz_utils
from object_detection.utils import config_util
from object_detection.builders import model_builder

PATH_TO_LABELS = '/home/localryu/catkin_ws/src/tf2_object_detection_ros/src/object_detection/inference_graph/label_map.pbtxt'
PATH_TO_MODEL_DIR = '/home/localryu/catkin_ws/src/tf2_object_detection_ros/src/object_detection/inference_graph'
PATH_TO_SAVED_MODEL = PATH_TO_MODEL_DIR + "/saved_model"
# PATH_TO_CKPT = "/home/localryu/models/research/object_detection/training"
# PATH_TO_CKPT = "/home/localryu/catkin_ws/src/tf2_object_detection_ros/src/object_detection/inference_graph/checkpoint"
# PATH_TO_CFG = PATH_TO_MODEL_DIR + "/pipeline.config"
print('Loading model...', end='')
start_time = time.time()

# Load saved model and build the detection function
detect_fn = tf.saved_model.load(PATH_TO_SAVED_MODEL)


# configs = config_util.get_configs_from_pipeline_file(PATH_TO_CFG)
# model_config = configs['model']
# detection_model = model_builder.build(model_config=model_config, is_training=False)

# ckpt = tf.compat.v2.train.Checkpoint(model=detection_model)
# ckpt.restore(os.path.join(PATH_TO_CKPT, 'ckpt-0')).expect_partial()

# def detect_fn(image):
#     """Detect objects in image."""

#     image, shapes = detection_model.preprocess(image)
#     prediction_dict = detection_model.predict(image, shapes)
#     detections = detection_model.postprocess(prediction_dict, shapes)

#     return detections

end_time = time.time()
elapsed_time = end_time - start_time
print('Done! Took {} seconds'.format(elapsed_time))

category_index = label_map_util.create_category_index_from_labelmap(PATH_TO_LABELS,
                                                                    use_display_name=True)


import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import cv2
import warnings
warnings.filterwarnings('ignore')   # Suppress Matplotlib warnings



image_np = cv2.imread('/home/localryu/models/research/object_detection/images/train/AOframe0068.jpg',cv2.IMREAD_COLOR)
image_infer = cv2.cvtColor(image_np, cv2.COLOR_BGR2RGB)

# image_np = image_np.astype(np.uint8)
# Things to try:
# Flip horizontally
# image_np = np.fliplr(image_np).copy()

# Convert image to grayscale
# image_np = np.tile(
#     np.mean(image_np, 2, keepdims=True), (1, 1, 3)).astype(np.uint8)

# The input needs to be a tensor, convert it using `tf.convert_to_tensor`.
input_tensor = tf.convert_to_tensor(image_infer)
# The model expects a batch of images, so add an axis with `tf.newaxis`.
input_tensor = input_tensor[tf.newaxis, ...]

# input_tensor = tf.convert_to_tensor(np.expand_dims(image_infer, 0), dtype=tf.float32)
# input_tensor = np.expand_dims(image_np, 0)
detections = detect_fn(input_tensor)

# All outputs are batches tensors.
# Convert to numpy arrays, and take index [0] to remove the batch dimension.
# We're only interested in the first num_detections.
num_detections = int(detections.pop('num_detections'))
print(num_detections)
detections = {key: value[0, :num_detections].numpy()
                for key, value in detections.items()}
detections['num_detections'] = num_detections

# detection_classes should be ints.
detections['detection_classes'] = detections['detection_classes'].astype(np.int64)
label_id_offset = 1
image_np_with_detections = image_np.copy()

viz_utils.visualize_boxes_and_labels_on_image_array(
        image_np_with_detections,
        detections['detection_boxes'],
        detections['detection_classes'],#+label_id_offset,
        detections['detection_scores'],
        category_index,
        use_normalized_coordinates=True,
        max_boxes_to_draw=200,
        min_score_thresh=.70,
        agnostic_mode=False)

# image_np_with_detections = cv2.resize(image_np_with_detections, dsize=(640, 480), interpolation=cv2.INTER_AREA)
cv2.imshow('test',image_np_with_detections)
cv2.waitKey(0)
print('Done')


# sphinx_gallery_thumbnail_number = 2
