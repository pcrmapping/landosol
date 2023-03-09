import pynecone as pc
from landosol.pages import routes

def header():
    return pc.box(
        pc.hstack(
            pc.text("GM"),
        ),
        bg="rgba(204, 204, 204, 0.75)",
        position="sticky",
        width="100%",
        top="0px",
        z_index="99",
        backdrop_filter="blur(10px)",
        padding_y=["0.8em", "0.8em", "0.5em"]
    )