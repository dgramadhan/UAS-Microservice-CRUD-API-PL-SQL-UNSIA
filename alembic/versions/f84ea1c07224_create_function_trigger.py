"""create function trigger

Revision ID: f84ea1c07224
Revises: b2d3b30a0361
Create Date: 2024-02-11 14:56:21.961716

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f84ea1c07224'
down_revision: Union[str, None] = 'b2d3b30a0361'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() :
    op.execute(
        '''
        CREATE OR REPLACE FUNCTION func_log_changes() RETURNS TRIGGER AS $func_log_changes$
            BEGIN
                IF NEW.username IS DISTINCT FROM OLD.username THEN
                    INSERT INTO log_changes (changed_field, id_user, old_value, new_value)
                    VALUES ('username', NEW.id, OLD.username, NEW.username);
                END IF;
                IF NEW.email IS DISTINCT FROM OLD.email THEN
                    INSERT INTO log_changes (changed_field, id_user, old_value, new_value)
                    VALUES ('email',  NEW.id, OLD.email, NEW.email);
                END IF;
                IF NEW.password IS DISTINCT FROM OLD.password THEN
                    INSERT INTO log_changes (changed_field, id_user, old_value, new_value)
                    VALUES ('password',  NEW.id, OLD.email, NEW.email);
                END IF;
                RETURN NEW;
            END;
        $func_log_changes$ LANGUAGE plpgsql;
        '''
    )


def downgrade() -> None:
    pass
