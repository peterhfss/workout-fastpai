from src.models.settings.metadata import metadata
from sqlalchemy import Table, Column, Integer, String, ForeignKey

Addresses = Table(
    "addresses",
    metadata,
    Column("address_id", Integer, primary_key=True),
    Column("address_line1", String, nullable=True),
    Column("address_line2", String, nullable=True),
    Column("city", String, nullable=True),
    Column("state_province", String, nullable=True),
    Column("postal_code", String, nullable=True),
    Column("country", String, nullable=True),
    Column("training_center_id", Integer, ForeignKey("training_center.id")),
)