"""add attractions table

Revision ID: 133999a7ea20
Revises: 792c5f21dfe8
Create Date: 2021-11-07 23:49:10.569175

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '133999a7ea20'
down_revision = '792c5f21dfe8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('events_attractions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('event_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('map_id', sa.String(), nullable=True),
    sa.Column('map_category', sa.String(), nullable=True),
    sa.Column('geo_data', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.Column('recommended_activity_ind', sa.Boolean(), nullable=True),
    sa.Column('queue_time_display', sa.String(), nullable=True),
    sa.Column('virtual_queue_ind', sa.Boolean(), nullable=True),
    sa.Column('paid_skip_the_line', sa.String(), nullable=True),
    sa.Column('special_operating_time_ind', sa.Boolean(), nullable=True),
    sa.Column('show_duration', sa.String(), nullable=True),
    sa.Column('opening_time', sa.String(), nullable=True),
    sa.Column('closing_time', sa.String(), nullable=True),
    sa.Column('spot_times', sa.String(), nullable=True),
    sa.Column('food_ordering_ind', sa.Boolean(), nullable=True),
    sa.Column('food_menu', sa.String(), nullable=True),
    sa.Column('activity_rating', sa.Integer(), nullable=True),
    sa.Column('target_market', sa.String(), nullable=True),
    sa.Column('height_requirement', sa.Integer(), nullable=True),
    sa.Column('picture', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['event_id'], ['events_event.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_events_attractions_id'), 'events_attractions', ['id'], unique=False)
    op.drop_index('ix_events_event_event_id', table_name='events_event')
    op.drop_index('ix_events_event_rating_id', table_name='events_event')
    op.drop_constraint('events_event_rating_id_fkey', 'events_event', type_='foreignkey')
    op.drop_column('events_event', 'event_id')
    op.drop_column('events_event', 'rating_id')
    op.add_column('rating', sa.Column('score', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('rating', 'score')
    op.add_column('events_event', sa.Column('rating_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('events_event', sa.Column('event_id', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.create_foreign_key('events_event_rating_id_fkey', 'events_event', 'rating', ['rating_id'], ['id'])
    op.create_index('ix_events_event_rating_id', 'events_event', ['rating_id'], unique=False)
    op.create_index('ix_events_event_event_id', 'events_event', ['event_id'], unique=False)
    op.drop_index(op.f('ix_events_attractions_id'), table_name='events_attractions')
    op.drop_table('events_attractions')
    # ### end Alembic commands ###