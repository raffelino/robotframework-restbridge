from robot.errors import HandlerExecutionFailed
from robot.libraries.BuiltIn import BuiltIn
from flask import Flask, request, jsonify
import json
import re
import traceback
import jsonpickle
import types


TAB = re.compile('  +|\t')

def run(server, command):
    parsed = TAB.split(command)

class RestBridge:

    app = None

    def accept_keywords(self):
        app = Flask(__name__)
        app.add_url_rule("/", "execute_keyword", self.execute_keyword, methods=['POST'])
        app.run(host="0.0.0.0", port=8882)


    def execute_keyword(self):
        try:
            json_body = request.data.decode('utf-8')
            BuiltIn().run_keyword("Log to Console", json_body)
            data = json.loads(json_body)
            command = data['command']
            parsed = TAB.split(command)
            result_from_keyword = BuiltIn().run_keyword(parsed[0], *parsed[1:])
            context = BuiltIn()._get_context()
            # with the following statement we can start the debugger
            #import sys, pdb; pdb.Pdb(stdout=sys.__stdout__).set_trace()
            result = types.SimpleNamespace()
            result.payload = result_from_keyword
            result.variables = context.variables.as_dict()
            result.mateo_status = "OK"
            return jsonpickle.encode(result)
        except HandlerExecutionFailed as e:
            result = types.SimpleNamespace()
            result.payload = e.message
            result.mateo_status = e.status
            BuiltIn().run_keyword("Log to Console", jsonpickle.encode(result))
            return jsonpickle.encode(result), 400
        except Exception as e:
            result = types.SimpleNamespace()
            result.payload = traceback.format_exc()
            result.mateo_status = "FATAL"
            return jsonpickle.encode(result), 500
