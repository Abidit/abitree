# 🌳 abitree

Generate beautiful, icon-rich file trees for your README — instantly.

```
📁 my-project/
├── 📁 src/
│   ├── 🐍 main.py
│   ├── ⚛️  App.tsx
│   └── 🎨 styles.css
├── 📦 package.json
├── 🐳 Dockerfile
└── 📝 README.md
```

## Installation

```bash
pip install abitree
```

## Usage

```bash
# Current directory
abitree

# Specific path
abitree ./my-project

# Limit depth
abitree -L 2

# Output to file
abitree -o structure.md

# Wrap in markdown code block
abitree --md

# Directories only
abitree --dirs-only

# Ignore extra folders
abitree -i dist,build,.cache

# No icons (plain text)
abitree --no-icons
```

## Options

| Flag | Description |
|------|-------------|
| `path` | Directory to scan (default: `.`) |
| `-L, --level` | Max depth |
| `-o, --output` | Write output to file |
| `-i, --ignore` | Comma-separated ignore list |
| `--dirs-only` | Show directories only |
| `--no-icons` | Disable icons |
| `--no-default-ignore` | Don't ignore `.git`, `node_modules`, etc. |
| `--md` | Wrap output in markdown code block |

## Default ignored

`.git`, `__pycache__`, `.DS_Store`, `.idea`, `.vscode`, `node_modules`

## Author

Built by [Abidit Shrestha](https://github.com/abiditshrestha)

## License

MIT
