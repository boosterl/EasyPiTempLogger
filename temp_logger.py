from subprocess import *
from time import sleep, strftime
from datetime import datetime
import sys
import os

cmd = "/opt/vc/bin/vcgencmd measure_temp | grep -o '[0-9.]\+'"
file = open("temperatures.csv","wb")

def run_cmd(cmd):
    p = Popen(cmd, shell=True, stdout=PIPE)
    output = p.communicate()[0]
    return output

def main():
    print("Logging temperature... Press ^C to stop")
    file.write("Temperature,Date and Time,Temperature Rating\n")
    while 1:
        temp=float(run_cmd(cmd))
	tempRating = "OK"
	if(temp >= 70):
	    tempRating = "Warning"
	if(temp >= 80):
	    tempRating = "Danger"
	file.write("%.2f,%s,%s\n"%(temp,datetime.now(),tempRating))
        sleep(1)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
	file.close()
        print("Program stopped")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
