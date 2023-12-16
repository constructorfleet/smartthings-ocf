"""Common untility functions."""

from typing import Any, List


def get_attribute_value(attributes: Any, path: List[str] | str) -> str:
    """Get attribute from path."""
    if isinstance(path, str):
        path = path.split(".")

    if len(path) > 1:
        return get_attribute_value(attributes[path[0]], path[1:])

    if path[0].endswith("!"):
        return attributes[path[0].rstrip("!")]
    return attributes[path[0]].value


def sanitize_attribute(attribute_path: str) -> str:
    """Sanitize attribute path."""
    return attribute_path.replace(".", "").replace("!", "")
