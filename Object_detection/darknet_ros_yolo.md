## 1. make dataset list file
  run write_train_txt.py\
  make train.txt file

      (data/folder/jpeg, labels)
      path = "/home/ryu/catkin_ws/src/darknet_ros/darknet/data/cam1_label/"
      save_path = "/home/ryu/catkin_ws/src/darknet_ros/darknet/data/"


## 2. make files
  darknet/cfg/mission2.data
  
      --
      classes= 5
      train  = /home/ryu/catkin_ws/src/darknet_ros/darknet/data/train.txt
      valid  = /home/ryu/catkin_ws/src/darknet_ros/darknet/data/test.txt
      names = data/mission2.names
      backup = /home/ryu/catkin_ws/src/darknet_ros/darknet/backup
      --

  darknet/data/mission2.names
      
      --
      red
      green
      blue
      orange
      plate
      --

  darknet/cfg/yolov3_mission2.cfg
  
      --
      filter = 30 (in convolutional, activation=linear part)
      classes = 5 
      --

## 3. training

      ./darknet detector train cfg/mission2.data cfg/yolov3_mission2.cfg darknet53.conv.74 -gpus 0,1

## 4. modify darknet_ros cfg file
 
  yolo_v3.launch
  
      --
      <arg name="network_param_file"         default="$(find darknet_ros)/config/yolov3_bricks.yaml"/>
      <arg name="image" default="camera/image_raw" />
      --
      
  darknet_ros/config/yolov3_bricks.yaml

      --
      yolo_model:

        config_file:
          name: yolov3_bricks.cfg
        weight_file:
          name: yolov3_bricks.backup
        threshold:
          value: 0.6
        detection_classes:
          names:
            - red
            - green
            - blue
            - orange
            - plate
      --
      
## 5. move files

      cp darket/cfg/yolov3_bricks.cfg darknet_ros/yolo_network_config/cfg/
      cp darket/backup/yolov3_bricks.backup darknet_ros/yolo_network_config/weights/

## 6.run

      roslaunch darknet_ros yolo_v3.launch
