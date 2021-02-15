# Build AirSim on Linux
 (reference : https://microsoft.github.io/AirSim/build_linux/)
 
#### Environment
    - Ubuntu 18.04 LTS

### Build Unreal Engine
    git clone -b 4.24 https://github.com/EpicGames/UnrealEngine.git
    cd UnrealEngine
    ./Setup.sh
    ./GenerateProjectFiles.sh
    make
    
### Build AirSim
    git clone https://github.com/Microsoft/AirSim.git
    cd AirSim
    ./setup.sh
    ./build.sh
    
## ROS set up
### install Airsim and ros package
    https://github.com/microsoft/AirSim/blob/master/docs/airsim_ros_pkgs.md

### ERROR
  fatal error: filesystem: No such file or directory
   - Because of gcc version (lower than 8)
   - upate gcc version

#### - Update gcc version 
    sudo add-apt-repository ppa:ubuntu-toolchain-r/test
    sudo apt-get update
    sudo apt-get install gcc-8 g++-8
    gcc-8 --version
#### - Make gcc8 to default version
    sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-7 700 --slave /usr/bin/g++ g++ /usr/bin/g++-7
    sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-8 800 --slave /usr/bin/g++ g++ /usr/bin/g++-8
