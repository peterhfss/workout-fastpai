from src.models.settings.metadata import metadata
from sqlalchemy import Table, Column, Integer, String

Training_center = Table(
    "training_center",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("name", String, nullable=True),
    Column("address", String, nullable=True),
    Column("owner", String, nullable=True),
)