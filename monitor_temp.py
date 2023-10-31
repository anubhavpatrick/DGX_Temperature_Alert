
# create a directory for reports if it doesn't exist
import os
if not os.path.exists('reports'):
    os.mkdir('reports')

# execute command to get temperature after every 15 minutes
import time
import subprocess
#import custom_twilio_whatsapp
from twilio_whatsapp import send_whatsapp_message

while True:
    # get the current time
    import datetime
    now = datetime.datetime.now()
    
    # get the temperature
    command = "ipmitool -I lanplus -H 192.168.12.4 -U abesit-gril-dgx -P 'DGX19abesit!bmc(' sensor list | grep TEMP_AMBIENT | grep -Eo '[[:digit:]]*\.[[:digit:]]*' | sed -n '1p'"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    # The stdout attribute contains the output
    output = result.stdout.strip()

    # send a message 
    send_whatsapp_message(account_sid='account_sid', 
                          auth_token='auth_token',
                          from_number='14155238886',
                          to_number='phone_number',
                          message=f'Your appointment is coming up on {output}')
    
    # write the temperature to a file
    with open('reports/temperature.txt', 'a') as f:
        f.write(str(now) + ', ' + output + '\n')
    
    # wait for 15 minutes if the temperature is less than 30 otherwise wait for 5 minutes
    if float(output) < 30:
        time.sleep(15 * 60)
    else:
        time.sleep(5 * 60)