"""Perform an automated doubling experiment to measure performance of cryptography."""

from enum import Enum
from typing import List, Tuple

import typer
from rich.console import Console

# create a Typer object to support the command-line interface
cli = typer.Typer()

# create a console for rich text output
console = Console()


class Mode(Enum):
    """An enumeration of the possible modes for the cryptography benchmarking."""

    encrypt = "encrypt"
    decrypt = "decrypt"


class Library(Enum):
    """An enumeration of the possible libraries for implementation of Fernet."""

    fernet = "fernet"
    rfernet = "rfernet"
    both = "both"


def print_results(results: List[Tuple[bytes, int, int, float, float]]) -> None:
    """Print the results in a table."""
    # TODO: provide a complete implementation of this function
    # TODO: make sure that this function uses rich to display the table
    # TODO: make sure that the table has the appropriate columns and labels
    # and that the data in the table is properly aligned
    return None



@cli.command()
def cryptobenchmark(
    verbose: bool = typer.Option(
        False, "--verbose", "-v", help="Enable verbose output."
    ),
    textsize: int = typer.Option(
        256,
        "--textsize",
        help="Specify the starting size of text input to cryptography.",
    ),
    doublerounds: int = typer.Option(
        5, "--doublerounds", help="Specify the number of doubling rounds."
    ),
    mode: Mode = typer.Option(
        Mode.encrypt,
        "--mode",
        help="Specify the mode: encrypt or decrypt.",
    ),
    library: Library = typer.Option(
        Library.fernet,
        "--library",
        help="Specify the library: fernet, rfernet, or both.",
    ),
) -> None:
    """Conduct a benchmarking campaign to automatically study cryptography performance."""
    # TODO: provide a complete implementation of this function
    # that meets the requirements outlined in the README.md file
