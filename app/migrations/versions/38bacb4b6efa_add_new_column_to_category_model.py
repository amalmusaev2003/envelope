"""Add new column to category model

Revision ID: 38bacb4b6efa
Revises: 013e8aa6e296
Create Date: 2024-06-26 23:43:01.307102

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '38bacb4b6efa'
down_revision: Union[str, None] = '013e8aa6e296'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('categories', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'categories', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'categories', type_='foreignkey')
    op.drop_column('categories', 'user_id')
    # ### end Alembic commands ###
