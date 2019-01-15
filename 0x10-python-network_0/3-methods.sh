#!/bin/bash
# takes in URL and displays HTTP methods server will allos
curl -sI $1 | grep "Allow: " | cut -d " " -f2-
