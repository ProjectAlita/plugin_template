import uuid
from datetime import datetime

from tools import db_tools, db, config as c
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, DateTime, func



class MyTable(db.Base):
    __tablename__ = 'my_test_table'
    __table_args__ = (
        {'schema': c.POSTGRES_TENANT_SCHEMA},
    )
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    uuid: Mapped[str] = mapped_column(UUID(as_uuid=True), unique=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String, nullable=False)
    meta: Mapped[dict] = mapped_column(JSONB, nullable=False, default=dict)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=True, onupdate=func.now())
