import matplotlib.pyplot as plt
import numpy as np
from collections import deque
from scapy.all import sniff
from scapy.layers.inet import IP  # Import the IP layer
import argparse
from os import getuid
import sys

#ARGS

parser = argparse.ArgumentParser(description='Real-Time Traffic Analyzer')
parser.add_argument('interface', help="Network Interface", type=str)
parser.add_argument('--count', help="Capture X packets and exit", type=int)
args = parser.parse_args()

#CHK ROOT

if getuid() != 0:
    print("Warning: Not running as a root, packet listening may not work.")

    try:
        print("--Trying to listen on {}".format(args.interface))
        sniff(iface=args.interface, count=1)
        print("--Success!")
    
    except:
        print("--Failed!\nError: Unable to save packets, Try using sudo.")
        quit()

# Initialize variables
WINDOW_SIZE = 30  # Number of points to show on the graph

# Initialize plot
plt.ion()
fig, ax = plt.subplots()
ax.set_xlabel("Time")
ax.set_ylabel("Bytes")
ax.set_title("Real-time Network Traffic")

# Create initial empty plot
x_data = np.linspace(0, WINDOW_SIZE - 1, WINDOW_SIZE)
y_data = np.zeros(WINDOW_SIZE)
line, = ax.plot(x_data, y_data)

# Function to update graph
def update_graph(pkt):
    global y_data
    if IP in pkt:
        new_value = pkt[IP].len
        y_data = np.append(y_data[1:], new_value)
        line.set_ydata(y_data)
        ax.relim()  # Update the data limits
        ax.autoscale_view(True, True, True)  # Autoscale the view
        plt.draw()
        plt.pause(0.001)

# Start sniffing
i = 0
try:
    while True:
        for pkt in sniff(iface=args.interface, count=1):
            update_graph(pkt)
            i += 1
            if args.count and i >= args.count:
                print("Captured {} packets on interface {}".format(i, args.interface))
                sys.exit()

except KeyboardInterrupt:
    print("\nCaptured {} packets on interface {}".format(i, args.interface))
    sys.exit()
