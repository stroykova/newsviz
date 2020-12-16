"""create news table

Revision ID: bf1b97c317a9
Revises:
Create Date: 2020-12-16 17:52:41.794539

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "bf1b97c317a9"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'news',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('text', sa.UnicodeText),
    )


def downgrade():
    op.drop_table('news')
