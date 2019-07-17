# Around View Detection

## 1. Motivation
  - UAM needs to detect and avoidance objects like as drones or birds.
  - Detects objects using multiple vision sensors and locates them in their vehicles. Further, since the position of the obstacle is known, collision avoidance can be performed. 

 
## 2. Product
  1. e-con system : https://www.e-consystems.com/blog/camera/build-your-dream-ai-applications-with-e-cam130_cuxvr-on-the-nvidia-jetson-agx-xavier/
  2. leopard : https://leopardimaging.com/product/li-xavier-kit-imx577-x/


## 3. Details of Idea
  ### HW 
    sensors
      - Using 6 eo sensors (the product)
    PC
      - NVIDIA Xavier (can subtitude to X2)
      - or other pc (Nuc etc.)
      
  ### SW : Using Deep Learning to detect birds, UAMs or other objects.
    Linux(ubuntu 18.04) + ROS (melodic)
        - For ease of development
    DL Net
        - Tensorflow SSD mobileNet -> video :  fps / real-time :  fps
        - Tiny yolo -> video :  fps / real-time :  fps
        - yolo V3 -> video : 5-6 fps / real-time : fps
        - RCNN -> video :  fps / real-time :  fps
