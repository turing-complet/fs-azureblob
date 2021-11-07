from fs import open_fs
from pathlib import Path


def get_bfs():
    account_name = "jtestwk"
    account_key = "REPLACE_ME"
    container = "scenariodata"
    url = f"azblob://{account_name}:{account_key}@{container}"
    return open_fs(url)


def get_lfs():
    data_dir = Path.home() / "work/plug/standalone/pcm"
    return open_fs(str(data_dir))


bfs = get_bfs()
lfs = get_lfs()


def upload(path):
    with lfs.openbin(path) as f:
        bfs.upload(path, f)


upload("data/output/2_PF.pkl")
upload("data/output/2_PG.pkl")
upload("data/input/2_ct.pkl")
upload("data/input/2_grid.mat")

pf = bfs.getinfo("data/output/2_PF.pkl", namespaces=["details"])
