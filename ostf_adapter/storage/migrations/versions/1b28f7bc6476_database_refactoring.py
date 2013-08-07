"""Database refactoring

Revision ID: 1b28f7bc6476
Revises: 4e9905279776
Create Date: 2013-08-07 13:20:06.373200

"""

# revision identifiers, used by Alembic.
revision = '1b28f7bc6476'
down_revision = '4e9905279776'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from ostf_adapter.storage import fields


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('test_runs', sa.Column('test_set_id', sa.String(length=128),
                                         nullable=True))
    op.add_column('test_runs',
                  sa.Column('meta', fields.JsonField(), nullable=True))
    op.add_column('test_runs',
                  sa.Column('cluster_id', sa.Integer(), nullable=False))
    op.drop_column('test_runs', u'type')
    op.drop_column('test_runs', u'stats')
    op.drop_column('test_runs', u'external_id')
    op.drop_column('test_runs', u'data')
    op.alter_column('test_runs', 'status',
                    existing_type=sa.VARCHAR(length=128),
                    nullable=False)
    op.add_column('test_sets', sa.Column('cleanup_path', sa.String(length=128),
                                         nullable=True))
    op.add_column('test_sets',
                  sa.Column('meta', fields.JsonField(), nullable=True))
    op.add_column('test_sets',
                  sa.Column('driver', sa.String(length=128), nullable=True))
    op.add_column('test_sets',
                  sa.Column('additional_arguments', fields.ListField(),
                            nullable=True))
    op.add_column('test_sets',
                  sa.Column('test_path', sa.String(length=256), nullable=True))
    op.drop_column('test_sets', u'data')
    op.add_column('tests', sa.Column('description', sa.Text(), nullable=True))
    op.add_column('tests', sa.Column('traceback', sa.Text(), nullable=True))
    op.add_column('tests', sa.Column('step', sa.Integer(), nullable=True))
    op.add_column('tests', sa.Column('meta', fields.JsonField(), nullable=True))
    op.add_column('tests',
                  sa.Column('duration', sa.String(length=512), nullable=True))
    op.add_column('tests', sa.Column('message', sa.Text(), nullable=True))
    op.add_column('tests',
                  sa.Column('time_taken', sa.Float(), nullable=True))
    op.drop_column('tests', u'taken')
    op.drop_column('tests', u'data')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tests', sa.Column(u'data', sa.TEXT(), nullable=True))
    op.add_column('tests', sa.Column(u'taken',
                                     postgresql.DOUBLE_PRECISION(precision=53),
                                     nullable=True))
    op.drop_column('tests', 'time_taken')
    op.drop_column('tests', 'message')
    op.drop_column('tests', 'duration')
    op.drop_column('tests', 'meta')
    op.drop_column('tests', 'step')
    op.drop_column('tests', 'traceback')
    op.drop_column('tests', 'description')
    op.add_column('test_sets', sa.Column(u'data', sa.TEXT(), nullable=True))
    op.drop_column('test_sets', 'test_path')
    op.drop_column('test_sets', 'additional_arguments')
    op.drop_column('test_sets', 'driver')
    op.drop_column('test_sets', 'meta')
    op.drop_column('test_sets', 'cleanup_path')
    op.alter_column('test_runs', 'status',
                    existing_type=sa.VARCHAR(length=128),
                    nullable=True)
    op.add_column('test_runs', sa.Column(u'data', sa.TEXT(), nullable=True))
    op.add_column('test_runs',
                  sa.Column(u'external_id', sa.VARCHAR(length=128),
                            nullable=True))
    op.add_column('test_runs', sa.Column(u'stats', sa.TEXT(), nullable=True))
    op.add_column('test_runs',
                  sa.Column(u'type', sa.VARCHAR(length=128), nullable=True))
    op.drop_column('test_runs', 'cluster_id')
    op.drop_column('test_runs', 'meta')
    op.drop_column('test_runs', 'test_set_id')
    ### end Alembic commands ###
