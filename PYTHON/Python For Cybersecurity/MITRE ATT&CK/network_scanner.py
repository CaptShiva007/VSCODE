from scapy.all import *

ports=[22,23,25,53,80,443,445,8080,8443]

def SynScan(host):
    ans,unans=sr(IP(dst=host)/TCP(sport=5555,dport=ports,flags='S'),timeout=2,verbose=0)
    print("Open ports at %s " % host)
    for (s,r) in ans:
        if s[TCP].dport == r[TCP].sport:
            print(s[TCP].dport)

def DNSScan(host):
    ans,unans=sr(IP(dst=host)/UDP(sport=5555,dport=53)/DNS(rd=1,qd=DNSQR(qname='google.com')),timeout=2,verbose=0)
    if ans:
        print("DNS Server is at %s " % host)

host=input("Enter the host IPV4: ")

SynScan(host)
DNSScan(host)