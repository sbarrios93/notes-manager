from src import build, utils
from src.structs import Area
from pathlib import Path
import yaml
from enum import Enum


import click


ROOT = Path(__file__).parent.absolute()
# Read structure and config info from this file
CONFIG_FILE = "notes.yaml"

# Structure file notes.yaml should be at the root level of the folder. [same level as main.py]
CONFIG_FILE_PATH = ROOT / CONFIG_FILE
assert (
    CONFIG_FILE_PATH.exists()
), f"Config file {CONFIG_FILE} was not found at expected location. Should be at root level"

PATH_HIDDEN_FILE = ".meta.yaml"
PATH_HIDDEN_FILE_PATH = ROOT / PATH_HIDDEN_FILE


def get_topics():
    cfg = utils.load_config(PATH_HIDDEN_FILE)
    return {k: v for k, v in cfg.items()}


def get_aliases():
    return [topic["alias"] for topic in get_topics().values()]


@click.command()
@click.option(
    "--topic",
    "topic",
    type=click.Choice(get_aliases(), case_sensitive=False),
    prompt="What topic do you want to create?",
)
def make_note(
    topic,
):
    print(f"Making note for {topic}")


if __name__ == "__main__":
    make_note()  # Replace typer.run() with app()
