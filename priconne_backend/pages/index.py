import pynecone as pc
from priconne_backend.utils.template import content_page

def placeholder():
    return pc.box(
        pc.text('Hello!')
    )

@content_page(path="/")
def index() -> pc.Component:
    """Homepage"""
    return pc.box(
        placeholder()
    )