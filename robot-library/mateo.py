from robot.libraries.BuiltIn import BuiltIn
from flask import Flask, request, jsonify
import json
import re
import traceback

TAB = re.compile('  +|\t')

def run(server, command):
    parsed = TAB.split(command)

class mateo:

    app = None

    def accept_keywords(self):
        app = Flask(__name__)
        app.add_url_rule("/", "dorun", self.dorun, methods=['POST'])
        #app.add_url_rule("/shutdown", "shutdown", self.shutdown)
        app.run(host="0.0.0.0", port=8889)
    
    
    def dorun(self):
        try:
            json_body = request.data.decode('utf-8')
            data = json.loads(json_body)
            parsed = TAB.split(data['command'])
            result_from_keyword = BuiltIn().run_keyword(parsed[0], *parsed[1:])
            context = BuiltIn()._get_context()
            #import sys, pdb; pdb.Pdb(stdout=sys.__stdout__).set_trace()

            result = str(result_from_keyword) + "\n"
            variables = context.variables.as_dict()
            for key in variables:
                result = f"{result} {key} : {variables[key]} \n"
            return result
        except Exception as e:
            return traceback.format_exc()

