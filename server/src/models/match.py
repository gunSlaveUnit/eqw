import datetime

from sqlalchemy import Column,  Integer, ForeignKey
from sqlalchemy.orm import relationship

from server.src.models.entity import Entity


class Match(Entity):
    __tablename__ = "matchs"

    attack_id = Column(Integer, ForeignKey("attacks.id"), index=True)
    check_id = Column(Integer, ForeignKey("searches.id"), index=True)

    attack = relationship("Attack", backref="attacks")
    check= relationship("Check", backref="searches")
