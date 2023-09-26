"""Init migration

Revision ID: b26e282722ba
Revises: 
Create Date: 2023-09-17 16:20:03.417472

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'b26e282722ba'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tweets', sa.Column('author_id', sa.Integer(), nullable=True))
    op.add_column('tweets', sa.Column('likes_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'tweets', 'users', ['author_id'], ['id'])
    op.create_foreign_key(None, 'tweets', 'users', ['likes_id'], ['id'])
    op.drop_column('tweets', 'likes')
    op.drop_column('tweets', 'author')
    op.add_column('users', sa.Column('followers_id', sa.Integer(), nullable=True))
    op.add_column('users', sa.Column('following_id', sa.Integer(), nullable=True))
    op.drop_column('users', 'following')
    op.drop_column('users', 'followers')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('followers', postgresql.ARRAY(postgresql.JSON(astext_type=sa.Text())), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('following', postgresql.ARRAY(postgresql.JSON(astext_type=sa.Text())), autoincrement=False, nullable=True))
    op.drop_column('users', 'following_id')
    op.drop_column('users', 'followers_id')
    op.add_column('tweets', sa.Column('author', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=True))
    op.add_column('tweets', sa.Column('likes', postgresql.ARRAY(postgresql.JSON(astext_type=sa.Text())), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'tweets', type_='foreignkey')
    op.drop_constraint(None, 'tweets', type_='foreignkey')
    op.drop_column('tweets', 'likes_id')
    op.drop_column('tweets', 'author_id')
    # ### end Alembic commands ###
