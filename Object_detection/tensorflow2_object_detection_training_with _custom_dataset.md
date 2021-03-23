# Object detection model training with custom dataset in tensorflow2
    
  ## 1. Environment setup
    cd ~/models/research
    protoc object_detection/protos/*.proto --python_out=.
    cd ~/models
    export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/research:`pwd`/research/slim:`pwd`/research/object_detection
    
  ## 2. Making dataset
   labeling train image using tool (ex. labelimg, openlabel)//
   ~~~
   python xml_to_csv.py
   ~~~
   In the generate_tfrecord.py file, modify the label map  
    For example,  
   ~~~
   def class_text_to_int(row_label):
     if row_label == 'car':
         return 1
     elif row_label == 'people':
         return 2
     elif row_label == 'tree':
         return 3
     else:
        None
   ~~~
   generate_tfrecord
   ~~~
   python3 generate_tfrecord.py --csv_input=images/train_labels.csv --image_dir=images/train --output_path=train.record
   python3 generate_tfrecord.py --csv_input=images/test_labels.csv --image_dir=images/test --output_path=test.record
   ~~~
    
   ### image folder
        images/test/,train/,train.csv,test.csv
        
  ## 3. Config
 
   ### Create labelmap
    item {
      id: 1
      name: 'car'
    }
    item {
      id: 2
      name: 'people'
    }
    item {
      id: 3
      name: 'tree'
    }
    
   ### Modify pipeline.config file for custom training
   For example
   #### num_classes
        3 (number of classes)
   #### fine_tune_checkpoint
        fine_tune_checkpoint: "/home/localryu/models/research/object_detection/ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8/checkpoint/ckpt-0"
   #### fine_tune_checkpoint_type
        fine_tune_checkpoint_type: "detection"
   #### batch_size
        16
   #### num_steps
        100000
   #### train/label_map_path
        label_map_path: "/home/localryu/models/research/object_detection/training/label_map.pbtxt"
   #### train/tf_record_input_reader
        input_path: "/home/localryu/models/research/object_detection/training/train.record"
   #### test/label_map_path
        label_map_path: "/home/localryu/models/research/object_detection/training/label_map.pbtxt"
   #### test/tf_record_input_reader
        input_path: "/home/localryu/models/research/object_detection/training/test.record"
        
   ### training folder
    training/labelmap.pbtxt,(model).config      
  
  ## 4. Run the training
 
    python3 model_main_tf2.py --pipeline_config_path=training/pipeline.config --model_dir=training --alsologtostderr

  ## 5. tensorboard for monitoring

    tensorboard --logdir=training/train
    
   ### If you want to see evaluation results during training,
   run (CUDA_VISIBLE_DEVICES=-1 option makes evaluation will use only cpu)
   ~~~
   CUDA_VISIBLE_DEVICES=-1 python3 model_main_tf2.py --checkpoint_dir training --pipeline_config_path=training/pipeline.config --model_dir=training --alsologtostderr
   ~~~
   tensorboard
   ~~~
   tensorboard --logdir=training/eval
   ~~~

  ## 6. Export the graph

    python3 /home/localryu/models/research/object_detection/exporter_main_v2.py \
    --trained_checkpoint_dir training \
    --output_directory inference_graph \
    --pipeline_config_path training/pipeline.config
    
  ## 7. test custom model
    - python3 test_model.py
    or
    - https://github.com/localryu/tf2_object_detection_ros.git

    
