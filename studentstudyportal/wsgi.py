# Developed by Peace Oloruntoba aka Prof Prince Peace
# you can contact me on whatsapp and phone call @+2348166846226
# email @ profprincepeace@gmail.com or peascainc@gmail.com
# social media @ Peace Oloruntoba or PeaceOloruntoba including LinkedIn, Facebook, Twitter, etc.
#
# copyright 2022.

"""
WSGI config for studentstudyportal project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'studentstudyportal.settings')

application = get_wsgi_application()
