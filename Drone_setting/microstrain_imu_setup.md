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
  
## launch
  recive data from IMU to ROS
    
   1) first check IMU device connection
    
            ls /dev
       : usually device ID is ttyACM0
       
   2) change the IMU device ID in the launch file
    
            cd catkin_ws/src/microstrain_mips/launch
            vim microstrain.launch
            
         change the device ID
           
            <arg name="port" default="/dev/microstrain" />  -->  <arg name="port" default="/dev/ttyACM0" />
            
   3) Before launch the program, the user must change their permissions to the root.\
      (The microstrain_mips program must be run under root privileges.)
         
            bash
         or
         
            cd catkin_ws/src
            chown -R user microstrain_mips  
            
   4) launch the program
            
            roslaunch microstrain_mips microstrain_mips.launch
            
            
            
        
        
    
  
