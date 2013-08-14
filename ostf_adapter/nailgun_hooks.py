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

import logging
from ostf_adapter.storage import alembic_cli
from ostf_adapter.nose_plugin import nose_discovery

LOG = logging.getLogger(__name__)


def after_initialization_environment_hook():
    try:
        alembic_cli.do_apply_migrations()
        nose_discovery.discovery()
        return 0
    except Exception:
        LOG.exception('Exception on initialization.')
        return 1