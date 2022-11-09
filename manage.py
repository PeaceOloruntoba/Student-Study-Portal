# Developed by Peace Oloruntoba aka Prof Prince Peace
# you can contact me on whatsapp and phone call @+2348166846226
# email @ profprincepeace@gmail.com or peascainc@gmail.com
# social media @ Peace Oloruntoba or PeaceOloruntoba including LinkedIn, Facebook, Twitter, etc.
#
# copyright 2022.

#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'studentstudyportal.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
