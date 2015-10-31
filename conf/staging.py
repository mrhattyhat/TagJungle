# Staging Defaults

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

# Specify apps that should not be installed in this environment.  Apps in this list will be removed from INSTALLED_APPS
# when the settings first load.  The rest will be inherited from prod.
DISABLED_APPS = ['']