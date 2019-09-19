# camera setup

## 1. Use nvidia SDK, flashing xavier.

## 2. Update kernel to use multi camera drive.

 ### setting up the environment(host pc)
 #### settup the environment
    mkdir top_dir/kernel_out -p
    
    export TOP_DIR=/home/ryu/top_dir \
    export RELEASE_PACK_DIR=$TOP_DIR/e-CAM20_CUXVR_JETSON_XAVIER_L4T32.1_09-JULY-2019_R01 \
    export L4T_DIR=$TOP_DIR/Linux_for_Tegra \
    export LDK_ROOTFS_DIR=$TOP_DIR/Linux_for_Tegra/rootfs \
    export ARCH=arm64 \
    export CROSS_COMPILE=aarch64-linux-gnu- \
    export CROSS32CC=arm-linux-gnueabihf-gcc \
    export TEGRA_KERNEL_OUT=$TOP_DIR/kernel_out \
    export KERNEL_PATH=$TOP_DIR/kernel_out
 
 #### downloading the requirements
    tar -xf ~/home/ryu/gcc-linaro-6.4.1-2017.08-x86_64_aarch64-linux-gnu.tar.xz
    export PATH=/home/ryu/gcc-linaro-6.4.1-2017.08-x86_64_aarch64-linux-gnu/bin:${PATH}
    cp $HOME/Downloads/JAX-TX2-Jetson_Linux_R32.1.0_aarch64.tbz2 $TOP_DIR
    cp $HOME/Downloads/JAX-TX2-Tegra_Linux_Sample-Root-Filesystem_R32.1.0_aarch64.tbz2 $TOP_DIR
    
 #### Extracting and Preparing L4T
    cd $TOP_DIR
    sudo tar -I lbzip2 -xpf JAX-TX2-Jetson_Linux_R32.1.0_aarch64.tbz2
    
    cd $LDK_ROOTFS_DIR
    sudo tar -I lbzip2 -xpf $TOP_DIR/JAX-TX2-Tegra_Linux_Sample-Root-Filesystem_R32.1.0_aarch64.tbz2
    
    (sudo apt-get install lbzip2)
    
    cd $L4T_DIR
    sudo ./apply_binaries.sh
    
 #### Extracting the Release Package
    cd $TOP_DIR
    
    tar -xaf e-CAM20_CUXVR_JETSON_XAVIER_L4T32.1_09-JULY-2019_R01.tar.gz
    
 ### Upgrade Procedure
 
 #### Upgrading Kernel Supplements(xavier)
    mkdir top_dir/kernel_out -p
    
    export TOP_DIR=/home/ryu/top_dir \
    export RELEASE_PACK_DIR=$TOP_DIR/e-CAM20_CUXVR_JETSON_XAVIER_L4T32.1_09-JULY-2019_R01
    cp e-CAM20_CUXVR_JETSON_XAVIER_L4T32.1_09-JULY-2019_R01.tar.gz $TOP_DIR/
    cd $TOP_DIR
    tar -xaf e-CAM20_CUXVR_JETSON_XAVIER_L4T32.1_09-JULY-2019_R01.tar.gz
    
    sudo tar xjpmf $RELEASE_PACK_DIR/Kernel/Binaries/kernel_supplements.tar.bz2 -C /
    sudo cp $RELEASE_PACK_DIR/Rootfs/camera_overrides.isp $LDK_ROOTFS_DIR/var/nvidia/nvcam/settings/ -f
    sudo sudo chmod 664 $LDK_ROOTFS_DIR/var/nvidia/nvcam/settings/camera_overrides.isp
    sudo chown root:root $LDK_ROOTFS_DIR/var/nvidia/nvcam/settings/camera_overrides.isp
    sudo cp $RELEASE_PACK_DIR/Rootfs/max-isp-vi-clks.sh $LDK_ROOTFS_DIR/home/max-isp-vi-clks.sh -f
    sudo chmod +x $LDK_ROOTFS_DIR/home/max-isp-vi-clks.sh
    
 #### Upgrading kernel image and dtb file(host pc)
    sudo cp $RELEASE_PACK_DIR/Kernel/Binaries/tegra194-p2888-0001-p2822-0000-camera-4lane-eimx290.dtb
    sudo cp $RELEASE_PACK_DIR/Kernel/Binaries/Image $L4T_DIR/kernel/Image -f
    cd $L4T_DIR
    ls ./bootloader/system.img
    sudo ./flash.sh --no-flash jetson-xavier mmcblk0p1
    
    (xavier : recovery mode)
    
    lsusb <- chk
    
    sudo ./flash.sh -r -k kernel jetson-xavier mmcblk0p1
     >> the kernel has been flashed successfully
     
    sudo ./flash.sh -r -k kernel-dtb jetson-xavier mmcblk0p1
     >> the kernel-dtb has been flashed successfully.
    
