import pecan
from ostf_adapter.wsgi.controllers import v1


class RootController(object):

    v1 = v1.V1Controller()

    @pecan.expose(generic=True)
    def index(self):
        return dict()