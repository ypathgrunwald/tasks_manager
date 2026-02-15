# Task Manager Project – Specification

## Purpose
A simple Python application to manage tasks, focusing on TDD and unit testing practice.

## Core Features
1. Task Class - Create and store tasks (title, description, priority).
2. Task Class - Mark tasks as completed /pending/ unassigned
3. Task Class - Change task priority between low/high/medium/unassigned
4. Task Manager Class - List and filter tasks by priority or completion.
5. Task Manager Class - Save tasks to a file.

## Classes
- **Task**
  - Attributes: `title`, `description`, `priority`, `status`
  - Methods: `mark_status_complete()`, `is_done()`, `mark_status_pending()`, `mark_status_unassigned()`
- **TaskManager**
  - Attributes: `tasks` (list of Task objects)
  - Methods: `add_task(Task)`, `remove_task(Task)`, `get_pending()`, `get_completed()`, `get_priority(priority)`

## CONSTANTS
- **Status constants**
 - UNASSIGNED = "Unassigned" - Tasks are created in Unassigned Status
 - PENDING = "Pending" - Tasks moved to Pending Status once a task is in work
 - COMPLETE = "Complete" - Tasks move to complete status once they are finished

- **Priority constants**
 - UNASSIGNED = "Unassigned"
 - LOW = "Low"
 - MEDIUM = "Medium"
 - HIGH = "High"

## Testing Goals
- Use TDD for all new functionality.
- Use mocks to simulate:
  - File operations
  - Notifications or external services
- Apply autospec and patch where appropriate.

## Test Scenarios
- **Task**
 - Task Creation
 - Task Mark As Completed
 - Task Is Done
 - Task Priority Low
 - Task Priority High
 - Task Priority Medium
 - Task Priority Incorrect
 - Status Pending
 - Status Incorrect
 - Status Completed
- **TaskManager**
 - Task List Creation
 - Add Task
 - Remove Task
 - Task List Remove From 0 Tasks List
 - Get Pending Tasks
 - Get Completed Tasks
 - Get High Priority
 - Get Medium Priority
 - Get Low Priority

## Notes
- Start with Task → then TaskManager → then optional file saving.
- Write tests before implementing each feature.