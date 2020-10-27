#!/usr/bin/env python3
import shutil
import os
os.chdir('/home/student/mycode/')

#the followin gline will move file from a folder to another folder with same name
shutil.move('raynor.obj', 'ceph_storage/')

#The following line will prompt user to rename before moving the file
xname = input('What is the new name for kerrigan.obj? ')

#The following line will take user input to rename
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

