from src.models.settings.metadata import metadata
from sqlalchemy import ForeignKey, Table ,Column, Integer, String, Float

Athletes = Table(
    "athletes",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("name", String, nullable=True),
    Column("cpf", String, nullable=True),
    Column("age", Integer),
    Column("height", Float),
    Column("weight", Float),
    Column("gender", String),
    Column("categorie_id", Integer, ForeignKey("categories.id")),
    Column("training_center_id", Integer, ForeignKey("training_center.id")),
)
