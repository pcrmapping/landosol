import pynecone as pc

def footer():
    return pc.box(
        pc.vstack(
            pc.text("The PriConne Mapping Project is not associated with Cygames or Nippon Columbia, Co. Ltd. Please don't sue me, thanks.", color="deepslategrey"),
            pc.text("A passion project by <a href='https://til.pm'>tilda</a>.")
        )    
    )