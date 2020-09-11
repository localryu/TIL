## Full backup of Jetson xavier

### Creating the backup image file

#### On Host pc
    - enter the jetson xavier through ssh
    ssh jetsonUser@JetsonIP
    
    - stop the filesystem and force it to read only access
    sudo -i 
    echo u > /proc/sysrq-trigger
    
    - transferring an image of full internal memory hard drive over ssh to host pc
    dd if=/dev/mmcblk0p1 | ssh hostuser@hostpcIP dd of=/home/ryu/nx/image.raw
    
    - convert the .raw image to a .img file
    cd /home/ryu/nvidia/nvidia_sdk/JetPack_4.4_Linux_P2888/Linux_for_Tegra/bootloader/
    sudo ./mksparse -v --fillpattern=0 /home/ryu/nx/image.raw /home/ryu/nx/system.img
    
### Restoring the image file

#### On Host pc
    - boot the jetson on resore mode and connect jetsion with usb to the hostpc
    cd /home/ryu/nvidia/nvidia_sdk/JetPack_4.4_Linux_P2888/Linux_for_Tegra/bootloader/
    
    - copy bootloader folder
    (check the name 'jetson-xavier')
    sudo ./flash.sh -r jetson-xavier mmcblk0p1
    
    
