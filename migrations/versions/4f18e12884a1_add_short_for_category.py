"""add short for category

Revision ID: 4f18e12884a1
Revises: 
Create Date: 2018-04-15 17:20:37.272993

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4f18e12884a1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tb_category', sa.Column('short', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tb_category', 'short')
    # ### end Alembic commands ###