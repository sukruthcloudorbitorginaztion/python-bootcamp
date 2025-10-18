"""
MakoFileUpdator
-----------------------
MakoFileUpdator - Updates the mako files with the command line arguments.


Example Usuage
-------------
MakoFileUpdator --input_path input
                        --output_path output
                        --phone_number 12345
                        --event_name python_book_club
"""

import argparse
import os
from os import listdir

from mako.template import Template


class MakoFileUpdator:
    """
    MakoFileUpdator updates the mako files with the command line arguments.
    """

    def __init__(self):
        """
        Initializes the class.
        """
        pass
 

    def update(self):
        """
        Updates the variable names in the mako files
        """
        pass


if __name__ == "__main__":
    mako_file_updator = MakoFileUpdator()
    mako_file_updator.update()
