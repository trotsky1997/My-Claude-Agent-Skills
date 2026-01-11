# Victoria 3 Modding Examples

## Complete Decision Example

```plaintext
# File: common/decisions/my_mod_decisions.txt

revive_olympic_games_decision = {
	is_shown = {
		exists = c:GRE
		c:GRE ?= THIS
	}

	possible = {
		c:GRE ?= THIS
		has_technology_researched = organized_sports
		hidden_trigger = {
			NOT = { has_variable = revive_olympics_decision_taken }
		}
	}

	when_taken = {
		set_variable = {
			name = revive_olympics_decision_taken
			value = yes
		}
		add_modifier = {
			name = modifier_olympic_games
		}
		add_modifier = {
			name = modifier_olympic_games_bureaucracy
			days = short_modifier_time
		}
	}

	ai_chance = {
		value = 0
		if = {
			limit = { bureaucracy > 0 }
			add = 5
		}
		if = {
			limit = {
				OR = {
					is_diplomatic_play_committed_participant = yes
					is_at_war = yes
				}
			}
			multiply = 0
		}
	}
}
```

## Complete Event Example

```plaintext
# File: events/my_mod_events.txt

namespace = mymod

mymod.1 = {
	type = country_event
	
	title = mymod.1.t
	desc = mymod.1.desc
	
	trigger = {
		has_modifier = modifier_olympic_games
		year >= 1900
	}
	
	mean_time_to_happen = {
		days = 365
	}
	
	option = {
		name = mymod.1.a
		add_modifier = {
			name = olympic_boost
			days = 90
		}
	}
	
	option = {
		name = mymod.1.b
		remove_modifier = modifier_olympic_games
	}
}
```

## Complete Localization Example

```yaml
# File: localization/english/my_mod_l_english.yml

l_english:
 # Decision localization
 revive_olympic_games_decision:0 "Revive Olympic Games"
 revive_olympic_games_decision_desc:0 "Restore the ancient tradition of the Olympic Games."
 
 # Event localization
 mymod.1.t:0 "Olympic Games Success"
 mymod.1.desc:0 "The Olympic Games have been a great success, boosting national prestige."
 mymod.1.a:0 "Excellent!"
 mymod.1.b:0 "End the games"
```

## Building Modification Example

```plaintext
# File: common/buildings/my_mod_buildings.txt

# Override existing building
building_factory = {
	# Copy base definition and modify
	base_building = building_factory
	
	# Add new production method
	production_method_groups = {
		pmg_my_custom_method
	}
}
```

## Modifier Definition Example

```plaintext
# File: common/static_modifiers/my_mod_modifiers.txt

modifier_olympic_games = {
	icon = "gfx/interface/icons/modifiers/modifier_positive.dds"
	
	country_prestige_add = 10
	country_trade_route_competitiveness_add = 0.05
}
```

## Technology Addition Example

```plaintext
# File: common/technology/my_mod_tech.txt

tech_my_custom_tech = {
	icon = "gfx/interface/icons/technology/industrial_tech.dds"
	
	cost = 10000
	
	prerequisites = {
		tech_steam_engine
	}
	
	unlocks = {
		building_my_custom_building
	}
}
```

## On Action Trigger Example

```plaintext
# File: common/on_actions/my_mod_on_actions.txt

on_game_start = {
	events = {
		mymod.1
	}
}

on_monthly_pulse = {
	events = {
		mymod.monthly.1
	}
}
```

## Scripted Effect Example

```plaintext
# File: common/scripted_effects/my_mod_effects.txt

my_custom_effect = {
	if = {
		limit = {
			NOT = { has_modifier = my_modifier }
		}
		add_modifier = {
			name = my_modifier
			days = 365
		}
	}
	
	add_to_variable = {
		name = my_counter
		value = 1
	}
}
```

## Scripted Trigger Example

```plaintext
# File: common/scripted_triggers/my_mod_triggers.txt

is_eligible_for_my_decision = {
	has_technology_researched = required_tech
	bureaucracy > 100
	NOT = { has_variable = decision_taken }
}
```
