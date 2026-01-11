---

name: victoria3-mod-dev

description: Comprehensive Victoria 3 modding skill for creating, modifying, and debugging mods. Use when working with Victoria 3 mods for (1) Creating new mods from scratch, (2) Adding or modifying game content (decisions, events, buildings, laws, technologies, etc.), (3) Understanding mod file structure and syntax, (4) Debugging mod errors, (5) Creating localization files, (6) Working with .mod descriptor files, or any other Victoria 3 modding tasks.
metadata:
  short-description: Create mod for the game victoria3

---

# Victoria 3 Mod Development

Guide for creating and modifying Victoria 3 mods using Paradox's scripting language.

## Quick Start

### Mod Structure

Every Victoria 3 mod requires:

- `.mod` descriptor file in `Documents/Paradox Interactive/Victoria 3/mod/`
- Mod folder with content in subdirectories:
  - `common/` - Game logic (decisions, buildings, laws, technologies, etc.)
  - `events/` - Event files
  - `localization/` - Localization files (YAML format)
  - `gfx/` - Graphics assets
  - `gui/` - GUI modifications

### Basic .mod File Format

```plaintext
version="1.0.0"
tags={
	"Gameplay"
}
name="My Mod"
supported_version="*"
path="mod/MyMod"
remote_file_id=""
```

## Common Modding Tasks

### Creating Decisions

Decisions go in `common/decisions/`. Format:

```plaintext
my_decision = {
	is_shown = {
		# Conditions for decision to appear
		is_ai = no
	}
	possible = {
		# Conditions for decision to be available
		bureaucracy > 100
	}
	when_taken = {
		# Effects when decision is taken
		add_modifier = {
			name = my_modifier
			days = 365
		}
	}
	ai_chance = {
		base = 0
	}
}
```

### Creating Events

Events go in `events/`. Format:

```plaintext
namespace = mymod

mymod.1 = {
	type = country_event
	
	title = mymod.1.t
	desc = mymod.1.desc
	
	option = {
		name = mymod.1.a
		# Option effects
	}
}
```

### Localization

Localization files go in `localization/<language>/` as YAML:

```yaml
l_english:
 mymod.1.t:0 "Event Title"
 mymod.1.desc:0 "Event description."
 mymod.1.a:0 "OK"
```

### Common File Types

- **Decisions**: `common/decisions/*.txt`
- **Events**: `events/*.txt`
- **Buildings**: `common/buildings/*.txt`
- **Laws**: `common/laws/*.txt` - See [Creating Laws](references/creating-laws.md) for detailed guide
- **Law Groups**: `common/law_groups/*.txt` - Required for laws
- **Technologies**: `common/technology/*.txt`
- **Cultures**: `common/cultures/*.txt`
- **Countries**: `common/country_definitions/*.txt`
- **Modifiers**: `common/static_modifiers/*.txt`
- **Scripted Effects**: `common/scripted_effects/*.txt`
- **Scripted Triggers**: `common/scripted_triggers/*.txt`

### Creating Laws

Quick example:

```plaintext
# 1. Create law group (common/law_groups/my_group.txt)
my_law_group = {
    law_group_category = economy
}

# 2. Create law (common/laws/my_law.txt)
my_custom_law = {
    group = my_law_group
    icon = "gfx/interface/icons/law_icons/my_law.dds"
    progressiveness = 50
    modifier = {
        country_construction_efficiency_add = 0.1
    }
}

# 3. Add localization (localization/english/my_law_l_english.yml)
# my_custom_law:0 "My Custom Law"
```

See [Creating Laws](references/creating-laws.md) for complete guide.

## Syntax Guidelines

### Scope Operators

- `ROOT` - Original scope
- `THIS` - Current scope
- `FROM` - Previous scope
- `PREV` - Previous scope in chain

### Common Conditions

- `is_ai = yes/no` - Check if AI controlled
- `has_modifier = <name>` - Check for modifier
- `has_technology_researched = <tech>` - Check technology
- `bureaucracy > <value>` - Numeric comparisons
- `owns_entire_state_region = <state>` - State ownership

### Common Effects

- `add_modifier = { name = <name> days = <days> }`
- `set_variable = { name = <name> value = <value> }`
- `add_technology_researched = <tech>`
- `trigger_event = { id = <event_id> }`

## Reference Files

For detailed information on specific modding areas, see:

- [File Structure](references/file-structure.md) - Complete directory structure
- [Syntax Reference](references/syntax-reference.md) - Detailed syntax guide
- [Common Patterns](references/common-patterns.md) - Common modding patterns
- [Examples](references/examples.md) - Real-world examples
- [Glossary](references/glossary.md) - Comprehensive terminology dictionary
- [CWTools Guide](references/cwtools-guide.md) - Using CWTools for validation and auto-completion
- [Creating Laws](references/creating-laws.md) - Complete guide for creating new laws

## Debugging

Common issues:

1. **Syntax errors**: Check brackets, quotes, and indentation
2. **Missing localization**: Ensure all keys exist in localization files
3. **Scope errors**: Verify scope operators are correct
4. **File paths**: Ensure files are in correct directories

Use game's error log to identify issues. Check `Documents/Paradox Interactive/Victoria 3/logs/` for error messages.