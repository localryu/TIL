# Around View Detection for UAM

## 1. Motivation

  - UAM needs to detect and avoidance objects like as drones or birds.
  - Detects objects using multiple vision sensors and find the position from the vehicles. Further, since know the obstacles position, collision avoidance can be performed. 

 
## 2. Product

### multi-camera
  1. e-con system : https://www.e-consystems.com/nvidia-cameras/jetson-agx-xavier-cameras/sony-starvis-imx290-synchronized-multi-camera.asp#kit-contents
  2. leopard : https://leopardimaging.com/product/li-xavier-kit-imx577-x/
  
### 360 camera
  1. theta ricoh : http://www.saeki.co.kr/brand/brand2_detail.asp?pno=3512050007&utm_source=theta360.com&utm_medium=referral
      (4k, H264: 3840X1920/29.97fps/56Mbps), ros support
  2. picam 360 : http://store.picam360.com/#!/PICAM360-4KHDR/p/144496447/category=24004796
      (3840X2888/15fps)


## 3. Details of Idea

  ### HW 
  
    sensors
      - plan A : Using 6 or 4 EO sensors
      - plan B : Using 1 360 camera
      
    PC
      - NVIDIA Xavier (can be replaced by TX2)
      - or other pc (Nuc etc.)
      
  ### SW : Using Deep Learning to detect objects.
  
    environment : Linux(ubuntu 18.04) + ROS (melodic)
        
    fisrt, using Lidar for alret object
    second, select roi
    third, detect the object.
        
    DL Net
        - Tensorflow SSD mobileNet -> 8-10fps
        - Tiny yolo -> 45 fps
        - yolo V3 -> 5-6 fps
        - RCNN -> fps
