"""uuid_user_id

Revision ID: 002
Revises: 001_initial
Create Date: 2024-02-09 19:53:00.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic
revision = '002'
down_revision = '001'
branch_labels = None
depends_on = None

def upgrade():
    # Create temporary tables with new schema
    op.create_table(
        'user_new',
        sa.Column('id', sa.String(), nullable=False),
        sa.Column('age', sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    
    op.create_table(
        'progress_new',
        sa.Column('user_id', sa.String(), nullable=False),
        sa.Column('exercise_slug', sa.String(), nullable=False),
        sa.Column('completed', sa.Boolean(), nullable=False, default=False),
        sa.Column('completed_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('attempts', sa.Integer(), nullable=False, default=0),
        sa.Column('last_attempted_code', sa.String(), nullable=True),
        sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
        sa.PrimaryKeyConstraint('user_id', 'exercise_slug')
    )
    
    op.create_table(
        'user_achievement_new',
        sa.Column('user_id', sa.String(), nullable=False),
        sa.Column('achievement_id', sa.Integer(), nullable=False),
        sa.Column('unlocked_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.ForeignKeyConstraint(['achievement_id'], ['achievement.id'], ),
        sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
        sa.PrimaryKeyConstraint('user_id', 'achievement_id')
    )

    # Copy data (converting user_id to string)
    op.execute('INSERT INTO user_new (id, age) SELECT CAST(id AS VARCHAR), age FROM "user"')
    op.execute('INSERT INTO progress_new (user_id, exercise_slug, completed, completed_at, attempts, last_attempted_code) SELECT CAST(user_id AS VARCHAR), exercise_slug, completed, completed_at, attempts, last_attempted_code FROM progress')
    op.execute('INSERT INTO user_achievement_new (user_id, achievement_id, unlocked_at) SELECT CAST(user_id AS VARCHAR), achievement_id, unlocked_at FROM user_achievement')

    # Drop old tables
    op.drop_table('user_achievement')
    op.drop_table('progress')
    op.drop_table('user')

    # Rename new tables to original names
    op.rename_table('user_new', 'user')
    op.rename_table('progress_new', 'progress')
    op.rename_table('user_achievement_new', 'user_achievement')

def downgrade():
    # Note: Downgrade might lose data if any UUIDs can't be converted to integers
    # Create temporary tables with old schema
    op.create_table(
        'user_old',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('age', sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    
    op.create_table(
        'progress_old',
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('exercise_slug', sa.String(), nullable=False),
        sa.Column('completed', sa.Boolean(), nullable=False, default=False),
        sa.Column('completed_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('attempts', sa.Integer(), nullable=False, default=0),
        sa.Column('last_attempted_code', sa.String(), nullable=True),
        sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
        sa.PrimaryKeyConstraint('user_id', 'exercise_slug')
    )
    
    op.create_table(
        'user_achievement_old',
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('achievement_id', sa.Integer(), nullable=False),
        sa.Column('unlocked_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.ForeignKeyConstraint(['achievement_id'], ['achievement.id'], ),
        sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
        sa.PrimaryKeyConstraint('user_id', 'achievement_id')
    )

    # Copy data (attempting to convert UUIDs back to integers)
    op.execute('INSERT INTO user_old (id, age) SELECT CAST(id AS INTEGER), age FROM "user"')
    op.execute('INSERT INTO progress_old (user_id, exercise_slug, completed, completed_at, attempts, last_attempted_code) SELECT CAST(user_id AS INTEGER), exercise_slug, completed, completed_at, attempts, last_attempted_code FROM progress')
    op.execute('INSERT INTO user_achievement_old (user_id, achievement_id, unlocked_at) SELECT CAST(user_id AS INTEGER), achievement_id, unlocked_at FROM user_achievement')

    # Drop new tables
    op.drop_table('user_achievement')
    op.drop_table('progress')
    op.drop_table('user')

    # Rename old tables to original names
    op.rename_table('user_old', 'user')
    op.rename_table('progress_old', 'progress')
    op.rename_table('user_achievement_old', 'user_achievement')