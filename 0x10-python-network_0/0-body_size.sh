#!/bin/bash
# takes in a URL, sends request to the URL, and displays body of response
curl -Is $1 | grep "Content-Length: " | cut -d " " -f2
