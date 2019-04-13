"""empty message

Revision ID: a12f9fc86c4f
Revises: 
Create Date: 2019-04-13 13:14:53.209758

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a12f9fc86c4f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('createTime', sa.DateTime(), nullable=True),
    sa.Column('title', sa.Text(), nullable=True),
    sa.Column('editTime', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('todo')
    # ### end Alembic commands ###
