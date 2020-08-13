# -*- coding: utf-8 -*-

from pprint import pprint

import click
from prompt_toolkit.shortcuts import prompt
from prompt_toolkit.completion import FuzzyWordCompleter

from .utils import find_project, licenses, classifiers


@click.group("feta")
@click.pass_context
def cli(*args, **kwargs):
    """Yet another project manager."""
    pass


@cli.command("find", short_help="Check if project name is available")
@click.argument("project_name")
@click.pass_context
def find(*args, **kwargs):
    project_name = kwargs["project_name"]

    find_project("pypi", project_name)
    find_project("rtfd", project_name)


@cli.command("new", short_help="Create new project")
@click.argument("project_name")
@click.pass_context
def new(*args, **kwargs):
    project_name = kwargs["project_name"]

    description = click.prompt("description")
    author_name = click.prompt("author_name")
    author_email = click.prompt("author_email")

    license_completer = FuzzyWordCompleter(licenses)
    license = prompt(
        "Select license: ",
        completer=license_completer,
        complete_while_typing=True,
    )

    classifier_completer = FuzzyWordCompleter(classifiers)
    classifier = prompt(
        "Select classifier: ",
        completer=classifier_completer,
        complete_while_typing=True,
    )

    metadata = {
        "name": project_name,
        "description": description,
        "author_name": author_name,
        "author_email": author_email,
        "license": license,
        "classifiers": classifier,
    }

    print()
    pprint(metadata)
