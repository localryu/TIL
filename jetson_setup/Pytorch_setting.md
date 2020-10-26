## Pytorch & torchvision install

##### Reference link (https://forums.developer.nvidia.com/t/pytorch-for-jetson-version-1-6-0-now-available/72048)
### Pytorch install

#### 1. Download pytoch.whl file
    - python3
    wget https://nvidia.box.com/shared/static/c3d7vm4gcs9m728j6o5vjay2jdedqb55.whl
    
    - python2
    wget https://nvidia.box.com/shared/static/yhlmaie35hu8jv2xzvtxsh0rrpcu97yj.whl
#### 2. install dependencies
    - python3
    sudo apt-get install python3-pip libopenblas-base libopenmpi-dev
    pip3 install Cython numpy
    
    - python2
    sudo apt-get install python-pip libopenblas-base libopenmpi-dev
    pip install Cython numpy  
    
#### 3. install whl file
    - python3
    pip3 install torch-1.4.0-cp36-cp36m-linux_aarch64.whl
    
    - python2
    pip install torch-1.4.0-cp27-cp27mu-linux_aarch64.whl    

### torchvision install

#### 1. install dependencies
    sudo apt-get install libjpeg-dev zlib1g-dev

#### 2. clone torchvision
    git clone --branch v0.6.0 https://github.com/pytorch/vision torchvision

#### 3. build torchvision
    cd torchvision
    sudo python setup.py install
    
### ERROR

#### ImportError: No module named builtin
    pip install future
 
