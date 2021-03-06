from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class ProjectsAppHook(CMSApp):
    name = _("Projects App")
    urls = ["projects.urls"]

apphook_pool.register(ProjectsAppHook)
