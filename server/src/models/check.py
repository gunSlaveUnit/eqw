import datetime

from sqlalchemy import Column, String, Boolean,  Integer, ForeignKey
from sqlalchemy.orm import relationship

from server.src.models.entity import Entity


class Check(Entity):
    __tablename__ = "searches"

    result = Column(String, index=True, nullable=False)
    is_attack = Column(Boolean, nullable=False, default=False)
    type_id = Column(Integer, ForeignKey("attacks.id"), index=True)
    person_id = Column(Integer, ForeignKey("users.id"), index=True)
