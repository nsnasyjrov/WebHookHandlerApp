from alembic import op
import sqlalchemy as sa

revision = '1c75748545ad'
down_revision = 'ff70deeee177'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('transactions',
                    sa.Column('id', sa.Integer, primary_key=True),
                    sa.Column('amount', sa.Float, nullable=False),
                    sa.Column('timestamp', sa.Integer, nullable=False),
                    sa.Column('account_id', sa.Integer, nullable=False),
                    sa.ForeignKeyConstraint(['account_id'], ['accounts.id'], ondelete='CASCADE'))
    pass


def downgrade():
    op.drop_table('transactions')
    pass
