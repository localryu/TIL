    # Object detection model training with custom dataset in tensorflow2
    
    ## Environment setup
    ~~~
    cd ~/models/research
    protoc object_detection/protos/*.proto --python_out=.
    cd ~/models
    export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/research:`pwd`/research/slim:`pwd`/research/object_detection
    ~~~
