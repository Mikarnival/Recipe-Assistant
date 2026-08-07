# Open Questions

## 1. Purpose

This document records requirements and design questions that have not yet been finalized.

These questions are based on the current User Stories and Use Case Specification.

Each question should be reviewed before the related design or implementation work begins.

---

## 2. Status Values

| Status | Meaning |
|---|---|
| Open | The question has not been decided. |
| In Review | The question is currently being analyzed. |
| Decided | A decision has been made and documented. |
| Deferred | The decision is intentionally postponed. |
| Out of Scope | The topic is excluded from the current product scope. |

---

# 3. Recipe Library

## OQ-LIB-01 Empty Recipe Library

**Question:** What should the Home Cook see when no recipes exist?

Possible decisions:

- Display an empty state.
- Display a create-recipe action.
- Display sample recipes.
- Display onboarding information.

**Why it matters:**

This affects:

- Browse Recipes
- First-use experience
- UI design
- Acceptance criteria

**Status:** Open

**Target phase:** UI Design / Acceptance Criteria

---

## OQ-LIB-02 Search Matching Rules

**Question:** How should recipe search match recipe names?

Possible decisions:

- Exact match only.
- Partial match.
- Case-insensitive match.
- Prefix match.
- Typo-tolerant match.

**Why it matters:**

This affects:

- Search behavior
- REST API query design
- Test cases
- User expectations

**Status:** Open

**Target phase:** REST API Design

---

## OQ-LIB-03 Search Result Ordering

**Question:** How should search results be ordered?

Possible decisions:

- Exact matches first.
- Alphabetical order.
- Most recently used first.
- Favorite recipes first.
- Use the currently selected sort order.

**Why it matters:**

This affects:

- Search behavior
- Sort behavior
- UI consistency
- Test cases

**Status:** Open

**Target phase:** REST API Design / UI Design

---

## OQ-LIB-04 Favorite Storage

**Question:** How should favorite status be stored?

Possible decisions:

- Store favorite status directly on the recipe.
- Store a separate favorite relationship.
- Store favorites only locally.
- Store favorites in a user profile.

**Why it matters:**

This affects:

- Domain Model
- Database Design
- Authentication requirements
- REST API Design

**Status:** Open

**Target phase:** Domain Model

---

## OQ-LIB-05 Available Recipe Categories

**Question:** Which recipe categories are available in the MVP?

Possible examples:

- Breakfast
- Lunch
- Dinner
- Dessert
- Soup
- Noodles
- Meat
- Vegetarian

**Why it matters:**

This affects:

- Filter Recipes by Category
- Recipe data model
- Validation
- UI options

**Status:** Open

**Target phase:** Domain Model

---

## OQ-LIB-06 Category Assignment

**Question:** Can one recipe belong to one category or multiple categories?

Possible decisions:

- One category per recipe.
- Multiple categories per recipe.
- One primary category and multiple tags.

**Why it matters:**

This affects:

- Domain Model
- Database relationships
- Filter behavior
- Recipe creation and editing

**Status:** Open

**Target phase:** Domain Model

---

## OQ-LIB-07 Sorting Options

**Question:** Which sorting options are required in the MVP?

Possible options:

- Recipe name
- Creation date
- Last updated date
- Favorite status
- Category
- Most recently opened

**Why it matters:**

This affects:

- Sort Recipes
- REST API query parameters
- UI controls
- Test cases

**Status:** Open

**Target phase:** REST API Design

---

## OQ-LIB-08 Default Sorting

**Question:** Which sort order should be used by default?

Possible decisions:

- Alphabetical order.
- Most recently created first.
- Most recently updated first.
- Favorites first.

**Why it matters:**

This affects:

- Browse Recipes
- Sort Recipes
- User experience
- Acceptance criteria

**Status:** Open

**Target phase:** Requirements / UI Design

---

# 4. Recipe Import

## OQ-IMP-01 Required Recipe Fields

**Question:** Which fields are required when creating a recipe manually?

Possible fields:

- Recipe title
- Ingredients
- Ingredient quantities
- Cooking steps
- Preparation tasks
- Category
- Serving size
- Cooking time
- Notes

**Why it matters:**

This affects:

- Create Recipe Manually
- Validation rules
- Domain Model
- Database Design
- REST API request models

**Status:** Open

**Target phase:** Domain Model

---

## OQ-IMP-02 Optional Recipe Fields

**Question:** Which recipe fields are optional?

Possible fields:

- Description
- Image
- Notes
- Source
- Preparation time
- Cooking time
- Difficulty
- Category

**Why it matters:**

This affects:

- Recipe creation
- Recipe editing
- UI forms
- Database nullability

**Status:** Open

**Target phase:** Domain Model

---

## OQ-IMP-03 Ingredient Structure

**Question:** How should ingredients be represented?

Possible decisions:

- Free-text ingredient lines.
- Separate name, quantity, and unit fields.
- Structured ingredient objects with optional notes.
- A combination of structured fields and free text.

**Why it matters:**

This affects:

- Recipe creation
- Ingredient quantities
- Measurement units
- Spoon profiles
- Database Design
- REST API Design

**Status:** Open

**Target phase:** Domain Model

---

## OQ-IMP-04 Cooking Step Structure

**Question:** What information belongs to one cooking step?

Possible fields:

- Step number
- Instruction text
- Ingredient references
- Quantity references
- Timer
- Image
- Notes
- Completion status

**Why it matters:**

This affects:

- Follow a Recipe Step by Step
- View One Cooking Step at a Time
- Mark Cooking Steps as Completed
- Domain Model
- Database Design

**Status:** Open

**Target phase:** Domain Model

---

## OQ-IMP-05 Preparation Task Structure

**Question:** How are preparation tasks different from cooking steps?

Possible decisions:

- Preparation tasks are stored separately.
- Preparation tasks are cooking steps with a preparation type.
- Preparation tasks are a checklist before Cooking Mode.

**Why it matters:**

This affects:

- View Preparation Tasks
- Recipe creation
- Domain Model
- Cooking workflow

**Status:** Open

**Target phase:** BPMN / Domain Model

---

## OQ-IMP-06 Recipe Drafts

**Question:** Should partially completed manual recipes be saved as drafts?

Possible decisions:

- No draft support.
- Save drafts manually.
- Save drafts automatically.
- Save drafts only after required fields are entered.

**Why it matters:**

This affects:

- Create Recipe Manually
- Edit Recipe
- Data persistence
- User experience

**Status:** Open

**Target phase:** MVP Scope / Domain Model

---

## OQ-IMP-07 Edit Permissions

**Question:** Which recipes can the Home Cook edit?

Possible decisions:

- Only manually created recipes.
- All recipes in the library.
- Only recipes owned by the Home Cook.
- Imported recipes and manually created recipes.

**Why it matters:**

This affects:

- Edit Recipe
- Recipe ownership
- Access control
- Future import behavior

**Status:** Open

**Target phase:** Domain Model

---

## OQ-IMP-08 Delete Confirmation

**Question:** Should deleting a recipe always require confirmation?

Possible decisions:

- Always require confirmation.
- Delete immediately with undo.
- Require confirmation only when related data exists.

**Why it matters:**

This affects:

- Delete Recipe
- Accidental deletion risk
- BPMN
- UI design

**Status:** Open

**Target phase:** BPMN / UI Design

---

## OQ-IMP-09 Delete Behavior

**Question:** Should recipe deletion be permanent or reversible?

Possible decisions:

- Permanent deletion.
- Soft deletion.
- Move to trash.
- Archive the recipe.

**Why it matters:**

This affects:

- Database Design
- Recipe history
- Recovery behavior
- Referential integrity

**Status:** Open

**Target phase:** Database Design

---

## OQ-IMP-10 Related Data on Delete

**Question:** What happens to related data when a recipe is deleted?

Possible related data:

- Favorite status
- Cooking step completion data
- Personal adjustments
- Preparation tasks
- Spoon conversions

**Why it matters:**

This affects:

- Database relationships
- Data consistency
- Delete Recipe
- Future history features

**Status:** Open

**Target phase:** Domain Model / Database Design

---

# 5. Cooking Experience

## OQ-COOK-01 Cooking Mode Entry

**Question:** From which screen can the Home Cook start Cooking Mode?

Possible decisions:

- Recipe Details only.
- Recipe list.
- Preparation Tasks screen.
- Multiple entry points.

**Why it matters:**

This affects:

- Start Cooking Mode
- BPMN
- Navigation
- UI design

**Status:** Open

**Target phase:** BPMN / UI Design

---

## OQ-COOK-02 First Cooking Step

**Question:** Which step should appear when Cooking Mode starts?

Possible decisions:

- Always show the first cooking step.
- Show preparation tasks first.
- Resume the last viewed step.
- Ask the Home Cook where to start.

**Why it matters:**

This affects:

- Start Cooking Mode
- View Preparation Tasks
- View One Cooking Step at a Time
- Session state

**Status:** Open

**Target phase:** BPMN

---

## OQ-COOK-03 Preparation Tasks Timing

**Question:** When should preparation tasks be displayed?

Possible decisions:

- Before Cooking Mode starts.
- As the first screen in Cooking Mode.
- Only when the Home Cook opens them manually.
- Both before and during Cooking Mode.

**Why it matters:**

This affects:

- View Preparation Tasks
- Cooking flow
- BPMN
- UI design

**Status:** Open

**Target phase:** BPMN

---

## OQ-COOK-04 Step Navigation Boundaries

**Question:** What should happen when the Home Cook selects Previous on the first step or Next on the last step?

Possible decisions:

- Disable the unavailable action.
- Keep the current step visible.
- Show a message.
- Move to a completion screen after the last step.

**Why it matters:**

This affects:

- Navigate Between Cooking Steps
- User experience
- Acceptance criteria
- Test cases

**Status:** Open

**Target phase:** BPMN / UI Design

---

## OQ-COOK-05 Step Completion Persistence

**Question:** How long should completed-step status be stored?

Possible decisions:

- Only during the current app session.
- Until Cooking Mode is closed.
- Persist between application sessions.
- Persist until the Home Cook resets progress.

**Why it matters:**

This affects:

- Mark Cooking Steps as Completed
- Database Design
- Cooking session behavior
- Resume behavior

**Status:** Open

**Target phase:** Domain Model

---

## OQ-COOK-06 Step Completion Rules

**Question:** Can the Home Cook mark steps as completed in any order?

Possible decisions:

- Any step can be marked completed.
- Only the current step can be completed.
- Steps must be completed sequentially.
- The system warns but allows out-of-order completion.

**Why it matters:**

This affects:

- Mark Cooking Steps as Completed
- Cooking workflow
- Validation
- Test cases

**Status:** Open

**Target phase:** BPMN / Domain Model

---

## OQ-COOK-07 Unmark Completed Steps

**Question:** Can the Home Cook remove a completed status from a step?

Possible decisions:

- Yes, at any time.
- Yes, only for the current step.
- No, completion is final.
- Allow undo only for a short period.

**Why it matters:**

This affects:

- Mark Cooking Steps as Completed
- State transitions
- UI behavior
- Test cases

**Status:** Open

**Target phase:** BPMN

---

## OQ-COOK-08 Ingredient Quantity Display

**Question:** Should ingredient quantities show all recipe ingredients or only ingredients relevant to the current step?

Possible decisions:

- Show all ingredients.
- Show only step-specific ingredients.
- Allow switching between both views.

**Why it matters:**

This affects:

- View Ingredient Quantities
- Cooking Step structure
- UI design
- Ingredient-to-step relationships

**Status:** Open

**Target phase:** Domain Model / UI Design

---

## OQ-COOK-09 Cooking Progress

**Question:** How should progress be shown during Cooking Mode?

Possible decisions:

- Current step number.
- Percentage completed.
- Completed-step count.
- Progress bar.
- No visual progress indicator.

**Why it matters:**

This affects:

- View One Cooking Step at a Time
- Mark Cooking Steps as Completed
- UI design

**Status:** Open

**Target phase:** UI Design

---

# 6. Personalization

## OQ-PER-01 Spoon Profile Fields

**Question:** Which fields belong to a spoon profile?

Possible fields:

- Profile name
- Spoon type
- Volume
- Unit
- Notes
- Default status

**Why it matters:**

This affects:

- Manage Spoon Profiles
- Domain Model
- Database Design
- Quantity conversion

**Status:** Open

**Target phase:** Domain Model

---

## OQ-PER-02 Multiple Spoon Profiles

**Question:** Can the Home Cook create multiple spoon profiles?

Possible decisions:

- One profile only.
- Multiple named profiles.
- One profile per spoon type.
- One default profile plus optional alternatives.

**Why it matters:**

This affects:

- Manage Spoon Profiles
- Database relationships
- UI design
- Conversion behavior

**Status:** Open

**Target phase:** Domain Model

---

## OQ-PER-03 Supported Taste Preferences

**Question:** Which taste preferences are included in the MVP?

Possible examples:

- Salt level
- Spiciness
- Sweetness
- Oil level

**Why it matters:**

This affects:

- Set Taste Preference
- Domain Model
- Recipe adjustment rules
- UI options

**Status:** Open

**Target phase:** MVP Scope / Domain Model

---

## OQ-PER-04 Taste Preference Scale

**Question:** How should taste preferences be represented?

Possible decisions:

- Low, medium, high.
- Numeric scale.
- Percentage adjustment.
- Custom text.

**Why it matters:**

This affects:

- Set Taste Preference
- Data validation
- Recipe adjustment logic
- UI design

**Status:** Open

**Target phase:** Domain Model

---

## OQ-PER-05 Supported Measurement Units

**Question:** Which measurement units are supported in the MVP?

Possible examples:

- Grams
- Kilograms
- Milliliters
- Liters
- Teaspoons
- Tablespoons
- Cups
- Pieces

**Why it matters:**

This affects:

- Choose Measurement Unit
- Ingredient data
- Spoon profiles
- Quantity conversion
- Validation

**Status:** Open

**Target phase:** Domain Model

---

## OQ-PER-06 Unit Preference Scope

**Question:** Does the selected measurement unit apply to all recipes or only compatible quantities?

Possible decisions:

- Apply globally where conversion is possible.
- Apply only to selected recipes.
- Store one preferred unit per quantity type.
- Let the Home Cook choose per recipe.

**Why it matters:**

This affects:

- Choose Measurement Unit
- Conversion rules
- Personalization model
- UI behavior

**Status:** Open

**Target phase:** Domain Model

---

## OQ-PER-07 Default Serving Size Values

**Question:** Which values are allowed as the default serving size?

Possible decisions:

- Positive whole numbers only.
- Fixed options.
- Decimal values.
- A defined minimum and maximum.

**Why it matters:**

This affects:

- Set Default Serving Size
- Validation
- Recipe quantity adjustment
- UI design

**Status:** Open

**Target phase:** Domain Model

---

## OQ-PER-08 Preference Save Timing

**Question:** When should personal preferences be saved?

Possible decisions:

- Save immediately after each change.
- Save when the Home Cook selects Save.
- Save when leaving the settings screen.
- Save automatically after validation.

**Why it matters:**

This affects:

- Save Personal Preferences
- Use Case relationships
- Error handling
- UI design

**Status:** Open

**Target phase:** BPMN / UI Design

---

## OQ-PER-09 Preference Persistence

**Question:** Where should personal preferences be stored?

Possible decisions:

- Local device storage.
- Backend database.
- User account.
- Anonymous user profile.

**Why it matters:**

This affects:

- Save Personal Preferences
- Architecture
- Authentication
- Database Design
- Cross-device behavior

**Status:** Open

**Target phase:** Architecture / Database Design

---

## OQ-PER-10 Preference Save Failure

**Question:** What should happen when a personal preference cannot be saved?

Possible decisions:

- Show an error and keep the unsaved value visible.
- Revert to the previous saved value.
- Retry automatically.
- Store the change locally and synchronize later.

**Why it matters:**

This affects:

- Save Personal Preferences
- Error handling
- User experience
- Test cases

**Status:** Open

**Target phase:** BPMN / REST API Design

---

# 7. Cross-Cutting Questions

## OQ-GEN-01 Authentication

**Question:** Does the MVP require user authentication?

Possible decisions:

- No authentication.
- Authentication is required.
- Authentication is optional.
- Local use first, account support later.

**Why it matters:**

This affects:

- Favorite status
- Recipe ownership
- Personal preferences
- Data persistence
- Architecture

**Status:** Open

**Target phase:** MVP Scope / Architecture

---

## OQ-GEN-02 Recipe Ownership

**Question:** Who owns recipes created manually?

Possible decisions:

- The current Home Cook.
- All recipes are shared globally.
- Recipes are stored only on the local device.
- Ownership depends on authentication.

**Why it matters:**

This affects:

- Edit Recipe
- Delete Recipe
- Favorite Recipes
- Access control
- Database Design

**Status:** Open

**Target phase:** Domain Model

---

## OQ-GEN-03 Data Persistence Without Authentication

**Question:** How should data be stored if authentication is not included?

Possible decisions:

- Local device storage.
- Anonymous backend profile.
- Temporary application state.
- No persistence between sessions.

**Why it matters:**

This affects:

- Recipes
- Favorites
- Completed cooking steps
- Personal preferences
- Architecture

**Status:** Open

**Target phase:** Architecture

---

## OQ-GEN-04 Validation Error Format

**Question:** How should validation errors be presented consistently?

Possible decisions:

- One message per field.
- One summary message.
- Inline field errors and a summary.
- Standard error codes with user-facing messages.

**Why it matters:**

This affects:

- Create Recipe Manually
- Edit Recipe
- Manage Spoon Profiles
- Set Default Serving Size
- REST API Design
- UI Design

**Status:** Open

**Target phase:** REST API Design / UI Design

---

# 8. Decisions Log

| Decision ID | Question | Decision | Date | Related Document |
|---|---|---|---|---|
| DEC-001 | Is EP-02 kept as Recipe Import? | Yes. The current Epic name remains unchanged. | 2026-08-06 | `UserStories.md` |
| DEC-002 | Is marking a cooking step as completed mandatory? | No. It is optional and extends viewing a cooking step. | 2026-08-06 | `use_case.puml` |
| DEC-003 | Are personal preferences saved? | Yes. Saving personal preferences is included in the current User Stories. | 2026-08-06 | `UserStories.md` |

---

# 9. Review Priority

Resolve before BPMN is finalized:

1. OQ-IMP-05 Preparation Task Structure
2. OQ-IMP-08 Delete Confirmation
3. OQ-COOK-01 Cooking Mode Entry
4. OQ-COOK-02 First Cooking Step
5. OQ-COOK-03 Preparation Tasks Timing
6. OQ-COOK-04 Step Navigation Boundaries
7. OQ-COOK-06 Step Completion Rules
8. OQ-PER-08 Preference Save Timing

Resolve before the Domain Model is finalized:

1. OQ-LIB-04 Favorite Storage
2. OQ-LIB-06 Category Assignment
3. OQ-IMP-01 Required Recipe Fields
4. OQ-IMP-03 Ingredient Structure
5. OQ-IMP-04 Cooking Step Structure
6. OQ-IMP-09 Delete Behavior
7. OQ-COOK-05 Step Completion Persistence
8. OQ-COOK-08 Ingredient Quantity Display
9. OQ-PER-01 Spoon Profile Fields
10. OQ-PER-02 Multiple Spoon Profiles
11. OQ-PER-03 Supported Taste Preferences
12. OQ-PER-05 Supported Measurement Units
13. OQ-PER-07 Default Serving Size Values
14. OQ-GEN-01 Authentication
15. OQ-GEN-02 Recipe Ownership

Resolve before REST API Design is finalized:

1. OQ-LIB-02 Search Matching Rules
2. OQ-LIB-03 Search Result Ordering
3. OQ-LIB-07 Sorting Options
4. OQ-PER-10 Preference Save Failure
5. OQ-GEN-04 Validation Error Format
