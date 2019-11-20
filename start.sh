#!/bin/bash
while true
do
    echo "Starting program";
    python Scraper2.py
    python Comparer.py 2>&1 /dev/null
    script_output=$?
    if [ $script_output -eq "0" ]; then
        echo "Everything is good";
      else
        echo "Sending Sms"
        #python SendSms.py 2>&1 /dev/null
        script_output=$?
        if [ $script_output -eq "0" ]; then
            echo "Sms sent";
            exit;
          else
            echo "Sending Sms again";
            #python SendSms.py
        fi
    fi
    sleep 30
done