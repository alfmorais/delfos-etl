from typing import Annotated

from sqlalchemy import JSON, BigInteger, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.utils.base import Base

intpk = Annotated[int, mapped_column(primary_key=True, unique=True)]
string_mapped = Annotated[str, mapped_column(String(512), nullable=False)]


class Signal(Base):
    __tablename__ = "signal"

    id: Mapped[intpk]
    name: Mapped[string_mapped]

    data: Mapped[list["Data"]] = relationship("Data", back_populates="signal")


class Data(Base):
    __tablename__ = "data"

    id: Mapped[intpk]
    value: Mapped[dict] = mapped_column(JSON)
    timestamp: Mapped[int] = mapped_column(BigInteger)
    signal_id: Mapped[int] = mapped_column(ForeignKey("signal.id"))

    signal: Mapped[Signal] = relationship("Signal", back_populates="data")

    def __repr__(self) -> str:
        return f"Data[id={self.id}, timestamp={self.timestamp}]"
