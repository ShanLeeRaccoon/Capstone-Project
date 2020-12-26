import bluedot
import signal

def data_received(data):
    print(data)

s = bluedot.btcomm.BluetoothServer(data_received)
signal.pause()
