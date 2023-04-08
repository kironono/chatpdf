import click

from pathlib import Path
from dotenv import load_dotenv

from chatpdf.config import Config
from chatpdf.repl import Repl
from chatpdf.indexer import Indexer


@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    # load environments from dotenv
    load_dotenv()

    config = Config()
    ctx.obj = {'config': config}

    if ctx.invoked_subcommand is None:
        Repl(config).run()


@click.command()
@click.argument('source', type=click.Path(exists=True))
@click.pass_obj
def create_index(obj, source):
    click.echo('Create index')
    source = Path(click.format_filename(source))

    indexer = Indexer(obj['config'], source)
    indexer.execute()


cli.add_command(create_index)
