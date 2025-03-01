from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    
    id = Column(String, primary_key=True)
    age = Column(Integer)

class Progress(Base):
    __tablename__ = "progress"
    
    user_id = Column(String, ForeignKey("user.id"), primary_key=True)
    exercise_slug = Column(String, primary_key=True)
    completed = Column(Boolean, nullable=False, default=False)
    completed_at = Column(DateTime(timezone=True))
    attempts = Column(Integer, nullable=False, default=0)
    last_attempted_code = Column(String)

class Achievement(Base):
    __tablename__ = "achievement"
    
    id = Column(Integer, primary_key=True)
    slug = Column(String, nullable=False, unique=True)
    title = Column(String, nullable=False)
    description = Column(String)
    criteria = Column(String, nullable=False)  # JSON string of requirements

class UserAchievement(Base):
    __tablename__ = "user_achievement"
    
    user_id = Column(String, ForeignKey("user.id"), primary_key=True)
    achievement_id = Column(Integer, ForeignKey("achievement.id"), primary_key=True)
    unlocked_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())