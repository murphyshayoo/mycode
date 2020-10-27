#!/usr/bin/env python3
import shutil
import os

#The following line will change directory to mycode directory
os.chdir('/home/student/mycode/')

#The following line will copy sdn_network text file into a nother copy
shutil.copy('5g_research/sdn_network.txt', '5g_research/sdn_network.txt.copy')

#The following line will copy all the directory and sub dir to another directory
shutil.copytree('5g_research/', '5g_research_backup/')

