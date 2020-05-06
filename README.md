# Detect-web-page-change

## sudo pip install
    python3.7
    netrc
    selenium
    twilio

## Create .netrc file && sudo chmod 600 .netrc
    machine VU_login
    login <login>
    password <password>

    machine Sms_send
    login <ACCOUNT_SID>
    password <AUTH_TOKEN>

    machine Numbers
    login <firstNumber>
    password <secondNumber>

## Install chrome
    sudo curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add
    sudo echo "deb [arch=amd64]  http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
    sudo apt-get -y update
    sudo apt-get -y install google-chrome-stable

## Download chromedriver
    sudo bash chrome.sh
### Or
    sudo mv chromedriver /usr/bin/chromedriver
    sudo chown root:root /usr/bin/chromedriver
    sudo chmod +x /usr/bin/chromedriver
