import OpenSSL
import ssl, socket
import os
import json
import threading
import time
import datetime

objarray = []
outputfile = open(os.getcwd()+'/data/'+'final.txt', 'w')



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
          print(epoch)

          certobj = {}
          certobj['host'] = self.address
          certobj['expiration'] = epoch
          certobj['version'] = x509.get_version()
          certobj['sig_algorithm'] = x509.get_signature_algorithm()
          objarray.append(certobj)
      except Exception as e:
        print(e)




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