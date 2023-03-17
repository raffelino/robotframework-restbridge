# Single Keyword Execution Tool for Robot Framework

This tool provides a simple web service for executing individual Robot Framework keywords using a Flask web server. The service maintains the context of a test suite between keyword executions, allowing users to execute keywords from different libraries and test cases without losing the imported library context.

## Requirements

- Python 3.6 or newer
- Flask
- Robot Framework

## Installation

1. Install Python 3.6 or newer, if not already installed.

2. Install the required Python packages:

`pip install Flask robotframework`

3. Clone the repository or download the `run.py` script.

## Usage

1. Start the web server by running the `run.py` script:

`python run.py`

2. Execute Robot Framework keywords by sending a POST request to the `/execute-keyword` endpoint. The request body should be a JSON object with the following properties:

- `library`: The name of the Robot Framework library containing the keyword.
- `keyword`: The name of the keyword to execute.
- `args` (optional): An array of arguments for the keyword.

Example:

```json
{
    "library": "BuiltIn",
    "keyword": "Sleep",
    "args": ["2 seconds"]
}
```
You can use a tool like curl or an API client like Postman to send the POST request.

Example curl command:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"library": "BuiltIn", "keyword": "Sleep", "args": ["2 seconds"]}' http://localhost:5000/execute-keyword
The response will be a JSON object containing the execution result:

{
    "message": "Keyword executed",
    "result": "OK"
}
```

## Notes

The tool maintains the context of a test suite between keyword executions. This means that libraries are imported only once, even when executing multiple keywords from the same library.
If you need to use a specific version of Robot Framework or another library, install the desired version using pip before running the script.
bash
Copy code

This README provides an overview of the tool, its requirements, installation, and usage. You can include this in your project folder to help users understand how to use the tool.