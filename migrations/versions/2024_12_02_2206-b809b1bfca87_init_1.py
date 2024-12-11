"""init_1

Revision ID: b809b1bfca87
Revises: 5f6307012e03
Create Date: 2024-12-02 22:06:30.389758

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'b809b1bfca87'
down_revision: Union[str, None] = '5f6307012e03'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('images',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('image_path', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('rooms',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=30), nullable=True),
    sa.Column('help_checked', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('external_id', sa.String(length=26), nullable=True),
    sa.Column('email', sa.String(length=64), nullable=False),
    sa.Column('phone', sa.String(length=13), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('profile_image', sa.String(length=255), nullable=True),
    sa.Column('social_provider', sa.Enum('GOOGLE', 'NAVER', 'KAKAO', name='social_provider_enum'), nullable=True),
    sa.Column('first_login', sa.Boolean(), nullable=False),
    sa.Column('role', sa.Enum('STUDENT', 'TEACHER', name='user_role_enum'), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('deactivated_at', sa.DateTime(), nullable=True),
    sa.Column('is_privacy_accepted', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('external_id'),
    sa.UniqueConstraint('phone')
    )
    op.create_table('participants',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('student_id', sa.BigInteger(), nullable=False),
    sa.Column('teacher_id', sa.BigInteger(), nullable=False),
    sa.Column('room_id', sa.BigInteger(), nullable=False),
    sa.ForeignKeyConstraint(['room_id'], ['rooms.id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('posts',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('external_id', sa.String(length=26), nullable=False),
    sa.Column('author_id', sa.BigInteger(), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('visibility', sa.Enum('PUBLIC', 'PRIVATE', 'TEACHER', 'STUDENT', name='visibility'), nullable=False),
    sa.Column('like_count', sa.Integer(), nullable=False),
    sa.Column('comment_count', sa.Integer(), nullable=False),
    sa.Column('is_with_teacher', sa.Boolean(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.CheckConstraint('comment_count >= 0', name='check_positive_comment_count'),
    sa.CheckConstraint('like_count >= 0', name='check_positive_like_count'),
    sa.ForeignKeyConstraint(['author_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('students',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('school', sa.String(length=20), nullable=False),
    sa.Column('grade', sa.Integer(), nullable=False),
    sa.Column('career_aspiration', sa.String(length=30), nullable=True),
    sa.Column('interest', sa.String(length=30), nullable=True),
    sa.Column('description', sa.String(length=25), nullable=True),
    sa.Column('user_id', sa.BigInteger(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tags',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('nickname', sa.String(length=12), nullable=False),
    sa.Column('user_id', sa.BigInteger(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nickname')
    )
    op.create_table('teachers',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.BigInteger(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comments',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('post_id', sa.BigInteger(), nullable=False),
    sa.Column('author_id', sa.BigInteger(), nullable=False),
    sa.Column('content', sa.String(length=300), nullable=False),
    sa.Column('recomment_count', sa.BigInteger(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('parent_comment_id', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['parent_comment_id'], ['comments.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('organizations',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.Column('type', sa.String(length=32), nullable=False),
    sa.Column('position', sa.String(length=32), nullable=True),
    sa.Column('teacher_id', sa.BigInteger(), nullable=False),
    sa.ForeignKeyConstraint(['teacher_id'], ['teachers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('post_images',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('image_id', sa.BigInteger(), nullable=False),
    sa.Column('post_id', sa.BigInteger(), nullable=False),
    sa.ForeignKeyConstraint(['image_id'], ['images.id'], ),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('post_likes',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.BigInteger(), nullable=False),
    sa.Column('post_id', sa.BigInteger(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('study_groups',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('student_id', sa.BigInteger(), nullable=False),
    sa.Column('teacher_id', sa.BigInteger(), nullable=False),
    sa.ForeignKeyConstraint(['student_id'], ['students.id'], ),
    sa.ForeignKeyConstraint(['teacher_id'], ['teachers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comment_tags',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('comment_id', sa.BigInteger(), nullable=False),
    sa.Column('tag_id', sa.BigInteger(), nullable=False),
    sa.ForeignKeyConstraint(['comment_id'], ['comments.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['tag_id'], ['tags.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comment_tags')
    op.drop_table('study_groups')
    op.drop_table('post_likes')
    op.drop_table('post_images')
    op.drop_table('organizations')
    op.drop_table('comments')
    op.drop_table('teachers')
    op.drop_table('tags')
    op.drop_table('students')
    op.drop_table('posts')
    op.drop_table('participants')
    op.drop_table('users')
    op.drop_table('rooms')
    op.drop_table('images')
    # ### end Alembic commands ###
