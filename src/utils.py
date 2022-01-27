"""
Url: https://gist.github.com/wassname/1393c4a57cfcbf03641dbc31886123b8
"""
import unicodedata
import string
import yaml


def load_config(config_file_path):
    """Load the config file into a dict"""
    with open(config_file_path, "r") as ymlfile:
        return yaml.load(ymlfile, Loader=yaml.FullLoader)


def clean_dirname(dirname, replace=" "):
    """
    Replace invalid characters in a string so that it can be used as a
    directory name in the current platform.

    :param dirname: The string to be cleaned.
    :type dirname: str
    :param replace: The string to use as replacement for invalid characters.
    :type replace: str
    :returns: The cleaned up string.
    :rtype: str
    """
    whitelist = "-_.() %s%s" % (string.ascii_letters, string.digits)
    char_limit = 255
    # replace spaces
    if replace:
        for r in replace:
            dirname = dirname.replace(r, "-")
    # keep only valid ascii chars
    cleaned_dirname = unicodedata.normalize("NFKD", dirname).encode("ASCII", "ignore").decode()

    # keep only whitelisted chars
    cleaned_dirname = "".join(c for c in cleaned_dirname if c in whitelist)
    if len(cleaned_dirname) > char_limit:
        print(
            "Warning, filename truncated because it was over {}. Filenames may no longer be unique".format(char_limit)
        )
    return cleaned_dirname[:char_limit].lower()
