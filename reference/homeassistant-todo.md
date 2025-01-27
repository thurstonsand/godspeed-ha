# Source: https://www.home-assistant.io/integrations/todo/

## URL: https://www.home-assistant.io/integrations/todo/

Title: To-do list

URL Source: https://www.home-assistant.io/integrations/todo/

Markdown Content:
The **To-do list** integrationIntegrations connect and integrate Home Assistant with your devices, services, and more. [\[Learn more\]](https://www.home-assistant.io/getting-started/concepts-terminology/#integrations) provides to-do list entitiesAn entity represents a sensor, actor, or function in Home Assistant. Entities are used to monitor physical properties or to control other entities. An entity is usually part of a device or a service. [\[Learn more\]](https://www.home-assistant.io/docs/configuration/entities_domains/), allowing other integrations to integrate to-do lists into Home Assistant. To-do lists are shown on the **To-do lists** dashboard for tracking items and whether or not they have been completed.

Note

**Building block integration**

This to-do list is a building block integration that cannot be added to your Home Assistant directly but is used and provided by other integrations.

A building block integration differs from the typical integration that connects to a device or service. Instead, other integrations that do integrate a device or service into Home Assistant use this to-do list building block to provide entities, services, and other functionality that you can use in your automations or dashboards.

If one of your integrations features this building block, this page documents the functionality the to-do list building block offers.

For example, [Local to-do](https://www.home-assistant.io/integrations/local_todo/) is a fully local integration to create to-do lists and tasks within your Home Assistant instance, [Shopping list](https://www.home-assistant.io/integrations/shopping_list) specifically for shopping that can be added to with Assist, or other integrations work with online services providing to-do list data.

## Viewing and managing to-do lists[](https://www.home-assistant.io/integrations/todo/#viewing-and-managing-to-do-lists)

Each to-do list is represented as its own entity in Home Assistant and can be viewed and managed on a to-do list dashboard. You can find the to-do list dashboard in the main sidebar of your Home Assistant instance.

## The state of a to-do list entity[](https://www.home-assistant.io/integrations/todo/#the-state-of-a-to-do-list-entity)

The state of a to-do list entity is a number, which represents the number of incomplete items in the list.

![Image 8: Screenshot showing the state of a to-do list entity in the developer tools](https://www.home-assistant.io/images/integrations/todo/state_todo.png) Screenshot showing the state of a to-do list entity in the developer tools.

In addition, the entity can have the following states:

- **Unavailable**: The entity is currently unavailable.
- **Unknown**: The state is not yet known.

## Blueprint to add an item to a dedicated list[](https://www.home-assistant.io/integrations/todo/#blueprint-to-add-an-item-to-a-dedicated-list)

This blueprint allows you to create a script to add an item to a pre-configured to-do list.

[![Image 9](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import?blueprint_url=https%3A%2F%2Fcommunity.home-assistant.io%2Ft%2Fadd-to-do-item%2F699193)

## Actions[](https://www.home-assistant.io/integrations/todo/#actions)

Some to-do list integrations allow Home Assistant to manage the to-do items in the list. The actions provided by some to-do list entities are described below or you can read more about [actions](https://www.home-assistant.io/docs/scripts/perform-actions/).

### Action todo.get_items[](https://www.home-assistant.io/integrations/todo/#action-todoget_items)

Get to-do items from a to-do list. A to-do list `target` is selected with a [target selector](https://www.home-assistant.io/docs/blueprint/selectors/#target-selector). The `data` payload supports the following fields:

| Data attribute | Optional | Description                               | Example                     |
| -------------- | -------- | ----------------------------------------- | --------------------------- |
| `status`       | yes      | Only return to-do items with this status. | `needs_action`, `completed` |

This is a full example that returns all to-do items that have not been completed:

```
action: todo.get_items
target:
  entity_id: todo.personal_tasks
data:
  status:
    - needs_action
```

### Action todo.add_item[](https://www.home-assistant.io/integrations/todo/#action-todoadd_item)

Add a new to-do item. A to-do list `target` is selected with a [Target Selector](https://www.home-assistant.io/docs/blueprint/selectors/#target-selector) and the `data` payload supports the following fields:

| Data attribute | Optional | Description                                                      | Example                                                      |
| -------------- | -------- | ---------------------------------------------------------------- | ------------------------------------------------------------ |
| `item`         | no       | the name of the to-do Item.                                      | Submit income tax return                                     |
| `due_date`     | yes      | The date the to-do item is expected to be completed.             | 2024-04-10                                                   |
| `due_datetime` | yes      | The date and time the to-do item is expected to be completed.    | 2024-04-10 23:00:00                                          |
| `description`  | yes      | A more complete description than the one provided by the summary | Collect all necessary documents and submit the final return. |

Only one of `due_date` or `due_datetime` may be specified.

This is a full example in YAML:

```
action: todo.add_item
target:
  entity_id: todo.personal_tasks
data:
  item: "Submit Income Tax Return"
  due_date: "2024-04-10"
  description: "Collect all necessary documents and submit the final return."
```

### Action todo.update_item[](https://www.home-assistant.io/integrations/todo/#action-todoupdate_item)

Update a to-do item. A to-do list `target` is selected with a [Target Selector](https://www.home-assistant.io/docs/blueprint/selectors/#target-selector) and the `data` payload supports the following fields:

| Data attribute | Optional | Description                                                       | Example                                                      |
| -------------- | -------- | ----------------------------------------------------------------- | ------------------------------------------------------------ |
| `item`         | no       | The name of the to-do Item to update.                             | Submit income tax return                                     |
| `rename`       | yes      | The new name of the to-do Item.                                   | Something else                                               |
| `status`       | yes      | The overall status of the To-do Item.                             | `needs_action` or `completed`                                |
| `due_date`     | yes      | The date the to-do item is expected to be completed.              | 2024-04-10                                                   |
| `due_datetime` | yes      | The date and time the to-do item is expected to be completed.     | 2024-04-10 23:00:00                                          |
| `description`  | yes      | A more complete description than the one provided by the summary. | Collect all necessary documents and submit the final return. |

At least one of `rename` or `status` is required. Only one of `due_date` or `due_datetime` may be specified. This is a full example that updates the status and the name of a to-do item.

```
action: todo.update_item
target:
  entity_id: todo.personal_tasks
data:
  item: "Submit income tax return"
  rename: "Something else"
  status: "completed"
```

### Action todo.remove_item[](https://www.home-assistant.io/integrations/todo/#action-todoremove_item)

Removing a to-do item. A to-do list `target` is selected with a [Target Selector](https://www.home-assistant.io/docs/blueprint/selectors/#target-selector), and the `data` payload supports the following fields:

| Data attribute | Optional | Description                 | Example                  |
| -------------- | -------- | --------------------------- | ------------------------ |
| `item`         | no       | The name of the to-do item. | Submit income tax return |

This is a full example that deletes a to-do Item with the specified name.

```
action: todo.remove_item
target:
  entity_id: todo.personal_tasks
data:
  item: "Submit income tax return"
```

### Action todo.remove_completed_items[](https://www.home-assistant.io/integrations/todo/#action-todoremove_completed_items)

Removes all completed to-do items. A to-do list `target` is selected with a [Target Selector](https://www.home-assistant.io/docs/blueprint/selectors/#target-selector).

This is a full example that deletes all completed to-do items.

```
action: todo.remove_completed_items
target:
  entity_id: todo.personal_tasks
```

#### **Help us improve our documentation**[](https://www.home-assistant.io/integrations/todo/#feedback_section)

Suggest an edit to this page, or provide/view feedback for this page.

[Edit](https://github.com/home-assistant/home-assistant.io/tree/current/source/_integrations/todo.markdown) [Provide feedback](https://github.com/home-assistant/home-assistant.io/issues/new?template=feedback.yml&url=https%3A%2F%2Fwww.home-assistant.io%2Fintegrations%2Ftodo%2F&version=2025.1.4&labels=current,integration%3A%20todo) [View pending feedback](https://github.com/home-assistant/home-assistant.io/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc+label%3A%22integration%3A+todo%22)

---

# Crawl Statistics

- **Source:** https://www.home-assistant.io/integrations/todo/
- **Depth:** 1
- **Pages processed:** 1
- **Crawl method:** api
- **Duration:** 3.32 seconds
- **Crawl completed:** 1/25/2025, 8:34:47 PM
