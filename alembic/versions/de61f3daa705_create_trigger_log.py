"""create trigger log

Revision ID: de61f3daa705
Revises: 2883455bf414
Create Date: 2024-02-11 16:29:24.696088

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'de61f3daa705'
down_revision: Union[str, None] = '2883455bf414'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() :
    op.execute(
        '''
        CREATE TRIGGER log_changes_trigger
        AFTER UPDATE ON users
        FOR EACH ROW
        EXECUTE FUNCTION func_log_changes();
        '''
    )


def downgrade() -> None:
    pass
