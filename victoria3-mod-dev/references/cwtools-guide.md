# CWTools for Victoria 3 Modding Guide

## What is CWTools?

CWTools is a language server and validation tool for Paradox game modding. The `cwtools-vic3-config` provides comprehensive configuration files that enable:

- **Syntax validation** - Real-time error checking
- **Auto-completion** - Intelligent code completion
- **Type checking** - Validates scope types, enums, and references
- **Documentation** - Inline help and tooltips
- **Link validation** - Checks file paths and references

## Setup Instructions

### For VSCode

1. **Install CWTools Extension**
   - Open VSCode
   - Go to Extensions (Ctrl+Shift+X)
   - Search for "CWTools" and install

2. **Configure CWTools**
   - Open Settings (File → Preferences → Settings)
   - Switch to "Workspace Settings" tab (to apply only to this project)
   - Set `cwtools.rules_version` to `"manual"`
   - Set `cwtools.rules_folder` to the path of `cwtools-vic3-config` folder
     - Example: `C:\Users\trots\Documents\Paradox Interactive\Victoria 3\mod\New\cwtools-vic3-config`

3. **Reload VSCode**
   - Press `Ctrl+Shift+P`
   - Type "Reload Window" and select it
   - CWTools will now validate your mod files

### For IntelliJ IDEA

1. **Install Paradox Language Support Plugin**
   - Open IntelliJ Settings
   - Go to Plugins
   - Search for "Paradox Language Support" and install

2. **Configure Remote Config**
   - Open Settings → Languages & Frameworks → Paradox Language Support
   - Enable "Remote config groups"
   - Set remote URL to: `https://github.com/cwtools/cwtools-vic3-config` (or local path)

## How CWTools Helps Modding

### 1. Real-Time Syntax Validation

**Before CWTools:**
```plaintext
my_decision = {
    is_shown = {
        is_ai = no
    }
    when_taken = {
        add_modifier = {
            name = my_modifier
            # Missing closing brace - error only found in-game
        }
    }
}
```

**With CWTools:**
- Red squiggly lines show syntax errors immediately
- Error messages explain what's wrong
- Prevents many crashes and bugs

### 2. Auto-Completion

When typing, CWTools provides suggestions:

```plaintext
my_decision = {
    is_shown = {
        is_ai = [suggestions: yes, no]
        has_modifier = [suggests all available modifiers]
        bureaucracy > [suggests numeric values]
    }
}
```

**Benefits:**
- Faster coding
- Fewer typos
- Discover available options
- Learn correct syntax

### 3. Scope Validation

CWTools validates scope types:

```plaintext
# Correct - country scope can use country conditions
country = {
    is_ai = yes  # ✓ Valid
    bureaucracy > 100  # ✓ Valid
}

# Error - state scope cannot use country-only conditions
state = {
    is_ai = yes  # ✗ Error: is_ai not available in state scope
}
```

### 4. Reference Validation

Checks if referenced items exist:

```plaintext
# CWTools checks if this modifier actually exists
add_modifier = {
    name = my_modifier  # ✗ Error if not defined in static_modifiers
}

# CWTools checks if this technology exists
has_technology_researched = tech_steam_engine  # ✓ Valid if exists
has_technology_researched = tech_fake_tech  # ✗ Error if doesn't exist
```

### 5. Localization Validation

Validates localization keys:

```plaintext
# In event file
title = mymod.1.t

# CWTools checks if this key exists in localization files
# ✗ Error if missing from localization/english/mymod_l_english.yml
```

### 6. Type Checking

Validates enum values and types:

```plaintext
# Event type must be one of: country_event, state_event, character_event
type = country_event  # ✓ Valid
type = invalid_type  # ✗ Error

# Boolean values
is_ai = yes  # ✓ Valid
is_ai = maybe  # ✗ Error: must be yes or no
```

### 7. File Path Validation

Checks if file references are correct:

```plaintext
# In event
event_image = {
    texture = "gfx/event_pictures/my_image.dds"  # ✓ Valid if file exists
    texture = "gfx/nonexistent.dds"  # ✗ Warning if file missing
}
```

## Key Configuration Files

### Scope Definitions (`config/scopes.cwt`)
- Defines all available scope types
- Validates scope transitions
- Lists available scopes: Country, State, Character, Building, etc.

### Triggers (`config/triggers.cwt`)
- Defines all trigger conditions
- Validates trigger syntax
- Shows available triggers for each scope type

### Effects (`config/effects.cwt`)
- Defines all effect commands
- Validates effect syntax
- Shows available effects for each scope type

### Common Files (`config/common/*.cwt`)
- **decisions.cwt** - Decision structure validation
- **buildings.cwt** - Building definition validation
- **laws.cwt** - Law definition validation
- **technology.cwt** - Technology definition validation
- And many more...

### Events (`config/events/events.cwt`)
- Event structure validation
- Event type checking
- Option validation

## Practical Workflow

### Step 1: Write Code
```plaintext
my_decision = {
    is_shown = {
        is_ai = no
    }
    when_taken = {
        add_modifier = {
            name = my_modifier
            days = 365
        }
    }
}
```

### Step 2: CWTools Validates
- Checks syntax ✓
- Validates scope ✓
- Checks modifier exists ✗ (if not defined)
- Suggests fixes

### Step 3: Fix Errors
- Create missing modifier definition
- Fix syntax errors
- Correct scope issues

### Step 4: Test in Game
- Most syntax errors already caught
- Fewer crashes
- Faster iteration

## Common CWTools Features

### Hover Information
Hover over any keyword to see:
- Description
- Valid values
- Scope requirements
- Examples

### Go to Definition
- Right-click on a reference
- Select "Go to Definition"
- Jump to where it's defined

### Find References
- Right-click on a definition
- Select "Find All References"
- See where it's used

### Quick Fixes
- Red lightbulb appears on errors
- Click to see suggested fixes
- Apply fixes automatically

## Best Practices

1. **Always use CWTools** - Catch errors before testing
2. **Fix warnings** - They often indicate real issues
3. **Use auto-completion** - Discover available options
4. **Check hover tooltips** - Learn correct syntax
5. **Validate before testing** - Save time debugging

## Troubleshooting

### CWTools Not Working
1. Check extension is installed
2. Verify rules folder path is correct
3. Reload window (Ctrl+Shift+P → Reload Window)
4. Check VSCode output panel for errors

### False Positives
- Some warnings may be false positives
- Use game testing to verify
- Report issues to CWTools repository

### Performance
- Large mods may slow down validation
- Disable validation for specific files if needed
- Use workspace settings to limit scope

## Integration with Mod Development

### Recommended Workflow

1. **Setup CWTools** - Configure once per project
2. **Write code** - Use auto-completion
3. **Fix errors** - Address CWTools warnings
4. **Test in game** - Verify functionality
5. **Iterate** - Repeat process

### Benefits Summary

- **Faster development** - Auto-completion speeds up coding
- **Fewer bugs** - Catch errors before testing
- **Better code quality** - Enforced best practices
- **Learning tool** - Discover available options
- **Documentation** - Inline help and tooltips

## Advanced Usage

### Custom Rules
You can extend CWTools with custom rules:
- Add project-specific validations
- Define custom types
- Create custom triggers/effects

### Script Documentation
The `script-docs/` folder contains:
- `triggers.log` - All available triggers
- `effects.log` - All available effects
- `modifiers.log` - All available modifiers
- `data_types_*.txt` - Type definitions

Use these for reference when CWTools doesn't have complete information.

## Conclusion

CWTools is an essential tool for Victoria 3 modding. It:
- Saves time by catching errors early
- Improves code quality
- Speeds up development
- Helps learn the modding system

Always use CWTools when developing mods to ensure better quality and faster iteration.
