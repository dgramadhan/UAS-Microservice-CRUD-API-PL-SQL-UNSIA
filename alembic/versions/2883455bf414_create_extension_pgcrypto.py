"""create extension pgcrypto

Revision ID: 2883455bf414
Revises: 078e50a03bf6
Create Date: 2024-02-11 15:16:24.519422

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2883455bf414'
down_revision: Union[str, None] = '078e50a03bf6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
     op.execute(
        '''
        CREATE EXTENSION IF NOT EXISTS pgcrypto;
        '''
    )


def downgrade() -> None:
    pass
