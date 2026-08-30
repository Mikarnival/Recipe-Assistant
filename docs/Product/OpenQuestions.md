# Open Questions

## Cooking Step Media

### Idea

A cooking step could optionally include visual guidance, such as:

- an image
- a GIF
- a short video clip
- a segment from the original recipe video

The goal is to help users understand how a specific cooking action should be performed without repeatedly searching through a full cooking video.

### Possible Future Behavior

A cooking step may contain:

- instruction text
- optional media type
- optional media URL
- optional start timestamp
- optional end timestamp

Example:

```json
{
  "instruction": "Fold the dumpling wrapper and seal the edge.",
  "media": {
    "type": "video",
    "url": "...",
    "start_seconds": 83,
    "end_seconds": 91
  }
}

# Open Questions

## Video Recipe Import and Structured Video Analysis

### Background

Many recipe sources are videos rather than structured text.

Watching a full cooking video while cooking is inconvenient because users often need to repeatedly:

- pause the video
- rewind
- search for a specific step
- remember ingredient quantities
- find where a certain action appears

A future Recipe Assistant feature could analyze a cooking video and convert it into a structured recipe.


### Core Idea

The application could accept a cooking video or video URL and extract structured information such as:

- recipe title
- servings
- ingredients
- ingredient quantities
- preparation tasks
- cooking steps
- cooking tips
- timestamps for individual steps
- uncertainty when information cannot be determined reliably

The result should first be treated as a draft rather than being saved automatically.


### Possible Workflow

```text
Video
  ↓
Audio / transcript extraction
  ↓
Visual frame analysis
  ↓
On-screen text extraction
  ↓
Multimodal AI analysis
  ↓
Structured Recipe Draft
  ↓
User review and correction
  ↓
Save to Recipe Library
```


### Possible Structured Output

Example:

```json
{
  "title": "Braised Beef",
  "servings": 4,
  "ingredients": [
    {
      "name": "Beef shank",
      "quantity": 800,
      "unit": "g"
    }
  ],
  "preparation_tasks": [
    "Cut the beef into large pieces."
  ],
  "steps": [
    {
      "instruction": "Blanch the beef and remove the foam.",
      "start_seconds": 42,
      "end_seconds": 68
    }
  ]
}
```


### Transcript Extraction

The first stage could extract speech from the video.

Possible sources include:

- existing video subtitles
- automatically generated subtitles
- speech-to-text transcription
- tools such as Whisper

If subtitles are available, they may be used directly.

If subtitles are unavailable or unreliable, speech-to-text could generate the transcript.


### Visual Analysis

Speech alone may not contain all recipe information.

Important information may also appear visually, for example:

- ingredient labels
- ingredient quantities displayed on screen
- cooking temperatures
- timers
- text overlays
- cooking actions
- changes in food appearance

A future importer may therefore combine transcript analysis with selected video frames.


### Frame Sampling

Instead of analyzing every video frame, the system could sample important frames.

Possible approaches include:

- fixed interval sampling
- scene change detection
- sampling around transcript timestamps
- sampling when on-screen text changes
- sampling around detected cooking steps

This could reduce processing cost while retaining useful visual information.


### Step Timestamp Detection

One important future capability could be assigning timestamps to recipe steps.

Example:

```text
Step 1 — Prepare the beef
00:32–00:45

Step 2 — Mix the sauce
01:18–01:31

Step 3 — Stir-fry the beef
03:02–03:17
```

This could later support step-specific media or direct navigation to the relevant part of the source video.


### Draft Review

Automatically extracted recipes should not be saved directly without review.

Cooking videos often contain vague instructions such as:

- "add a little salt"
- "cook for a while"
- "add an appropriate amount"
- "cook until it looks like this"

AI systems may incorrectly invent missing quantities or timings.

A safer workflow would be:

```text
AI extraction
     ↓
Draft Recipe
     ↓
User review
     ↓
Correction
     ↓
Save
```

Unknown or uncertain values should remain explicit rather than being silently guessed.


### Uncertainty Handling

The importer should ideally distinguish between:

- directly observed information
- inferred information
- uncertain information
- missing information

Example:

```json
{
  "name": "Salt",
  "quantity": null,
  "unit": null,
  "confidence": "low"
}
```

The system should prefer missing values over invented precision.


### Possible Import Sources

Future versions may support:

- uploaded video files
- YouTube videos
- other supported public video URLs
- locally recorded cooking videos
- previously downloaded videos

Support for individual platforms should depend on technical feasibility, platform terms, and copyright considerations.


### Copyright and Source Media

Importing information from a video and reusing the original video content are separate concerns.

The application may be able to extract structured recipe information without redistributing the original video.

However, storing or displaying clips from third-party videos may introduce copyright or licensing issues.

Possible strategies include:

- store only structured recipe data
- store source URL and timestamps without copying media
- allow users to access the original source
- use self-recorded or AI-generated guidance media instead of copied video clips
- only store source video clips when the user owns the content or appropriate rights exist


### Relationship to Cooking Step Media

Video Import and Cooking Guidance Media should remain separate concepts.

Video Import answers:

> What recipe information can be extracted from this source video?

Cooking Guidance Media answers:

> How can the user understand this cooking action while cooking?

A recipe imported from a video may contain timestamps pointing to the source video.

However, generic cooking actions could instead use reusable self-recorded or AI-generated guidance media.


### Possible Technical Pipeline

A future implementation could use a pipeline such as:

```text
Video URL / File
        ↓
Media Loader
        ↓
Transcript Extraction
        ↓
Frame Sampling
        ↓
Multimodal Analysis
        ↓
Structured Output Validation
        ↓
Recipe Draft
```

Possible technologies may include:

- ffmpeg
- yt-dlp
- Whisper or another speech-to-text model
- multimodal LLMs
- Pydantic structured output
- background processing for long-running jobs


### Generic Video Analysis Potential

The underlying video analysis capability may have uses beyond recipes.

The same general pipeline could potentially convert videos into structured information for:

- tutorials
- fitness exercises
- software demonstrations
- DIY instructions
- repair videos
- educational content
- lectures
- product demonstrations

For this reason, the video understanding component may eventually become an independent project or reusable service rather than remaining tightly coupled to Recipe Assistant.


### Possible Architecture

One possible future separation could be:

```text
Video Understanding Tool
          ↓
Structured Output
          ↓
Recipe Schema
          ↓
Recipe Assistant
```

The generic pipeline could remain domain-independent while different output schemas provide domain-specific extraction.

Examples:

```text
RecipeSchema
TutorialSchema
CourseSchema
ExerciseSchema
```


### Possible Development Strategy

#### Phase 1 — Proof of Concept

Input:

- one local cooking video

Output:

- transcript
- detected steps
- start/end timestamps
- JSON


#### Phase 2 — Recipe Extraction

Add:

- ingredients
- quantities
- preparation tasks
- structured Recipe output


#### Phase 3 — Visual Analysis

Add:

- sampled video frames
- on-screen text
- visually detected actions


#### Phase 4 — Recipe Assistant Integration

Add:

```text
Import Recipe
→ Analyze
→ Review Draft
→ Save
```


#### Phase 5 — Generic Video Understanding

Evaluate whether the pipeline should become an independent project or service.


### Open Questions

- Should the first implementation accept local files or video URLs?
- Which video platforms should be supported?
- Should transcription run locally or through an external AI service?
- How should long videos be processed efficiently?
- How should video frames be selected?
- How should step timestamps be detected?
- Should the system store source video timestamps?
- Should the original video ever be copied or stored?
- How should uncertainty be represented?
- Should imported recipes always require manual review?
- How should transcript and visual evidence be combined?
- Should this feature remain part of Recipe Assistant or become an independent video understanding project?
- Could the generic video analysis pipeline support other domains in the future?


---

## Reusable Cooking Guidance Media

### Background

Cooking steps are often easier to understand when users can see a visual demonstration instead of relying only on text.

For example, instructions such as:

- stir-fry
- mix evenly
- flip
- cut into strips
- dice
- blanch
- coat with flour
- beat eggs

describe actions that can be demonstrated visually.

However, using clips extracted from third-party cooking videos may introduce copyright and licensing concerns.

Instead of relying on media from individual recipe videos, the application could provide its own reusable cooking guidance library.


### Idea

Create a library of short, reusable cooking guidance media for common cooking actions.

The media could be:

- self-recorded videos
- AI-generated videos
- AI-generated images
- GIFs
- properly licensed media

These guidance assets would not represent a specific recipe.

They would demonstrate generic cooking techniques that can be reused across many recipes.


### Example

A recipe step:

```json
{
  "instruction": "Stir-fry the beef over high heat.",
  "guidance_action": "stir_fry"
}
```

The application could map:

```text
stir_fry
```

to a reusable media asset:

```text
guidance/stir_fry.mp4
```

The same media could then be used by many different recipes.


### Possible Guidance Actions

Examples of reusable actions may include:

- stir-fry
- stir
- mix evenly
- flip food in a pan
- turn food over
- cut into strips
- dice
- slice
- mince
- blanch
- drain
- coat with flour
- beat eggs
- knead dough
- fold
- toss ingredients
- pour slowly
- whisk
- roll dough
- wrap or fold dumplings


### Action Guidance vs State Guidance

Not every cooking instruction is suitable for generic video guidance.

It may be useful to distinguish between two types of guidance.


#### Action Guidance

Action guidance explains:

> How should I perform this movement?

Examples:

- stir-fry
- flip
- mix
- slice
- knead
- fold

These actions are good candidates for reusable images, GIFs, or short videos.


#### State Guidance

State guidance explains:

> What should the food look or feel like before I continue?

Examples:

- reduce sauce until thick
- fry sugar until amber
- knead dough until gluten develops
- cook steak until medium rare
- whip cream to stiff peaks
- cook onions until translucent

These states may be difficult to represent reliably with generic AI-generated video.

For these steps, a combination of:

- reference image
- textual description
- timing
- temperature
- sensory cues

may be more useful.


### Possible Step Presentation

A cooking step could eventually contain both action and state guidance.

Example:

```text
Step 4

Stir-fry the beef for about 30 seconds.

[Reusable stir-fry demonstration]

Action guidance:
Quickly move and turn the ingredients in the pan.

State guidance:
Stop when the outside of the beef has just changed color.
The inside does not need to be fully cooked yet.
```


### Possible Data Model

A simple first version could be:

```python
class CookingStep(BaseModel):
    instruction: str
    guidance_action: str | None = None
```

For example:

```json
{
  "instruction": "Mix the sauce until evenly combined.",
  "guidance_action": "mix_evenly"
}
```


A more flexible future model could be:

```python
class GuidanceMedia(BaseModel):
    action: str
    type: str
    url: str
    source: str
```

Possible `source` values:

```text
self_recorded
ai_generated
licensed
```

A cooking step could then reference a guidance asset instead of directly storing media information.


### Media Priority

A possible future priority could be:

1. Self-created or specifically produced guidance media
2. AI-generated reusable guidance media
3. Licensed media
4. Text-only guidance

If a recipe was imported from an original video and the application has permission to use that content, original footage could also be considered separately.


### Why Reusable Guidance Is Useful

Reusable guidance has several advantages.

One media asset can support many different recipes.

For example:

```text
stir_fry.mp4
```

could be reused for:

```text
Stir-fry beef.
Stir-fry vegetables.
Stir-fry noodles.
Stir-fry chicken.
```

This reduces:

- media generation costs
- storage requirements
- duplicated content
- maintenance work

It also creates a more consistent cooking experience.


### AI-generated Guidance

AI-generated media could be especially useful for simple and generic actions.

Suitable examples may include:

- stirring
- mixing
- flipping
- slicing
- whisking
- kneading

AI-generated media should probably not be used as the primary reference for steps where precise cooking state is important.

Before public or commercial release, the terms of the selected AI generation service and any applicable requirements for labeling AI-generated media should be reviewed.


### Copyright Considerations

Using clips from third-party cooking videos may require permission or appropriate licensing.

To reduce copyright complexity, reusable guidance media should preferably be:

- created by the application owner
- recorded specifically for the project
- generated using AI services with suitable usage rights
- obtained from appropriately licensed sources

This would keep the guidance library independent from individual external recipe videos.


### Possible Product Strategy

A phased implementation could be:

#### Phase 1

Support optional static guidance images for cooking steps.


#### Phase 2

Create a small reusable action library for the most common cooking techniques.


#### Phase 3

Support short video or GIF demonstrations.


#### Phase 4

Allow AI generation of missing guidance media.


#### Phase 5

Combine:

- action guidance
- state guidance
- recipe-specific instructions
- optional original media when appropriate


### Open Questions

- Which cooking actions should be included in the first guidance library?
- Should the first version use images, GIFs, or short videos?
- Should guidance media be generated automatically or curated manually?
- Should users be able to replace or disable guidance media?
- How should guidance assets be stored and cached?
- Should multiple guidance variants exist for the same action?
- Should guidance differ for different tools, such as wok vs frying pan?
- How should AI-generated guidance be labeled?
- Should state guidance use reference images rather than video?
- How should Recipe Assistant distinguish between generic action guidance and recipe-specific media?
- Should the guidance library eventually become a reusable module independent of Recipe Assistant?