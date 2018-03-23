ip ='10.10.10.10'
username = 'Administrator'
password = 'Password'

from socket import *
try:
    print("Establishing connection")
    connection = wmi.WMI(ip, user=username, password=password)
    print("Connection established")
except wmi.x_wmi:
    print("invalid")
