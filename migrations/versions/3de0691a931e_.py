"""empty message

Revision ID: 3de0691a931e
Revises: c2b2c05de454
Create Date: 2024-04-09 15:37:58.996159

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3de0691a931e'
down_revision = 'c2b2c05de454'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('answer', schema=None) as batch_op:
        batch_op.add_column(sa.Column('update_date', sa.DateTime(), nullable=False))

    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.add_column(sa.Column('update_date', sa.DateTime(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.drop_column('update_date')

    with op.batch_alter_table('answer', schema=None) as batch_op:
        batch_op.drop_column('update_date')

    # ### end Alembic commands ###
