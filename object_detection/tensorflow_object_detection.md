## Install CUDA, cuDNN, tensorflow

  ### install CUDA (version 10.2)
    Download CUDA : https://developer.nvidia.com/cuda-downloads
      cd ~/Downloads
      sudo dpkg -i cuda-repo-ubuntu1804-10-0-local-10.0.130-410.48_1.0-1_amd64.deb
      sudo apt-key add /var/cuda-repo-<version>/7fa2af80.pub
      sudo apt-get update
      sudo apt-get install cuda
      
      gedit ~/.bashrc
        Add this
          export PATH=/usr/local/cuda-10.0/bin${PATH:+:${PATH}}
          export LD_LIBRARY_PATH=/usr/local/cuda-10.0/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
      
  ### install cuDNN (version 7.6)
    - Download cuDNN : https://developer.nvidia.com/cudnn
      cd ~/Downloads
      sudo tar -xzvf cudnn-7.6.0-linux-x64-v7.0.tgz 
      cd cuda
      sudo cp include/cudnn.h /usr/local/cuda/include
      sudo cp lib64/libcudnn* /usr/local/cuda/lib64
      sudo chmod a+r /usr/local/cuda/lib64/libcudnn*
      cat /usr/local/cuda/include/cudnn.h | grep CUDNN_MAJOR -A 2
      
  ### install tensorflow (version 1.14)
    sudo pip install tensorflow-gpu==1.14

## Download TensorFlow Object Detection API repository from GitHub
    git clone https://github.com/tensorflow/models.git
    sudo apt-get install protobuf-compiler
    pip install Pillow
    pip install lxml
    pip install Cython
    pip install contextlib2
    pip install jupyter
    pip install matplotlib
    pip install pandas
    pip install opencv-python

    cd ~/tensorflow/models/research
    protoc object_detection/protos/*.proto --python_out=.
    cd ~/tensorflow/models/research
    (export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim:`pwd`/object_detection)
    export PYTHONPATH=$PYTHONPATH:~/tensorflow/models/research/:~/tensorflow/models/research/slim:~/tensorflow/models/research/object_detection/
    
## Making Dataset
  labeling train image using tool (ex. labelimg, openlabel)
    python xml_to_csv.py
  In the generate_tfrecord.py file, modify the label map
    For example,
    
      def class_text_to_int(row_label):
        if row_label == 'nine':
            return 1
        elif row_label == 'ten':
            return 2
        elif row_label == 'jack':
            return 3
        elif row_label == 'queen':
            return 4
        elif row_label == 'king':
            return 5
        elif row_label == 'ace':
            return 6
        else:
           None
           
    python generate_tfrecord.py --csv_input=images/train_labels.csv --image_dir=images/train --output_path=train.record
    python generate_tfrecord.py --csv_input=images/test_labels.csv --image_dir=images/test --output_path=test.record
    
   ### image folder
        images/test/,train/,train.csv,test.csv
    
 ## Config
 
  ### Create labelmap
    item {
      id: 1
      name: 'nine'
    }

    item {
      id: 2
      name: 'ten'
    }

    item {
      id: 3
      name: 'jack'
    }

    item {
      id: 4
      name: 'queen'
    }

    item {
      id: 5
      name: 'king'
    }

    item {
      id: 6
      name: 'ace'
    }
    
   ### training folder
        training/labelmap.pbtxt,(model).config
        
 ## Run the training
 
    PIPELINE_CONFIG_PATH=/home/ryu/tools/models/research/object_detection/training/ssd_mobilenet_v1_coco.config
    MODEL_DIR=/home/ryu/tools/models/research/object_detection/training
    NUM_TRAIN_STEPS=1000000
    SAMPLE_1_OF_N_EVAL_EXAMPLES=1
    
    python model_main.py --pipeline_config_path=/home/ryu/tools/models/research/object_detection/training/ssd_mobilenet_v1_coco.config --model_dir=/home/ryu/tools/models/research/object_detection/training --num_train_steps=1000000 --sample_1_of_n_eval_examples=1 --alsologtostderr

## tensorboard

    tensorboard --logdir=/home/ryu/tools/models/research/object_detection/training
    
## Export the graph

    python export_inference_graph.py --input_type image_tensor --pipeline_config_path training/ssd_mobilenet_v1_coco.config --trained_checkpoint_prefix training/model.ckpt-35487 --output_directory inference_graph_mbzirc


