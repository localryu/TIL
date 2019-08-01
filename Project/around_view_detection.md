# Around View Detection for UAM

## 1. Motivation

  - UAM needs to detect and avoidance objects like as drones or birds.
  - Detects objects using multiple vision sensors and find the position from the vehicles. Further, since know the obstacles position, collision avoidance can be performed. 

 
## 2. Product

  1. e-con system : https://www.e-consystems.com/nvidia-cameras/jetson-agx-xavier-cameras/sony-starvis-imx290-synchronized-multi-camera.asp#kit-contents
  2. leopard : https://leopardimaging.com/product/li-xavier-kit-imx577-x/
  


## 3. Details of Idea

  ### HW 
  
    sensors
      - Using 6 or 4 EO sensors
      
    PC
      - NVIDIA Xavier (can be replaced by TX2)
      - or other pc (Nuc etc.)
      
  ### SW : Using Deep Learning to detect objects.
  
    environment : Linux(ubuntu 18.04) + ROS (melodic)
        
    DL Net
        - Tensorflow SSD mobileNet -> 8-10fps
        - Tiny yolo -> 45 fps
        - yolo V3 -> 5-6 fps
        - RCNN -> fps
