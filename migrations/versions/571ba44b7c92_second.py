"""second

Revision ID: 571ba44b7c92
Revises: 9f2339056995
Create Date: 2021-03-06 12:00:54.767343

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '571ba44b7c92'
down_revision = '9f2339056995'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('microblog_posts', sa.Column('title', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('microblog_posts', 'title')
    # ### end Alembic commands ###
