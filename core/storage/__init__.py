from core.storage import sql_storage
from oslo.config import cfg
import logging

log = logging.getLogger(__name__)

CONF = cfg.CONF

STORAGE_OPTS = [
    cfg.StrOpt('database_connection',
               default='sqlite://',
               help='Database connection string',
               ),
]

CONF.register_opts(STORAGE_OPTS)


def get_storage():
    log.info('GET STORAGE FOR - %s' % cfg.CONF.database_connection)
    return sql_storage.SqlStorage(cfg.CONF.database_connection)