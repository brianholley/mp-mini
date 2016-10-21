import os
import subprocess
from os import path

os.chdir("/home/pi/")

source_dir = "/home/pi/.octoprint/timelapse/"

timelapses = [f for f in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, f))]

if len(timelapses) > 0:
    for i in range(0, len(timelapses)):
        print "Uploading", timelapses[i]
        source_file = os.path.join(source_dir, timelapses[i])    
        subprocess.call(['python', 'upload.py', source_file, '/3DPrints/'])
        subprocess.call(['mv', source_file, os.path.join(source_dir, 'uploaded/')])
else:
    print "Nothing to upload"
