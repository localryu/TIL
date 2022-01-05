# auto ROS start after booting

 ref : https://injae-kim.github.io/robot_operating_system/2020/04/25/ros-automatically-execute-program-on-booting.html

## 1. 

### a. cd /etx/systemd/system/
### b. touch ros_init.service
~~~
# /etc/systemd/system/ros_init.service
[Unit]
Description=Ros Init Daemon

[Service]
Type=simple
ExecStart=/home/ryu/start.sh	# 부팅 시 실행하고 싶은 스크립트의 경로

[Install]
WantedBy=multi-user.t
~~~

#### command options 
~~~
# service 파일의 다양한 옵션들 예시
[Unit]
Description=Ros Init Daemon 	# 추후 서비스 상태 확인 시 서비스 설명란에 출력됨
Requires=*.service 	# 이 서비스를 실행하기 위해 필요한 서비스 의존성
Before=*.service 	# 이 서비스 실행 후에 실행되어야 할 서비스
After=*.service 	# 이 서비스 실행 전에 실행되어야 할 서비스

[Service]
Type=simple # simple, forking, oneshot, notify, dbus 등 프로그램의 타입 명시를 원하는 경우
ExecStart=/home/sheco/injae.sh	# 부팅 시 실행하고 싶은 스크립트의 경로

[Install]
WantedBy=multi-user.target
~~~

## 2. make shell script file (/home/ryu/start.sh)
~~~
#! /bin/bash

source /opt/ros/melodic/setup.bash
source home/ryu/catkin_ws/devel/setup.bash

export ROS_MASTER_URI=http://127.0.0.1:11311
export ROS_HOSTNAME=127.0.0.1

sleep 3
cd /home/ryu/catkin_ws
roscore &
sleep 3

roslaunch vision_node vision_node.launch
~~~

## 3. update service file and restart service
~~~
systemctl daemon-reload
systemctl enable ros_init.service	# 부팅시 이 서비스를 자동시작 함
systemctl start ros_init.service	# 서비스 시작
~~~

#### service command options
~~~
systemctl status service_name.service	# 서비스 상태 확인
systemctl start service_name.service	# 서비스 시작
systemctl restart service_name.service	# 서비스 재시작
systemctl stop service_name.service		# 서비스 중지
systemctl enable service_name.service	# 부팅시 이 서비스 자동 실행
systemctl disable service_name.service	# 부팅시 이 서비스 자동 실행 해제
systemctl list-units --type=service		# 실행중인 서비스 목록 확인
~~~




