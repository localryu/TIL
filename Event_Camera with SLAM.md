# Event_camera w/ slam

## 1. sources 
  - http://rpg.ifi.uzh.ch/docs/RAL18_VidalRebecq.pdf
  - http://rpg.ifi.uzh.ch/research_dvs.html
  
## 2. Details

 ### strategy
  - event cameras output only little information when the amount of motion is limited.
  - event cameras do not suffer from motion blur and have a very high dynamic range, which enables them ro provide reliable visual information during high-speed motions or in scenes charactorized by high dynamic range.
 
 ### contributions
   a. state estimation pipeline that fuses events, standard frames, and imu. standard frames as an additional sensing modality, improvements to make it usable for real-time applications.
   b. improves the accuracy of state estimation while keeping the computational load tractable.
   c. can be apn onboard and autonomous quadrotor. system is able to fly reliably in challenging situations, such as low-light scenes or fast motions.
   
 ### overview
  1. coordinate frame notation
  2. spatio-temporal widows of event
   :synchronize the spatio-n-compenstated event  of motal windows of events on the timestamps of the statndard frames.o-temproal window of events
  3. synthesis of motion-compensate to a synth spatid event frames
    : collapse every spatio-temporal window of events to a synthetic event frame Ik by drawing each event on the image plane, after correcting for the motion of each event according to its individual timestamp.
  4. feature tracking
    : Fast corner detector ro extract freatures. independent features tracks(KLT tracker)(event, standard)
  5. visual-inerial fusion through nonlinear opiomization
