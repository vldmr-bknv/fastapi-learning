#!/bin/bash

curl \
	-H "User-Agent:" \
	-H 'Accept-Language: en-US,en;q=0.9,es;q=0.8' \
       	http://localhost:8000/headers

printf "\n"
