# Recipe Assistant

A recipe assistant designed to make cooking instructions easier to follow, especially when recipes come from videos or long-form content.

The project currently focuses on building a recipe library where users can browse, search, filter, sort, favorite, and view recipe details.

The first client is being developed as a WeChat Mini Program, with a FastAPI backend.

---

## Project Status

Current development status:

| User Story | Feature | Status |
|---|---|---|
| US-001 | Browse recipes | ✅ Completed |
| US-002 | Search recipes | ✅ Completed |
| US-003 | View recipe details | ✅ Completed |
| US-004 | Favorite recipes | ✅ Completed |
| US-005 | Filter recipes by category | ✅ Completed |
| US-006 | Sort recipes | ✅ Completed |

The current development batch covers US-004, US-005, and US-006.

---

## Features

### Recipe Library

Users can browse available recipes and see basic information such as:

- Recipe title
- Category
- Servings
- Favorite status

### Search

Users can search recipes by title.

Example:

```text
Beef
```

The backend supports case-insensitive title search.

Example API request:

```http
GET /api/recipes?q=Beef
```

### Category Filter

Users can filter recipes by category.

Example:

```http
GET /api/recipes?category=Main
```

Filtering can also be combined with search.

```http
GET /api/recipes?q=Beef&category=Main
```

### Sorting

Recipes can currently be sorted by title.

Supported values:

```text
title_asc
title_desc
```

Examples:

```http
GET /api/recipes?sort=title_asc
```

```http
GET /api/recipes?sort=title_desc
```

Search, category filtering, and sorting can be combined.

```http
GET /api/recipes?q=Beef&category=Main&sort=title_asc
```

### Favorite Recipes

Each recipe contains an `is_favorite` state.

Users can toggle the favorite state from the recipe list.

Example:

```http
PUT /api/recipes/recipe-001/favorite
```

The favorite button uses a separate tap event so that favoriting a recipe does not open the recipe details page.

### Recipe Details

Users can open a recipe from the Recipe Library and view its detailed information.

The application also handles:

- Loading state
- Recipe not found state
- Backend request errors

---

## Product Vision

Cooking from online recipes can be inconvenient when important information is spread across videos, descriptions, comments, or multiple timestamps.

Recipe Assistant aims to convert recipes into a structured cooking experience.

The long-term product direction includes:

- Importing recipes from videos or text
- Extracting ingredients and cooking steps
- Organizing cooking steps into a clear sequence
- Summarizing seasoning and marinade information
- Providing spoon-based measurement support
- Estimating ingredient weight from photos
- Estimating calories
- Supporting personal recipe preferences
- Improving the step-by-step cooking experience

---

## User Story Structure

The project is organized into several Epics.

### Epic 1: Recipe Library

The Recipe Library provides the basic recipe management and discovery experience.

Current User Stories:

```text
US-001 Browse recipes
US-002 Search recipes
US-003 View recipe details
US-004 Favorite recipes
US-005 Filter recipes by category
US-006 Sort recipes
```

### Epic 2: Recipe Import

Planned functionality for importing and structuring recipes from external sources.

### Epic 3: Cooking Experience

Planned functionality for step-by-step cooking guidance.

### Epic 4: Personalization

Planned functionality for user-specific settings and recipe preferences.

---

## Tech Stack

### Backend

- Python
- FastAPI
- Pydantic
- Uvicorn
- pytest
- HTTPX

### Frontend

- WeChat Mini Program
- TypeScript
- WXML
- WXSS
- WeChat Mini Program APIs

### Documentation

- Markdown
- PlantUML
- Graphviz

### Project Management

- Git
- GitHub
- GitHub Issues
- GitHub Projects
- GitHub Milestones

---

## Architecture

The current application uses a simple client-server architecture.

```text
┌──────────────────────────────┐
│      WeChat Mini Program     │
│                              │
│  Recipe Library              │
│  Recipe Details              │
│  Search / Filter / Sort      │
│  Favorite Toggle             │
└───────────────┬──────────────┘
                │
                │ HTTP
                ▼
┌──────────────────────────────┐
│        FastAPI Backend       │
│                              │
│  GET /api/recipes            │
│  GET /api/recipes/{id}       │
│  PUT /api/recipes/{id}/      │
│      favorite                │
└───────────────┬──────────────┘
                │
                ▼
┌──────────────────────────────┐
│       Recipe Data Layer      │
└──────────────────────────────┘
```

The current implementation uses local recipe data while the application structure and API behavior are developed.

A persistent database can be introduced in a later development stage.

---

## API

### Get Recipes

```http
GET /api/recipes
```

Optional query parameters:

| Parameter | Description |
|---|---|
| `q` | Search recipe titles |
| `category` | Filter recipes by category |
| `sort` | Sort recipe results |

Example:

```http
GET /api/recipes?q=Beef&category=Main&sort=title_asc
```

Supported sort values:

```text
title_asc
title_desc
```

An unsupported sort value returns:

```text
400 Bad Request
```

Empty or whitespace-only sort values are treated as no sorting.

---

### Get Recipe Details

```http
GET /api/recipes/{recipe_id}
```

Example:

```http
GET /api/recipes/recipe-001
```

If the recipe does not exist, the API returns a not-found response.

---

### Toggle Favorite

```http
PUT /api/recipes/{recipe_id}/favorite
```

Example:

```http
PUT /api/recipes/recipe-001/favorite
```

The API updates the recipe's favorite state and returns the updated recipe information.

---

## Recipe Data Model

A recipe summary currently contains fields such as:

```json
{
  "id": "recipe-001",
  "title": "Beef Noodle Soup",
  "category": "Main",
  "servings": 2,
  "is_favorite": false
}
```

The recipe detail model contains additional information required by the recipe details page.

---

## Search, Filter, and Sort Behavior

The backend handles recipe queries instead of performing the main filtering logic in the frontend.

The operations can be combined.

Conceptually:

```text
All Recipes
    │
    ▼
Search by title
    │
    ▼
Filter by category
    │
    ▼
Sort results
    │
    ▼
Return recipes
```

For example:

```http
GET /api/recipes?q=Beef&category=Main&sort=title_desc
```

returns recipes that:

1. Match the search term
2. Match the selected category
3. Are sorted by title in descending order

---

## Testing

Backend API behavior is covered with automated tests using `pytest`.

The test suite currently covers areas such as:

- Recipe list retrieval
- Recipe summary fields
- Recipe search
- Empty search values
- Category filtering
- Sorting
- Search and category combinations
- Search and sorting combinations
- Search, category, and sorting combinations
- Unsupported sort values
- Empty sort values
- Whitespace sort values
- Favorite state
- Favorite toggle

Run the backend tests with:

```bash
python -m pytest
```

For verbose output:

```bash
python -m pytest -v
```

Frontend functionality is currently validated with manual acceptance testing in the WeChat Developer Tools.

---

## Local Development

### Backend

Create and activate a Python virtual environment.

Windows Git Bash:

```bash
python -m venv .venv
source .venv/Scripts/activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Start the FastAPI backend:

```bash
cd backend
python -m uvicorn app.backend.main:app --reload
```

The backend is available by default at:

```text
http://127.0.0.1:8000
```

FastAPI API documentation:

```text
http://127.0.0.1:8000/docs
```

---

### Frontend

Open the Mini Program project with WeChat Developer Tools.

Make sure the FastAPI backend is running before testing API-dependent functionality.

The frontend communicates with the local backend through `wx.request`.

---

## Development Workflow

Development follows a User Story and GitHub Issue based workflow.

A typical feature flow is:

```text
User Story
    ↓
GitHub Issue
    ↓
Feature / Batch Branch
    ↓
Implementation
    ↓
Automated Tests
    ↓
Manual Acceptance Test
    ↓
Pull Request
    ↓
Merge
    ↓
Close Issue
```

For related features, development may use batch issues so that backend or frontend changes can be implemented and tested together.

For example:

```text
US-004 Favorite recipes
US-005 Filter recipes by category
US-006 Sort recipes

        │
        ├── Backend Batch
        │
        └── Frontend Batch
```

After both batches are completed, each User Story is validated as a complete frontend-to-backend flow.

---

## Documentation

Project documentation includes:

- Product Vision
- User Stories
- Use Case Diagram
- Use Case Specifications
- Architecture decisions
- Open questions
- API behavior
- GitHub Issues and acceptance criteria

PlantUML is used for UML diagrams.

Example workflow:

```text
PlantUML
   │
   ├── Java
   └── Graphviz
        │
        ▼
       SVG
```

---

## Roadmap

The current focus is completing the Recipe Library.

### Recipe Library

- [x] Browse recipes
- [x] Search recipes
- [x] View recipe details
- [x] Favorite recipes
- [x] Filter recipes by category
- [x] Sort recipes

### Recipe Import

- [ ] Import recipe from supported sources
- [ ] Extract recipe information
- [ ] Review imported recipe
- [ ] Save imported recipe

### Cooking Experience

- [ ] Structured cooking steps
- [ ] Step-by-step cooking mode
- [ ] Ingredient and seasoning summary
- [ ] Cooking progress tracking

### Personalization

- [ ] Spoon profiles
- [ ] Personal measurement preferences
- [ ] Recipe preferences
- [ ] Personalized cooking assistance

---

## Current Development Focus


---

## License

License information will be added before the project is published as an open-source project.