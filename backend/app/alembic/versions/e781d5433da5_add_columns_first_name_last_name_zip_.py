"""Add columns first_name, last_name, zip_code, phone_number to User model

Revision ID: e781d5433da5
Revises: 80798de367bd
Create Date: 2021-05-17 22:05:08.466383

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e781d5433da5'
down_revision = '80798de367bd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('zip_code', sa.BIGINT(), nullable=True))
    op.drop_index('ix_user_full_name', table_name='user')
    op.create_index(op.f('ix_user_zip_code'), 'user', ['zip_code'], unique=False)
    op.drop_column('user', 'full_name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('full_name', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_index(op.f('ix_user_zip_code'), table_name='user')
    op.create_index('ix_user_full_name', 'user', ['full_name'], unique=False)
    op.drop_column('user', 'zip_code')
    # ### end Alembic commands ###
