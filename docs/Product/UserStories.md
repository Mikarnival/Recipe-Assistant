# Recipe Assistant User Stories

## 1. Introduction

This document describes the initial user stories for the Recipe Assistant project.

The stories are grouped by epic and represent the functional requirements of the first product version (MVP).

---

## 2. Epics

| Epic ID | Epic | Description |
|----------|------|-------------|
| EP-01 | Recipe Library| Browse, search and organize recipes before cooking.|
| EP-02 | Recipe Import| Create recipes manually or import them from external sources.|
| EP-03 | Cooking Experience| Guide users through the cooking process with clear step-by-step instructions.|
| EP-04 | Personalization| Customize recipes according to personal preferences and kitchen tools.|

---

## 3. User Stories

### EP-01: Recipe Library

---

#### US-001

**Title**

Browse recipes

**User Story**

> As a home cook, I want to browse my recipes, so that I can quickly find the recipe I want to cook.

**Acceptance Criteria**

- [ ] All available recipes are displayed in the recipe library.
- [ ] Recipes can be navigated in the list.
- [ ] A recipe can be selected.
- [ ] A selected recipe can be opened.

**Priority**

High

**MVP**

Yes

---

#### US-002

**Title**

Search recipes

**User Story**

> As a home cook, I want to search recipes by name, so that I can quickly find a specific recipe.

**Acceptance Criteria**

- [ ] A search field is available in the recipe library.
- [ ] The user can enter a recipe name or part of a recipe name.
- [ ] Matching recipes are displayed.
- [ ] A search result can be opened.
- [ ] If no recipe matches the search term, an empty result is shown.

**Priority**

Medium

**MVP**

Yes

---

#### US-003

**Title**

View recipe details

**User Story**

> As a home cook, I want to open a recipe, so that I can view its details before cooking.

**Acceptance Criteria**

- [ ] A recipe can be opened from the recipe library.
- [ ] The recipe title is displayed.
- [ ] Ingredients and quantities are displayed.
- [ ] Cooking steps are displayed.
- [ ] The serving size is displayed when available.
- [ ] Preparation tasks are displayed when available.

**Priority**

Medium

**MVP**

Yes

---

#### US-004

**Title**

Favorite recipes

**User Story**

> As a home cook, I want to mark a recipe as a favorite, so that I can quickly access it later.

**Acceptance Criteria**

- [ ] A recipe can be marked as a favorite.
- [ ] A favorite recipe is visually identifiable.
- [ ] The favorite status is saved.
- [ ] A recipe can be removed from favorites.
- [ ] The updated favorite status is shown immediately.

**Priority**

Medium

**MVP**

Yes

---

#### US-005

**Title**

Filter recipes by category

**User Story**

> As a home cook, I want to filter recipes by category, so that I can quickly find similar recipes.

**Acceptance Criteria**

- [ ] Available categories can be selected as filters.
- [ ] Only recipes matching the selected category are displayed.
- [ ] The active filter is visible.
- [ ] The filter can be cleared.
- [ ] If no recipe matches the selected category, an empty result is shown.

**Priority**

Medium

**MVP**

Yes

---

#### US-006

**Title**

Sort recipes

**User Story**

> As a home cook, I want to sort recipes, so that I can quickly find the recipes I am looking for.

**Acceptance Criteria**

- [ ] A sorting control is available in the recipe library.
- [ ] At least one sorting option can be selected.
- [ ] Recipes are reordered according to the selected option.
- [ ] The active sorting option is visible.

**Priority**

Medium

**MVP**

Yes

---

### EP-02: Recipe Import

---

#### US-007

**Title**

Create a recipe manually

**User Story**

> As a home cook, I want to create a recipe manually, so that I can organize my own recipe in the application.

**Acceptance Criteria**

- [ ] A new recipe form can be opened.
- [ ] The user can enter a recipe title.
- [ ] The user can add ingredients and quantities.
- [ ] The user can add cooking steps.
- [ ] The recipe can be saved when required information is valid.
- [ ] Validation feedback is shown when required information is missing or invalid.
- [ ] A successfully created recipe appears in the recipe library.

**Priority**

High

**MVP**

Yes

---

#### US-008

**Title**

Edit a recipe

**User Story**

> As a home cook, I want to edit a recipe, so that I can correct or improve the recipe information.

**Acceptance Criteria**

- [ ] An existing recipe can be opened for editing.
- [ ] Existing recipe information is displayed in editable fields.
- [ ] The user can change recipe information.
- [ ] Invalid changes are rejected with validation feedback.
- [ ] Valid changes can be saved.
- [ ] The updated recipe details are shown after saving.
- [ ] Cancelling the edit keeps the previous recipe information unchanged.

**Priority**

Medium

**MVP**

Yes

---

#### US-009

**Title**

Delete a recipe

**User Story**

> As a home cook, I want to delete a recipe, so that I can keep my recipe library organized.

**Acceptance Criteria**

- [ ] A delete action is available for an existing recipe.
- [ ] The user is asked to confirm the deletion.
- [ ] Confirming the action removes the recipe from the recipe library.
- [ ] Cancelling the action keeps the recipe unchanged.
- [ ] A deleted recipe can no longer be opened from the recipe library.

**Priority**

Medium

**MVP**

Yes

---

### EP-03: Cooking Experience

---

#### US-010

**Title**

Follow a recipe step by step

**User Story**

> As a home cook, I want to start cooking mode, so that I can focus on cooking without repeatedly searching for information.

**Acceptance Criteria**

- [ ] Cooking mode can be started from a recipe.
- [ ] The current cooking step is clearly displayed.
- [ ] Ingredient quantities remain accessible during cooking.
- [ ] The user can navigate through the cooking steps.
- [ ] The user can leave cooking mode and return to the recipe.

**Priority**

Medium

**MVP**

Yes

---

#### US-011

**Title**

View one cooking step at a time

**User Story**

> As a home cook, I want to view one cooking step at a time, so that I always know what to do next.

**Acceptance Criteria**

- [ ] Only the current cooking step is shown as the primary instruction.
- [ ] The current step number is displayed.
- [ ] The total number of cooking steps is displayed.
- [ ] The instruction text for the current step is readable without opening another screen.

**Priority**

Medium

**MVP**

Yes

---

#### US-012

**Title**

Navigate between cooking steps

**User Story**

> As a home cook, I want to move to the next or previous cooking step, so that I can follow the recipe at my own pace.

**Acceptance Criteria**

- [ ] The user can move to the next cooking step.
- [ ] The user can move to the previous cooking step.
- [ ] The current step updates after navigation.
- [ ] Navigation does not move before the first step.
- [ ] Navigation does not move past the final step.

**Priority**

Medium

**MVP**

Yes

---

#### US-013

**Title**

View ingredient quantities during cooking

**User Story**

> As a home cook, I want to view ingredient quantities while cooking, so that I do not need to search through the recipe again.

**Acceptance Criteria**

- [ ] Ingredient quantities are accessible while cooking mode is active.
- [ ] Ingredient names are displayed together with their quantities.
- [ ] Measurement units are displayed when available.
- [ ] The user can return to the current cooking step after viewing ingredient quantities.

**Priority**

Medium

**MVP**

Yes

---

#### US-014

**Title**

Mark cooking steps as completed

**User Story**

> As a home cook, I want to mark completed cooking steps, so that I always know where I am in the recipe.

**Acceptance Criteria**

- [ ] A cooking step can be marked as completed.
- [ ] A completed step is visually distinguishable from an incomplete step.
- [ ] The completion status is retained while navigating between steps.
- [ ] A completed step can be marked as incomplete again.

**Priority**

Medium

**MVP**

Yes

---

#### US-015

**Title**

View preparation tasks

**User Story**

> As a home cook, I want to view all preparation tasks before cooking, so that I can prepare everything in advance.

**Acceptance Criteria**

- [ ] Preparation tasks are available before cooking starts.
- [ ] All preparation tasks for the selected recipe are displayed together.
- [ ] Preparation tasks are displayed in a clear order.
- [ ] The user can start cooking mode after reviewing the preparation tasks.
- [ ] If no preparation tasks exist, the application handles the empty state clearly.

**Priority**

Medium

**MVP**

Yes

---

### EP-04: Personalization

---

#### US-016

**Title**

Manage spoon profiles

**User Story**

> As a home cook, I want to configure the size of my kitchen spoon, so that ingredient quantities can be converted into measurements that I can easily use.

**Acceptance Criteria**

- [ ] A spoon profile can be created.
- [ ] The spoon size can be entered using a supported volume unit.
- [ ] Invalid spoon sizes are rejected with validation feedback.
- [ ] An existing spoon profile can be edited.
- [ ] An existing spoon profile can be deleted.
- [ ] Saved spoon profiles are available for quantity conversion.

**Priority**

Medium

**MVP**

Yes

---

#### US-017

**Title**

Set taste preference

**User Story**

> As a home cook, I want to set my taste preference, so that recipe seasoning can better match my personal preference.

**Acceptance Criteria**

- [ ] Available taste preferences can be viewed.
- [ ] The user can select or change a taste preference.
- [ ] The selected preference is saved.
- [ ] The saved preference is shown when the settings are opened again.

**Priority**

Medium

**MVP**

Yes

---

#### US-018

**Title**

Choose measurement unit

**User Story**

> As a home cook, I want to choose how ingredient quantities are displayed, so that I can use the measurements that I am familiar with.

**Acceptance Criteria**

- [ ] Supported measurement units can be viewed.
- [ ] The user can select a preferred measurement unit.
- [ ] The selected unit is saved.
- [ ] Compatible ingredient quantities are displayed using the selected unit.
- [ ] The saved unit remains selected when the settings are opened again.

**Priority**

Medium

**MVP**

Yes

---

#### US-019

**Title**

Set default serving size

**User Story**

> As a home cook, I want to set my default serving size, so that recipes are automatically adjusted to my household.

**Acceptance Criteria**

- [ ] The user can enter or select a default serving size.
- [ ] Invalid serving sizes are rejected with validation feedback.
- [ ] The selected serving size is saved.
- [ ] Recipes use the saved serving size as the default when applicable.
- [ ] The user can change the default serving size later.

**Priority**

Medium

**MVP**

Yes

---

#### US-020

**Title**

Save personal preferences

**User Story**

> As a home cook, I want my preferences to be saved, so that I do not need to configure them every time.

**Acceptance Criteria**

- [ ] Valid preference changes can be saved.
- [ ] Saved preferences remain available after leaving the settings screen.
- [ ] Saved preferences are restored when the application is opened again.
- [ ] Failed save operations are communicated to the user.
- [ ] Unsaved invalid values do not replace previously saved preferences.

**Priority**

Medium

**MVP**

Yes

---

## 4. Story Prioritization

| ID | Story | Priority | MVP |
|----|-------|----------|-----|
| US-001 | Browse recipes | High | Yes |
| US-002 | Search recipes | Medium | Yes |
| US-003 | View recipe details | Medium | Yes |
| US-004 | Favorite recipes | Medium | Yes |
| US-005 | Filter recipes by category | Medium | Yes |
| US-006 | Sort recipes | Medium | Yes |
| US-007 | Create a recipe manually | High | Yes |
| US-008 | Edit a recipe | Medium | Yes |
| US-009 | Delete a recipe | Medium | Yes |
| US-010 | Follow a recipe step by step | Medium | Yes |
| US-011 | View one cooking step at a time | Medium | Yes |
| US-012 | Navigate between cooking steps | Medium | Yes |
| US-013 | View ingredient quantities during cooking | Medium | Yes |
| US-014 | Mark cooking steps as completed | Medium | Yes |
| US-015 | View preparation tasks | Medium | Yes |
| US-016 | Manage spoon profiles | Medium | Yes |
| US-017 | Set taste preference | Medium | Yes |
| US-018 | Choose measurement unit | Medium | Yes |
| US-019 | Set default serving size | Medium | Yes |
| US-020 | Save personal preferences | Medium | Yes |

---

## 5. MVP Scope

The first version of Recipe Assistant focuses on the core recipe management and cooking workflow.

The MVP includes:

- Browsing the recipe library
- Searching recipes by name
- Viewing recipe details
- Marking recipes as favorites
- Filtering recipes by category
- Sorting recipes
- Creating recipes manually
- Editing recipes
- Deleting recipes
- Starting cooking mode
- Viewing one cooking step at a time
- Navigating between cooking steps
- Viewing ingredient quantities while cooking
- Marking cooking steps as completed
- Viewing preparation tasks before cooking
- Managing spoon profiles
- Setting taste preferences
- Choosing measurement units
- Setting a default serving size
- Saving personal preferences

The following features are excluded from the current MVP unless added through future User Stories:

- Automatic import from external video platforms
- Automatic import from webpages
- AI-based recipe extraction
- Cooking history
- Cooking statistics
- Cooking feedback
- Social sharing
- Multi-user collaboration
- Advanced recommendation features

---

## 6. Notes

The user stories defined in this document will be used as the foundation for:

- Product Backlog
- Sprint Planning
- Use Case Diagram
- BPMN
- Domain Model
- Database Design
- API Design
- UI Design
- Test Design

Acceptance Criteria describe expected functional behavior at the current requirements level. Detailed validation rules and technical constraints will be refined during later design phases.

---

## Review History

### Review 1 – 2026-08-01

**Status**

Draft

**Notes**

- Initial Epic structure created.
- Initial User Stories defined.
- Most Acceptance Criteria were still incomplete.

### Review 2 – 2026-08-07

**Status**

Ready for requirements review

**Notes**

- Acceptance Criteria completed for US-001 to US-020.
- Story Prioritization completed.
- MVP Scope completed.
- Existing Priority and MVP values from each User Story were used as the source of truth for the prioritization table.
- Minor wording and formatting issues corrected.
