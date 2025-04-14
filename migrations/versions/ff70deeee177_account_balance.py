from alembic import op
import sqlalchemy as sa


revision = 'ff70deeee177'
down_revision = 'bc8e4426a283'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('accounts'
                    ,sa.Column('id', sa.Integer(), primary_key=True),
                    sa.Column('user_id', sa.Integer(), nullable=False),
                    sa.Column('balance', sa.Float(), nullable=False),
                    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),)

    pass


def downgrade():
    op.drop_table('accounts')
    pass
