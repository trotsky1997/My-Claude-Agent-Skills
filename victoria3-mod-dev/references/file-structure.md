# Victoria 3 Mod File Structure

Complete directory structure for Victoria 3 mods.

## Root Directory Structure

```
mod/
├── MyMod.mod                    # Mod descriptor file
└── MyMod/                       # Mod content folder
    ├── common/                  # Game logic files
    ├── events/                  # Event files
    ├── localization/           # Localization files
    ├── gfx/                     # Graphics assets
    ├── gui/                     # GUI modifications
    ├── map_data/                # Map modifications
    └── thumbnail.png            # Mod thumbnail (256x256)
```

## Common Directory Structure

```
common/
├── achievements/                # Achievement definitions
├── ai_strategies/               # AI strategy definitions
├── amendments/                 # Law amendments
├── battle_conditions/           # Battle condition modifiers
├── building_groups/            # Building group definitions
├── buildings/                   # Building definitions
├── character_interactions/      # Character interaction definitions
├── character_traits/            # Character trait definitions
├── coat_of_arms/               # Coat of arms definitions
├── country_definitions/         # Country definitions
├── country_formation/          # Country formation decisions
├── cultures/                   # Culture definitions
├── decisions/                  # Decision definitions
├── decrees/                    # Decree definitions
├── defines/                    # Game defines
├── diplomatic_actions/        # Diplomatic action definitions
├── diplomatic_plays/           # Diplomatic play definitions
├── goods/                      # Good definitions
├── government_types/           # Government type definitions
├── history/                    # Historical data
│   ├── countries/              # Country history
│   ├── states/                 # State history
│   └── characters/             # Character history
├── ideologies/                 # Ideology definitions
├── institutions/               # Institution definitions
├── interest_groups/            # Interest group definitions
├── journal_entries/            # Journal entry definitions
├── laws/                       # Law definitions
├── modifier_type_definitions/  # Modifier type definitions
├── on_actions/                 # On action triggers
├── pop_types/                  # Pop type definitions
├── production_methods/         # Production method definitions
├── religions/                  # Religion definitions
├── scripted_effects/           # Scripted effect definitions
├── scripted_modifiers/         # Scripted modifier definitions
├── scripted_triggers/          # Scripted trigger definitions
├── static_modifiers/           # Static modifier definitions
├── strategic_regions/          # Strategic region definitions
├── technology/                 # Technology definitions
└── war_goal_types/             # War goal type definitions
```

## Events Directory

```
events/
├── 00_on_actions.txt           # On action triggers
└── <namespace>_events.txt      # Namespace-specific events
```

## Localization Directory

```
localization/
├── english/
│   └── <mod>_l_english.yml
├── simp_chinese/
│   └── <mod>_l_simp_chinese.yml
└── <other_languages>/
```

## File Naming Conventions

- Use descriptive names with underscores
- Prefix with numbers for load order (e.g., `00_`, `01_`)
- Use namespace prefixes for events
- Localization files: `<mod>_l_<language>.yml`
