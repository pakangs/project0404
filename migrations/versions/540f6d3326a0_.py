"""empty message

Revision ID: 540f6d3326a0
Revises: 975a9759cb97
Create Date: 2024-04-08 11:03:20.900973

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '540f6d3326a0'
down_revision = '975a9759cb97'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=150), nullable=False),
    sa.Column('password', sa.String(length=300), nullable=False),
    sa.Column('email', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
