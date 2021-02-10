
import IoTSixfab
from time import sleep

""" QMTT Class """
class IoTQmtt(IoTSixfab.IoT):
    def __init__(self,
                host_name='9.162.161.25',
                port="1883",
                topic="5G-Solutions",
                clientID="sixfab",
                tcpconnectID=0,
                msgID=1,
                qos=0,
                retain=0,
                msg = "Hello world 22",
                name='IoTQmtt'):
        super(IoTQmtt, self).__init__()         # name=name

        self.host_name = host_name
        self.port = port
        self.topic = topic
        self.clientID = clientID
        self.tcpconnectID = tcpconnectID
        self.msgID = msgID
        self.qos = qos
        self.retain = retain
        self.msg = msg
        # <tcpconnectID> QMTT socket identifier. The range is 0-5.
        # <clientID> The client identifier string.
        # <username> User name of the client. It can be used for authentication.
        # <password> Password corresponding to the user name of the client.

    def qmtt_open(self):
        # AT+QMTOPEN=<tcpconnectID>,“<host_name>”,<port>
        self.sendATComm("AT+QMTOPEN=0,\"9.161.154.25\",1883","+QMTOPEN: 0")         # OK
        # self.sendATComm("AT+QMTOPEN?","OK")    # +QMTOPEN: 0,"9.161.154.25",1883
        # self.sendATComm("AT+QMTCLOSE=0","\r\n")     # ?

    def qmtt_status(self):
        self.sendATComm("AT+QMTOPEN?","OK")

    def qmtt_connect(self):
        # AT+QMTCONN=<tcpconnectID>,“<clientID>”[,“<username>”[,“<password>”]]
        # self.sendATComm("AT+QMTCONN=0,\"sixfab\"","+QMTCONN: 0,0")      # this worked once
        self.sendATComm("AT+QMTCONN=0,\"sixfab\"","+QMTCONN: 0")    # this worked today 04/02

    def qmtt_publish(self):
        # AT+QMTPUB=<tcpconnectID>,<msgID>,<qos>,<retain>,“<topic>”
        # self.sendATComm("AT+QMTPUB=0,1,0,0,\"QMTTsecondcode\"","+QMTPUB: 0,1,0")
        self.sendATComm("AT+QMTPUB=0,0,0,0,\"5G-Solutions\"",">")
        print("Waiting 5 seconds before sending a message....")
        sleep(5)
        self.sendATComm("Hello 2022"+self.CTRL_Z,"+QMTPUB: 0,0,0")

    def qmtt_close(self):
        # # AT+QMTCLOSE=<tcpconnectID>
        self.sendATComm("AT+QMTCLOSE=0","+QMTCLOSE: 0")



''' Class for Cellular IoT Application Shield Sensor Readings. '''
class IoTQmtt(IoTSixfab.IoT):
    def __init__(self,
                host_name='9.162.161.25',
                port="1883",
                topic="5G-Solutions",
                clientID="sixfab",
                tcpconnectID=0,
                msgID=1,
                qos=0,
                retain=0,
                msg = "Hello world 22",
                name='IoTQmtt'):
        super(IoTQmtt, self).__init__()         # name=name

        self.host_name = host_name
        self.port = port
        self.topic = topic
        self.clientID = clientID
        self.tcpconnectID = tcpconnectID
        self.msgID = msgID
        self.qos = qos
        self.retain = retain
        self.msg = msg
        # <tcpconnectID> QMTT socket identifier. The range is 0-5.
        # <clientID> The client identifier string.
        # <username> User name of the client. It can be used for authentication.
        # <password> Password corresponding to the user name of the client.

    def qmtt_open(self):
        # AT+QMTOPEN=<tcpconnectID>,“<host_name>”,<port>
        self.sendATComm("AT+QMTOPEN=0,\"9.161.154.25\",1883","+QMTOPEN: 0")         # OK
        # self.sendATComm("AT+QMTOPEN?","OK")    # +QMTOPEN: 0,"9.161.154.25",1883
        # self.sendATComm("AT+QMTCLOSE=0","\r\n")     # ?


from cellulariot import cellulariot

node = cellulariot.CellularIoTApp()
# node.setupGPIO()
# node.disable()
# sleep(1)
# node.enable()
sleep(0.5)
print("Acceleration: "+str(node.readAccel()))
sleep(0.5)
print("Humidity: " + str(node.readHum()))
sleep(0.5)
print("Temperature: " + str(node.readTemp()))
sleep(0.5)
print("Lux: " + str(node.readLux()))
print("ADC1: " + str(node.readAdc(0)))
sleep(0.5)
print("ADC2: " + str(node.readAdc(1)))
sleep(0.5)
print("ADC3: " + str(node.readAdc(2)))
sleep(0.5)
print("ADC4: " + str(node.readAdc(3)))
sleep(0.5)
node.turnOnRelay()
sleep(2)
node.turnOffRelay()
sleep(0.5)
node.turnOnUserLED()
sleep(2)
node.turnOffUserLED()

from Adafruit_ADS1x15 import ADS1015
from .SDL_Pi_HDC1000 import *
from .MMA8452Q import MMA8452Q

	# Function for reading accelerometer
	def readAccel(self):
		mma = MMA8452Q()
		return mma.readAcc()


# some_file.py
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '/home/pi/Sixfab_RPi_CellularIoT_Library/cellulariot')
import MMA8452Q.py
import SDL_Pi_HDC1000.py


""" I need to study timeout wrtitten with self and then self.timeout I need also to check the return of each method
and cmpare then do something like delay/try&except ...  try and except and assert """

import IoTQmtt
from time import sleep
node = IoTQmtt.IoTQmtt()
node.qmtt_open()
node.qmtt_status()
node.qmtt_connect()
node.qmtt_publish()
node.qmtt_close()

# mosquitto_sub -t "5G-Solutions"
# mosquitto_sub -t "MQTTsecondcode"

# Turn on cellular functionality
# AT+CFUN=1
#   Check the received signal strength
# AT+QCSQ
#   Query network registration status (0,1=Registered, on home network, 0,5=Registered, roaming) other - not connected
# AT+CEREG?
#   Query network technology and carrier:
# AT+COPS?

#################################################################################
#   Activate PDP context
# AT+QIACT=1

#   Confirm PDP context was activated
# AT+QIACT?

#   Configure QMTT session          # Configure Optional Parameters of QMTT
# AT+QMTCFG=“aliauth”,0
#################################################################################



#
