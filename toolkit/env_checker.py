import shutil
import subprocess
from typing import Dict, List, Tuple

REQUIRED_TOOLS = ["git", "python3", "curl"]
RECOMMENDED_TOOLS = ["docker", "gh", "node"]

def check_binary(name: str) -> Tuple[bool, str]:
    path = shutil.which(name)
    if not path:
        return False, "Not Installed"
    try:
        ver_output = subprocess.check_output([name, "--version"], text=True, stderr=subprocess.STDOUT).splitlines()[0]
        return True, ver_output.strip()
    except Exception:
        return True, path

def audit_environment() -> Dict[str, Dict[str, str]]:
    results = {"required": {}, "recommended": {}}
    for tool in REQUIRED_TOOLS:
        ok, detail = check_binary(tool)
        results["required"][tool] = detail
    for tool in RECOMMENDED_TOOLS:
        ok, detail = check_binary(tool)
        results["recommended"][tool] = detail
    return results
