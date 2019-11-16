#!/bin/bash

LATEST_CHROMEDRIVER=$(curl https://chromedriver.storage.googleapis.com/LATEST_RELEASE)
curl -L https://chromedriver.storage.googleapis.com/$LATEST_CHROMEDRIVER/chromedriver_linux64.zip >> chromedriver.zip
mv -f chromedriver.zip /usr/local/bin/chromedriver.zip
unzip /usr/local/bin/chromedriver.zip -d /usr/local/bin
chmod a+x /usr/local/bin/chromedriver
sudo ln -s /usr/local/bin/chromedriver /usr/bin/chromedriver
rm /usr/local/bin/chromedriver.zip