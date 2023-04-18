from robot.libraries.BuiltIn import BuiltIn
import re

TAB = re.compile('  +|\t')

def run(command: str):
    parsed = TAB.split(command)
    BuiltIn().run_keyword(parsed[0], *parsed[1:])

class mateo:
    def accept_keywords(self):
        run("New Browser    chromium    headless=false")
        run("New Page   https://playwright.dev")
        run("Get Text    h1    contains    Playwright")