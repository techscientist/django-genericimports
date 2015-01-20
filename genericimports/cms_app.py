# -*- coding: utf-8 -*-

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


class ImportHubHook(CMSApp):
    name = "User Import Hub"
    urls = ["apps.CustomApphooks.ImportHub.urls"]

apphook_pool.register(ImportHubHook)
