# Tensorflow2 object detection installion & tutorial

#### System environment
    Ubuntu 18.04
    CUDA 10.1
    CuDNN 7.5.2
    python3.6

## Tensorflow2 installation

  ##### Install pip3 and version upgrade
  - Required : pip version > 19.0
  ~~~
  sudo apt install python3-pip
  pip3 install --upgrade pip
  ~~~
  
  ##### Install tensorflow2
  - install current stable release  
  ~~~
  pip3 install tensorflow
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
  ~~~
  # From within ~/models/research/
  cp object_detection/packages/tf2/setup.py .
  python -m pip install .
  ~~~
  
### Test installation
  ~~~
  # From within ~/models/research/
  python object_detection/builders/model_builder_tf2_test.py
  ~~~
