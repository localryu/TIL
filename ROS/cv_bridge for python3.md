# Setup cv_bridge for python3 version

## Dependencies
  Install the python build tools  
   ~~~
   sudo apt-get install python3-pip python-catkin-tools python3-dev python3-numpy
   sudo pip3 install rospkg catkin_pkg
   ~~~
## Workspace
#### Create workspace for compile cv_bridge
  Create a separate workspace to compile the cv_bridge package.  
  To avoid angy future problems eith catkin_make and config catkin to use python3 when building packages.  
  ~~~
  mkdir -p ~/cvbridge_build_ws/src && cd ~/cvbridge_build_ws/src
  ~~~
#### Clone the open_vision repository
  download the melodic branch.  
  ~~~
  git clone -b melodic https://github.com/ros-perception/vision_opencv.git
  ~~~
#### Compilation
  before compile, check the python 3 version and path.  
  ~~~
  cd ~/cvbridge_build_ws
  catkin config -DPYTHON_EXECUTABLE=/usr/bin/python3 -DPYTHON_INCLUDE_DIR=/usr/include/python3.6m -DPYTHON_LIBRARY=/usr/lib/x86_64-linux-gnu/libpython3.6m.so  
  catkin config --install
  catkin_make
  ~~~
  After build, add the below command in the ~/.bashrc file.  
  ~~~
  vim ~/.bashrc
  source ~/cvbridge_build_ws/install/setup.bash --extend
  ~~~
