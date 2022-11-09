# Developed by Peace Oloruntoba aka Prof Prince Peace
# you can contact me on whatsapp and phone call @+2348166846226
# email @ profprincepeace@gmail.com or peascainc@gmail.com
# social media @ Peace Oloruntoba or PeaceOloruntoba including LinkedIn, Facebook, Twitter, etc.
#
# copyright 2022.

"""
ASGI config for studentstudyportal project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'studentstudyportal.settings')

application = get_asgi_application()
