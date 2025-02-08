# Learning Python App Design

## Database Backend Redesign

### Current Issues
1. Data duplication between database and frontend files
2. Disconnected exercise management
3. Complex progress tracking due to split content
4. No single source of truth for exercise content
5. Difficulty in inserting new exercises while maintaining progress

### Proposed Solution

#### 1. Enhanced Database Schema

```sql
-- Lesson table remains unchanged
CREATE TABLE lesson (
    id INTEGER PRIMARY KEY,
    slug TEXT NOT NULL UNIQUE,
    title TEXT NOT NULL,
    description TEXT,
    order INTEGER NOT NULL
);

-- Enhanced exercise table
CREATE TABLE exercise (
    id INTEGER PRIMARY KEY,
    lesson_id INTEGER NOT NULL,
    slug TEXT NOT NULL UNIQUE,
    title TEXT NOT NULL,
    description TEXT,
    sequence_key REAL NOT NULL,  -- Allows inserting exercises between existing ones (e.g., 1.5)
    initial_code TEXT,
    solution TEXT,
    task_description TEXT,
    hint_text TEXT,
    visual_content JSON,  -- Stores structured visual content
    validation_params JSON, -- Stores validation configuration
    prerequisites JSON,   -- Array of exercise slugs that should be completed first
    FOREIGN KEY (lesson_id) REFERENCES lesson(id)
);

-- Enhanced progress table
CREATE TABLE progress (
    user_id INTEGER NOT NULL,
    exercise_id INTEGER NOT NULL,
    completed BOOLEAN NOT NULL DEFAULT FALSE,
    completed_at INTEGER,
    attempts INTEGER NOT NULL DEFAULT 0,
    -- Track which version of the exercise was completed
    exercise_version TEXT,  -- Hash or version identifier of exercise content
    PRIMARY KEY (user_id, exercise_id),
    FOREIGN KEY (user_id) REFERENCES user(id),
    FOREIGN KEY (exercise_id) REFERENCES exercise(id)
);

-- New table for exercise versions
CREATE TABLE exercise_version (
    exercise_id INTEGER NOT NULL,
    version TEXT NOT NULL,  -- Hash of exercise content
    content JSON NOT NULL,  -- Full exercise content at this version
    created_at INTEGER NOT NULL,
    PRIMARY KEY (exercise_id, version),
    FOREIGN KEY (exercise_id) REFERENCES exercise(id)
);
```

#### 2. Content Management System

Exercise content in JSON format:

```json
{
  "lesson": "variables",
  "exercises": [
    {
      "slug": "variables-1",
      "title": "The Toy Organizer",
      "description": "Help organize the toy collection by creating variables for different toy counts!",
      "sequenceKey": 1.0,  // Can insert new exercise at 1.5
      "prerequisites": [],  // No prerequisites for first exercise
      "taskDescription": "Create variables for blocks, dolls, and cars with the counts shown in the boxes.",
      "initialCode": "# Create variables for toy counts\n# Example: blocks = 12",
      "solution": "blocks = 12\ndolls = 5\ncars = 8",
      "hintText": "Remember to use = to assign values to variables!",
      "visualContent": {
        "type": "grid",
        "items": [
          {
            "type": "box",
            "theme": "yellow",
            "title": "Blocks Box",
            "value": 12,
            "label": "blocks"
          },
          {
            "type": "box",
            "theme": "pink",
            "title": "Dolls Box",
            "value": 5,
            "label": "dolls"
          },
          {
            "type": "box",
            "theme": "blue",
            "title": "Cars Box",
            "value": 8,
            "label": "cars"
          }
        ]
      },
      "validationParams": {
        "concept": "variables",
        "expectedOutcome": "blocks = 12\ndolls = 5\ncars = 8"
      }
    }
  ]
}
```

#### 3. Exercise Management Workflow

1. Content Creation:
   - Authors create/edit exercises in JSON format
   - Each exercise has a sequence_key for ordering
   - Prerequisites define required exercises
   - Content changes create new versions

2. Exercise Insertion Process:
   - New exercise can be inserted with sequence_key between existing exercises
   - Example: Insert between 1.0 and 2.0 using 1.5
   - Progress tracking remains intact due to:
     * Unique exercise IDs
     * Version tracking
     * Prerequisites system

3. Progress Tracking:
   - Track completion by exercise ID
   - Store version completed
   - Prerequisites determine available exercises
   - Sequence keys determine display order

4. User Experience:
   - Show exercise completion status
   - Indicate new exercises added
   - Prerequisites guide learning path
   - Maintain progress while allowing curriculum updates

#### 4. Implementation Steps

1. Update Database Schema:
   - Add sequence_key field
   - Create exercise_version table
   - Add prerequisites support
   - Add version tracking to progress

2. Create Content Structure:
   - Define JSON schema for exercises
   - Convert existing exercises to JSON format
   - Add sequence keys and prerequisites
   - Implement versioning

3. Build Management Tools:
   - CLI tool for content validation
   - Admin interface for:
     * Exercise CRUD operations
     * Sequence management
     * Prerequisites management
     * Version control
   - Build scripts for route generation

4. Update Frontend:
   - Create dynamic route handling
   - Update progress tracking
   - Implement prerequisites checking
   - Show exercise versions/changes

5. Migrate Existing Content:
   - Convert current exercises to new format
   - Assign initial sequence keys
   - Set up version tracking
   - Define prerequisites

### Benefits

1. Flexible Exercise Management:
   - Insert exercises anywhere in sequence
   - Maintain user progress
   - Track content versions
   - Guide learning path with prerequisites

2. Robust Progress Tracking:
   - Track specific versions completed
   - Prerequisites ensure proper skill building
   - Progress preserved during curriculum updates

3. Enhanced User Experience:
   - Clear learning path
   - Progress preservation
   - New content indication
   - Prerequisite guidance

4. Improved Maintainability:
   - Structured content format
   - Version control
   - Automated validation
   - Easy content updates

### Next Steps

1. Create JSON schema with sequence keys
2. Update database schema
3. Implement version tracking
4. Build prerequisite system
5. Create admin interface
6. Convert existing exercises