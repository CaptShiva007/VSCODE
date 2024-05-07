import argparse
from os import getuid
import sys
import numpy as np
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from scapy.all import sniff
from scapy.layers.inet import IP

# Initialize Flask app and SocketIO
app = Flask(__name__)
socketio = SocketIO(app)

# Define window size and initial data arrays
WINDOW_SIZE = 30
x_data = np.arange(WINDOW_SIZE)
y_data = np.zeros(WINDOW_SIZE)

# Define command-line arguments
parser = argparse.ArgumentParser(description='Real-Time Traffic Analyzer')
parser.add_argument('interface', nargs='?', default='wlan0', help="Network Interface")
args = parser.parse_args()

# Check if interface is provided
if args.interface is None:
    print("Please specify a network interface.")
    sys.exit(1)

# Check if running as root
if getuid() != 0:
    print("Warning: Not running as root, packet listening may not work.")

# Route for serving index.html
@app.route('/')
def index():
    return render_template('index.html')

# WebSocket event handler for client connection
@socketio.on('connect')
def handle_connect():
    print('Client connected')
    emit('initial_data', {'x_data': x_data.tolist(), 'y_data': y_data.tolist()})

# Function to update graph with new packet
def update_graph(pkt):
    global y_data
    if IP in pkt:
        new_value = pkt[IP].len
        y_data = np.append(y_data[1:], new_value)
        # Emit update_graph event to update client-side graph
        socketio.emit('update_graph', {'y_data': new_value})

# WebSocket event handler to start packet sniffing
@socketio.on('start_sniffing')
def start_sniffing(interface):
    print('Starting sniffing on interface:', interface)
    # Start sniffing packets on specified interface and call update_graph for each packet
    sniff(iface=interface, prn=update_graph)

# Run the Flask app with SocketIO
if __name__ == '__main__':
    socketio.run(app, port=5000)
