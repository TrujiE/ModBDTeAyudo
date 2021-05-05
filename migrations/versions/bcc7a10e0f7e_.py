"""empty message

Revision ID: bcc7a10e0f7e
Revises: 
Create Date: 2021-05-05 11:50:13.114628

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bcc7a10e0f7e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('communes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name_region', sa.String(length=100), nullable=False),
    sa.Column('name_commune', sa.String(length=150), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('services',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name_service', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('rut', sa.String(length=10), nullable=True),
    sa.Column('email', sa.String(length=30), nullable=False),
    sa.Column('password', sa.String(length=10), nullable=False),
    sa.Column('full_name', sa.String(length=60), nullable=False),
    sa.Column('last_name', sa.String(length=90), nullable=False),
    sa.Column('phone', sa.Integer(), nullable=False),
    sa.Column('address', sa.String(length=150), nullable=False),
    sa.Column('id_commune', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_commune'], ['communes.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('rut')
    )
    op.create_table('profile',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('role', sa.String(length=15), nullable=False),
    sa.Column('question', sa.String(length=100), nullable=True),
    sa.Column('answer', sa.String(length=200), nullable=True),
    sa.Column('attention_communes', sa.String(length=200), nullable=True),
    sa.Column('experience', sa.String(length=200), nullable=True),
    sa.Column('id_user', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_user'], ['user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('availability',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.String(length=10), nullable=False),
    sa.Column('hour', sa.String(length=10), nullable=False),
    sa.Column('id_profile', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_profile'], ['profile.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ratings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_profile', sa.Integer(), nullable=False),
    sa.Column('rating', sa.Integer(), nullable=False),
    sa.Column('profile_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['profile_id'], ['profile.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', 'id_profile')
    )
    op.create_table('requests',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_commune', sa.Integer(), nullable=False),
    sa.Column('request_status', sa.String(length=10), nullable=False),
    sa.Column('full_name', sa.String(length=60), nullable=False),
    sa.Column('last_name', sa.String(length=90), nullable=False),
    sa.Column('contact_phone', sa.Integer(), nullable=False),
    sa.Column('address', sa.String(length=150), nullable=False),
    sa.Column('date', sa.String(length=10), nullable=False),
    sa.Column('hour', sa.String(length=10), nullable=False),
    sa.Column('id_profile', sa.Integer(), nullable=True),
    sa.Column('id_service', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_profile'], ['profile.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['id_service'], ['services.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('requests')
    op.drop_table('ratings')
    op.drop_table('availability')
    op.drop_table('profile')
    op.drop_table('user')
    op.drop_table('services')
    op.drop_table('communes')
    # ### end Alembic commands ###
