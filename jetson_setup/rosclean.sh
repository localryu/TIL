#! /bin/bash
sudo jetson_clocks
sudo nvpmodel -m 0
x=1
while [ $x -le 5 ]
do
  rm -rf /home/mbzirc/.ros/log
  x=$(( $x + 1 ))
  echo "rosclean $x times"
  sleep 300
done
