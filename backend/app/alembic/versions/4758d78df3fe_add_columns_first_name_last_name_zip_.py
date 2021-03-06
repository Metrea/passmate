"""Add columns first_name, last_name, zip_code, phone_number to User model

Revision ID: 4758d78df3fe
Revises: e781d5433da5
Create Date: 2021-05-17 22:36:35.438561

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4758d78df3fe'
down_revision = 'e781d5433da5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_user_phone_number', table_name='user')
    op.drop_index('ix_user_zip_code', table_name='user')
    op.drop_column('user', 'zip_code')
    op.drop_column('user', 'phone_number')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('phone_number', sa.BIGINT(), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('zip_code', sa.BIGINT(), autoincrement=False, nullable=True))
    op.create_index('ix_user_zip_code', 'user', ['zip_code'], unique=False)
    op.create_index('ix_user_phone_number', 'user', ['phone_number'], unique=False)
    # ### end Alembic commands ###
