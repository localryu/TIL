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
    wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/3.4.0.zip

    unzip opencv.zip
    unzip opencv_contrib.zip

#### 3. build opencv
    cd opencv
    mkdir build && cd build
    
    
   ##### Desktop (arm-linux)
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
    sudo sh -c 'echo '/usr/local/lib' > /etc/ld.so.conf.d/opencv.conf'
    sudo ldconfig
    
   ##### Desktop (x86_64-linux)    
    cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D WITH_TBB=OFF \
    -D WITH_IPP=OFF \
    -D WITH_1394=OFF \
    -D BUILD_WITH_DEBUG_INFO=OFF \
    -D BUILD_DOCS=OFF \
    -D INSTALL_C_EXAMPLES=ON \
    -D INSTALL_PYTHON_EXAMPLES=ON \
    -D BUILD_EXAMPLES=OFF \
    -D BUILD_TESTS=OFF \
    -D BUILD_PERF_TESTS=OFF \
    -D WITH_QT=OFF \
    -D WITH_GTK=ON \
    -D WITH_OPENGL=ON \
    -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib-3.4.0/modules \
    -D WITH_V4L=ON  \
    -D WITH_FFMPEG=ON \
    -D WITH_XINE=ON \
    -D BUILD_NEW_PYTHON_SUPPORT=ON \
    -D PYTHON2_INCLUDE_DIR=/usr/include/python2.7 \
    -D PYTHON2_NUMPY_INCLUDE_DIRS=/usr/lib/python2.7/dist-packages/numpy/core/include/ \
    -D PYTHON2_PACKAGES_PATH=/usr/lib/python2.7/dist-packages \
    -D PYTHON2_LIBRARY=/usr/lib/x86_64-linux-gnu/libpython2.7.so \
    -D PYTHON3_INCLUDE_DIR=/usr/include/python3.6m \
    -D PYTHON3_NUMPY_INCLUDE_DIRS=/usr/lib/python3/dist-packages/numpy/core/include/  \
    -D PYTHON3_PACKAGES_PATH=/usr/lib/python3/dist-packages \
    -D PYTHON3_LIBRARY=/usr/lib/x86_64-linux-gnu/libpython3.6m.so \
    ../
    
    make -j 6
    sudo -H make install
    sudo sh -c 'echo '/usr/local/lib' > /etc/ld.so.conf.d/opencv.conf'
    sudo ldconfig
    
   ##### Jetsion
    cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D WITH_TBB=OFF \
    -D WITH_IPP=OFF \
    -D WITH_1394=OFF \
    -D BUILD_WITH_DEBUG_INFO=OFF \
    -D BUILD_DOCS=OFF \
    -D INSTALL_C_EXAMPLES=ON \
    -D INSTALL_PYTHON_EXAMPLES=ON \
    -D BUILD_EXAMPLES=OFF \
    -D BUILD_TESTS=OFF \
    -D BUILD_PERF_TESTS=OFF \
    -D WITH_QT=OFF \
    -D WITH_GTK=ON \
    -D WITH_OPENGL=ON \
    -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib-3.4.0/modules \
    -D WITH_V4L=ON  \
    -D WITH_FFMPEG=ON \
    -D WITH_XINE=ON \
    -D BUILD_NEW_PYTHON_SUPPORT=ON \
    -D PYTHON2_INCLUDE_DIR=/usr/include/python2.7 \
    -D PYTHON2_NUMPY_INCLUDE_DIRS=/usr/lib/python2.7/dist-packages/numpy/core/include/ \
    -D PYTHON2_PACKAGES_PATH=/usr/lib/python2.7/dist-packages \
    -D PYTHON2_LIBRARY=/usr/lib/aarch64-linux-gnu/libpython2.7.so \
    -D PYTHON3_INCLUDE_DIR=/usr/include/python3.6m \
    -D PYTHON3_NUMPY_INCLUDE_DIRS=/usr/lib/python3/dist-packages/numpy/core/include/  \
    -D PYTHON3_PACKAGES_PATH=/usr/lib/python3/dist-packages \
    -D PYTHON3_LIBRARY=/usr/lib/aarch64-linux-gnu/libpython3.6m.so \
    ../
    
    make -j 6
    sudo -H make install
    sudo sh -c 'echo '/usr/local/lib' > /etc/ld.so.conf.d/opencv.conf'
    sudo ldconfig
    
#### 4. check installed opencv
    python3
    import cv2
    print(cv2.__version__)
