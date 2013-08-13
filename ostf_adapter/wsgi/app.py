#    Copyright 2013 Mirantis, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import pecan
from ostf_adapter.wsgi import hooks


PECAN_DEFAULT = {
    'server': {
        'host': '0.0.0.0',
        'port': 8989
    },
    'app': {
        'root': 'ostf_adapter.wsgi.root.RootController',
        'modules': ['ostf_adapter.wsgi'],
        'debug': False,
    },
    'nailgun': {
        'host': '127.0.0.1',
        'port': 8000
    },
    'dbpath': 'postgresql+psycopg2://ostf:ostf@localhost/ostf'
}


def setup_config(pecan_config=None):
    if pecan_config:
        PECAN_DEFAULT.update(pecan_config)
    pecan.conf.update(PECAN_DEFAULT)


def setup_app(debug=False):
    app_hooks = [hooks.ExceptionHandlingHook(),
                 hooks.StorageHook(),
                 hooks.PluginsHook()]
    app = pecan.make_app(
        pecan.conf.app.root,
        debug=debug,
        force_canonical=True,
        hooks=app_hooks
    )
    return app

