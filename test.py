import os
os.chdir("/home/ec2-user")
term='error'
file=open('test_file.txt')
for line in file:
   if term in line:
      print line
file.close()
