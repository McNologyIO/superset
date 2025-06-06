# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
"""add_alerts

Revision ID: 2f1d15e8a6af
Revises: a72cb0ebeb22
Create Date: 2020-05-26 23:21:50.059635

"""

import sqlalchemy as sa
from alembic import op

from superset.migrations.shared.utils import create_table

# revision identifiers, used by Alembic.
revision = "2f1d15e8a6af"
down_revision = "a72cb0ebeb22"


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    create_table(
        "alerts",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("label", sa.String(length=150), nullable=False),
        sa.Column("active", sa.Boolean(), nullable=True),
        sa.Column("crontab", sa.String(length=50), nullable=True),
        sa.Column("sql", sa.Text(), nullable=True),
        sa.Column("alert_type", sa.String(length=50), nullable=True),
        sa.Column("log_retention", sa.Integer(), nullable=False, default=90),
        sa.Column("grace_period", sa.Integer(), nullable=False, default=60 * 60 * 24),
        sa.Column("recipients", sa.Text(), nullable=True),
        sa.Column("slice_id", sa.Integer(), nullable=True),
        sa.Column("database_id", sa.Integer(), nullable=False),
        sa.Column("dashboard_id", sa.Integer(), nullable=True),
        sa.Column("last_eval_dttm", sa.DateTime(), nullable=True),
        sa.Column("last_state", sa.String(length=10), nullable=True),
        sa.ForeignKeyConstraint(
            ["dashboard_id"],
            ["dashboards.id"],
        ),
        sa.ForeignKeyConstraint(
            ["slice_id"],
            ["slices.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_alerts_active"), "alerts", ["active"], unique=False)
    create_table(
        "alert_logs",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("scheduled_dttm", sa.DateTime(), nullable=True),
        sa.Column("dttm_start", sa.DateTime(), nullable=True),
        sa.Column("dttm_end", sa.DateTime(), nullable=True),
        sa.Column("alert_id", sa.Integer(), nullable=True),
        sa.Column("state", sa.String(length=10), nullable=True),
        sa.ForeignKeyConstraint(
            ["alert_id"],
            ["alerts.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    create_table(
        "alert_owner",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.Column("alert_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["alert_id"],
            ["alerts.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["ab_user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade():
    op.drop_index(op.f("ix_alerts_active"), table_name="alerts")
    op.drop_table("alert_owner")
    op.drop_table("alert_logs")
    op.drop_table("alerts")
