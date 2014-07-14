#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    # Make sure the main app can be found
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_project.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
