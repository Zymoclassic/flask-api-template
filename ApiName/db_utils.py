from ApiName import db

def query_one_filtered(table, **kwargs):
    """Query a single item from the table based on filters."""
    return db.session.query(table).filter_by(**kwargs).first()


def query_all_filtered(table, **kwargs):
    """Query all items from the table based on filters."""
    return db.session.query(table).filter_by(**kwargs).all()


def query_one(table):
    """Query a single item from the table."""
    return db.session.query(table).first()


def query_all(table):
    """Query all items from the table."""
    return db.session.query(table).all()


def query_paginated(table, page):
    """Query paginated items from the table."""
    per_page = 10
    return db.session.query(table).order_by(table.createdAt.desc()).paginate(page, per_page, False)


def query_paginate_filtered(table, page, **kwargs):
    """Query paginated items from the table based on filters."""
    per_page = 10
    return db.session.query(table).filter_by(**kwargs).order_by(table.createdAt.desc()).paginate(page, per_page, False, 10)

from pydantic import BaseModel
from uuid import UUID


class IdSchema(BaseModel):
    id: UUID

