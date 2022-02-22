"""create posts table

Revision ID: 7c16a13df9dc
Revises: 
Create Date: 2022-02-20 20:13:44.315438

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c16a13df9dc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("posts", sa.Column("id", sa.Integer(), nullable=False,
                    primary_key=True), sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table("posts")
    pass
