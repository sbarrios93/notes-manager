#!/Users/seba/.pyenv/shims/python
import click
from pathlib import Path
import regex as re


@click.command()
@click.argument("filename", type=click.Path(exists=True))
@click.argument("filedirname", type=click.Path(exists=True))
def cli(filename, filedirname):
    def get_file_path(filename):

        assert Path(filename).suffix in [".md", ".txt", ".rst"], "File must be a .md, .txt, or .rst file."

        return Path(filename)

    def read_file(file_path):
        return open(file_path, mode="r", encoding="utf-8").read()

    content = read_file(get_file_path(filename))

    def margin_figure(content, filedirname):

        latex_wrapper = fr"""
\\begin{{marginfigure}}
\includegraphics[width=\\textwidth]{{{filedirname}/\2}}
\caption{{\1}}
\end{{marginfigure}}
            """

        lookup = re.compile(r"^@marginfigure\s!\[(.*)\]\((.*)\)", re.MULTILINE)
        return re.sub(lookup, latex_wrapper, content)

    print(margin_figure(content, filedirname))


if __name__ == "__main__":
    cli()
