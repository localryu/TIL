## Install nvidia-driver, CUDA, cuDNN
  ### install nvidia-driver
    sudo apt-get install nvidia-driver-[version] (ex. nvidia-driver-440)

  ### install CUDA (version 10.0/10.1)
  
  #### CUDA version 10.0
    Download CUDA : https://developer.nvidia.com/compute/cuda/10.0/Prod/local_installers/cuda_10.0.130_410.48_linux (env config: Linux, ubuntu, 18.04, runfile)
    
      cd ~/Downloads
      sudo sh cuda_10.0.130_410.48_linux.run
      - Fallow the command-line prompts except install nvidia-driver(make sure press 'n')
      
      gedit ~/.bashrc
      - Add this
          export PATH=/usr/local/cuda-10.0/bin${PATH:+:${PATH}}
          export LD_LIBRARY_PATH=/usr/local/cuda-10.0/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
  
  #### CUDA version 10.1 (recommend)
    Download CUDA :https://developer.nvidia.com/compute/cuda/10.1/Prod/local_installers/cuda-repo-ubuntu1804-10-1-local-10.1.105-418.39_1.0-1_amd64.deb (env config: Linux, ubuntu, 18.04, deb)
    
      cd ~/Downloads
      sudo dpkg -i cuda-repo-ubuntu1804-10-1-local-10.1.105-418.39_1.0-1_amd64.deb
      sudo apt-key add /var/cuda-repo-10-1-local-10.1.105-418.39/7fa2af80.pub
      sudo apt-get update
      sudo apt-get install cuda
      
      gedit ~/.bashrc
      - Add this
          export PATH=/usr/local/cuda-10.1/bin${PATH:+:${PATH}}
          export LD_LIBRARY_PATH=/usr/local/cuda-10.1/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
      
  ### install cuDNN (version 7.5.1)
    - Download cuDNN : https://developer.nvidia.com/cudnn
    
    (CUDA 10.0 version)
      https://developer.nvidia.com/compute/machine-learning/cudnn/secure/v7.5.1/prod/10.0_20190418/cudnn-10.0-linux-x64-v7.5.1.10.tgz
    (CUDA 10.1 version)
      https://developer.nvidia.com/compute/machine-learning/cudnn/secure/v7.5.1/prod/10.1_20190418/cudnn-10.1-linux-x64-v7.5.1.10.tgz
      
      cd ~/Downloads
      sudo tar -xzvf cudnn-*.tgz 
      cd cuda
      sudo cp include/cudnn.h /usr/local/cuda/include
      sudo cp lib64/libcudnn* /usr/local/cuda/lib64
      sudo chmod a+r /usr/local/cuda/lib64/libcudnn*
      
  ### Verify CUDA & CuDNN installation
  ##### CUDA
      nvcc -V
  ##### CuDNN
      cat /usr/local/cuda/include/cudnn.h | grep CUDNN_MAJOR -A 2
