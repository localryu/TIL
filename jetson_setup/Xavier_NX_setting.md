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
    
    
## OpenCV 3.4 build

#### 1. install dependencies
    sudo apt install build-essential cmake pkg-config -y
    
    sudo apt install libjpeg-dev libtiff5-dev libpng-dev \
    libavcodec-dev libavformat-dev libswscale-dev libv4l-dev \
    libxvidcore-dev libx264-dev libx265-dev libgtk2.0-dev \
    libgtk-3-dev libatlas-base-dev gfortran python3-dev
    
    sudo apt install libgstreamer1.0-0 gstreamer1.0-plugins-base \
    gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly \
    gstreamer1.0-libav gstreamer1.0-doc gstreamer1.0-tools gstreamer1.0-x \
    gstreamer1.0-alsa gstreamer1.0-gl gstreamer1.0-gtk3 gstreamer1.0-pulseaudio \
    libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev
    
#### 2. download source
    wget -O opencv.zip https://github.com/Itseez/opencv/archive/3.4.5.zip
    unzip opencv.zip
#### 3. build opencv
    cd opencv
    mkdir build && cd build
    
    cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D WITH_TBB=OFF \
    -D WITH_IPP=OFF \
    -D WITH_1394=OFF \
    -D BUILD_WITH_DEBUG_INFO=OFF \
    -D BUILD_DOCS=OFF \
    -D INSTALL_C_EXAMPLES=OFF \
    -D INSTALL_PYTHON_EXAMPLES=OFF \
    -D BUILD_EXAMPLES=OFF \
    -D BUILD_TESTS=OFF \
    -D BUILD_PERF_TESTS=OFF \
    -D WITH_QT=OFF \
    -D WITH_GTK=ON \
    -D WITH_OPENGL=OFF \
    -D WITH_V4L=ON  \
    -D WITH_FFMPEG=ON \
    -D WITH_XINE=ON \
    -D WITH_GSTREAMER=ON \
    -D BUILD_NEW_PYTHON_SUPPORT=ON \
    -D PYTHON3_INCLUDE_DIR=/usr/include/python3.6m \
    -D PYTHON3_NUMPY_INCLUDE_DIR=/usr/local/lib/python3.6/dist-packages/numpy/core/include \
    -D PYTHON3_PACKAGES_PATH=/usr/local/lib/python3.6/dist-packages \
    -D PYTHON3_LIBRARY=/usr/lib/arm-linux-gnueabihf/libpython3.6m.so \
    ../
    
    make -j 6
    sudo -H make install
    
#### 4. check installed opencv
    python3
    import cv2
    print(cv2.__version__)
