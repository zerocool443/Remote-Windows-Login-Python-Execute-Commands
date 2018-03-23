ip = '10.10.10.1'
username = 'Administrator'
password = 'pass'
from socket import *
try:
    print("Establishing connection")
    connection = wmi.WMI(ip, user=username, password=password)
    print("Connection established")
except wmi.x_wmi:
    print("Your Username and Password of "+getfqdn(ip)+" are wrong.")
