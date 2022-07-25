"""empty message

Revision ID: a1511f640ccc
Revises: 6b4c50c71d3d
Create Date: 2022-07-18 12:15:47.014998

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a1511f640ccc'
down_revision = '6b4c50c71d3d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('username', sa.String(length=80), nullable=False))
    op.create_unique_constraint(None, 'user', ['username'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_column('user', 'username')
    # ### end Alembic commands ###
