#!/bin/bash
# Write script makes a request causes the server to respond with a message You got me!
curl -sL -X PUT -d "user_id=98" -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
