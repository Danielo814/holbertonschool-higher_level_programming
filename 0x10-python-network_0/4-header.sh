#!/bin/bash
# takes a URL as an argument, sends GET request, and displays the body of the response
curl -sX GET -H $1 "X-HolbertonSchool-User-Id: 98"
