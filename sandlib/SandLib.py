from robot.api import logger

class SandLib:

    def greet_me(self, name):
        logger.info(f"Hello {name}", also_console=True)
