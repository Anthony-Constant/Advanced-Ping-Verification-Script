# Ping_Verification.py
# Created a Advanced Ping verification script in Python
# Author: Anthony Constant (AC)

################################# SOME NOTES #########################################

## Advanced Ping automation script (specify the range method to the maximum number of hosts to ping inside the network and use 'write' to create/open/write the status to ping_logs.txt file. ) 


######################## HOW DOES IT WORK ##############################################
## Ping a maximum number of devices inside a network to return whether the network status is successful or unsuccessful. 

## Specify the maximum number of target IP addresses in the range method. 


############################# REFERENCES ###############################################

## https://www.cisco.com/c/en/us/support/docs/ios-nx-os-software/ios-software-releases-121-mainline/12778-ping-traceroute.html


########################################################################################
############################ START PROJECT HERE #######################################
############################################################################################

import os 


OS_TYPE = os.name ## verifies the OS type
count = '-n' if OS_TYPE == 'nt' else '-c' ## Sets the count modififer to the OS type. Specify amount of pings
logs_file = open("ping_logs.txt", "a" or "w") ## create a variable logs_file which opens/creates a ping_logs.txt file then writes the feedback status of the network to it. 
ip_list = [] ## create an empty list variable called ip_list to store ip addresses

for ip in range(1, 10): ## create a for loop using the range method to loop through 1-256 hosts (change 256 to specify maximum number of hosts in a network)
    ip_list.append("192.168.5." + str(ip)) ## append the ip_list starting with the default gateway (192.168.1.1) up to maximum hosts specified inside the range method. 
    ## convert the ip variable into a string format so we can use it.

for ip in ip_list: ## create a for loop here to loop through each ip address of ip_list
    response = os.popen(f"ping {ip} {count} 1").read() ## use -n 1 to send just one ping to the device to save time
    if "Received = 1" and "Approximate" in response: ## check to see if the response has "Received =1" AND Approximate inside the response variable. For more specific results we check for Approximate with response
        print(f"{ip} Ping was Successful! ")
        logs_file.write(f"{ip} Ping Successful " + "\n") ## write this to the logs_file
    else:
        print(f"{ip} Ping was Unsuccessful! ")
        logs_file.write(f"{ip} Ping Unsuccessful " + "\n") ## write this to the logs_file









