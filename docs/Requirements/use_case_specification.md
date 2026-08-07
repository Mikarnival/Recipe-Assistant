# Use Case Specification

## 1. Purpose

This document describes the main use cases and business rules of the Recipe Assistant application.

It complements the Use Case Diagram by documenting:

- User Story mappings
- Actors
- Preconditions
- Triggers
- Main flows
- Alternative flows
- Postconditions
- Use Case relationships
- Business rules

This document focuses on functional behavior. It does not define REST endpoints, database tables, programming classes, frontend components, or deployment architecture.

---

## 2. System Scope

The Recipe Assistant supports four functional areas:

- Recipe Library
- Recipe Import
- Cooking Experience
- Personalization

The current MVP scope is based on the User Stories defined in `UserStories.md`.

---

## 3. Primary Actor

### Home Cook

The Home Cook is the primary actor of the Recipe Assistant.

The Home Cook can:

- Browse recipes
- Search recipes
- View recipe details
- Manage favorite recipes
- Filter and sort recipes
- Create recipes manually
- Edit recipes
- Delete recipes
- Start Cooking Mode
- View cooking steps
- Navigate between cooking steps
- View ingredient quantities
- Mark cooking steps as completed
- View preparation tasks
- Manage spoon profiles
- Set taste preferences
- Choose measurement units
- Set a default serving size
- Save personal preferences

---

## 4. User Story Mapping

| User Story ID | User Story | Epic | Related Use Case |
|---|---|---|---|
| US-001 | Browse recipes | Recipe Library | Browse Recipes |
| US-002 | Search recipes | Recipe Library | Search Recipes |
| US-003 | View recipe details | Recipe Library | View Recipe Details |
| US-004 | Favorite recipes | Recipe Library | Manage Favorites |
| US-005 | Filter recipes by category | Recipe Library | Filter Recipes by Category |
| US-006 | Sort recipes | Recipe Library | Sort Recipes |
| US-007 | Create a recipe manually | Recipe Import | Create Recipe Manually |
| US-008 | Edit a recipe | Recipe Import | Edit Recipe |
| US-009 | Delete a recipe | Recipe Import | Delete Recipe |
| US-010 | Follow a recipe step by step | Cooking Experience | Start Cooking Mode |
| US-011 | View one cooking step at a time | Cooking Experience | View One Cooking Step at a Time |
| US-012 | Navigate between cooking steps | Cooking Experience | Navigate Between Cooking Steps |
| US-013 | View ingredient quantities during cooking | Cooking Experience | View Ingredient Quantities |
| US-014 | Mark cooking steps as completed | Cooking Experience | Mark Cooking Steps as Completed |
| US-015 | View preparation tasks | Cooking Experience | View Preparation Tasks |
| US-016 | Manage spoon profiles | Personalization | Manage Spoon Profiles |
| US-017 | Set taste preference | Personalization | Set Taste Preference |
| US-018 | Choose measurement unit | Personalization | Choose Measurement Unit |
| US-019 | Set default serving size | Personalization | Set Default Serving Size |
| US-020 | Save personal preferences | Personalization | Save Personal Preferences |

---

## 5. Use Case Relationships

### 5.1 `<<include>>`

An `<<include>>` relationship represents required behavior that is executed as part of another Use Case.

Current relationships:

- Start Cooking Mode includes View One Cooking Step at a Time.
- Start Cooking Mode includes Navigate Between Cooking Steps.
- Start Cooking Mode includes View Ingredient Quantities.
- Manage Spoon Profiles includes Save Personal Preferences.
- Set Taste Preference includes Save Personal Preferences.
- Choose Measurement Unit includes Save Personal Preferences.
- Set Default Serving Size includes Save Personal Preferences.

### 5.2 `<<extend>>`

An `<<extend>>` relationship represents optional or conditional behavior.

Current relationship:

- Mark Cooking Steps as Completed extends View One Cooking Step at a Time.

The user can view cooking steps without marking them as completed.

---

# 6. Recipe Library Use Cases

## UC-LIB-01 Browse Recipes

### Goal

The Home Cook views the available recipes and selects a recipe to open.

### Primary Actor

Home Cook

### Related User Story

US-001 — Browse recipes

### Preconditions

- The application is available.
- At least one recipe exists.

### Trigger

The Home Cook opens the Recipe Library.

### Main Flow

1. The Home Cook opens the Recipe Library.
2. The system displays all available recipes.
3. The Home Cook navigates through the recipe list.
4. The Home Cook selects a recipe.
5. The system opens the selected recipe.

### Alternative Flows

#### A1: No recipes exist

1. The Home Cook opens the Recipe Library.
2. The system detects that no recipes exist.
3. The system displays an empty state.

### Postconditions

- The recipe list has been displayed.
- A selected recipe may be opened.

---

## UC-LIB-02 Search Recipes

### Goal

The Home Cook searches for a recipe by name.

### Primary Actor

Home Cook

### Related User Story

US-002 — Search recipes

### Preconditions

- The Recipe Library is available.

### Trigger

The Home Cook enters a recipe name or search term.

### Main Flow

1. The Home Cook opens the search function.
2. The Home Cook enters a search term.
3. The system searches recipe names.
4. The system displays matching recipes.
5. The Home Cook selects a result.

### Alternative Flows

#### A1: No matching recipe exists

1. The system finds no matching recipe.
2. The system displays an empty result.

### Postconditions

- Matching recipes are displayed.

---

## UC-LIB-03 View Recipe Details

### Goal

The Home Cook views recipe information before cooking.

### Primary Actor

Home Cook

### Related User Story

US-003 — View recipe details

### Preconditions

- A recipe exists.
- The Home Cook has selected the recipe.

### Trigger

The Home Cook opens a recipe.

### Main Flow

1. The Home Cook selects a recipe.
2. The system opens the recipe details.
3. The system displays the available recipe information.

### Postconditions

- The recipe details are visible.

---

## UC-LIB-04 Manage Favorites

### Goal

The Home Cook marks or unmarks a recipe as a favorite.

### Primary Actor

Home Cook

### Related User Story

US-004 — Favorite recipes

### Preconditions

- A recipe exists.

### Trigger

The Home Cook selects the favorite action.

### Main Flow

1. The Home Cook opens or selects a recipe.
2. The Home Cook marks the recipe as a favorite.
3. The system saves the favorite status.
4. The system updates the recipe display.

### Alternative Flows

#### A1: Remove favorite

1. The Home Cook selects an existing favorite.
2. The Home Cook removes the favorite status.
3. The system saves the updated status.

### Postconditions

- The favorite status is stored.

---

## UC-LIB-05 Filter Recipes by Category

### Goal

The Home Cook filters recipes by category.

### Primary Actor

Home Cook

### Related User Story

US-005 — Filter recipes by category

### Preconditions

- Recipes exist.
- Recipe categories exist.

### Trigger

The Home Cook selects a category filter.

### Main Flow

1. The Home Cook opens the filter function.
2. The Home Cook selects a category.
3. The system applies the filter.
4. The system displays matching recipes.

### Alternative Flows

#### A1: No recipe matches the category

1. The system finds no matching recipe.
2. The system displays an empty result.

### Postconditions

- Only recipes matching the selected category are displayed.

---

## UC-LIB-06 Sort Recipes

### Goal

The Home Cook changes the order in which recipes are displayed.

### Primary Actor

Home Cook

### Related User Story

US-006 — Sort recipes

### Preconditions

- Multiple recipes exist.

### Trigger

The Home Cook selects a sorting option.

### Main Flow

1. The Home Cook opens the sorting function.
2. The Home Cook selects a sorting option.
3. The system sorts the recipes.
4. The system displays the updated order.

### Postconditions

- Recipes are displayed in the selected order.

---

# 7. Recipe Import Use Cases

## UC-IMP-01 Create Recipe Manually

### Goal

The Home Cook creates a recipe by entering recipe information manually.

### Primary Actor

Home Cook

### Related User Story

US-007 — Create a recipe manually

### Preconditions

- The application is available.

### Trigger

The Home Cook selects the create recipe function.

### Main Flow

1. The Home Cook selects Create Recipe.
2. The system displays a recipe form.
3. The Home Cook enters recipe information.
4. The Home Cook saves the recipe.
5. The system validates the entered information.
6. The system creates the recipe.
7. The system adds the recipe to the Recipe Library.

### Alternative Flows

#### A1: Required information is missing

1. The system detects missing required information.
2. The system highlights the missing fields.
3. The Home Cook completes the information.
4. The Home Cook tries to save again.

#### A2: User cancels creation

1. The Home Cook cancels the creation process.
2. The system does not create a recipe.

### Postconditions

#### Success Postcondition

- A new recipe exists in the Recipe Library.

#### Minimal Postcondition

- No recipe is created if validation fails or the Home Cook cancels.

---

## UC-IMP-02 Edit Recipe

### Goal

The Home Cook corrects or improves existing recipe information.

### Primary Actor

Home Cook

### Related User Story

US-008 — Edit a recipe

### Preconditions

- The recipe exists.
- The Home Cook can access the recipe.

### Trigger

The Home Cook selects the edit function.

### Main Flow

1. The Home Cook opens a recipe.
2. The Home Cook selects Edit.
3. The system displays the editable recipe information.
4. The Home Cook changes one or more fields.
5. The Home Cook saves the changes.
6. The system validates the updated information.
7. The system updates the recipe.

### Alternative Flows

#### A1: Updated information is invalid

1. The system detects invalid information.
2. The system displays a validation message.
3. The Home Cook corrects the information.

#### A2: User cancels editing

1. The Home Cook cancels the edit.
2. The system keeps the existing recipe unchanged.

### Postconditions

- The recipe contains the saved changes.

---

## UC-IMP-03 Delete Recipe

### Goal

The Home Cook removes a recipe from the Recipe Library.

### Primary Actor

Home Cook

### Related User Story

US-009 — Delete a recipe

### Preconditions

- The recipe exists.

### Trigger

The Home Cook selects the delete function.

### Main Flow

1. The Home Cook opens or selects a recipe.
2. The Home Cook selects Delete.
3. The system asks for confirmation.
4. The Home Cook confirms deletion.
5. The system deletes the recipe.
6. The system removes the recipe from the Recipe Library.

### Alternative Flows

#### A1: User cancels deletion

1. The system asks for confirmation.
2. The Home Cook cancels deletion.
3. The recipe remains unchanged.

### Postconditions

- The deleted recipe is no longer available in the Recipe Library.

---

# 8. Cooking Experience Use Cases

## UC-COOK-01 Start Cooking Mode

### Goal

The Home Cook follows a recipe step by step without repeatedly searching for information.

### Primary Actor

Home Cook

### Related User Story

US-010 — Follow a recipe step by step

### Preconditions

- A recipe exists.
- The recipe contains cooking steps.
- The Home Cook has opened the recipe.

### Trigger

The Home Cook selects Start Cooking.

### Main Flow

1. The Home Cook opens a recipe.
2. The Home Cook starts Cooking Mode.
3. The system displays one cooking step.
4. The system displays the ingredient quantities needed during cooking.
5. The Home Cook follows the instructions.
6. The Home Cook moves to the next or previous step.

### Alternative Flows

#### A1: Recipe has no cooking steps

1. The system detects that no cooking steps exist.
2. The system informs the Home Cook.
3. Cooking Mode does not start.

### Postconditions

- Cooking Mode is active.
- A cooking step is displayed.

### Included Use Cases

- UC-COOK-02 View One Cooking Step at a Time
- UC-COOK-03 Navigate Between Cooking Steps
- UC-COOK-04 View Ingredient Quantities

---

## UC-COOK-02 View One Cooking Step at a Time

### Goal

The Home Cook focuses on one cooking step at a time.

### Primary Actor

Home Cook

### Related User Story

US-011 — View one cooking step at a time

### Preconditions

- Cooking Mode is active.
- The recipe contains cooking steps.

### Trigger

The system displays the current cooking step.

### Main Flow

1. The system identifies the current step.
2. The system displays only the current step.
3. The Home Cook follows the displayed instruction.

### Postconditions

- The current step is visible.

---

## UC-COOK-03 Navigate Between Cooking Steps

### Goal

The Home Cook moves between cooking steps at their own pace.

### Primary Actor

Home Cook

### Related User Story

US-012 — Navigate between cooking steps

### Preconditions

- Cooking Mode is active.
- More than one cooking step exists.

### Trigger

The Home Cook selects the next or previous action.

### Main Flow

1. The Home Cook selects Next or Previous.
2. The system identifies the requested step.
3. The system displays that step.

### Alternative Flows

#### A1: First step selected

1. The Home Cook selects Previous on the first step.
2. The system keeps the first step visible.

#### A2: Final step selected

1. The Home Cook selects Next on the final step.
2. The system keeps the final step visible.

### Postconditions

- The selected cooking step is displayed.

---

## UC-COOK-04 View Ingredient Quantities

### Goal

The Home Cook views ingredient quantities while cooking.

### Primary Actor

Home Cook

### Related User Story

US-013 — View ingredient quantities during cooking

### Preconditions

- Cooking Mode is active.
- Ingredient quantities exist.

### Trigger

The system displays cooking information or the Home Cook opens the quantity view.

### Main Flow

1. The system retrieves the recipe ingredient quantities.
2. The system displays the quantities during cooking.

### Postconditions

- Ingredient quantities are visible during Cooking Mode.

---

## UC-COOK-05 Mark Cooking Steps as Completed

### Goal

The Home Cook marks completed cooking steps to track progress.

### Primary Actor

Home Cook

### Related User Story

US-014 — Mark cooking steps as completed

### Relationship

This Use Case extends `View One Cooking Step at a Time`.

### Preconditions

- Cooking Mode is active.
- A cooking step is displayed.

### Trigger

The Home Cook selects the completed action for the current step.

### Main Flow

1. The Home Cook marks the current step as completed.
2. The system saves the completion status.
3. The system updates the step display.

### Alternative Flows

#### A1: Remove completion mark

1. The Home Cook selects a completed step.
2. The Home Cook removes the completed status.
3. The system saves the updated status.

### Postconditions

- The completion status of the cooking step is stored.

---

## UC-COOK-06 View Preparation Tasks

### Goal

The Home Cook views all preparation tasks before cooking.

### Primary Actor

Home Cook

### Related User Story

US-015 — View preparation tasks

### Preconditions

- A recipe exists.
- Preparation tasks exist.

### Trigger

The Home Cook opens the preparation view.

### Main Flow

1. The Home Cook opens a recipe.
2. The Home Cook selects Preparation Tasks.
3. The system displays all preparation tasks.
4. The Home Cook reviews the tasks before cooking.

### Alternative Flows

#### A1: No preparation tasks exist

1. The system detects that no preparation tasks exist.
2. The system informs the Home Cook.

### Postconditions

- Preparation tasks are visible.

---

# 9. Personalization Use Cases

## UC-PER-01 Manage Spoon Profiles

### Goal

The Home Cook configures kitchen spoon sizes for quantity conversion.

### Primary Actor

Home Cook

### Related User Story

US-016 — Manage spoon profiles

### Preconditions

- The Personalization function is available.

### Trigger

The Home Cook opens Spoon Profiles.

### Main Flow

1. The Home Cook opens Spoon Profiles.
2. The system displays existing spoon profiles.
3. The Home Cook creates or edits a spoon profile.
4. The Home Cook enters the spoon size.
5. The system validates the value.
6. The system saves the profile.

### Alternative Flows

#### A1: Invalid spoon size

1. The system detects an invalid value.
2. The system displays a validation message.
3. The Home Cook corrects the value.

### Postconditions

- The spoon profile is saved.

### Included Use Case

- UC-PER-05 Save Personal Preferences

---

## UC-PER-02 Set Taste Preference

### Goal

The Home Cook configures personal taste preferences.

### Primary Actor

Home Cook

### Related User Story

US-017 — Set taste preference

### Preconditions

- The Personalization function is available.

### Trigger

The Home Cook opens Taste Preferences.

### Main Flow

1. The Home Cook opens Taste Preferences.
2. The system displays available preference options.
3. The Home Cook selects or enters a preference.
4. The system saves the preference.

### Postconditions

- The taste preference is saved.

### Included Use Case

- UC-PER-05 Save Personal Preferences

---

## UC-PER-03 Choose Measurement Unit

### Goal

The Home Cook chooses how ingredient quantities are displayed.

### Primary Actor

Home Cook

### Related User Story

US-018 — Choose measurement unit

### Preconditions

- The Personalization function is available.

### Trigger

The Home Cook opens Measurement Unit settings.

### Main Flow

1. The Home Cook opens Measurement Unit settings.
2. The system displays available units.
3. The Home Cook selects a unit.
4. The system saves the selected unit.

### Postconditions

- Ingredient quantities can be displayed using the selected unit.

### Included Use Case

- UC-PER-05 Save Personal Preferences

---

## UC-PER-04 Set Default Serving Size

### Goal

The Home Cook sets a default serving size for recipe adjustment.

### Primary Actor

Home Cook

### Related User Story

US-019 — Set default serving size

### Preconditions

- The Personalization function is available.

### Trigger

The Home Cook opens Serving Size settings.

### Main Flow

1. The Home Cook opens Serving Size settings.
2. The Home Cook enters or selects a serving size.
3. The system validates the value.
4. The system saves the default serving size.

### Alternative Flows

#### A1: Invalid serving size

1. The system detects an invalid serving size.
2. The system displays a validation message.
3. The Home Cook enters another value.

### Postconditions

- The default serving size is saved.

### Included Use Case

- UC-PER-05 Save Personal Preferences

---

## UC-PER-05 Save Personal Preferences

### Goal

The system stores the Home Cook's personal preferences.

### Primary Actor

Home Cook

### Related User Story

US-020 — Save personal preferences

### Preconditions

- The Home Cook has changed at least one preference.

### Trigger

A preference is created or changed.

### Main Flow

1. The Home Cook creates or changes a preference.
2. The system validates the preference.
3. The system saves the preference.
4. The system confirms the saved state where required.

### Alternative Flows

#### A1: Preference cannot be saved

1. The system cannot save the preference.
2. The system displays an error message.
3. The Home Cook can retry.

### Postconditions

#### Success Postcondition

- The preference is available in future sessions.

#### Minimal Postcondition

- An invalid or failed preference change is not treated as saved.

---

# 10. Business Rules

## 10.1 Recipe Library

- Recipes must be available before they can be browsed, searched, filtered, or sorted.
- Search currently applies to recipe names, based on US-002.
- Filtering currently applies to recipe categories, based on US-005.
- Sorting options are not yet defined in the User Stories.

## 10.2 Recipe Import

- Recipes can be created manually.
- Existing recipes can be edited.
- Existing recipes can be deleted.
- Required recipe fields are not yet defined in the User Stories.
- Delete confirmation behavior is included as a working requirement and should be reviewed before implementation.

## 10.3 Cooking Experience

- Cooking Mode presents recipe information step by step.
- The Home Cook can navigate to the next or previous step.
- Ingredient quantities remain accessible during cooking.
- Marking cooking steps as completed is optional.
- Preparation tasks are shown before cooking when they exist.

## 10.4 Personalization

- Spoon profiles contain user-configured spoon sizes.
- Taste preferences can be stored.
- A measurement unit can be selected.
- A default serving size can be stored.
- Saved preferences should remain available in later sessions.
- The exact storage mechanism is not defined in this phase.

---

# 11. Assumptions

The current specification uses the following assumptions:

- The application has one primary actor: Home Cook.
- Recipes already exist before browsing, searching, filtering, or sorting.
- Manual recipe creation is part of the Recipe Import Epic.
- Marking cooking steps as completed is optional.
- Personal preferences are persistent.
- Authentication and user accounts are not yet defined.
- Detailed validation rules will be defined later.
- Sorting criteria are not yet defined.
- Required recipe fields are not yet defined.
- The exact available measurement units are not yet defined.

---

# 12. Out of Scope for This Document

This document does not define:

- REST API endpoints
- HTTP methods
- Database tables
- Database columns
- Programming classes
- UI components
- Authentication implementation
- Cloud infrastructure
- Deployment
- AI model selection
- External recipe source integration
- Video processing
- Cooking history
- Cooking statistics
- Cooking session completion
