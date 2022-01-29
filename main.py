from distutils.command.config import config
from pathlib import Path
import click
import yaml


CONFIG_FILE_NAME = "notes.yaml"


def load_config(config_file_name=CONFIG_FILE_NAME):
    assert Path(
        config_file_name
    ).exists(), f"Config file {config_file_name} was not found at expected location. Should be at root level"

    return yaml.load(open(config_file_name), Loader=yaml.SafeLoader)


@click.command()
@click.option(
    "--topic",
    "topic",
    type=click.Choice(get_aliases(), case_sensitive=False),
    prompt="What topic do you want to create?",
)
def run(
    topic,
):
    print(f"Making note for {topic}")


if __name__ == "__main__":

    # config has all the paths and notes structures
    # this file MUST be at the root level folder
    config = load_config()

    # assign paths
    config_file_path = Path(CONFIG_FILE_NAME).resolve()
    root_path = config_file_path.parent
    meta_file_path = config["Paths"]["hidden-file"]
    notes_path = config["Paths"]["notes-dir"]

    run()
