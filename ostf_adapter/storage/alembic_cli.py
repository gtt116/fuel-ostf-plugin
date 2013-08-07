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

import os
from alembic import command, config
from pecan import conf
import logging


log = logging.getLogger(__name__)


def do_apply_migrations():
    try:
        alembic_conf = config.Config(
            os.path.join(os.path.dirname(__file__), 'alembic.ini')
        )
        alembic_conf.set_main_option('script_location',
                                     'ostf_adapter.storage.sql:migrations')
        alembic_conf.set_main_option('sqlalchemy.url', conf.dbpath)
        getattr(command, 'upgrade')(alembic_conf, 'head')
        return 0
    except Exception:
        log.exception('Migration failed')
        return 1