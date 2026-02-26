import os
from .icons import get_icon


def build_tree(
    root: str,
    prefix: str = "",
    max_depth: int = None,
    current_depth: int = 0,
    ignore: list = None,
    dirs_only: bool = False,
    use_icons: bool = True,
) -> list:
    if ignore is None:
        ignore = []

    if max_depth is not None and current_depth >= max_depth:
        return []

    try:
        entries = sorted(os.scandir(root), key=lambda e: (not e.is_dir(), e.name.lower()))
    except (PermissionError, OSError):
        return []

    # Skip symlinks that point to directories to avoid infinite loops
    entries = [e for e in entries if not (e.is_symlink() and e.is_dir())]

    # Filter ignored
    entries = [e for e in entries if e.name not in ignore]

    # Filter files if dirs only
    if dirs_only:
        entries = [e for e in entries if e.is_dir()]

    lines = []
    for i, entry in enumerate(entries):
        is_last = i == len(entries) - 1
        connector = "└── " if is_last else "├── "
        extension = "    " if is_last else "│   "

        icon = get_icon(entry.name, entry.is_dir()) + " " if use_icons else ""
        trail = "/" if entry.is_dir() else ""

        lines.append(f"{prefix}{connector}{icon}{entry.name}{trail}")

        if entry.is_dir():
            lines.extend(
                build_tree(
                    root=entry.path,
                    prefix=prefix + extension,
                    max_depth=max_depth,
                    current_depth=current_depth + 1,
                    ignore=ignore,
                    dirs_only=dirs_only,
                    use_icons=use_icons,
                )
            )

    return lines


def generate_tree(
    path: str = ".",
    max_depth: int = None,
    ignore: list = None,
    dirs_only: bool = False,
    use_icons: bool = True,
) -> str:
    path = os.path.abspath(path)
    root_name = os.path.basename(path)
    icon = get_icon(root_name, is_dir=True) + " " if use_icons else ""

    lines = [f"{icon}{root_name}/"]
    lines += build_tree(
        root=path,
        max_depth=max_depth,
        ignore=ignore or [],
        dirs_only=dirs_only,
        use_icons=use_icons,
    )

    return "\n".join(lines)
