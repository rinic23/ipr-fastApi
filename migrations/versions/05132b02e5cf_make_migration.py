"""make migration

Revision ID: 05132b02e5cf
Revises: 563a8ea5555e
Create Date: 2021-03-07 15:55:04.080866

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '05132b02e5cf'
down_revision = '563a8ea5555e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'password')
    # ### end Alembic commands ###
