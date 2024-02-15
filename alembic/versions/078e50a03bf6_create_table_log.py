"""create table log

Revision ID: 078e50a03bf6
Revises: f84ea1c07224
Create Date: 2024-02-11 14:59:07.693653

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '078e50a03bf6'
down_revision: Union[str, None] = 'f84ea1c07224'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.execute(
        '''
        CREATE TABLE log_changes (
            id SERIAL PRIMARY KEY,
            changed_field VARCHAR(255),
            id_user VARCHAR(255),
            old_value VARCHAR(255),
            new_value VARCHAR(255),
            log_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        '''
    )


def downgrade() :
    op.execute('DROP TABLE log_changes')
