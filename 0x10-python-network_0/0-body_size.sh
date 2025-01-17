#!/bin/bash
# This script to get the size of http response
curl -s $1 | wc -c
