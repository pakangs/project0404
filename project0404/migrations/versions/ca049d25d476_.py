"""empty message

Revision ID: ca049d25d476
Revises: 321724805412
Create Date: 2024-04-12 09:35:09.100551

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ca049d25d476'
down_revision = '321724805412'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('_alembic_tmp_product')
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

    op.create_table('_alembic_tmp_product',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('shop_id', sa.INTEGER(), nullable=True),
    sa.Column('name', sa.VARCHAR(), nullable=False),
    sa.Column('cost', sa.INTEGER(), nullable=False),
    sa.Column('manufacturing_date', sa.DATETIME(), nullable=False),
    sa.Column('expiration_date', sa.DATETIME(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.Column('info', sa.VARCHAR(length=100), nullable=True),
    sa.ForeignKeyConstraint(['shop_id'], ['shop.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='fk_product_user_id_user', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
