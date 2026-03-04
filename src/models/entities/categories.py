from src.models.settings.metadata import metadata
from sqlalchemy import Table, Column, Integer, String

Categories = Table(
    "categories",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("name", String, nullable=True),
)