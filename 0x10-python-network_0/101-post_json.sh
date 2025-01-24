#!/bin/bash
# Script that takes in a URL and displays the body of the response
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" -X POST "$1"
