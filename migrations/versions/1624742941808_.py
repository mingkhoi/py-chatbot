"""empty message

Revision ID: 1624742941808
Revises: 1624742875772
Create Date: 2021-06-27 04:29:02.479106

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1624742941808'
down_revision = '1624742875772'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'meeting_location', ['name'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'meeting_location', type_='unique')
    # ### end Alembic commands ###