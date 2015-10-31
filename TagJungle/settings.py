import os

# Import default (global) settings

from conf.prod import *

# Inherit environment specifics

"""
The DJANGO_ENV environment variable must be set to point to the appropriate settings file for the environment. The
various settings files are found in ServiceHub/conf and are named as follows:

prod.py = settings for production
staging.py = default settings for staging environments

Default settings for the designated environment (staging, dev, etc) will override the production settings (prod.py).
Further, any environmental default settings can be overridden by creating a local_settings.py file (next to settings.py)
and including in it any settings that should be overridden for the local environment. A good example is the case of
development.  It's handy to have default settings for development environments, but developers may need to override some
of the settings (e.g. databases) for their personal local environments.

Settings files are included in the git repo, except local_settings.py, which is intentionally ignored and should not be
checked into the VCS.
"""
DJANGO_ENV = os.environ.get('DJANGO_ENV', 'prod')
if DJANGO_ENV != 'prod':
    module = __import__('conf.{env}'.format(env=DJANGO_ENV), globals(), locals(), ['*'])
    for k in dir(module):
        locals()[k] = getattr(module, k)

try:
    from TagJungle.local_settings import *
except ImportError:
    pass

if 'DISABLED_APPS' in locals():
    INSTALLED_APPS = [k for k in INSTALLED_APPS if k not in DISABLED_APPS]

    MIDDLEWARE_CLASSES = list(MIDDLEWARE_CLASSES)
    TEMPLATE_CONTEXT_PROCESSORS = list(TEMPLATE_CONTEXT_PROCESSORS)

    for a in DISABLED_APPS:
        for x, m in enumerate(MIDDLEWARE_CLASSES):
            if m.startswith(a):
                MIDDLEWARE_CLASSES.pop(x)

        for x, m in enumerate(TEMPLATE_CONTEXT_PROCESSORS):
            if m.startswith(a):
                TEMPLATE_CONTEXT_PROCESSORS.pop(x)