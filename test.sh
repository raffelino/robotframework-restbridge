#!/bin/bash
robot robot-library/test.robot

sleep 1

curl -H "Content-Type: application/json" -X POST http://localhost:8889/ -d '{ "command": "Browser.New Page    https://www.google.de" }'
curl -H "Content-Type: application/json" -X POST http://localhost:8889/ -d '{ "command": "Browser.Click    #W0wltc > div" }'