# Install ubuntu on Dell Alienware laptop

### 1. BIOS Setup
  - Secure boot : disable
  - Advanced-> SATA Operations : from RAID on to AHCI
  
### 2. Ubuntu booting USB
  - press F12, go to boot option
  - boot from ubuntu booting usb
  - press 'e' to edit the menu entry you choose (Install Ubuntu)
  - Find the line which ends with quiet splash and add 'nomodeset'
  - Press Ctrl+X to boot with this parameter
  
### 3. install Nvidia-driver
  - After install ubuntu with 'nomodeset', you should install nvidia driver.
    ~~~
    sudo add-apt-repository ppa:graphics-drivers/ppa
    sudo apt update
    sudo apt-get install nvidia-driver-440
    ~~~
  - reboot pc
