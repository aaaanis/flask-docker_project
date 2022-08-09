"""removed foreign key

Revision ID: e940e449eeec
Revises: b34981d6ffb8
Create Date: 2022-04-23 15:35:41.936227

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e940e449eeec'
down_revision = 'b34981d6ffb8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('purchases_buyer_id_fkey', 'purchases', type_='foreignkey')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key('purchases_buyer_id_fkey', 'purchases', 'users', ['buyer_id'], ['id'])
    # ### end Alembic commands ###