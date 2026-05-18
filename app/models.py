from sqlalchemy import (
    Column,
    BigInteger,
    String,
    Text,
    Date,
    DateTime,
    Enum,
    ForeignKey,
    DECIMAL,
    func,
)
from sqlalchemy.orm import relationship
from app.database import Base


class Task(Base):
    __tablename__ = "task"

    id = Column(BigInteger, primary_key=True, index=True)
    task_date = Column(Date, nullable=False)
    title = Column(String(255), nullable=False)

    description = Column(Text)
    priority = Column(
        Enum("LOW", "MEDIUM", "HIGH", name="task_priority_name"),
        default="MEDIUM",
        nullable=False,
    )

    status = Column(
        Enum(
            "PENDING",
            "IN_PROGRESS",
            "COMPLETED",
            "CARRIED_FORWARD",
            name="task_status_enum",
        ),
        default="PENDING",
        nullable=False,
    )

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )


class Project(Base):
    __tablename__ = "project"

    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    link = Column(Text)

    description = Column(Text)

    status = Column(
        Enum("PENDING", "COMPLETED", "HALTED", name="project_status_enum"),
        default="PENDING",
        nullable=False,
    )

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    works = relationship(
        "ProjectWork", back_populates="project", cascade="all, delete-orphan"
    )


class ProjectWork(Base):
    __tablename__ = "project_work"

    project_id = Column(
        BigInteger, ForeignKey("project.id", ondelete="CASCADE"), primary_key=True
    )
    work_date = Column(Date, primary_key=True)
    description = Column(Text, nullable=False)
    hours_worked = Column(DECIMAL(4, 2))

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    updated_at = Column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    # Relationship
    project = relationship("Project", back_populates="works")


class Journal(Base):
    __tablename__ = "journal"

    journal_date = Column(Date, primary_key=True)
    learning_of_day = Column(Text)
    notes_for_tomorrow = Column(Text)
    reflection = Column(Text)

    mood = Column(Enum("BAD", "AVERAGE", "GOOD", "EXCELLENT", name="mood_enum"))

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    updated_at = Column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )
