# Creating Laws in Victoria 3

Complete guide for creating new laws in Victoria 3 mods.

## Overview

Laws in Victoria 3 are policies that affect how a country functions. Each law belongs to a **law group** and can have modifiers, requirements, and effects.

## Step-by-Step Process

### Step 1: Create or Use a Law Group

Laws must belong to a law group. You can either:
- Use an existing law group from the base game
- Create a new law group

#### Creating a New Law Group

File: `common/law_groups/my_law_group.txt`

```plaintext
my_law_group = {
    law_group_category = economy  # Options: economy, power_structure, human_rights, other
    
    # Optional: Base enactment time in days
    base_enactment_days = 150
    
    # Optional: Multiplier for approval effects when changing this law
    enactment_approval_mult = 1.0
    
    # Optional: Whether regime changes affect this law group
    affected_by_regime_change = yes
    
    # Optional: Trigger to allow law changes
    change_allowed_trigger = {
        # Conditions for when law changes are allowed
    }
}
```

**Law Group Categories:**
- `economy` - Economic laws
- `power_structure` - Government structure laws
- `human_rights` - Rights and freedoms laws
- `other` - Miscellaneous laws

### Step 2: Create the Law Definition

File: `common/laws/my_law.txt`

#### Basic Law Structure

```plaintext
my_custom_law = {
    # Required: Law group this law belongs to
    group = my_law_group
    
    # Required: Icon file path
    icon = "gfx/interface/icons/law_icons/my_law.dds"
    
    # Required: Progressiveness value (0-100)
    # Higher = more progressive, affects IG opinions
    progressiveness = 50
    
    # Optional: Modifier applied when law is active
    modifier = {
        country_construction_efficiency_add = 0.1
        country_innovation_add = 0.05
    }
}
```

#### Complete Law Example

```plaintext
my_custom_law = {
    group = my_law_group
    icon = "gfx/interface/icons/law_icons/my_law.dds"
    progressiveness = 50
    
    # Modifier when law is active
    modifier = {
        country_construction_efficiency_add = 0.1
    }
    
    # Technology required to unlock
    unlocking_technologies = {
        tech_steam_engine
    }
    
    # Laws that must be active (OR condition)
    requires_law_or = {
        law_type:law_public_healthcare
    }
    
    # Laws that cannot be active with this law
    disallowing_laws = {
        law_type:law_no_healthcare
    }
    
    # Laws unlocked when this law is active
    unlocking_laws = {
        law_type:law_advanced_healthcare
    }
    
    # Conditions for law to be visible
    is_visible = {
        has_technology_researched = tech_medicine
    }
    
    # Conditions for law to be enactable
    can_enact = {
        bureaucracy > 100
    }
    
    # Effects when law is enacted (starts enactment process)
    on_enact = {
        add_modifier = {
            name = enacting_my_law
            days = 180
        }
    }
    
    # Effects when law is activated (becomes active)
    on_activate = {
        add_modifier = {
            name = my_law_active
            days = -1  # Permanent
        }
    }
    
    # Effects when law is deactivated
    on_deactivate = {
        remove_modifier = my_law_active
    }
    
    # AI behavior
    ai_will_do = {
        value = 1
        if = {
            limit = { bureaucracy > 200 }
            multiply = 2
        }
    }
}
```

### Step 3: Create Localization

File: `localization/english/my_law_l_english.yml`

```yaml
l_english:
 # Law name
 my_custom_law:0 "My Custom Law"
 
 # Law description (optional but recommended)
 my_custom_law_desc:0 "This law provides various benefits to the country."
```

### Step 4: Create Law Icon (Optional)

Create or use an icon file:
- Path: `gfx/interface/icons/law_icons/my_law.dds`
- Size: Typically 64x64 or 128x128 pixels
- Format: DDS

## Law Properties Explained

### Required Properties

| Property | Type | Description |
|----------|------|-------------|
| `group` | `<law_group>` | Law group this law belongs to |
| `icon` | `filepath` | Path to icon image file |
| `progressiveness` | `int` | Progressiveness value (0-100) |

### Optional Properties

#### Modifiers

```plaintext
# Basic modifier
modifier = {
    country_construction_efficiency_add = 0.1
}

# Tax modifiers (for tax laws)
tax_modifier_very_low = {
    country_tax_income_add = 0.05
}
tax_modifier_low = {
    country_tax_income_add = 0.10
}
tax_modifier_medium = {
    country_tax_income_add = 0.15
}
tax_modifier_high = {
    country_tax_income_add = 0.20
}
tax_modifier_very_high = {
    country_tax_income_add = 0.25
}

# Tariff modifiers
tariff_modifier_no_priority = {
    tariff_export_add = 0.05
    tariff_import_add = 0.05
}
```

#### Requirements and Dependencies

```plaintext
# Technology required to unlock
unlocking_technologies = {
    tech_steam_engine
    tech_railways
}

# Laws that must be active (OR condition)
requires_law_or = {
    law_type:law_public_healthcare
    law_type:law_private_healthcare
}

# Laws that cannot coexist
disallowing_laws = {
    law_type:law_no_healthcare
}

# Laws unlocked when this is active
unlocking_laws = {
    law_type:law_advanced_healthcare
}

# Parent law (for law hierarchies)
parent = law_type:law_basic_healthcare
```

#### Conditions

```plaintext
# When law is visible
is_visible = {
    has_technology_researched = tech_medicine
}

# When law can be enacted
can_enact = {
    bureaucracy > 100
    NOT = { is_at_war = yes }
}

# When law can be imposed (forced)
can_impose = {
    authority > 50
}
```

#### Effects

```plaintext
# When enactment starts
on_enact = {
    add_modifier = {
        name = enacting_my_law
        days = 180
    }
}

# When law becomes active
on_activate = {
    add_modifier = {
        name = my_law_active
        days = -1  # Permanent
    }
    trigger_event = {
        id = mymod.1
    }
}

# When law is deactivated
on_deactivate = {
    remove_modifier = my_law_active
}
```

#### Institutions

```plaintext
# Institution linked to this law
institution = institution_workplace_safety

# Modifier for the institution
institution_modifier = {
    building_minimum_wage_mult = 0.15
}
```

#### AI Behavior

```plaintext
# AI willingness to enact
ai_will_do = {
    value = 1
    if = {
        limit = { bureaucracy > 200 }
        multiply = 2
    }
}

# AI chance to impose
ai_impose_chance = {
    value = 0
    if = {
        limit = { authority > 100 }
        add = 10
    }
}

# Weight modifier for AI enactment
ai_enact_weight_modifier = {
    value = 0
    if = {
        limit = { has_law = law_type:law_council_republic }
        add = 750
    }
}
```

## Law Group Properties

### Law Group Categories

```plaintext
law_group_category = economy          # Economic laws
law_group_category = power_structure  # Government structure
law_group_category = human_rights    # Rights and freedoms
law_group_category = other            # Miscellaneous
```

### Law Group Example

```plaintext
my_law_group = {
    law_group_category = economy
    base_enactment_days = 150
    enactment_approval_mult = 1.5
    affected_by_regime_change = yes
    
    change_allowed_trigger = {
        NOT = { is_subject = yes }
    }
}
```

## Ideology Support

To make ideologies support or oppose your law, modify ideology files:

File: `common/ideologies/my_ideology.txt`

```plaintext
my_ideology = {
    # ... other ideology properties ...
    
    # Law stance: strongly_disapprove, disapprove, neutral, approve, strongly_approve
    my_law_group = {
        my_custom_law = approve
    }
}
```

## Common Patterns

### Simple Law with Modifier

```plaintext
simple_law = {
    group = my_law_group
    icon = "gfx/interface/icons/law_icons/simple.dds"
    progressiveness = 50
    
    modifier = {
        country_construction_efficiency_add = 0.1
    }
}
```

### Technology-Gated Law

```plaintext
tech_law = {
    group = my_law_group
    icon = "gfx/interface/icons/law_icons/tech.dds"
    progressiveness = 75
    
    unlocking_technologies = {
        tech_steam_engine
    }
    
    modifier = {
        country_innovation_add = 0.15
    }
}
```

### Law with Institution

```plaintext
institution_law = {
    group = my_law_group
    icon = "gfx/interface/icons/law_icons/institution.dds"
    progressiveness = 60
    
    institution = institution_workplace_safety
    institution_modifier = {
        building_minimum_wage_mult = 0.20
    }
}
```

### Mutually Exclusive Laws

```plaintext
law_a = {
    group = my_law_group
    icon = "gfx/interface/icons/law_icons/a.dds"
    progressiveness = 50
    
    disallowing_laws = {
        law_type:law_b
    }
    
    modifier = {
        country_authority_add = 10
    }
}

law_b = {
    group = my_law_group
    icon = "gfx/interface/icons/law_icons/b.dds"
    progressiveness = 50
    
    disallowing_laws = {
        law_type:law_a
    }
    
    modifier = {
        country_influence_add = 10
    }
}
```

## Replacing Existing Laws

To modify an existing law, use `REPLACE:` prefix:

```plaintext
REPLACE:law_public_healthcare = {
    group = lawgroup_health_system
    icon = "gfx/interface/icons/law_icons/public_healthcare.dds"
    progressiveness = 75
    
    # Your modifications here
    modifier = {
        country_pop_health_add = 0.1
    }
}
```

## Testing Your Law

1. **Check syntax** - Use CWTools to validate
2. **Test in game** - Load mod and check law appears
3. **Verify effects** - Check modifiers are applied
4. **Test AI behavior** - See if AI enacts it appropriately
5. **Check localization** - Verify text displays correctly

## Common Issues

### Law Not Appearing
- Check `is_visible` conditions
- Verify law group exists
- Check localization keys

### Law Not Enactable
- Check `can_enact` conditions
- Verify requirements are met
- Check `unlocking_technologies`

### Modifiers Not Working
- Verify modifier syntax
- Check modifier types are valid
- Test in game to confirm

### AI Not Using Law
- Adjust `ai_will_do` values
- Check `ai_enact_weight_modifier`
- Verify conditions in AI triggers

## File Organization

```
mod/
├── common/
│   ├── law_groups/
│   │   └── my_law_groups.txt
│   └── laws/
│       └── my_laws.txt
└── localization/
    └── english/
        └── my_laws_l_english.yml
```

## Best Practices

1. **Use descriptive names** - `law_public_healthcare` not `law_1`
2. **Set appropriate progressiveness** - Match historical context
3. **Add localization** - Always provide descriptions
4. **Test thoroughly** - Verify all effects work
5. **Consider balance** - Don't make laws too powerful
6. **Document dependencies** - Use `requires_law_or` and `disallowing_laws`
7. **Set AI behavior** - Make AI use laws appropriately

## Example: Complete Law Creation

### 1. Law Group

File: `common/law_groups/my_health_laws.txt`

```plaintext
lawgroup_health_system = {
    law_group_category = human_rights
    base_enactment_days = 180
    enactment_approval_mult = 2.0
}
```

### 2. Law Definition

File: `common/laws/my_health_laws.txt`

```plaintext
law_public_healthcare = {
    group = lawgroup_health_system
    icon = "gfx/interface/icons/law_icons/public_healthcare.dds"
    progressiveness = 75
    
    unlocking_technologies = {
        tech_medicine
    }
    
    modifier = {
        country_pop_health_add = 0.15
        country_pop_growth_add = 0.05
    }
    
    institution = institution_public_health
    institution_modifier = {
        country_pop_health_add = 0.10
    }
    
    ai_will_do = {
        value = 1
        if = {
            limit = { has_law = law_type:law_council_republic }
            multiply = 2
        }
    }
}
```

### 3. Localization

File: `localization/english/my_health_laws_l_english.yml`

```yaml
l_english:
 lawgroup_health_system:0 "Health System"
 law_public_healthcare:0 "Public Healthcare"
 law_public_healthcare_desc:0 "The state provides healthcare to all citizens, improving public health and population growth."
```

This completes the law creation process!
