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
        self._args = self.parse_command_line_args()

    def parse_command_line_args(self):
        """
        Parse command line arguments.
        """
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "--input_path", required=True, help="Input directory path where mako files are stored"
        )
        parser.add_argument(
            "--output_path",
            required=True,
            help="Output directory path where converted mako files are stored",
        )
        parser.add_argument(
            "--phone_number", required=True, help="Phone number to be updated in the mako files"
        )
        parser.add_argument(
            "--event_name", required=True, help="Event name to be updated in the mako files"
        )
        args = parser.parse_args()
        return args

    def update(self):
        """
        Updates the variable names in the mako files
        """
        for filename in listdir(self._args.input_path):
            if not filename.endswith("mako"):
                continue
            with open(os.path.join(self._args.input_path, filename), "r") as fp:
                mako_file_content = fp.read()

            output_file_name = filename.split(".mako")[0]

            template = Template(text=mako_file_content)
            convert_text = template.render(
                **{
                    "INDIA_PHONE_NUMBER": self._args.phone_number,
                    "EVENT_NAME": self._args.event_name,
                }
            )

            if not os.path.exists(self._args.output_path):
                os.mkdir(self._args.output_path)
            with open(os.path.join(self._args.output_path, output_file_name), "w") as fp:
                fp.write(convert_text)


if __name__ == "__main__":
    mako_file_updator = MakoFileUpdator()
    mako_file_updator.update()
