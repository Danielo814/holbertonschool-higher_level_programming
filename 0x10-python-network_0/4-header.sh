#!/bin/bash
# takes a URL as an argument, sends GET request, and displays the body of the response
curl -sX GET -H "X-HolbertonSchool-User-Id: 98" $1
