from lego.apps.oauth.models import APIApplication
from lego.apps.permissions import register
from lego.apps.permissions.index import PermissionIndex


class OAuthPermissionIndex(PermissionIndex):

    model = APIApplication

    list = ['/sudo/admin/apiapplications/list/']
    create = ['/sudo/admin/apiapplications/create/']


register(OAuthPermissionIndex)