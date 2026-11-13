import re
from typing import Dict, List

def parse_conventional_commit(message: str) -> Dict[str, str]:
    match = re.match(r"^(\w+)(?:\(([^)]+)\))?:\s*(.+)$", message.strip())
    if match:
        return {
            "type": match.group(1).lower(),
            "scope": match.group(2) or "",
            "description": match.group(3)
        }
    return {"type": "other", "scope": "", "description": message.strip()}

def format_changelog_section(commits: List[str]) -> str:
    categories: Dict[str, List[str]] = {
        "feat": [],
        "fix": [],
        "docs": [],
        "refactor": [],
        "other": []
    }
    for c in commits:
        parsed = parse_conventional_commit(c)
        ctype = parsed["type"] if parsed["type"] in categories else "other"
        prefix = f"**{parsed['scope']}**: " if parsed["scope"] else ""
        categories[ctype].append(f"- {prefix}{parsed['description']}")

    output = []
    headers = [("feat", "### ✨ Features"), ("fix", "### 🐛 Bug Fixes"), ("docs", "### 📝 Documentation"), ("refactor", "### ♻️ Refactoring"), ("other", "### 🔧 Other Changes")]
    for key, title in headers:
        if categories[key]:
            output.append(title)
            output.extend(categories[key])
            output.append("")
    return "\n".join(output).strip()
