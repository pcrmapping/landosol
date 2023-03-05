from pcconfig import config
from priconne_backend import styles
import pynecone as pc
from priconne_backend.state import State
from priconne_backend.pages import routes

app = pc.App(state=State, style=styles.BASE_STYLE, stylesheets=styles.STYLESHEETS)

for route in routes:
    app.add_page(
        route.component,
        route.path,
        route.title,
        description="A passion project to map all songs from Princess Connect! Re:Dive in osu!"
    )

app.compile()
