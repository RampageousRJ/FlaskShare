"""Typ

Revision ID: e07d4a5f652f
Revises: 7bcacc44897d
Create Date: 2023-12-22 00:58:59.902832

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e07d4a5f652f'
down_revision = '7bcacc44897d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('people', schema=None) as batch_op:
        batch_op.add_column(sa.Column('type', sa.String(length=128), nullable=False))
        batch_op.alter_column('password_hash',
               existing_type=mysql.VARCHAR(length=1024),
               type_=sa.String(length=128),
               existing_nullable=False)
        batch_op.drop_column('password_hash2')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('people', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password_hash2', mysql.VARCHAR(length=1024), nullable=True))
        batch_op.alter_column('password_hash',
               existing_type=sa.String(length=128),
               type_=mysql.VARCHAR(length=1024),
               existing_nullable=False)
        batch_op.drop_column('type')

    # ### end Alembic commands ###
