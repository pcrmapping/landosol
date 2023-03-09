import pynecone as pc

def footer():
    return pc.box(
        pc.vstack(
            pc.text("The PriConne Mapping Project is not associated with Cygames or Nippon Columbia, Co. Ltd.", as_="small"),
            pc.text("(But if anyone there sees this and would like to get in touch, feel free!)", as_="small")
        )    
    )