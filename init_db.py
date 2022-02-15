from ..shared.db_manager import Base, engine


def init_db():
    # from .models.your_module import YourModel
    Base.metadata.create_all(bind=engine)
