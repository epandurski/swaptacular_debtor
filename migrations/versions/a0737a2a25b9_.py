"""empty message

Revision ID: a0737a2a25b9
Revises: 8fbee8027a90
Create Date: 2019-02-24 11:27:21.766025

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a0737a2a25b9'
down_revision = '8fbee8027a90'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('idx_prepared_transfer_sender_creditor_id', table_name='prepared_transfer')
    op.create_index('idx_prepared_transfer_sender_creditor_id', 'prepared_transfer', ['debtor_id', 'sender_creditor_id', 'withdrawal_request_seqnum'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('idx_prepared_transfer_sender_creditor_id', table_name='prepared_transfer')
    op.create_index('idx_prepared_transfer_sender_creditor_id', 'prepared_transfer', ['debtor_id', 'sender_creditor_id'], unique=False)
    # ### end Alembic commands ###