#!/bin/bash
# Displays all HTTP methods that the server of a given URL will accept.
curl -X OPTIONS -sI "$1" | grep "Allow" | cut -d " " -f 2-
