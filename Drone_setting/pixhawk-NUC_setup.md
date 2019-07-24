# Pixhawk - NUC setting

## environment
    NUC : Ubuntu 18.0, ROS melodic
    Pixhawk : 1.8.2v
    HW : FTDI serial-to-USB Cable
  
## install Mavros in NUC
    sudo apt-get update
    sudo apt-get install ros-melodic-mavros ros-melodic-mavros-extras
    cd ~/catkin_ws
    catkin_make
    source devel/setup.bash
    
## connect serial-to-USB Cable
  ![pinmap](./img/pinmap.png)
    ** MCU_TX => board RX,MCU_RX => board TX 
  
## Pixhawk configuration
   lauch Qgroundcontrol
   
    Parameter -> SYS_COMPANION -> select Companion Link(921600 baudrate 8N1)
   reboot the vehicle
   
## Test
    ## permission problem
    sudo chmod 777 /dev/ttyUSB0
    
    ## launch programs
    roscore
    rosrun mavros mavros_node _fcu_url:="/dev/ttyUSB0:921600"
    
    ## rostopic check
    rostopic /mavros/state -c
    rostopic /mavros/imu/data -c
    
    

