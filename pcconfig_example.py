import pynecone as pc

# // IMPORTANT!
# Rename me to "pcconfig.py" before attempting dev stuff

config = pc.Config(
    app_name="priconne_backend",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
    secret_key="CHANGE_ME_FUCKER"
)
