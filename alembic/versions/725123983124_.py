"""empty message

Revision ID: 725123983124
Revises: ff92a9ecb4e2
Create Date: 2025-02-26 10:17:12.009637

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '725123983124'
down_revision: Union[str, None] = 'ff92a9ecb4e2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tbl_users', sa.Column('created_date', sa.DateTime(), nullable=True))
    op.add_column('tbl_users', sa.Column('is_deleted', sa.Boolean(), nullable=True))
    op.add_column('tbl_users', sa.Column('updated_date', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_tbl_users_created_date'), 'tbl_users', ['created_date'], unique=False)
    op.create_index(op.f('ix_tbl_users_is_deleted'), 'tbl_users', ['is_deleted'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_tbl_users_is_deleted'), table_name='tbl_users')
    op.drop_index(op.f('ix_tbl_users_created_date'), table_name='tbl_users')
    op.drop_column('tbl_users', 'updated_date')
    op.drop_column('tbl_users', 'is_deleted')
    op.drop_column('tbl_users', 'created_date')
    # ### end Alembic commands ###
