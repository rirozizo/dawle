import time, os, requests

hostname = "192.168.18.155"
response = 0
number_of_attempts = 0
kahraba = True
first_run = True
URL = "IFTT WEBHOOK FOR DAWLE HERE"
no_URL = "IFTT WEBHOOK FOR NO DAWLE HERE"


def n2ata3it_aw_ba3ed():
    global first_run
    number_of_attempts = 0
    while number_of_attempts < 10:
        try:
            response = os.system("ping -c 1 " + hostname)
        except Exception as e:
            print(e)
            time.sleep(5)
            break
        if response != 0:
            number_of_attempts += 1
            continue
        number_of_attempts = 0
        first_run = False
        print(str(response))
        print("Host is up")
        time.sleep(5)
    n2ata3it()


def n2ata3it():
    global first_run
    kahraba = False
    print("Host is down")
    print("=============================================")
    if not first_run:
        print("ra7it el dawle IFTTT WebHook")
        requests.get(no_URL)
    else:
        first_run = False

    while not kahraba:
        try:
            response = os.system("ping -c 1 " + hostname)
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
