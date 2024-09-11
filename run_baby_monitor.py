import subprocess

subprocess.call(['bash /home/pi/babymonitoringsystem/start_baby_monitor.sh'],shell = True)
subprocess.call(['ngrok http 5600'],shell = True)
