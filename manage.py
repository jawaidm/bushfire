#!/usr/bin/env python
import os
import sys
import confy

confy.read_environment_file()
if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)

#    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bushfire_project.settings")
#    from django.core.management import execute_from_command_line
#    execute_from_command_line(sys.argv)
