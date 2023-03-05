import pynecone as pc

class Mapset(pc.Model, table=True):
    set_id: int
    artist: str
    title: str

class OsuUser(pc.Model, table=True):
    user_id: int
    username: str
    joined: bool
    mapsets: list[Mapset]