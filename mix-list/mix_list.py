#!/usr/bin/env python3
# I am working on a list called my_list
my_list = [ "192.168.0.5", 5060, "UP" ]

#I am trying to print out ip address of 192.168.0.5
print("The first item in the list (IP): " + my_list[0] )

#Trying to print out the port number
print("The second item in the list (port): " + str(my_list[1]) )

# Setting port to UP state
print("The last item in the list (state): " + my_list[2] )

new_list = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

print(f"When i {new_list[5]} into IP addresses {new_list[3]} or {new_list[4]} i am unable to ping port {new_list[0]} {new_list[1]} or {new_list[2]}") 
