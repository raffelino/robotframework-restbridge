#!/bin/bash
curl -H "Content-Type: application/json" -X POST http://localhost:8882/ -d '{ "command": "Browser.Open Browser   https://www.google.de    chromium      False" }'
curl -H "Content-Type: application/json" -X POST http://localhost:8882/ -d '{ "command": "Browser.Click    #W0wltc > div" }'
curl -H "Content-Type: application/json" -X POST http://localhost:8882/ -d '{ "command": "RequestsLibrary.GET    https://www.google.de" }'