"""add content column to post table

Revision ID: 6766900aac1e
Revises: 7c16a13df9dc
Create Date: 2022-02-20 20:26:10.301373

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6766900aac1e'
down_revision = '7c16a13df9dc'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column("posts", "content")
    pass
