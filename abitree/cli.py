import argparse
import sys
from .tree import generate_tree

DEFAULT_IGNORE = [".git", "__pycache__", ".DS_Store", ".idea", ".vscode", "node_modules"]


def main():
    parser = argparse.ArgumentParser(
        prog="abitree",
        description="🌳 abitree — generate beautiful file trees for your README",
    )

    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Path to directory (default: current directory)",
    )

    parser.add_argument(
        "-L", "--level",
        type=int,
        default=None,
        metavar="DEPTH",
        help="Max depth of the tree",
    )

    parser.add_argument(
        "-o", "--output",
        type=str,
        default=None,
        metavar="FILE",
        help="Output to a file (e.g. README.md)",
    )

    parser.add_argument(
        "-i", "--ignore",
        type=str,
        default=None,
        metavar="PATTERNS",
        help="Comma-separated list of names to ignore (e.g. node_modules,.git)",
    )

    parser.add_argument(
        "--dirs-only",
        action="store_true",
        help="Show directories only",
    )

    parser.add_argument(
        "--no-icons",
        action="store_true",
        help="Disable icons (plain text output)",
    )

    parser.add_argument(
        "--no-default-ignore",
        action="store_true",
        help="Disable default ignored folders (.git, node_modules, etc.)",
    )

    parser.add_argument(
        "--md",
        action="store_true",
        help="Wrap output in a markdown code block",
    )

    args = parser.parse_args()

    # Build ignore list
    ignore = [] if args.no_default_ignore else list(DEFAULT_IGNORE)
    if args.ignore:
        ignore += [i.strip() for i in args.ignore.split(",")]

    tree = generate_tree(
        path=args.path,
        max_depth=args.level,
        ignore=ignore,
        dirs_only=args.dirs_only,
        use_icons=not args.no_icons,
    )

    if args.md:
        output = f"```\n{tree}\n```"
    else:
        output = tree

    if args.output:
        with open(args.output, "w") as f:
            f.write(output + "\n")
        print(f"✅ Tree written to {args.output}")
    else:
        print(output)


if __name__ == "__main__":
    main()
