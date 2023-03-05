import pynecone as pc
from pynecone.base import Base
from typing import Callable

class Route(Base):
    """A page route."""
    
    path: str # Path of route
    title: str | None = None # Page title
    component: pc.Component | Callable[[], pc.Component] # Component we are rendering