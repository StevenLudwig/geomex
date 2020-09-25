"""empty message

Revision ID: 0d8f7e3deefd
Revises: 
Create Date: 2020-09-25 07:18:49.310110

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0d8f7e3deefd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('state',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=90), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('municipality',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=90), nullable=False),
    sa.Column('state_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['state_id'], ['state.id'], name='fk_state__municipality'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('neighborhood',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=90), nullable=False),
    sa.Column('postal_code', sa.String(length=5), nullable=False),
    sa.Column('municipality_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['municipality_id'], ['municipality.id'], name='fk_municipality__neighborhood'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_neighborhood_postal_code'), 'neighborhood', ['postal_code'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_neighborhood_postal_code'), table_name='neighborhood')
    op.drop_table('neighborhood')
    op.drop_table('municipality')
    op.drop_table('state')
    # ### end Alembic commands ###