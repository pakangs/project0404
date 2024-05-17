"""empty message

Revision ID: 451b58349c33
Revises: 51fbbab44726
Create Date: 2024-04-09 11:59:53.396033

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '451b58349c33'
down_revision = '51fbbab44726'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('_alembic_tmp_product')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('_alembic_tmp_product',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('shop_id', sa.INTEGER(), nullable=True),
    sa.Column('name', sa.VARCHAR(), nullable=False),
    sa.Column('cost', sa.INTEGER(), nullable=False),
    sa.Column('manufacturing_date', sa.DATETIME(), nullable=False),
    sa.Column('expiration_date', sa.DATETIME(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['shop_id'], ['shop.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='fk_product_user_id_user', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
