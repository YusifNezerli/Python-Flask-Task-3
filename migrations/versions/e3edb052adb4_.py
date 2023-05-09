"""empty message

Revision ID: e3edb052adb4
Revises: 0f08ccd9760b
Create Date: 2023-05-06 11:14:48.610066

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e3edb052adb4'
down_revision = '0f08ccd9760b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('producer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('movie', schema=None) as batch_op:
        batch_op.alter_column('imdb',
               existing_type=mysql.DECIMAL(precision=2, scale=2),
               type_=sa.Float(),
               nullable=False)
        batch_op.alter_column('producer',
               existing_type=mysql.VARCHAR(length=100),
               type_=sa.Integer(),
               nullable=False)
        batch_op.create_foreign_key(None, 'producer', ['producer'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('movie', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.alter_column('producer',
               existing_type=sa.Integer(),
               type_=mysql.VARCHAR(length=100),
               nullable=True)
        batch_op.alter_column('imdb',
               existing_type=sa.Float(),
               type_=mysql.DECIMAL(precision=2, scale=2),
               nullable=True)

    op.drop_table('producer')
    # ### end Alembic commands ###
