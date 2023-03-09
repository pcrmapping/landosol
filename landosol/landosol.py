from pcconfig import config
from landosol import styles
import pynecone as pc
from landosol.state import State
from landosol.pages import routes

app = pc.App(state=State, style=styles.BASE_STYLE, stylesheets=styles.STYLESHEETS)

for route in routes:
    app.add_page(
        route.component,
        route.path,
        route.title,
        description="A passion project to map all songs from Princess Connect! Re:Dive in osu!"
    )

app.compile()
