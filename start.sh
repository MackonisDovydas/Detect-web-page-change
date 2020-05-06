#!/bin/bash
while true
do
    now=$(date +"%T")
    H=$(date +"%k");
    echo "Starting program": $now, $H;
    # -gt: greater-than, -lt: less-than   m=$(date +"%M")
    if [[ $H > 5 || $H < 3 ]]; then
      python3 Scraper2.py
      python3 Comparer.py 2>&1 /dev/null
      script_output=$?
      if [ $script_output -eq "0" ]; then
	        now=$(date +"%T");
          echo "Everything is good": $now, $H;
      else
	      for i in {1..5}
	      do
		        now=$(date +"%T");
        	  echo "Sending Sms": $now;
        	  python3 SendSms.py 2>&1 /dev/null
        	  script_output=$?
        	  if [ $script_output -eq "0" ]; then
	    		      now=$(date +"%T");
             	  echo "Sms sent": $now;
          		  else
            		echo "Sending Sms again";
            		python3 SendSms.py
        	  fi
	          sleep 60
	      done
	    exit;
      fi
    else
        now=$(date +"%T")
        echo "Timeout": $now;
    fi
    sleep 30
done
