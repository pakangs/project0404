"""empty message

Revision ID: c2b2c05de454
Revises: 14e1e7e71f99
Create Date: 2024-04-09 15:32:09.372632

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c2b2c05de454'
down_revision = '14e1e7e71f99'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('answer', schema=None) as batch_op:
        batch_op.add_column(sa.Column('update_date', sa.DateTime(), nullable=False))

    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.add_column(sa.Column('update_date', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.drop_column('update_date')

    with op.batch_alter_table('answer', schema=None) as batch_op:
        batch_op.drop_column('update_date')

    # ### end Alembic commands ###
