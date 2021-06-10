import socket, os


file = open('results.txt','w')
lignes = [ligne.rstrip('\n') for ligne in open('source.txt')]
for ligne in lignes:
        #print("Primary IP address, Alias names and other IP addresses of the host name {}: {}".format(ligne, ipAddress))
        #print('Ip du domaine'+' '+ ligne + '->' + socket.gethostbyname_ex(dom))
    try: 
        ipAddress   = socket.gethostbyname_ex(ligne)
        file.write("{}".format(ipAddress)+'\n')
    except socket.gaierror:
       file.write('error'+'\n')
   

file.close()

