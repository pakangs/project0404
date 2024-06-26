"""empty message

Revision ID: 414991e70d06
Revises: 8227e58fa95d
Create Date: 2024-04-12 09:58:47.900550

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '414991e70d06'
down_revision = '8227e58fa95d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###
