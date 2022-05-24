"""empty message

Revision ID: 9bd74d2cd513
Revises: 0036831f9eb7
Create Date: 2022-05-20 12:30:27.386693

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "9bd74d2cd513"
down_revision = "0036831f9eb7"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "project_param",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("key", sa.String(length=500), nullable=True),
        sa.Column("value", sa.String(length=8000), nullable=True),
        sa.Column("project_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["project_id"],
            ["project.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_project_param_id"), "project_param", ["id"], unique=False)
    op.create_index(
        op.f("ix_project_param_project_id"),
        "project_param",
        ["project_id"],
        unique=False,
    )
    op.drop_index("ix_project_params_id", table_name="project_params")
    op.drop_index("ix_project_params_project_id", table_name="project_params")
    op.drop_table("project_params")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "project_params",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("key", sa.VARCHAR(length=500), autoincrement=False, nullable=True),
        sa.Column("value", sa.VARCHAR(length=8000), autoincrement=False, nullable=True),
        sa.Column("project_id", sa.INTEGER(), autoincrement=False, nullable=True),
        sa.ForeignKeyConstraint(
            ["project_id"], ["project.id"], name="project_params_project_id_fkey"
        ),
        sa.PrimaryKeyConstraint("id", name="project_params_pkey"),
    )
    op.create_index(
        "ix_project_params_project_id", "project_params", ["project_id"], unique=False
    )
    op.create_index("ix_project_params_id", "project_params", ["id"], unique=False)
    op.drop_index(op.f("ix_project_param_project_id"), table_name="project_param")
    op.drop_index(op.f("ix_project_param_id"), table_name="project_param")
    op.drop_table("project_param")
    # ### end Alembic commands ###
