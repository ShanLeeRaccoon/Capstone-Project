import os
import subprocess
# import bluetooth

address = "00:00:AB:CC:5C:E0"

# subprocess.run(["sudo", "bluetoothctl", "agent", "on"])
# subprocess.run(["sudo", "bluetoothctl", "power", "on"])
command = ["sudo", "bluetoothctl", "scan", "on"]
# command = ["echo", "hello"]
process = subprocess.Popen(command, stdout = subprocess.PIPE, stderr=subprocess.PIPE)
# print(process.stdout.readlines())

i=0
while True:
    print(i)
    i += 1
    output = process.stdout.readline().decode('utf-8')[17:41]
    print(output)

    # if output.startswith("Device"):
    #     print(output)

    # if output.endswith(address):
    #     break

# subprocess.run(["sudo", "bluetoothctl", "trust", address])
# subprocess.run(["sudo", "bluetoothctl", "pair", address])
# subprocess.run(["sudo", "bluetoothctl", "connect", address])