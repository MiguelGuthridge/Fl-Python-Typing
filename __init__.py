"""
FL-Python-Typing

Initialize substitute modules to add them to the path variable, so that they
can be imported normally.

WARNING: The substitute modules aren't complete replacements, and should only
be used for purposes that have no effect at runtime, such as type checking.

This code is licensed under the GNU GPL v3
"""

import sys

try:
    import typing
    import abc
    del typing
    del abc
except ImportError:
    # Calculate directory from this filename
    directory = __file__.removesuffix("__init__.py")[:-1]
    # Add right to the start of the path
    sys.path.insert(0, directory)
