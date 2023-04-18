import sys

# Allows running as a script. __name__ check needed with multiprocessing:
# https://github.com/robotframework/robotframework/issues/1137
#if 'robot' not in sys.modules and __name__ == '__main__':
#    import pythonpathsetter

from robot.conf import RobotSettings
from robot.model import ModelModifier
from robot.output import LOGGER, pyloggingconf
from robot.reporting import ResultWriter
from robot.running.builder import TestSuiteBuilder
from robot.utils import Application, text
from robot.running.model import TestSuite


class RobotFramework(Application):

    def __init__(self):
        Application.__init__(self, """USAGE""", arg_limits=(1,), env_options='ROBOT_OPTIONS',
                             logger=LOGGER)

    def main(self, datasources, **options):
        try:
            settings = RobotSettings(options)
        except:
            LOGGER.register_console_logger(stdout=options.get('stdout'),
                                           stderr=options.get('stderr'))
            raise
        LOGGER.register_console_logger(**settings.console_output_config)
        LOGGER.info(f'Settings:\n{settings}')
        if settings.pythonpath:
            sys.path = settings.pythonpath + sys.path
        builder = TestSuiteBuilder(settings.suite_names,
                                   included_extensions=settings.extension,
                                   rpa=settings.rpa,
                                   lang=settings.languages,
                                   allow_empty_suite=settings.run_empty_suite)
        suite = builder.build(*datasources)
        settings.rpa = suite.rpa
        if settings.pre_run_modifiers:
            suite.visit(ModelModifier(settings.pre_run_modifiers,
                                      settings.run_empty_suite, LOGGER))
        suite.configure(**settings.suite_config)
        with pyloggingconf.robot_handler_enabled(settings.log_level):
            old_max_error_lines = text.MAX_ERROR_LINES
            old_max_assign_length = text.MAX_ASSIGN_LENGTH
            text.MAX_ERROR_LINES = settings.max_error_lines
            text.MAX_ASSIGN_LENGTH = settings.max_assign_length
            try:
                customsuite = TestSuite(name='xxxxx')

                # Add an infinite loop test case to the suite
                test = customsuite.tests.create(name='Infinite Loop')
                test.body.create_keyword(name='BuiltIn.Wait Until Keyword Succeeds', args=['0.1 seconds', '2 seconds', 'True'])
                result = customsuite.run(settings)
            finally:
                text.MAX_ERROR_LINES = old_max_error_lines
                text.MAX_ASSIGN_LENGTH = old_max_assign_length
            LOGGER.info("Tests execution ended. Statistics:\n%s"
                        % result.suite.stat_message)
            if settings.log or settings.report or settings.xunit:
                writer = ResultWriter(settings.output if settings.log
                                      else result)
                writer.write_results(settings.get_rebot_settings())
        return result.return_code

    def validate(self, options, arguments):
        return self._filter_options_without_value(options), arguments

    def _filter_options_without_value(self, options):
        return dict((name, value) for name, value in options.items()
                    if value not in (None, []))


def run_cli(arguments=None, exit=True):
    if arguments is None:
        arguments = sys.argv[1:]
    return RobotFramework().execute_cli(arguments, exit=exit)


def run(*tests, **options):
    return RobotFramework().execute(*tests, **options)


if __name__ == '__main__':
    #run_cli(sys.argv[1:])
    run_cli(["test.robot"])
    #run_cli(sys.argv[1:])


