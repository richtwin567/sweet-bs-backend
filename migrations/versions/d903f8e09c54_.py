"""empty message

Revision ID: d903f8e09c54
Revises: 6707a6f32c07
Create Date: 2021-02-26 16:56:20.917955

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd903f8e09c54'
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
