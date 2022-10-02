import time, os, requests

hostname = "192.168.18.155"
global response
global number_of_attempts
global kahraba
global first_run
first_run = True
URL = "IFTT WEBHOOK FOR DAWLE HERE"
no_URL = "IFTT WEBHOOK FOR NO DAWLE HERE"

def n2ata3it_aw_ba3ed():
    number_of_attempts = 0
    while number_of_attempts < 10:
      try:
        response= os.system("ping -c 1 " + hostname)
      except Exception as e:
        print(e)
        time.sleep(5)
        break
      if response != 0:
        number_of_attempts += 1
        continue
      number_of_attempts = 0
      print(str(response))
      print("Host is up")
      time.sleep(5)
    n2ata3it()

def n2ata3it():
    kahraba = False
    print("Host is down")
    if first_run = False:
        requests.get(no_URL)
    if first_run = True:
        first_run = False
#    requests.get(no_URL)

    while kahraba == False:
      try:
        response= os.system("ping -c 1 " + hostname)
      except:
#        print("ERROR: Unreachable")
        time.sleep(5)
        break
      if response == 0:
        kahraba = True
        print("Host is up")
        print("Sending IFTTT WebHook")
        requests.get(URL)

while True:
  n2ata3it_aw_ba3ed()
