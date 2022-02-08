"""Add columns first_name, last_name, zip_code, phone_number to User model

Revision ID: 48872b8033a3
Revises: e8a0f31f3119
Create Date: 2021-05-17 23:09:33.599433

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '48872b8033a3'
down_revision = 'e8a0f31f3119'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('zip_code', sa.BigInteger(), nullable=True))
    op.create_index(op.f('ix_user_zip_code'), 'user', ['zip_code'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_zip_code'), table_name='user')
    op.drop_column('user', 'zip_code')
    # ### end Alembic commands ###
