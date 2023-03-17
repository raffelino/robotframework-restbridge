from robot.running.model import TestSuite
from robot.api import ResultWriter
from robot import run

# Create a Robot Framework test suite object
suite = TestSuite(name='Endless Loop')

# Add an infinite loop test case to the suite
test = suite.tests.create(name='Infinite Loop')
test.body.create_keyword(name='BuiltIn.Wait Until Keyword Succeeds', args=['0.1 seconds', '2 seconds', 'True'])

# Set up the result writer to write the results to a temporary file
result_writer = ResultWriter('/path/to/output/directory')

# Execute the test suite asynchronously
task = run(suite, outputdir=result_writer.output_directory, background=True)

# Do some work with the test suite object in another thread while the test is running
# ...

# Wait for the test to finish and get the result
result = task.result(timeout=None)

# Check the result object to see if the test execution was successful
if result.return_code != 0:
    print('Test execution failed')
else:
    print('Test execution successful')
