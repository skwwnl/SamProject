from sqlalchemy import BigInteger, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.config.database import Base


class Organization(Base):
    __tablename__ = "organizations"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(64), nullable=False)
    type: Mapped[str] = mapped_column(String(32), nullable=False)
    position: Mapped[str] = mapped_column(String(32), nullable=True)
    teacher_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("teachers.id"), nullable=False)

    # one-to-one 관계
    teacher = relationship("Teacher", back_populates="organization", uselist=False)
