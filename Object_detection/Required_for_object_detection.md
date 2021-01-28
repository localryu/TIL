## Install nvidia-driver, CUDA, cuDNN
  ### install nvidia-driver
    sudo apt-get install nvidia-driver-[version] (ex. nvidia-driver-440)

  ### install CUDA (version 10.1)
    Download CUDA : https://developer.nvidia.com/compute/cuda/10.1/Prod/local_installers/cuda_10.1.105_418.39_linux.run (env config: Linux, ubuntu, 18.04)
    
      cd ~/Downloads
      sudo sh cuda_10.1.105_418.39_linux.run
      - Fallow the command-line prompts except install nvidia-driver(make sure press 'n')
      
      gedit ~/.bashrc
      - Add this
          export PATH=/usr/local/cuda-10.1/bin${PATH:+:${PATH}}
          export LD_LIBRARY_PATH=/usr/local/cuda-10.1/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
      
  ### install cuDNN (version 7.5.1)
    - Download cuDNN : https://developer.nvidia.com/cudnn
      https://developer.nvidia.com/compute/machine-learning/cudnn/secure/v7.5.1/prod/10.1_20190418/cudnn-10.1-linux-x64-v7.5.1.10.tgz
      cd ~/Downloads
      sudo tar -xzvf cudnn-7.5.1*.tgz 
      cd cuda
      sudo cp include/cudnn.h /usr/local/cuda/include
      sudo cp lib64/libcudnn* /usr/local/cuda/lib64
      sudo chmod a+r /usr/local/cuda/lib64/libcudnn*
      
  ##### check cuda & cudnn installed
      cat /usr/local/cuda/include/cudnn.h | grep CUDNN_MAJOR -A 2
