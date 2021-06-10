import socket, os


file = open('results.txt','w')
lignes = [ligne.rstrip('\n') for ligne in open('source.txt')]
for ligne in lignes:
        
    try: 
        ipAddress   = socket.gethostbyname_ex(ligne)
        file.write("{}".format(ipAddress)+'\n')
    except socket.gaierror:
       file.write('error'+'\n')
   

file.close()

