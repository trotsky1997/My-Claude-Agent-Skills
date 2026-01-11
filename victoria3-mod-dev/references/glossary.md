# Victoria 3 Modding Glossary

Comprehensive glossary of terms used in Victoria 3 modding.

## A

**AI Chance** - A value (0-100) in decisions that determines how likely the AI is to take that decision. `base = 0` means AI never takes it, `base = 100` means AI always takes it.

**Amendment** - A modification to an existing law that can be passed separately. Defined in `common/amendments/`.

**Authority** - A country resource representing the government's ability to enforce laws and decrees. Used in conditions like `authority > 100`.

## B

**Building** - A structure in a state that produces goods, provides services, or generates income. Defined in `common/buildings/`.

**Building Group** - A category that groups related buildings together. Defined in `common/building_groups/`.

**Bureaucracy** - A country resource representing administrative capacity. Required for many government functions. Used in conditions like `bureaucracy > 200`.

## C

**Character** - An individual person in the game (ruler, general, admiral, etc.). Has traits, age, and other properties.

**Character Event** - An event that targets a specific character. Type: `character_event`.

**Character Interaction** - An action that can be taken on a character (e.g., exile, promote). Defined in `common/character_interactions/`.

**Character Trait** - A property of a character that affects their abilities or behavior. Defined in `common/character_traits/`.

**Condition** - A check that evaluates to true or false. Used in `is_shown`, `possible`, `trigger`, and `limit` blocks.

**Country** - A political entity in the game. The primary scope for many modding operations.

**Country Event** - An event that targets a country. Type: `country_event`.

**Culture** - A group of people sharing common traditions. Defined in `common/cultures/`.

## D

**Decision** - A player or AI action that can be taken when certain conditions are met. Defined in `common/decisions/`.

**Decree** - A state-level action that provides temporary or permanent effects. Defined in `common/decrees/`.

**Descriptor File** - The `.mod` file that tells the game about your mod. Contains mod metadata.

**Diplomatic Action** - An action between countries (e.g., declare war, form alliance). Defined in `common/diplomatic_actions/`.

**Diplomatic Play** - A diplomatic crisis that can escalate to war. Defined in `common/diplomatic_plays/`.

## E

**Effect** - An action that changes the game state. Examples: `add_modifier`, `set_variable`, `trigger_event`.

**Event** - A popup or notification that presents information and choices to the player. Defined in `events/`.

**Event Chain** - A series of events triggered in sequence, often with delays between them.

**Event Namespace** - A prefix for event IDs to avoid conflicts. Example: `namespace = mymod` means events are `mymod.1`, `mymod.2`, etc.

## F

**FROM** - A scope operator that refers to the previous scope in the scope chain.

**FROMFROM** - A scope operator that refers to two scopes back in the chain.

## G

**Good** - A tradeable commodity in the game (e.g., grain, iron, tools). Defined in `common/goods/`.

**Government Type** - The type of government a country has (e.g., monarchy, republic). Defined in `common/government_types/`.

## H

**Hidden Trigger** - A condition in decisions that is checked but not displayed to the player. Used for internal logic.

**Homeland** - A state region where a culture is considered native. Cultures have stronger presence in their homelands.

## I

**Ideology** - A set of political beliefs that interest groups can have. Defined in `common/ideologies/`.

**Influence** - A country resource representing diplomatic power. Used in conditions like `influence > 50`.

**Interest Group** - A political faction representing a segment of society (e.g., landowners, industrialists). Defined in `common/interest_groups/`.

**Is Shown** - A block in decisions that determines when the decision appears in the decision list.

## J

**Journal Entry** - A long-term objective or situation that tracks progress over time. Defined in `common/journal_entries/`.

## L

**Law** - A policy that affects how a country functions (e.g., voting rights, economic system). Defined in `common/laws/`.

**Limit** - A block that filters which items are processed in loops or conditional effects.

**Localization** - Text displayed to players in their language. Stored in `localization/<language>/` as YAML files.

## M

**Mean Time To Happen (MTTH)** - The average time before a random event fires. Used in event definitions.

**Modifier** - A temporary or permanent effect that changes game values (e.g., production efficiency, prestige). Defined in `common/static_modifiers/` or added dynamically.

**Modifier Type** - A category of modifiers that defines what values they can affect. Defined in `common/modifier_type_definitions/`.

## N

**Namespace** - A prefix used to avoid naming conflicts. Required for events, optional for other content.

## O

**On Action** - A trigger that fires at specific game moments (e.g., `on_game_start`, `on_monthly_pulse`). Defined in `common/on_actions/`.

**Option** - A choice available in an event. Each option can have different effects.

## P

**Possible** - A block in decisions that determines when the decision is available (not grayed out).

**Pop** - A population unit representing a group of people with shared culture, religion, and profession.

**Pop Type** - A category of pops (e.g., aristocrats, laborers, machinists). Defined in `common/pop_types/`.

**PREV** - A scope operator that refers to the previous scope, same as `FROM`.

**Production Method** - A way a building can produce goods, with different inputs, outputs, and workforce requirements. Defined in `common/production_methods/`.

**Prestige** - A country resource representing international standing. Used in conditions like `prestige > 100`.

## R

**Religion** - A faith system in the game. Defined in `common/religions/`.

**ROOT** - A scope operator that refers to the original scope where an effect chain started.

## S

**Scope** - The current context of evaluation (country, state, character, etc.). Determines what conditions and effects are available.

**Scope Change** - Changing from one scope type to another (e.g., `country = { }` changes to country scope).

**Scripted Effect** - A reusable block of effects that can be called by name. Defined in `common/scripted_effects/`.

**Scripted Modifier** - A reusable modifier definition. Defined in `common/scripted_modifiers/`.

**Scripted Trigger** - A reusable condition block that can be called by name. Defined in `common/scripted_triggers/`.

**State** - A province or region in the game. Can be owned by countries and contain buildings.

**State Event** - An event that targets a specific state. Type: `state_event`.

**State Region** - A collection of states that form a historical region. Used in conditions like `owns_entire_state_region`.

**Static Modifier** - A predefined modifier that can be referenced by name. Defined in `common/static_modifiers/`.

**Strategic Region** - A large geographic area used for military and diplomatic purposes. Defined in `common/strategic_regions/`.

## T

**Technology** - A researchable advancement that unlocks new buildings, production methods, or capabilities. Defined in `common/technology/`.

**THIS** - A scope operator that refers to the current scope.

**Trigger** - A condition block that determines when an event fires or an effect applies.

**Type** - Specifies the category of an event (`country_event`, `state_event`, `character_event`).

## V

**Variable** - A custom value that can be stored and checked. Created with `set_variable`, checked with `has_variable` or `check_variable`.

## W

**When Taken** - A block in decisions that contains effects executed when the decision is taken.

**War Goal** - An objective in a diplomatic play or war. Defined in `common/war_goal_types/`.

## Scope Operators Reference

| Operator | Meaning | Use Case |
|----------|---------|----------|
| `ROOT` | Original scope | Access the starting scope from deep in a scope chain |
| `THIS` | Current scope | Explicitly reference current scope (rarely needed) |
| `FROM` | Previous scope | Access the scope one level up |
| `PREV` | Previous scope | Same as FROM |
| `FROMFROM` | Two scopes back | Access scope two levels up |
| `FROMFROMFROM` | Three scopes back | Access scope three levels up |

## Common Scope Types

| Scope Type | Description | Common Uses |
|------------|-------------|-------------|
| `country` | A country | Most decisions, country events, country modifiers |
| `state` | A state/province | State events, building operations, state modifiers |
| `character` | A person | Character events, character interactions |
| `building` | A building | Production method changes, building modifiers |
| `interest_group` | An interest group | Political operations, approval changes |
| `culture` | A culture | Cultural operations, assimilation |
| `religion` | A religion | Religious operations, conversion |

## Common Resource Types

| Resource | Description | Typical Range |
|----------|-------------|---------------|
| `bureaucracy` | Administrative capacity | 0-1000+ |
| `authority` | Government enforcement power | 0-500+ |
| `influence` | Diplomatic power | 0-1000+ |
| `prestige` | International standing | -1000 to 1000+ |
| `money` | Treasury balance | Can be negative |

## File Extension Reference

| Extension | Purpose | Location |
|-----------|---------|----------|
| `.mod` | Mod descriptor | `mod/` directory |
| `.txt` | Game logic files | `common/`, `events/` |
| `.yml` | Localization files | `localization/<language>/` |
| `.dds` | Graphics files | `gfx/` |
| `.gui` | GUI definitions | `gui/` |

## Event Type Reference

| Type | Scope | Use Case |
|------|-------|----------|
| `country_event` | Country | National events, policy changes |
| `state_event` | State | Regional events, local crises |
| `character_event` | Character | Personal events, character interactions |

## Common Condition Patterns

| Pattern | Example | Meaning |
|---------|---------|---------|
| `is_ai = no` | `is_ai = no` | Player only |
| `has_modifier` | `has_modifier = my_modifier` | Check for modifier |
| `has_technology` | `has_technology_researched = tech_steam` | Check technology |
| `numeric comparison` | `bureaucracy > 100` | Compare resource value |
| `scope exists` | `exists = target_country` | Check if scope exists |
| `has_variable` | `has_variable = my_var` | Check if variable exists |

## Common Effect Patterns

| Pattern | Example | Meaning |
|---------|---------|---------|
| `add_modifier` | `add_modifier = { name = mod days = 365 }` | Add temporary modifier |
| `set_variable` | `set_variable = { name = var value = 10 }` | Set variable value |
| `trigger_event` | `trigger_event = { id = event.1 }` | Fire an event |
| `add_technology` | `add_technology_researched = tech` | Grant technology |

## Game Mechanics Terms

**Assimilation** - The process of pops converting to the primary culture of their country.

**Bureaucratic Capacity** - The maximum amount of bureaucracy a country can have, determined by government administration buildings.

**Cash Reserves** - Money stored by buildings for expansion and maintenance.

**Construction** - The process of building new structures or expanding existing ones.

**Cultural Obsession** - A strong preference for a specific good within a culture, increasing demand.

**Discrimination** - How pops are treated based on their culture or religion relative to the country's primary culture and state religion.

**Economic System** - A law category determining how the economy is organized (e.g., Traditionalism, Interventionism, Laissez-Faire).

**Government Legitimacy** - A measure of how stable and accepted the current government is.

**Incorporation** - The process of making a state a full part of the country (vs. unincorporated territory).

**Interest Group Approval** - How much an interest group supports the current government (-100 to +100).

**Investment Pool** - Money from capitalists and aristocrats used for private construction.

**Literacy** - The percentage of pops who can read and write, affecting research speed and pop qualifications.

**Market** - A collection of states that trade goods with each other.

**Migration** - The movement of pops between states, often seeking better opportunities.

**Political Movement** - A movement pushing for a specific law change, supported by interest groups.

**Pop Growth** - The natural increase or decrease of population over time.

**Production Method** - How a building produces goods, affecting inputs, outputs, and workforce.

**Radicalism** - A measure of pops' dissatisfaction with the current system.

**Standard of Living** - The quality of life for pops, affecting their happiness and political behavior.

**Subject** - A country that is subordinate to another (puppet, vassal, etc.).

**Throughput** - A bonus to production efficiency based on input availability.

**Trade Route** - A connection between markets for exchanging goods.

**Unemployment** - Pops without jobs, which can lead to radicalism and migration.

**War Exhaustion** - A measure of how tired a country is of fighting, affecting willingness to continue war.

## Logical Operators

**AND** - All conditions inside must be true for the block to be true.

**OR** - At least one condition inside must be true for the block to be true.

**NOT** - The condition inside must be false for the block to be true.

**NOR** - None of the conditions inside must be true for the block to be true.

## Special Concepts

**Custom Tooltip** - A way to show additional information to the player when a condition is not met. Format: `custom_tooltip = { text = key condition = { ... } }`.

**Hidden Effect** - An effect that executes but doesn't show in tooltips. Useful for internal logic.

**Hidden Trigger** - A condition that is checked but not displayed to the player. Used for internal decision logic.

**Iteration** - Looping through multiple scopes. Examples: `every_scope_state`, `every_scope_country`, `random_state`.

**Mean Time To Happen (MTTH)** - The average time before a random event fires. Lower values mean more frequent events.

**Random Selection** - Picking a random scope from matching conditions. Examples: `random_state`, `random_country`, `random_character`.

**Scope Chain** - The sequence of scope changes from ROOT through nested scopes. Scope operators navigate this chain.

**Tooltip** - Information displayed when hovering over UI elements. Can be customized with `custom_tooltip`.

## Modding-Specific Terms

**Base Game** - The original game files, typically located in the game installation directory.

**Dependency** - A mod that must be loaded before your mod. Specified in `.mod` file with `dependencies = { "mod_name" }`.

**Override** - Replacing a game file with a mod file. Files with the same path override base game files.

**Replace Folder** - A folder in localization that completely replaces base game localization instead of merging.

**Thumbnail** - A 256x256 pixel image displayed in the mod launcher. Named `thumbnail.png` in mod root.

**Version Tag** - The `supported_version` field in `.mod` file. Use `"*"` for all versions or specific version strings.
