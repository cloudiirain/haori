"""Bot class.

This class represents the base bot that can send HTTP requests to the Novel
Updates Forum. Does not interact with javascript.

"""

__author__ = 'cloudiirain'


import requests


class Bot(object):
    """Represents a bot that can interact with NUF.

    Attributes:
        session: A Session object from the python requests library.

    """

    def __init__(self):
        """Construct a bot object."""
        self.session = requests.Session()
