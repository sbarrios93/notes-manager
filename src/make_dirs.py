def get_topics():
    cfg = utils.load_config(PATH_HIDDEN_FILE)
    return {k: v for k, v in cfg.items()}


def get_aliases():
    return [topic["alias"] for topic in get_topics().values()]
