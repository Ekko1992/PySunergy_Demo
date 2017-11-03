# PySunergy_Demo
This is a demo script for Sunergy python wrapper

Please follow these steps, you need to recompile libpysunergy.so on your own computer:
1. clone sunergy repository from github:
git clone https://github.com/VMaxxInc/Sunergy_linux.git

2.go to PySunergy directory:
cd Sunergy_linux/PySunergy

3.make
If you counter issue at this step or while using libpysunergy.so, please reinstall cuda and cudnn of the correspoding version.

4.copy libpysunergy.so to your own working directory

5.Write your own code refering to demo.py

6.Put cfg, data and weights files into the corresponding folders

(7. This demo script detects and crops cars in images, original pictures are in 'pics' folder, cropped cars are in 'result' folder

cfg and data files can be downloaded from: 
https://github.com/pjreddie/darknet

weights file can be downloaded from:
https://pjreddie.com/media/files/yolo.weights
)


