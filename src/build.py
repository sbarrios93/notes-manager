from pathlib import Path
import yaml
from src.structs import Area
from src import utils


def parse_area(area_name: str, area: dict) -> Area:
    return Area(area_name, area)


def make_dir(parent_dir_path, path_):
    """Create the content directory structure"""
    path_ = parent_dir_path / path_
    path_.mkdir(parents=True, exist_ok=True)
    return True


def get_asset_relative_paths(asset_tree):
    asset_paths = []

    for k, v in asset_tree.items():
        for item in v:
            asset_paths.append("/".join([k, item]))
    return asset_paths


def build_structure(root_path, config_file_path, path_hidden_file_path):
    cfg = utils.load_config(config_file_path)

    notes_dir = cfg["Paths"]["notes-dir"]
    make_dir(root_path, notes_dir)

    asset_tree = cfg["Options"]["asset-tree"]
    asset_paths = get_asset_relative_paths(asset_tree)

    areas = cfg["Area"]

    children_yaml = {}

    for area_name, area in areas.items():
        area = parse_area(area_name, area)
        area.expand_children()
        for child in area.children_objects.values():
            child_path = root_path / notes_dir / area.normalized_name / child.normalized_name
            Path.mkdir(child_path, parents=True, exist_ok=True)
            for asset_path in asset_paths:
                Path.mkdir(child_path / asset_path, parents=True, exist_ok=True)
            children_yaml[child.short_name] = {
                "alias": child.alias,
                "short_name": child.short_name,
                "type": child.type_,
                "parent": child.parent_name,
                "path": str(child_path),
            }

    # save yaml
    with open(path_hidden_file_path, "w") as f:
        f.write(yaml.dump(children_yaml, default_flow_style=False))
