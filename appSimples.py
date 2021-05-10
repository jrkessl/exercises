# this is a simple application that just writes to a log file.
# the objective is just to produce a log to test another solution that consumes logs (cloudwatch agent and cloudwatch logs).
# keywords: log, logfile, cloudwatch, cloudwatch agent, cloudwatch logs

import random
import time
from datetime import date
from datetime import datetime

# this loop writes to the log every 1 second
while True:
    now = datetime.now()
    with open('appSimples.log', 'a') as f: # this is the log file
        f.write('appSimples: ' + str(now.strftime("%d/%m/%Y %H:%M:%S")) + ' logging... OK\n')
        n = random.randint(1,1000) # out of every 10 tries, one will be an error logging
        if n%10 == 0:
            f.write('appSimples: ' + str(now.strftime("%d/%m/%Y %H:%M:%S")) + ' ERRO: SE FERROU\n')
        f.close()
    del(now)
    del(f)
    del(n)
    time.sleep(1)
