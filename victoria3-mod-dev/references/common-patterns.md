# Common Victoria 3 Modding Patterns

## Decision Patterns

### Player-Only Decision
```plaintext
my_decision = {
	is_shown = {
		is_ai = no
	}
	possible = {
		# Conditions
	}
	when_taken = {
		# Effects
	}
	ai_chance = {
		base = 0  # AI never takes
	}
}
```

### Conditional Decision
```plaintext
conditional_decision = {
	is_shown = {
		has_modifier = required_modifier
		NOT = { has_variable = decision_taken }
	}
	possible = {
		bureaucracy > 100
	}
	when_taken = {
		set_variable = decision_taken
		# Effects
	}
}
```

## Event Patterns

### Country Event with Multiple Options
```plaintext
namespace = mymod

mymod.1 = {
	type = country_event
	
	title = mymod.1.t
	desc = mymod.1.desc
	
	option = {
		name = mymod.1.a
		add_modifier = {
			name = option_a_modifier
			days = 365
		}
	}
	
	option = {
		name = mymod.1.b
		add_modifier = {
			name = option_b_modifier
			days = 365
		}
	}
}
```

### Triggered Event Chain
```plaintext
mymod.1 = {
	type = country_event
	title = mymod.1.t
	desc = mymod.1.desc
	
	option = {
		name = mymod.1.a
		trigger_event = {
			id = mymod.2
			days = 30
		}
	}
}

mymod.2 = {
	type = country_event
	title = mymod.2.t
	desc = mymod.2.desc
	
	option = {
		name = mymod.2.a
		# Final effects
	}
}
```

## Modifier Patterns

### Temporary Modifier
```plaintext
add_modifier = {
	name = temporary_boost
	days = 90  # 3 months
}
```

### Permanent Modifier
```plaintext
add_modifier = {
	name = permanent_change
	days = -1  # Permanent
}
```

### Conditional Modifier
```plaintext
if = {
	limit = {
		NOT = { has_modifier = my_modifier }
	}
	add_modifier = {
		name = my_modifier
		days = -1
	}
}
```

## Variable Patterns

### Initialize Variable
```plaintext
if = {
	limit = {
		NOT = { has_variable = counter }
	}
	set_variable = {
		name = counter
		value = 0
	}
}
```

### Increment Variable
```plaintext
add_to_variable = {
	name = counter
	value = 1
}
```

### Check Variable Range
```plaintext
if = {
	limit = {
		check_variable = {
			name = counter
			value >= 10
		}
	}
	# Effects when counter >= 10
}
```

## State Manipulation Patterns

### Add Building to State
```plaintext
target_state = {
	add_building = {
		type = building_factory
		level = 1
	}
}
```

### Modify State Infrastructure
```plaintext
target_state = {
	add_state_modifier = {
		name = infrastructure_boost
		days = -1
	}
}
```

## Technology Patterns

### Grant Technology
```plaintext
add_technology_researched = tech_steam_engine
```

### Check Technology Prerequisite
```plaintext
possible = {
	has_technology_researched = prerequisite_tech
}
```

## Localization Patterns

### Basic Localization
```yaml
l_english:
 mymod.1.t:0 "Event Title"
 mymod.1.desc:0 "Event description with $concept_variable$."
 mymod.1.a:0 "Option A"
```

### Localization with Variables
```yaml
l_english:
 mymod.1.desc:0 "The value is [ROOT.GetVariable('counter').GetValue]."
```

### Localization with Concepts
```yaml
l_english:
 mymod.1.desc:0 "This affects $concept_bureaucracy$ and $concept_authority$."
```

## Error Prevention Patterns

### Safe Variable Access
```plaintext
if = {
	limit = {
		has_variable = my_variable
	}
	# Use variable
}
```

### Safe Scope Access
```plaintext
if = {
	limit = {
		exists = target_country
	}
	target_country = {
		# Safe to access
	}
}
```
