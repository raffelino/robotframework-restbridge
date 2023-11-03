from robot.libraries.BuiltIn import BuiltIn
from flask import Flask, request, jsonify
import json
import re
import traceback
import jsonpickle


TAB = re.compile('  +|\t')

def run(server, command):
    parsed = TAB.split(command)

class RestBridge:

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
            result = ""
            # with the following statement we can start the deugger
            #import sys, pdb; pdb.Pdb(stdout=sys.__stdout__).set_trace()
            #variables = context.variables.as_dict()
            #for key in variables:
            #    result = f"{result} {key} : {variables[key]} \n"
            result = result + jsonpickle.encode(result_from_keyword)
           
            return result
        except Exception as e:
            return traceback.format_exc()


    # TODO: wie geht robot mit vergleichen um (erwartet 1=1 , aber 2=1 -> fehleer)

    #TODO: Abbruch Endpunkt für einzelne Kommandos
    # 