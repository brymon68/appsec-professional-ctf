import OpenSSL
import ssl, socket
import os
import json
import threading
import time
import datetime
import sys
sys.path.append("..")


objarray = []
outputfile = open(os.getcwd()+'/data/'+'final.json', 'w')
currenttime = time.time()


class GetCertInfo(threading.Thread):
    def __init__(self, address):
        threading.Thread.__init__(self)
        self.address = address

    def convertTimestamp(self, timestamp):
        try:
            timestamp = timestamp[:-1]
            epoch = time.mktime(datetime.datetime.strptime(timestamp, "%Y%m%d%H%M%S").timetuple())
            return epoch
        except Exception as e:
            print(e)


    def run(self):
        try:
            cert=ssl.get_server_certificate((self.address, 443))
            x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)

            epoch = self.convertTimestamp(x509.get_notAfter())
            if self.check_if_within_one_year(epoch):
                #we shouldnt append to objectarray
                return None
            else: 
                certobj = {}
                certobj['host'] = self.address
                certobj['expiration'] = epoch
                certobj['version'] = x509.get_version()
                certobj['sig_algorithm'] = x509.get_signature_algorithm()
                objarray.append(certobj)
        except Exception as e:
            print(e)

    def check_if_within_one_year(self, epoch):
        date_next_year = currenttime + 31622400
        print(str(time.localtime(date_next_year))  + '- '+str(date_next_year)+ ' -  date next year')
        print(str(time.localtime(epoch)) + '- '+ str(epoch) + ' - epoch current')
        if date_next_year > epoch:
            print("Wont add")
            return False
        else:
            print("Will add")
            return True
            

def main():

    threads = []
    #first process aggregated hostnames]
    for filename in os.listdir(os.getcwd()+'/data/'):
        with open(os.getcwd()+'/data/'+filename) as f1:
            if (filename == 'final.txt'):
                continue
                
            for line in f1: 
                print(line)
                line = line.strip()
                cert_thread = GetCertInfo(line)
                threads.append(cert_thread)
                cert_thread.start()

            for thread in threads:
                thread.join()

    print(json.dumps(objarray))      
    outputfile.write(json.dumps(objarray))

if __name__== "__main__":
  main()