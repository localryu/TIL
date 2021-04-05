#!/bin/bash

## Bash script for setting up ROS Melodic (with Gazebo 9) development environment for PX4 on Ubuntu LTS (18.04). 
## It installs the common dependencies for all targets (including Qt Creator)
##
## Installs:
## - Common dependencies libraries and tools as defined in `ubuntu_sim_common_deps.sh`
## - ROS Melodic (including Gazebo9)
## - MAVROS

if [[ $(lsb_release -sc) == *"xenial"* ]]; then
  echo "OS version detected as $(lsb_release -sc) (16.04)."
  echo "ROS Melodic requires at least Ubuntu 18.04."
  echo "Exiting ...."
  return 1;
fi

echo "Downloading dependent script 'ubuntu_sim_common_deps.sh'"
# Source the ubuntu_sim_common_deps.sh script directly from github
common_deps=$(wget https://raw.githubusercontent.com/PX4/Devguide/master/build_scripts/ubuntu_sim_common_deps.sh -O -)
wget_return_code=$?
# If there was an error downloading the dependent script, we must warn the user and exit at this point.
if [[ $wget_return_code -ne 0 ]]; then echo "Error downloading 'ubuntu_sim_common_deps.sh'. Sorry but I cannot proceed further :("; exit 1; fi
# Otherwise source the downloaded script.
. <(echo "${common_deps}")

# # ROS Melodic
# ## Gazebo simulator dependencies
# sudo apt install protobuf-compiler libeigen3-dev libopencv-dev -y

# ## ROS Gazebo: http://wiki.ros.org/melodic/Installation/Ubuntu
# ## Setup keys
# sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
# sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
# ## For keyserver connection problems substitute hkp://pgp.mit.edu:80 or hkp://keyserver.ubuntu.com:80 above.
# sudo apt update
# ## Get ROS/Gazebo
# sudo apt install ros-melodic-desktop-full -y
# ## Initialize rosdep
# sudo rosdep init
# rosdep update
# ## Setup environment variables
# tagsource="
# # Set ROS Melodic"
# echo "$tagsource" >> ~/.bashrc
# rossource="source /opt/ros/melodic/setup.bash"
# if grep -Fxq "$rossource" ~/.bashrc; then echo ROS setup.bash already in .bashrc;
# else echo "$rossource" >> ~/.bashrc; fi
# eval $rossource

## Install rosinstall and other dependencies
sudo apt install python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential -y


# MAVROS: https://dev.px4.io/en/ros/mavros_installation.html
## Install dependencies
sudo apt install python-catkin-tools python-rosinstall-generator -y

## Create catkin workspace
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws
catkin init
wstool init src


# Install MAVROS
sudo apt install ros-melodic-mavros ros-melodic-mavros-extras -y

#Install geographiclib
sudo apt install geographiclib -y
echo "Downloading dependent script 'install_geographiclib_datasets.sh'"
# Source the install_geographiclib_datasets.sh script directly from github
install_geo=$(wget https://raw.githubusercontent.com/mavlink/mavros/master/mavros/scripts/install_geographiclib_datasets.sh -O -)
wget_return_code=$?
# If there was an error downloading the dependent script, we must warn the user and exit at this point.
if [[ $wget_return_code -ne 0 ]]; then echo "Error downloading 'install_geographiclib_datasets.sh'. Sorry but I cannot proceed further :("; exit 1; fi
# Otherwise source the downloaded script.
sudo bash -c "$install_geo"

## Build!
catkin build
## Re-source environment to reflect new packages/build environment
catkin_ws_source="source ~/catkin_ws/devel/setup.bash"
if grep -Fxq "$catkin_ws_source" ~/.bashrc; then echo ROS catkin_ws setup.bash already in .bashrc; 
else echo "$catkin_ws_source" >> ~/.bashrc; fi
eval $catkin_ws_source

# Get PX4-Autopilot
sudo apt install git-all -y
cd
git clone https://github.com/PX4/PX4-Autopilot.git --recursive
bash ~/PX4-Autopilot/Tools/setup/ubuntu.sh

# Setup sitl_gazebo environment variables
sitl_gazebo_source="
# Set sitl_gazebo path
source ~/PX4-Autopilot/Tools/setup_gazebo.bash ~/PX4-Autopilot ~/PX4-Autopilot/build/px4_sitl_default
export ROS_PACKAGE_PATH=~/PX4-Autopilot:~/PX4-Autopilot/Tools/sitl_gazebo${ROS_PACKAGE_PATH:+:${ROS_PACKAGE_PATH}}"
echo "$sitl_gazebo_source" >> ~/.bashrc
sed -i '23,25s+echo+#echo+g' ~/PX4-Autopilot/Tools/setup_gazebo.bash

# Set Alias
echo "
# Set ROS Network
export ROS_MASTER_URI=http://localhost:11311
export ROS_HOSTNAME=localhost
export ROS_IP=127.0.0.1

# set ROS Alias Command
alias cw='cd ~/catkin_ws'
alias cs='cd ~/catkin_ws/src'
alias cm='cd ~/catkin_ws && catkin_make'
alias cb='cd ~/catkin_ws && catkin build'

# Set User Alias
alias eb='gedit ~/.bashrc' 
alias sb='source ~/.bashrc' 

# Set PX4 Alias
alias qgc='cd && ./QGroundControl.AppImage'
alias px4_sitl='roslaunch px4 mavros_posix_sitl.launch'
" >> ~/.bashrc

source ~/.bashrc

sudo usermod -a -G dialout $USER
sudo apt remove modemmanager -y
sudo apt install gstreamer1.0-plugins-bad gstreamer1.0-libav gstreamer1.0-gl -y
sudo apt --reinstall install libignition-math4 libignition-math4-dev -y
sudo apt upgrade -y

cd
wget https://github.com/mavlink/qgroundcontrol/releases/download/v4.0.9/QGroundControl.AppImage
chmod +x ./QGroundControl.AppImage

./QGroundControl.AppImage&

cd ~/PX4-Autopilot && make px4_sitl_default gazebo


# roslaunch px4 mavros_posix_sitl.launch
