"""empty message

Revision ID: 23f3da432c69
Revises: 86895732dc4a
Create Date: 2019-02-24 17:01:11.106121

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '23f3da432c69'
down_revision = '86895732dc4a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'withdrawal_signal', 'withdrawal', ['debtor_id', 'creditor_id', 'withdrawal_request_seqnum'], ['debtor_id', 'creditor_id', 'withdrawal_request_seqnum'], ondelete='CASCADE')
    op.drop_column('withdrawal_signal', 'operator_branch_id')
    op.drop_column('withdrawal_signal', 'operator_user_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('withdrawal_signal', sa.Column('operator_user_id', sa.BIGINT(), autoincrement=False, nullable=False))
    op.add_column('withdrawal_signal', sa.Column('operator_branch_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'withdrawal_signal', type_='foreignkey')
    # ### end Alembic commands ###
