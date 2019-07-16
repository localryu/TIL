# Event-based Vision meets Deep Learning on Steering Prediction for Self-driving Cars

## source
  - http://rpg.ifi.uzh.ch/docs/CVPR18_Maqueda.pdf
  - https://youtu.be/_r_bsjkJTHA
  
## details

### abstract
  - deep neurak network approach that unlocks the potential of event cameras on a challenging motion-estimation task
  - why event cameras allow robust steering prediction even in case where traditional cameras fails.
  - advantages of leveraging transfer learning from readitional to event based vision.
  
### contributions
  - Show why event camera is better suited to motion estimation tasks than a traditional camera.
  - Show that it is possible to leverage reansfer learning from pre-trained convolutional networks on classification tasks, even if the networks were trained on frames collected by traditional cameras.
  - Prove that this methodology is outperforming state-of-the-art systems on a publicly available dataset.
  
### relatewited work
  - first attempt to learn a visuomotor policy (with ALVINN) - shallow network was used to predict actions directly from images. -> it onlt succeeded in simple scenarios.
  - NVIDIA used a CNN to learn a driving policy from video frames.->able to drive a car in basic scenarios.
  - leverage large-scale driving video datasets and to do transfer learning to generate more robust policies.->showed good performance but uas limited to only a set of discreate actions and was susceptible to failures in undemonstrated regions of the policy space.
  
### describes
