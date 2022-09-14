import dns 
import dns.resolver
import socket
import sys

def ReverseDNS(ip):
    try:
        result = socket.gethostbyaddr(ip)
        return [result[0]]+result[1]
    except socket.herror:
        return None

def DNSrequest(domain):
    try:
        result = dns.resolver.resolve(domain)
        if result:
            print(domain)
            for answer in result:
                print("Domain Names: %s "  % ReverseDNS(answer.to_text())) 
                print(answer)

        return result
    except (dns.resolver.NXDOMAIN, dns.exception.Timeout):
        return 
    
    

def SubdomainSearch(domain, dictionary, nums):
   for word in dictionary:
       subdomain = word + "."+domain
       DNSrequest(subdomain)
       if nums:
           for i in range(0,10):
               s = word + str(i)+"."+domain
               DNSrequest(s) 



try:
    domain = sys.argv[1]
    d = "subdomains.txt"
    dictionary = []
    with open(d,"r") as f:
        dictionary = f.read().splitlines()
    SubdomainSearch(domain, dictionary, True)
except:
    print("Error syntax : try sudo python3 recons google.com")