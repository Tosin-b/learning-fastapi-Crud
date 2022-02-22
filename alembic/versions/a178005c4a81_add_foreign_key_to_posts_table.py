"""add foreign-key to posts table

Revision ID: a178005c4a81
Revises: ca5426c89ea8
Create Date: 2022-02-22 11:35:46.312779

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a178005c4a81'
down_revision = 'ca5426c89ea8'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("owner_id", sa.Integer(),nullable=False))
    op.create_foreign_key('posts_users_fk',source_table="posts",referent_table="users",local_cols=['owner_id'],remote_cols=['id'],ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint("posts_users_fk", table_name="posts")
    op.drop_column("posts", 'owner_id')
    pass
