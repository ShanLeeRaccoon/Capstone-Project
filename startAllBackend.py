
import os 

os.system("/usr/bin/node /home/pi/Desktop/Capstone/backend/app.js & sudo /usr/bin/python3 /home/pi/Desktop/Capstone/getGPS.py & /usr/bin/python3 /home/pi/Desktop/Capstone/GoogleMapAPI.py & /usr/bin/python3 /home/pi/Desktop/Capstone/gyro.py & sudo /usr/bin/python3 /home/pi/Desktop/Capstone/navigation.py")
# os.system("sudo /usr/bin/python3 /home/pi/Desktop/Capstone/getGPS.py")
# os.system("/usr/bin/python3 /home/pi/Desktop/Capstone/GoogleMapAPI.py")
# os.system("/usr/bin/python3 /home/pi/Desktop/Capstone/gyro.py")
# os.system("sudo /usr/bin/python3 /home/pi/Desktop/Capstone/navigation.py")