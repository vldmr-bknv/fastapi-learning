#!/bin/bash

curl -d '{"username": "Jerry", "password": "qwerty"}' \
       	-H "Content-Type: application/json" \
       	-X POST http://localhost:8000/login

printf "\n"
