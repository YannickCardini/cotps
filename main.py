import time
import cotps
import sys
import traceback
from getpass import getpass
from datetime import datetime

def get_accounts():
    list_accounts = []
    try:
        with open('/data/accounts.txt') as f:
            for line in f:
                line_splited = line.split(',')
                list_accounts.append(line_splited)
    except:
        codeCountry = input("Enter your international country code: ")
        phoneNumber = input("Enter your phone number: ")
        password = getpass("Enter your password: ")
        list_accounts.append([codeCountry,phoneNumber,password])

    return list_accounts


def arbritage_all_accounts():

    while True:
        start = time.time()
        list_accounts = get_accounts()
        for i in range(0,len(list_accounts)):
            dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            print( dt_string)
            cot = cotps.Cotps()
            logged = cot.login_process(list_accounts[i][0],list_accounts[i][1],list_accounts[i][2])
            if(logged):
                cot.sell()
            cot.kill()
        end = time.time()
        elapesd_time = int(end - start)
        sleeping = ((7980 - elapesd_time) + 9) // 10 * 10
        print("Sleep for ",sleeping," seconds")
        for i in range(sleeping,0,-10):
            sys.stdout.write(str(i)+'s left \n')
            sys.stdout.flush()
            time.sleep(10)

if __name__ == "__main__":
    print("Bot starting !\n")
    try:
        arbritage_all_accounts()
    except:
        with open("exceptions.log", "a") as logfile:
            traceback.print_exc(file=logfile)
        raise