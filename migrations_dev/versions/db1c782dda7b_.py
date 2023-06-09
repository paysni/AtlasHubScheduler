"""empty message

Revision ID: db1c782dda7b
Revises: 1759736c94df
Create Date: 2023-06-09 08:49:05.133912

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'db1c782dda7b'
down_revision = '1759736c94df'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email_completion_subject', sa.String(length=8000), nullable=True))
        batch_op.add_column(sa.Column('email_error_subject', sa.String(length=8000), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.drop_column('email_error_subject')
        batch_op.drop_column('email_completion_subject')

    # ### end Alembic commands ###
