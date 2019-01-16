#!/bin/bash
# takes in a URL, sends POST request and displays body of respons
curl -sX POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" $1
