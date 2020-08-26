# ROS ip configuration for communication

## Host PC

  ifconfig >> sereach the ip(A)
  
    vim ~/.bashrc
    
  add below contents
    
      # Configure ROS Network
      export ROS_LOCALIP=xxx.xxx.xxx.xxx(A)
      export ROS_MASTER_URI=http://${ROS_LOCALIP}:11311
      
    source ~/.bashrc
    
## Guest PC
  
  ifconfig >> serecah the ip(B)
  
    vim ~/.bashrc
    
  add below contents

      # Set ROS Network
      export ROS_MASTER_URI=http://xxx.xxx.xxx.xxx(A):11311
      export ROS_HOSTNAME=xxx.xxx.xxx.xxx(B)
  
    source ~/.bashrc


## useage

### guest PC

    ssh HOSTPC_NAME@xxx.xxx.xxx.xxx(A)
    roscore
