"""remove payment id

Revision ID: bf731d6eed88
Revises: 1984242fe9b2
Create Date: 2024-02-22 10:52:26.332676

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bf731d6eed88'
down_revision: Union[str, None] = '1984242fe9b2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
