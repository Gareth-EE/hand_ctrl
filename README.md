# remote hand_ctrl
run hand.py

## prepare

1. pip install opencv-python

2. pip install opencv-python mediapipe

3. copy "cv2.abi3.so" from "/PycharmProjects/hand/venv/lib/python3.8/site-packages/cv2" to "/PycharmProjects/hand/venv/lib/python3.8/site-packages"

4. mkdir temp and touch data.txt in "hand" file

5. clone the python files to pycharm

## test

1. remote ssh by vscode to cyberdog

2. cd cyberdog_proto/TieDan

3. python cyberdog_ctrl.py

4. run hand.py in local environment
