"""add last few column of table posts

Revision ID: e79c30747a92
Revises: a178005c4a81
Create Date: 2022-02-22 11:46:55.864951

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e79c30747a92'
down_revision = 'a178005c4a81'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column(
        "published",sa.Boolean(),nullable=False,server_default="TRUE"),
    )
    op.add_column('posts',sa.Column(
        'created_at',sa.TIMESTAMP(timezone=True),nullable= False,server_default=sa.text("NOW()"
    )),)
    pass


def downgrade():
    op.drop_column('posts','published')
    op.drop_column('posts','created_at')

    pass
