# Source: https://godspeedapp.com/guides/api

## URL: https://godspeedapp.com/guides/api

Title: Godspeed

URL Source: https://godspeedapp.com/guides/api

Markdown Content:
Godspeed offers a few API endpoints to list, create, and update tasks and lists.

### Rate limits

All API endpoints are guarded by rate limits. If you exceed the rate limit you'll get a 429 response.

When listing tasks or lists we ask that you not exceed 10 requests per minute or 200 per hour. When creating or updating tasks we ask that you not exceed 60 requests per minute or 1,000 per hour.

If you have a use case that requires higher rate limits, please [reach out to us](https://godspeedapp.com/contact) and we'd be happy to discuss it.

### Get an access token

Use your email and password to sign in and get an access token:

POST https://api.godspeedapp.com/sessions/sign\_in Content-Type: application/json { "email": "email@example.com", "password": "your password" }

The response will contain a `token` field with the access token:

{ "token": "abc123", "success": "true", "user": { ... } }

Use this access token to authorize all other requests to the API by including an `Authorization` header:

Authorization: Bearer abc123

You can also get your access token from the [Command Palette](https://godspeedapp.com/guides/command-palette) in the desktop app by running the "Copy API access token" command. If you've signed in with Setapp, this is the only way to get an access token.

### Create task

You can log tasks to Godspeed using a simple API endpoint. The endpoint allows you to specify the list, title, notes, due date, start date, and labels for a task.

POST https://api.godspeedapp.com/tasks Authorization: Bearer abc123 Content-Type: application/json { "title": "buy milk", "list_id": "def-456", "location": "start", "notes": "vitamin D", "due_at": "2024-03-30T01:21:22Z", "starts_at": "2024-03-15T01:00:00Z", "duration_minutes": 30, "label_names": \["Dairy", "Urgent"\] }

Description of each field:

`title` (required) - the title of the task.

`list_id` (optional) - the ID of the list to log to. You can find a list's ID by selecting the list and running the "Copy list ID" command in the Command Palette. If this parameter isn't specified then the task will be logged to your Inbox.

`location` (optional) - whether to log the task at the start or end of the list. This must be either `"start"` or `"end"`. If not specified, the default is `"end"`.

`notes` (optional) - the notes for the task.

`due_at` (optional) - the due date and time for the task formatted as an ISO8601 timestamp. Do not specify both this and `timeless_due_at`. If neither is specified the task will not have a due date.

`timeless_due_at` (optional) - the due date for the task, without a time, formatted as YYYY-MM-DD. Do not specify both this and `due_at`. If neither is specified the task will not have a due date.

`starts_at` (optional) - the start date and time for the task formatted as an ISO8601 timestamp. Do not specify both this and `timeless_starts_at`. If neither is specified the task will not have a start date.

`timeless_starts_at` (optional) - the start date for the task, without a time, formatted as YYYY-MM-DD. Do not specify both this and `starts_at`. If neither is specified the task will not have a start date.

`duration_minutes` (optional) - the duration of the task as an integer number of minutes. If not specified the task will not have a duration.

`label_names` (optional) - an array of label names to add to the task. The names must exactly match existing labels, including spaces and casing.

### Get tasks

GET https://api.godspeedapp.com/tasks Authorization: Bearer abc123

This endpoint returns up to 250 tasks, ordered by the `updated_at` field descending.

There are several optional query parameters you can specify to filter the tasks that are returned:

`status` - either `incomplete` or `complete`.

`list_id` - You can find a list's ID by selecting the list and running the "Copy list ID" command in the Command Palette.

`updated_before` - An ISO8601 timestamp to be compared against `updated_at`.

`updated_after` - An ISO8601 timestamp to be compared against `updated_at`.

If you need more than the 250 tasks returned, you can use the `updated_before` parameter to paginate the response. But be mindful of the rate limit, which is about 10 requests per minute.

Each returned task will have a `list_id` field and a `label_ids` field. All corresponding lists and labels are returned as separate top-level keys in the response, as `lists` and `labels` respectively.

### Get task

GET https://api.godspeedapp.com/tasks/:task\_id Authorization: Bearer abc123

This endpoint lets you fetch a single task with a given ID. Be sure to replace `:task_id` in the URL with your task's ID.

### Update task

PATCH https://api.godspeedapp.com/tasks/:task\_id Authorization: Bearer abc123 Content-Type: application/json { "title": "buy whole milk", "notes": "dairy section", "due_at": "2024-03-30T01:21:22Z", "starts_at": "2024-03-15T01:00:00Z", "duration_minutes": 20, "is_complete": false, "is_cleared": false }

This endpoint lets you update a task with a given ID. Be sure to replace `:task_id` in the URL with your task's ID.

All body parameters are optional and will be updated only if specified:

`title` - the title of the task.

`notes` - the notes for the task.

`due_at` - the due date and time for the task formatted as an ISO8601 timestamp. Do not specify both this and `timeless_due_at`

`timeless_due_at` - the due date for the task, without a time, formatted as YYYY-MM-DD. Do not specify both this and `due_at`

`snoozed_until` - the snooze date and time for the task formatted as an ISO8601 timestamp. Do not specify both this and `timeless_snoozed_until`

`timeless_snoozed_until` - the snooze date for the task, without a time, formatted as YYYY-MM-DD. Do not specify both this and `snoozed_until`

`starts_at` - the start date and time for the task formatted as an ISO8601 timestamp. Do not specify both this and `timeless_starts_at`

`timeless_starts_at` - the start date for the task, without a time, formatted as YYYY-MM-DD. Do not specify both this and `starts_at`

`duration_minutes` - the duration of the task as an integer number of minutes.

`is_complete` - a boolean indicating whether the task should be marked complete or incomplete.

`is_cleared` - a boolean indicating whether the task should be cleared or not. Note that a task cannot be cleared while incomplete, and the API will report an error if you try to update a task to this state.

### Get lists

GET https://api.godspeedapp.com/lists Authorization: Bearer abc123

This endpoint returns all lists accessible by your user account, including shared lists.

### Duplicate list

POST https://api.godspeedapp.com/lists/:list\_id/duplicate Authorization: Bearer abc123 Content-Type: application/json { "name": "New list name", }

This endpoint duplicates a list and all it's tasks.

The `name` parameter is optional.

---

# Crawl Statistics

- **Source:** https://godspeedapp.com/guides/api
- **Depth:** 1
- **Pages processed:** 1
- **Crawl method:** api
- **Duration:** 4.64 seconds
- **Crawl completed:** 1/25/2025, 8:02:02 PM
