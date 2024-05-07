#IMPS
from scapy.all import *
import matplotlib.pyplot as plt
import argparse
from os import getuid

#ARGS

parser=argparse.ArgumentParser(description='Real-Time Traffic Analyzer')
parser.add_argument('interface',help="Network Interface",type=str)
parser.add_argument('--count',help="Capture X packets and exit",type=int)
args=parser.parse_args()

#CHK ROOT

if getuid()!=0:
    print("Warning: Not running as a root, packet listening may not work.")

    try:
        print("--Trying to listen on {}".format(args.interface))
        sniff(iface=args.interface,count=1)
        print("--Success!")
    
    except:
        print("--Failed!\nError:Unable to save packets, Try using sudo.")
        quit()

#PLT

plt.ion()
plt.xlabel("Count")
plt.ylabel("Bytes")
plt.title("Real-time Network Traffic")
plt.tight_layout()

yData=[]
i=0
while True:
    for pkt in sniff(iface=args.interface,count=1):
        try:
            if IP in pkt:
                yData.append(pkt[IP].len)
                plt.plot(yData)
                plt.pause(0.1)
                i+=1
                if args.count:
                    if i>=args.count:
                        quit()
        
        except KeyboardInterrupt:
            print("Captured {} packets on interface {}".format(i,args.interface))
            quit()