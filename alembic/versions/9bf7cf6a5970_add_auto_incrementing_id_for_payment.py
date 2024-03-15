"""add auto incrementing id for payment

Revision ID: 9bf7cf6a5970
Revises: bf731d6eed88
Create Date: 2024-02-22 10:55:31.929148

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9bf7cf6a5970'
down_revision: Union[str, None] = 'bf731d6eed88'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
