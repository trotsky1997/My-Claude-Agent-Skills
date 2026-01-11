# Victoria 3 Modding Syntax Reference

## Basic Syntax Rules

1. **Case sensitivity**: Keys are case-sensitive
2. **Indentation**: Use tabs (not spaces)
3. **Comments**: Use `#` for comments
4. **Strings**: Use quotes for strings, no quotes for keys/identifiers
5. **Brackets**: Use `{}` for blocks, `[]` for lists

## Scope System

### Scope Types
- `country` - Country scope
- `state` - State scope
- `character` - Character scope
- `building` - Building scope
- `interest_group` - Interest group scope
- `culture` - Culture scope
- `religion` - Religion scope

### Scope Operators
- `ROOT` - Original scope (where effect chain started)
- `THIS` - Current scope
- `FROM` - Previous scope
- `PREV` - Previous scope in chain
- `FROMFROM` - Two scopes back
- `FROMFROMFROM` - Three scopes back

### Scope Changes
```plaintext
# Change to country scope
country = {
    # Now in country scope
}

# Change to state scope
state = {
    # Now in state scope
}

# Iterate over all states
every_scope_state = {
    # Loop through all states
}
```

## Common Conditions

### Country Conditions
- `is_ai = yes/no`
- `is_player = yes/no`
- `has_modifier = <modifier_name>`
- `has_technology_researched = <tech_key>`
- `bureaucracy > <value>`
- `authority > <value>`
- `influence > <value>`
- `prestige > <value>`
- `is_at_war = yes/no`
- `is_subject = yes/no`
- `is_overlord = yes/no`

### State Conditions
- `is_incorporated = yes/no`
- `is_treaty_port = yes/no`
- `has_building = <building_type>`
- `infrastructure > <value>`
- `is_homeland_of_country_cultures = <country>`

### Character Conditions
- `age > <value>`
- `has_trait = <trait>`
- `is_ruler = yes/no`
- `is_heir = yes/no`

### Logical Operators
- `AND = { ... }` - All conditions must be true
- `OR = { ... }` - At least one condition must be true
- `NOT = { ... }` - Condition must be false
- `NOR = { ... }` - None of the conditions must be true

## Common Effects

### Modifiers
```plaintext
add_modifier = {
    name = modifier_name
    days = 365  # -1 for permanent
}

remove_modifier = modifier_name
```

### Variables
```plaintext
set_variable = {
    name = variable_name
    value = 100
}

add_to_variable = {
    name = variable_name
    value = 10
}

multiply_variable = {
    name = variable_name
    value = 1.5
}
```

### Technology
```plaintext
add_technology_researched = tech_key
remove_technology_researched = tech_key
```

### Events
```plaintext
trigger_event = {
    id = event_namespace.1
    popup = yes  # Optional: show as popup
}
```

### State Ownership
```plaintext
set_state_owner = country_scope
cede_state = country_scope
```

### Pops
```plaintext
convert_population = {
    target = culture_key
    value = 0.15  # 15% conversion
}
```

## Conditional Logic

### If-Else
```plaintext
if = {
    limit = {
        # Conditions
    }
    # Effects if true
}
else = {
    # Effects if false
}
```

### While Loop
```plaintext
while = {
    limit = {
        # Condition to continue
    }
    # Effects to execute
}
```

## Common Patterns

### Check and Set Variable
```plaintext
if = {
    limit = {
        NOT = { has_variable = my_variable }
    }
    set_variable = {
        name = my_variable
        value = 0
    }
}
```

### Iterate with Limit
```plaintext
every_scope_state = {
    limit = {
        # Conditions for states to process
        is_incorporated = yes
    }
    # Effects for each matching state
}
```

### Random Selection
```plaintext
random_state = {
    limit = {
        # Conditions
    }
    # Effects on random state
}
```
