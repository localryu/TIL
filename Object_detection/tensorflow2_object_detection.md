# Tensorflow2 object detection installation & tutorial

#### System environment
    Ubuntu 18.04
    CUDA 10.1
    CuDNN 7.5.2
    python3.6

## Required package for Tensorflow2 installation

  ##### Install pip3 and version upgrade
  - Required : pip version > 19.0
  ~~~
  sudo apt install python3-pip
  pip3 install --upgrade pip
  ~~~  

## Download the Tensorflow Model Garden
  ~~~
  git clone https://github.com/tensorflow/models.git
  ~~~
  
### Protoc / Protobuf installation
  ~~~
  sudo apt install -y protobuf-compiler
  
  # From within ~/models/research/
  protoc object_detection/protos/*.proto --python_out=.
  ~~~
  
### COCO API installation
  ~~~
  git clone https://github.com/cocodataset/cocoapi.git
  cd cocoapi/PythonAPI
  make
  cp -r pycocotools ~/models/research/
  ~~~
  
### Installation the Object Detection API
   #### 1. the latest stable version of tensorflow will installed in this progress
  ~~~
  # From within ~/models/research/
  cp object_detection/packages/tf2/setup.py .
  python3 -m pip install .
  ~~~
   #### 2. Downgrade tensorflow version (2.3.0)
  ~~~
  !pip3 install tensorflow==2.3.0 tensorflow-gpu==2.3.0
  ~~~
  
### Test installation
  ~~~
  # From within ~/models/research/
  python3 object_detection/builders/model_builder_tf2_test.py
  ~~~
