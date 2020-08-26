## 1. size 변경
    v4l2-ctl --list-formats-ext : video 마다 지원하는 pixel format & size 정보 확인

## 2. pixel format 변경
    <param name="pixel_format" value="yuyv" />  ->  <param name="pixel_format" value="mjpeg" />

## 3. auto_focus, autoexposure, auto white balance
    - In usb_cam_node.cpp
    node_.param("autofocus", autofocus_, false);
    node_.param("autoexposure", autoexposure_, false);
    node_.param("auto_white_balance", auto_white_balance_, false);
