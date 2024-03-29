"""empty message

Revision ID: 10b9f17adb29
Revises: 526f190d3434
Create Date: 2021-02-27 02:11:03.320764

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '10b9f17adb29'
down_revision = '526f190d3434'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('orders', sa.Column('created_on', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('orders', 'created_on')
    # ### end Alembic commands ###
