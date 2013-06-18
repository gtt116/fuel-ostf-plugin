"""Initial migration

Revision ID: b739e5a3653
Revises: None
Create Date: 2013-06-17 18:05:10.265315

"""

# revision identifiers, used by Alembic.
revision = 'b739e5a3653'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('test_runs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tests',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=512), nullable=True),
    sa.Column('status', sa.String(length=128), nullable=True),
    sa.Column('taken', sa.Float(), nullable=True),
    sa.Column('data', sa.Text(), nullable=True),
    sa.Column('test_run_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['test_run_id'], ['test_runs.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tests')
    op.drop_table('test_runs')
    ### end Alembic commands ###