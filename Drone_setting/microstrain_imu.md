# microstrain IMU ros setup

## environment
    IMU : microstrain_3dm_gx5_45
    OS  : Ubuntu 18.04 + ROS melodic
  
## installation
  1. Forked from microstarin wiki page. (http://wiki.ros.org/microstrain_3dm_gx5_45#Build_Instructions)
    
    cd catkin_ws/src
    git clone https://github.com/ros-drivers/microstrain_mips.git
    cd ..
    rosdep update
    catkin_make
    source devel/setup.bash
  
  2. validate if the package is well installed
      
    rospack profile 
   : should have microstrain_mips string
  
  3. recive data from IMU to ROS
    
    1) first check IMU device connection
    
        ls /dev
       : usually device ID is ttyACM0
       
    2) change device ID in launch file
    
        cd catkin_ws/src/microstrain_mips/launch
        vim microstrain.launch
        
        
    
  
