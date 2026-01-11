#!/usr/bin/env python3
"""
List all available skills with their metadata.

This script scans the skills directory and extracts skill metadata
(name and description) from each skill's SKILL.md frontmatter.
"""

import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional

# Default Codex skills directory
# CODEX_HOME defaults to ~/.codex, so skills are at ~/.codex/skills
DEFAULT_SKILLS_DIR = Path.home() / ".codex" / "skills"
codex_home = os.getenv("CODEX_HOME")
if codex_home:
    SKILLS_DIR = Path(codex_home) / "skills"
else:
    SKILLS_DIR = DEFAULT_SKILLS_DIR


def extract_frontmatter(file_path: Path) -> Optional[Dict[str, str]]:
    """
    Extract YAML frontmatter from a SKILL.md file.
    
    Returns:
        Dictionary with 'name' and 'description' keys, or None if not found
    """
    try:
        content = file_path.read_text(encoding='utf-8')
    except Exception as e:
        print(f"Warning: Could not read {file_path}: {e}", file=sys.stderr)
        return None
    
    # Match YAML frontmatter between --- markers
    frontmatter_pattern = r'^---\s*\n(.*?)\n---\s*\n'
    match = re.search(frontmatter_pattern, content, re.DOTALL | re.MULTILINE)
    
    if not match:
        return None
    
    frontmatter_text = match.group(1)
    metadata = {}
    
    # Extract name and description
    name_match = re.search(r'^name:\s*(.+)$', frontmatter_text, re.MULTILINE)
    if name_match:
        metadata['name'] = name_match.group(1).strip()
    
    desc_match = re.search(r'^description:\s*(.+)$', frontmatter_text, re.MULTILINE | re.DOTALL)
    if desc_match:
        # Handle multi-line descriptions
        desc = desc_match.group(1).strip()
        # Remove any trailing metadata fields
        desc = re.split(r'\nmetadata:', desc, flags=re.IGNORECASE)[0]
        desc = re.split(r'\n---', desc)[0]
        metadata['description'] = desc.strip()
    
    if 'name' in metadata and 'description' in metadata:
        return metadata
    
    return None


def find_all_skills(skills_dir: Path) -> List[Dict[str, str]]:
    """
    Find all skills in the skills directory.
    
    Returns:
        List of dictionaries with 'name', 'description', and 'path' keys
    """
    skills = []
    
    if not skills_dir.exists():
        print(f"Warning: Skills directory not found: {skills_dir}", file=sys.stderr)
        return skills
    
    # Walk through all subdirectories
    for skill_dir in skills_dir.iterdir():
        if not skill_dir.is_dir():
            continue
        
        # Skip hidden directories
        if skill_dir.name.startswith('.'):
            continue
        
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            continue
        
        metadata = extract_frontmatter(skill_md)
        if metadata:
            metadata['path'] = str(skill_dir)
            skills.append(metadata)
    
    return sorted(skills, key=lambda x: x['name'])


def format_output(skills: List[Dict[str, str]], format_type: str = "text") -> str:
    """
    Format skills list for output.
    
    Args:
        skills: List of skill dictionaries
        format_type: 'text', 'json', or 'markdown'
    """
    if format_type == "json":
        import json
        return json.dumps(skills, indent=2, ensure_ascii=False)
    
    elif format_type == "markdown":
        lines = ["# Available Skills\n"]
        for skill in skills:
            lines.append(f"## {skill['name']}")
            lines.append(f"\n{skill['description']}\n")
        return "\n".join(lines)
    
    else:  # text format
        lines = []
        for i, skill in enumerate(skills, 1):
            lines.append(f"{i}. **{skill['name']}**")
            lines.append(f"   {skill['description']}\n")
        return "\n".join(lines)


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="List all available Codex skills with their metadata"
    )
    parser.add_argument(
        "--format",
        choices=["text", "json", "markdown"],
        default="text",
        help="Output format (default: text)"
    )
    parser.add_argument(
        "--skills-dir",
        type=Path,
        default=SKILLS_DIR,
        help=f"Skills directory path (default: {SKILLS_DIR})"
    )
    
    args = parser.parse_args()
    
    skills = find_all_skills(args.skills_dir)
    
    if not skills:
        print("No skills found.", file=sys.stderr)
        sys.exit(1)
    
    output = format_output(skills, args.format)
    print(output)
    
    if args.format == "text":
        print(f"\nTotal: {len(skills)} skills found", file=sys.stderr)


if __name__ == "__main__":
    main()
