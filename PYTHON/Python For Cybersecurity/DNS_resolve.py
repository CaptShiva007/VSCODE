import dns
import dns.exception
import dns.resolver
import socket

def ReverseDNS(ip):
    try:
        result=socket.gethostbyaddr(ip)
    except:
        return []
    
def DNSRequest(domain):
    try:
        result=dns.resolver.resolve(domain)
        if result:
            print(domain)
            for answer in result:
                print(answer)
                print("Domain Names: %s " % ReverseDNS(answer.to_text()))
    except (dns.resolver.NXDOMAIN , dns.exception.Timeout):
        return
    
def SubDomainSearch(domain,dictionary,nums):
    for word in dictionary:
        subdomain=word+'.'+domain
        DNSRequest(subdomain)
        if nums:
            for i in range(0,10):
                s=word+str(i)+'.'+domain
                DNSRequest(s)

domain=input("Enter an IP: ")
d='subdomains.txt'
dictionary=[]

with open(d,'r') as f:
    dictionary=f.read().splitlines()
SubDomainSearch(domain,dictionary,True)