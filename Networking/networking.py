import os

def Ping(ip_address, count=1, wait_sec=1):
    dictionary = {}
    dictionary["hostname"] = ip_address

    response = os.system("ping -c {count} {ip_address}")
    if response == 0:
        dictionary["Status"] = "Online"
    else:
        dictionary["Status"] = "Offline"

    return dictionary 