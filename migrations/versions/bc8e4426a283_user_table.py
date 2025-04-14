from alembic import op
import sqlalchemy as sa

revision = 'bc8e4426a283'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer, primary_key=True),
                    sa.Column('fullname', sa.String(80), nullable=False),
                    sa.Column('email', sa.String(120), unique=True, nullable=False),
                    sa.Column('password_hash', sa.String(200), nullable=False),
                    sa.Column('role', sa.String(20), nullable=False),
                    sa.Column('created_at', sa.Integer, nullable=True),
                    sa.CheckConstraint("role in ('admin', 'user')", name='check_user_role')
                    )
    pass

def downgrade():
    op.drop_table('users')
    pass

