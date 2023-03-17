import sys
import json
import logging
from flask import Flask, request, jsonify
from robot.running.builder import TestSuiteBuilder
from robot.libraries.BuiltIn import BuiltIn
from robot.running.model import TestSuite, Keyword

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Global TestSuite object to maintain context between executions
suite = TestSuite('Single Keyword Execution Suite')

def is_library_imported(library_name):
    for lib in suite.resource.imports._library_imports:
        if lib.name == library_name:
            return True
    return False

def execute_keyword(library, keyword, *args):
    global suite
    #if not is_library_imported(library):
    #    suite.resource.imports.library(library)

    # Create a temporary test case to run the keyword
    test = suite.tests.create('TempTestCase')
    kw = Keyword(name=keyword, args=args)
    test.body.create_keyword(kw)
    
    # Instantiate BuiltIn library and use run_keyword to execute the keyword
    builtin = BuiltIn()
    result = builtin.run_keyword(keyword, *args)

    # Remove the temporary test case after execution
    suite.tests.remove(test)

    return result

@app.route('/execute-keyword', methods=['POST'])
def execute_keyword_endpoint():
    data = request.json

    if not data or 'library' not in data or 'keyword' not in data:
        return jsonify({"error": "Invalid request data"}), 400

    library = data['library']
    keyword = data['keyword']
    args = data.get('args', [])

    logger.info(f"Executing keyword: {keyword} from library: {library} with arguments: {args}")

    result = execute_keyword(library, keyword, *args)

    logger.info(f"Keyword executed: {keyword}, result: {result}")

    return jsonify({"message": "Keyword executed", "result": str(result)}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=6000, debug=True)
    suite.run()
