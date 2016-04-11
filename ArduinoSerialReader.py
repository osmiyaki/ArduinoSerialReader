import serial

print "Port Connection? (Leave Blank = ttyAMA0) "
port = raw_input()
print "Serial Baud Rate? (Leave Blank = 115200) "
baud = raw_input()

if port == "" :
  port = "ttyAMA0"
if baud == "" :
  baud = "115200"

ser = serial.Serial(port,int(baud))

while True:
  line = ser.readline()
  print (line)



