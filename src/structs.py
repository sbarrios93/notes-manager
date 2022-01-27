from src import utils


class Area:
    """Area is the top level of the notes structures. It should be a dict containing a type and a list of children. Each children will be a dict"""

    def __init__(self, name, area: dict):

        assert area.get("type", None) is not None, f"Area {name} does not have a notes type"

        self.name = name
        self.type_ = area["type"]
        self.children = self.collect_children(area)
        self.tree_level = 1
        self.path = None
        self.normalized_name = utils.clean_dirname(self.name)

        self.__children_objects = None

    def collect_children(self, area: dict):
        key = "topic"
        # see first if dict has any topic key
        children = area.get(key, None)
        return children

    def expand_children(self):
        if self.children is not None:
            self.__children_objects = {}
            for child in self.children:
                self.__children_objects[child["name"]] = Topic(child, self)

    @property
    def children_objects(self):
        return self.__children_objects


class Topic:
    """Topic is a  directory containing the the markdown files and the figures folder"""

    def __init__(self, topic: dict, parent) -> None:

        self.name = topic.get("name", None)
        self.short_name = topic.get("short", None)
        self.alias = topic.get("alias", None)
        assert None not in [
            self.name,
            self.short_name,
            self.alias,
        ], f"Topic {self.name} does not have a name, short name or alias"

        self.normalized_name = utils.clean_dirname(self.short_name)
        self.parent = parent
        self.parent_name = parent.name

        self.type_ = topic.get("type", parent.type_)
