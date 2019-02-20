# soon to be self-driving toy car

## notes to myself

### connecting from computer to client using xpra

1. on Raspberry after cd to the right dir: `xpra start --start='python2 vidcap.py' --bind-tcp=0.0.0.0:10000`
2. on Computer `xpra attach tcp:<raspberryIP>:10000`

In general:

* `xpra list` to see all current sessions or get the DISPLAY number
* To end: Ctrl+c in the Terminal, don't just close the window. Else you need to `xpra stop :DISPLAY` before `xpra start ...` again

To install xrpa `sudo apt install xpra`. The version we use is 0.15.8 on the computer and 0.17.? on the Raspberry. Don't build from Source and try to get a newer version - it failed.

## links, other projects

* interesting code with socket for video transmission https://stackoverflow.com/questions/30988033/sending-live-video-frame-over-network-in-python-opencv
* AutoRCCar the red car seen on Youtube code https://github.com/hamuchiwa/AutoRCCar
