"""Increment memberAge for all members

Revision ID: ${up_revision}
Revises: ${down_revision | comma,n}
Create Date: ${create_date}

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
${imports if imports else ""}

# revision identifiers, used by Alembic.
revision: str = ${repr(up_revision)}
down_revision: Union[str, None] = ${repr(down_revision)}
branch_labels: Union[str, Sequence[str], None] = ${repr(branch_labels)}
depends_on: Union[str, Sequence[str], None] = ${repr(depends_on)}


def upgrade():
op.execute("UPDATE members SET memberAge = memberAge + 1")
    # Additional logic can be added here if needed.
    # For example, you might need to add a new column, index, etc.
    ${upgrades if upgrades else "pass"}

def downgrade():
    """Downgrade script subtracting 1 from memberAge for all members."""
    op.execute("UPDATE members SET memberAge = memberAge - 1")
    # Additional logic for downgrade can be added here if needed.
    # For example, if you added a new column in upgrade, you might drop it here.
    ${downgrades if downgrades else "pass"}
