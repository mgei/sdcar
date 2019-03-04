# soon to be self-driving toy car

The goal of this project is to build an self-driving toy car. We plan to apply an end-to-end approach, also known as behavioral cloning. The car should be able to steer autonomously in an environment similar to the one it would be trained on. We plan to deploy the model on the edge a Movidius compute stick.

The current state of the work is this project is:

- [x] assembling the car
- [x] capable of driving with keyboard from a remote PC connected with xpra or ssh -X
- [x] capable of recording human driving data (images + sensor state especially steering) needed for training a neural network model
- [x] first tests of applying a neural network
- [ ] implement functionality to drive car given an input
- [ ] deploying the model on the car and have it drive itself
- [ ] test and improve

![](img/079A9654.JPG)

## Raspberry

This is what we use to control the car.

*drive.py* let's you control the car with the keyboard. *drive_rec.py* additionally records the drive, i.e. saves each frame as an image and also the state of the controls. This will be the imput for a neural network model.

### modules

Contains the Car class that is the main part of the controls. It's job is to not sent too many inputs to the motor controller, e.g. if it's already going forward to instruct to go forward again. Only at key release the relevant motor (drive or steering) is stopped.

### various

All code tests that are no longer used were moved to the *testing* directory. We were experimenting with getting the keyboard input be various means: sys approach, cv2.waitKey(), and pygame (of which various approaches). Pygame turned out to be the most efficient for keyboard control as multiple keys pressed simultaniously can be recognized.

Also we did tests with the webcam input and the potentiometer that is to be used for limiting the steering. For the latter, *gpiozero* was used first but replaced with more basic readout due to compability. 

## Computer

Training. We use a GPU but the models we plan to use are fairly simple and should also be training on CPU. 

## notes to myself

### connecting from computer to client using xpra

1. on Raspberry after cd to the right dir: `xpra start --start='python2 vidcap.py' --bind-tcp=0.0.0.0:10000`
2. on Computer `xpra attach tcp:<raspberryIP>:10000`

In general:

* `xpra list` to see all current sessions or get the DISPLAY number
* To end: Ctrl+c in the Terminal, don't just close the window. Else you need to `xpra stop :DISPLAY` before `xpra start ...` again

To install xrpa `sudo apt install xpra`. The version we use is 0.15.8 on the computer and 0.17.? on the Raspberry. Don't build from Source and try to get a newer version - it failed.

## links, other projects

* interesting code with socket for video transmission (we don't use that for the moment) https://stackoverflow.com/questions/30988033/sending-live-video-frame-over-network-in-python-opencv
* AutoRCCar the red car seen on Youtube code https://github.com/hamuchiwa/AutoRCCar
* for the potentiometer readout with gpiozero and MCP3008 (we no longer use that due to incompatibility with other use of the GPIO pins): https://github.com/pediehl/raspberry-pi-mcp3008
* Potentiometer readout MCP3008 https://electronicshobbyists.com/raspberry-pi-analog-sensing-mcp3008-raspberry-pi-interfacing/
* We use a L293D motor controller, there's a Python libray that we used first for testing https://github.com/jmsv/l293d
* What we use to controll the motors with L293D PWM https://www.instructables.com/id/DC-Motor-Control-With-Raspberry-Pi-and-L293D/
* OpenCV webcam video to Pygame screen https://gist.github.com/radames/1e7c794842755683162b
* Ultrasonic Sensor https://tutorials-raspberrypi.com/raspberry-pi-ultrasonic-sensor-hc-sr04/
* Use of Intel's OpenVINO and  Movidius Neural Compute Stick on a Raspberry https://www.youtube.com/watch?v=PNmH_ugW6Zw and https://software.intel.com/en-us/articles/OpenVINO-Install-RaspberryPI

## inspiring papers

* Bojarski, Mariusz, et al. "End to end learning for self-driving cars." arXiv preprint arXiv:1604.07316 (2016). https://arxiv.org/abs/1604.07316
* Intelligent Autonomous Driving, conference paper found here: http://folk.ntnu.no/skoge/prost/proceedings/ICSTCC-2018-Sinaia/ICSTCC2018/papers/0093.pdf
