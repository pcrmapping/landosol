import pynecone as pc
from landosol.utils.template import content_page

def placeholder():
    WELCOME_BLURB = """
    **Hello there!** Welcome to the home of the *Princess Connect Re:Dive* mapping project.
    Our goal is getting most, if not all reasonably mappable songs from the franchise onto *osu!*.
    """

    return pc.box(
        pc.heading("PriConne Mapping Project"),
        pc.markdown(WELCOME_BLURB)
    )

@content_page(path="/")
def index() -> pc.Component:
    """Homepage"""
    return pc.box(
        placeholder()
    )