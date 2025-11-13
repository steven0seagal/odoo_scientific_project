# Scientific Project Manager - API Reference

## Table of Contents

1. [Overview](#overview)
2. [Model Inheritance](#model-inheritance)
3. [Core Models](#core-models)
   - [scientific.project](#scientificproject)
   - [scientific.task](#scientifictask)
   - [scientific.experiment](#scientificexperiment)
   - [scientific.researcher](#scientificresearcher)
4. [Supporting Models](#supporting-models)
   - [scientific.document](#scientificdocument)
   - [scientific.equipment](#scientificequipment)
   - [scientific.reagent](#scientificreagent)
   - [scientific.schedule](#scientificschedule)
   - [scientific.tags](#scientifictags)
5. [Data Models](#data-models)
   - [scientific.funding](#scientificfunding)
   - [scientific.publication](#scientificpublication)
   - [scientific.data_management](#scientificdata_management)
   - [scientific.partner](#scientificpartner)
6. [Field Types Reference](#field-types-reference)
7. [Methods Reference](#methods-reference)
8. [Integration Points](#integration-points)

---

## Overview

This API reference provides complete technical documentation for all models, fields, and methods in the Scientific Project Manager module.

### Module Information

- **Module Name**: `scientific_project`
- **Technical Name**: `scientific_project`
- **Version**: 18.0.1.0.0
- **Category**: Project
- **Dependencies**: `base`, `mail`

### Naming Conventions

- **Model Names**: Use snake_case with `scientific.` prefix (e.g., `scientific.project`)
- **Field Names**: Use snake_case (e.g., `start_date`, `assigned_to_ids`)
- **Method Names**: Use snake_case with `action_` prefix for status changes
- **XML IDs**: Use underscore separation (e.g., `project_tree_view`)

---

## Model Inheritance

### Odoo Mail Integration

Models that inherit from `mail.thread` and `mail.activity.mixin`:

| Model | mail.thread | mail.activity.mixin |
|-------|-------------|---------------------|
| scientific.project | ✓ | ✓ |
| scientific.task | ✓ | ✓ |
| scientific.experiment | ✗ | ✗ |
| scientific.researcher | ✗ | ✗ |

**Features Inherited**:
- `mail.thread`: Chatter functionality, message posting, follower system
- `mail.activity.mixin`: Activity scheduling, activity tracking

---

## Core Models

### scientific.project

**Technical Name**: `scientific.project`
**Description**: Main project management model
**File Location**: `models/project.py`
**Inherits**: `mail.thread`, `mail.activity.mixin`

#### Fields

| Field Name | Field Type | Required | Default | Tracking | Description |
|------------|-----------|----------|---------|----------|-------------|
| `name` | Char | ✓ | - | ✗ | Project name |
| `start_date` | Date | ✗ | - | ✗ | Project start date |
| `end_date` | Date | ✗ | - | ✗ | Project end date |
| `description` | Text | ✗ | - | ✓ | Detailed project description |
| `status` | Selection | ✗ | 'draft' | ✓ | Current project status |
| `document_id` | Many2many | ✗ | - | ✓ | Related documents |
| `funding` | Many2many | ✗ | - | ✗ | Funding sources |
| `principal_investigator_id` | Many2one | ✗ | - | ✗ | Lead researcher |
| `collaborators_ids` | Many2many | ✗ | - | ✗ | Team members |
| `notes` | Text | ✗ | - | ✗ | Additional notes |

#### Selection Field Values

**status**:
- `'draft'`: Draft
- `'in_progress'`: In Progress
- `'done'`: Done
- `'cancelled'`: Cancelled

#### Relationships

| Field | Related Model | Type | Inverse Field |
|-------|---------------|------|---------------|
| `document_id` | scientific.document | Many2many | `project_id` |
| `funding` | scientific.funding | Many2many | - |
| `principal_investigator_id` | scientific.researcher | Many2one | - |
| `collaborators_ids` | scientific.researcher | Many2many | - |

#### Methods

```python
def action_draft(self):
    """Set project status to draft"""
    self.status = 'draft'

def action_in_progress(self):
    """Set project status to in progress"""
    self.status = 'in_progress'

def action_done(self):
    """Set project status to done"""
    self.status = 'done'

def action_cancelled(self):
    """Set project status to cancelled"""
    self.status = 'cancelled'
```

#### Views

- **Tree View**: `project_tree_view` (views/project.xml)
- **Form View**: `project_form_view` (views/project.xml)
- **Kanban View**: `project_kanban_view` (views/project.xml)
- **Calendar View**: `project_calendar_view` (views/project.xml)

#### Menu

**Main Menu**: `menu_scientific_project_root`
**Submenu**: `menu_project`
**Action**: `action_project`

---

### scientific.task

**Technical Name**: `scientific.task`
**Description**: Task management model
**File Location**: `models/task.py`
**Inherits**: `mail.thread`, `mail.activity.mixin`

#### Fields

| Field Name | Field Type | Required | Default | Tracking | Description |
|------------|-----------|----------|---------|----------|-------------|
| `name` | Char | ✓ | - | ✓ | Task name |
| `description` | Text | ✗ | - | ✓ | Task description |
| `assigned_to_ids` | Many2many | ✗ | - | ✓ | Assigned researchers |
| `start_date` | Date | ✗ | - | ✓ | Task start date |
| `end_date` | Date | ✗ | - | ✓ | Task deadline |
| `status` | Selection | ✗ | 'planning' | ✓ | Current task status |
| `project_id` | Many2one | ✗ | - | ✓ | Parent project |
| `document_id` | Many2many | ✗ | - | ✓ | Related documents |
| `notes` | Text | ✗ | - | ✓ | Additional notes |

#### Selection Field Values

**status**:
- `'planning'`: Planning
- `'in_progress'`: In Progress
- `'completed'`: Completed
- `'cancelled'`: Cancelled

#### Relationships

| Field | Related Model | Type | Inverse Field |
|-------|---------------|------|---------------|
| `assigned_to_ids` | scientific.researcher | Many2many | `tasks` |
| `project_id` | scientific.project | Many2one | - |
| `document_id` | scientific.document | Many2many | `task_id` |

#### Views

- **Tree View**: `task_tree_view` (views/task.xml)
- **Form View**: `task_form_view` (views/task.xml)
- **Kanban View**: `task_kanban_view` (views/task.xml)
- **Calendar View**: `task_calendar_view` (views/task.xml)

#### Menu

**Submenu**: `menu_task`
**Action**: `action_task`

---

### scientific.experiment

**Technical Name**: `scientific.experiment`
**Description**: Experiment tracking model
**File Location**: `models/experiment.py`
**Inherits**: None

#### Fields

| Field Name | Field Type | Required | Default | Description |
|------------|-----------|----------|---------|-------------|
| `name` | Char | ✓ | - | Experiment name |
| `description` | Text | ✗ | - | Brief description |
| `start_date` | Date | ✗ | - | Experiment start date |
| `end_date` | Date | ✗ | - | Experiment end date |
| `status` | Selection | ✗ | - | Current status |
| `project_id` | Many2one | ✗ | - | Parent project |
| `introduction` | Text | ✗ | - | Background and context |
| `hypothesis` | Text | ✗ | - | Research hypothesis |
| `methodology` | Text | ✗ | - | Experimental procedures |
| `results` | Text | ✗ | - | Experimental findings |
| `conclusion` | Text | ✗ | - | Analysis and interpretation |
| `raport_created` | Boolean | ✗ | False | Report generation flag |
| `notes` | Text | ✗ | - | Additional notes |
| `document_id` | Many2many | ✗ | - | Related documents |
| `assigned_to_ids` | Many2many | ✗ | - | Assigned researchers |
| `equipment_ids` | Many2many | ✗ | - | Required equipment |

#### Selection Field Values

**status**:
- `'planning'`: Planning
- `'in_progress'`: In Progress
- `'completed'`: Completed

#### Relationships

| Field | Related Model | Type | Inverse Field |
|-------|---------------|------|---------------|
| `project_id` | scientific.project | Many2one | - |
| `document_id` | scientific.document | Many2many | `associated_experiment_id` |
| `assigned_to_ids` | scientific.researcher | Many2many | `experiments` |
| `equipment_ids` | scientific.equipment | Many2many | `experiment_id` |

#### Views

- **Tree View**: `experiment_tree_view` (views/experiment.xml)
- **Form View**: `experiment_form_view` (views/experiment.xml)
- **Kanban View**: `experiment_kanban_view` (views/experiment.xml)

#### Menu

**Submenu**: `menu_experiment`
**Action**: `action_experiment`

---

### scientific.researcher

**Technical Name**: `scientific.researcher`
**Description**: Researcher profile management
**File Location**: `models/researcher.py`
**Inherits**: None

#### Fields

| Field Name | Field Type | Required | Default | Description |
|------------|-----------|----------|---------|-------------|
| `user_id` | Many2one | ✗ | - | Linked Odoo user |
| `name` | Char | ✓ | - | Researcher name |
| `type` | Selection | ✗ | - | Researcher category |
| `title` | Char | ✗ | - | Academic title |
| `affiliation` | Char | ✗ | - | Institution/department |
| `specialization` | Char | ✗ | - | Research area |
| `tags` | Many2many | ✗ | - | Categorization tags |
| `image` | Binary | ✗ | - | Profile photo |
| `street` | Char | ✗ | - | Street address |
| `street2` | Char | ✗ | - | Street address line 2 |
| `city` | Char | ✗ | - | City |
| `zip_code` | Char | ✗ | - | Postal code |
| `country` | Char | ✗ | - | Country |
| `phone` | Char | ✗ | - | Phone number |
| `email` | Char | ✗ | - | Email address |
| `comment` | Text | ✗ | - | Additional notes |
| `projects` | Many2many | ✗ | - | Associated projects |
| `tasks` | Many2many | ✗ | - | Assigned tasks |
| `experiments` | Many2many | ✗ | - | Assigned experiments |
| `documents` | Many2many | ✗ | - | Authored documents |

#### Selection Field Values

**type**:
- `'student'`: Student
- `'professor'`: Professor
- `'researcher'`: Researcher

#### Relationships

| Field | Related Model | Type | Inverse Field |
|-------|---------------|------|---------------|
| `user_id` | res.users | Many2one | - |
| `tags` | scientific.tags | Many2many | `researcher_ids` |
| `projects` | scientific.project | Many2many | - |
| `tasks` | scientific.task | Many2many | `assigned_to_ids` |
| `experiments` | scientific.experiment | Many2many | `assigned_to_ids` |
| `documents` | scientific.document | Many2many | `author_ids` |

#### Methods

```python
@api.model_create_multi
def create(self, vals_list):
    """
    Override create method to automatically create Odoo user account

    Creates:
    - User record with researcher name as login
    - Links user to researcher record via user_id field

    Returns:
        Recordset of created researchers
    """
    researchers = super(ScientificResearcher, self).create(vals_list)
    users = self.env['res.users']

    for researcher in researchers:
        user_vals = {
            'name': researcher.name,
            'login': researcher.name,
            'email': researcher.email,
        }
        user = users.create(user_vals)
        researcher.write({'user_id': user.id})

    return researchers
```

#### Views

- **Tree View**: `researcher_tree_view` (views/researcher.xml)
- **Form View**: `researcher_form_view` (views/researcher.xml)
- **Kanban View**: `researcher_kanban_view` (views/researcher.xml)

#### Menu

**Submenu**: `menu_researcher`
**Action**: `action_researcher`

---

## Supporting Models

### scientific.document

**Technical Name**: `scientific.document`
**Description**: Document management system
**File Location**: `models/document.py`
**Inherits**: None

#### Fields

| Field Name | Field Type | Required | Default | Description |
|------------|-----------|----------|---------|-------------|
| `title` | Char | ✓ | - | Document title |
| `file_name` | Char | ✗ | - | Name of uploaded file |
| `file` | Binary | ✗ | - | File content |
| `document_type` | Selection | ✗ | - | Type of document |
| `author_ids` | Many2many | ✗ | - | Document authors |
| `description` | Text | ✗ | - | Document description |
| `version` | Char | ✗ | - | Version number |
| `status` | Selection | ✗ | - | Document status |
| `creation_date` | Date | ✗ | - | Date created |
| `last_modified_date` | Date | ✗ | - | Last modification date |
| `review_date` | Date | ✗ | - | Date for review |
| `confidentiality_level` | Selection | ✗ | - | Access level |
| `project_id` | Many2many | ✗ | - | Related projects |
| `task_id` | Many2one | ✗ | - | Related task |
| `associated_experiment_id` | Many2many | ✗ | - | Related experiments |
| `keywords` | Char | ✗ | - | Search keywords |
| `comments` | Text | ✗ | - | Additional notes |

#### Selection Field Values

**document_type**:
- `'research_paper'`: Research Paper
- `'report'`: Report
- `'proposal'`: Proposal
- `'ethical_approval'`: Ethical Approval
- `'experimental_protocol'`: Experimental Protocol

**status**:
- `'draft'`: Draft
- `'submitted'`: Submitted
- `'approved'`: Approved
- `'published'`: Published

**confidentiality_level**:
- `'public'`: Public
- `'internal'`: Internal
- `'confidential'`: Confidential

#### Relationships

| Field | Related Model | Type | Inverse Field |
|-------|---------------|------|---------------|
| `author_ids` | scientific.researcher | Many2many | `documents` |
| `project_id` | scientific.project | Many2many | `document_id` |
| `task_id` | scientific.task | Many2one | `document_id` |
| `associated_experiment_id` | scientific.experiment | Many2many | `document_id` |

#### Views

- **Tree View**: `document_tree_view` (views/document.xml)
- **Form View**: `document_form_view` (views/document.xml)

#### Menu

**Submenu**: `menu_document`
**Action**: `action_document`

---

### scientific.equipment

**Technical Name**: `scientific.equipment`
**Description**: Laboratory equipment management
**File Location**: `models/equipment.py`
**Inherits**: None

#### Fields

| Field Name | Field Type | Required | Default | Description |
|------------|-----------|----------|---------|-------------|
| `name` | Char | ✓ | - | Equipment name |
| `equipment_type` | Char | ✗ | - | Type/category |
| `location` | Char | ✗ | - | Physical location |
| `status` | Selection | ✗ | - | Availability status |
| `maintenance_schedule` | Date | ✗ | - | Next maintenance date |
| `notes` | Text | ✗ | - | Additional information |
| `care_taker_id` | Many2one | ✗ | - | Responsible researcher |
| `document_id` | Many2many | ✗ | - | Related documents |
| `experiment_id` | Many2many | ✗ | - | Experiments using equipment |

#### Selection Field Values

**status**:
- `'available'`: Available
- `'in_use'`: In Use
- `'maintenance'`: Maintenance

#### Relationships

| Field | Related Model | Type | Inverse Field |
|-------|---------------|------|---------------|
| `care_taker_id` | scientific.researcher | Many2one | - |
| `document_id` | scientific.document | Many2many | - |
| `experiment_id` | scientific.experiment | Many2many | `equipment_ids` |

#### Views

- **Tree View**: `equipment_tree_view` (views/equipment.xml)
- **Form View**: `equipment_form_view` (views/equipment.xml)
- **Kanban View**: `equipment_kanban_view` (views/equipment.xml)

#### Menu

**Submenu**: `menu_equipment`
**Action**: `action_equipment`

---

### scientific.reagent

**Technical Name**: `scientific.reagent`
**Description**: Reagent and chemical inventory
**File Location**: `models/reagents.py`
**Inherits**: None

#### Fields

| Field Name | Field Type | Required | Default | Description |
|------------|-----------|----------|---------|-------------|
| `name` | Char | ✓ | - | Reagent name |
| `type` | Char | ✗ | - | Reagent category |
| `location` | Char | ✗ | - | Storage location |
| `status` | Selection | ✗ | - | Availability status |
| `amount` | Integer | ✗ | - | Quantity |
| `units` | Char | ✗ | - | Unit of measurement |
| `experiment_id` | Many2one | ✗ | - | Related experiment |
| `notes` | Text | ✗ | - | Additional information |

#### Selection Field Values

**status**:
- `'available'`: Available
- `'not_available'`: Not available
- `'in_delivery'`: In delivery

#### Relationships

| Field | Related Model | Type | Inverse Field |
|-------|---------------|------|---------------|
| `experiment_id` | scientific.experiment | Many2one | - |

#### Views

- **Tree View**: `reagent_tree_view` (views/reagents.xml)
- **Form View**: `reagent_form_view` (views/reagents.xml)
- **Kanban View**: `reagent_kanban_view` (views/reagents.xml)

#### Menu

**Submenu**: `menu_reagent`
**Action**: `action_reagent`

---

### scientific.schedule

**Technical Name**: `scientific.schedule`
**Description**: Resource scheduling system
**File Location**: `models/schedule.py`
**Inherits**: None

#### Fields

| Field Name | Field Type | Required | Default | Description |
|------------|-----------|----------|---------|-------------|
| `equipment_id` | Many2one | ✗ | - | Equipment to book |
| `researcher_id` | Many2one | ✗ | - | Assigned researcher |
| `start_time` | Datetime | ✗ | - | Booking start |
| `end_time` | Datetime | ✗ | - | Booking end |
| `notes` | Text | ✗ | - | Additional information |
| `experiment_id` | Many2one | ✗ | - | Related experiment |

#### Relationships

| Field | Related Model | Type | Inverse Field |
|-------|---------------|------|---------------|
| `equipment_id` | scientific.equipment | Many2one | - |
| `researcher_id` | scientific.researcher | Many2one | - |
| `experiment_id` | scientific.experiment | Many2one | - |

#### Views

- **Tree View**: `schedule_tree_view` (views/schedule.xml)
- **Form View**: `schedule_form_view` (views/schedule.xml)
- **Kanban View**: `schedule_kanban_view` (views/schedule.xml)
- **Calendar View**: `schedule_calendar_view` (views/schedule.xml)

#### Menu

**Submenu**: `menu_schedule`
**Action**: `action_schedule`

---

### scientific.tags

**Technical Name**: `scientific.tags`
**Description**: Researcher categorization tags
**File Location**: `models/researcher.py` and `models/tag.py`
**Inherits**: None

#### Fields

| Field Name | Field Type | Required | Default | Description |
|------------|-----------|----------|---------|-------------|
| `name` | Char | ✓ | - | Tag name |
| `researcher_ids` | Many2many | ✗ | - | Tagged researchers |
| `color` | Integer | ✗ | - | Color index (0-11) |

#### Relationships

| Field | Related Model | Type | Inverse Field |
|-------|---------------|------|---------------|
| `researcher_ids` | scientific.researcher | Many2many | `tags` |

#### Color Palette

Odoo uses a color index system (0-11):
- 0: No color (white)
- 1: Red
- 2: Orange
- 3: Yellow
- 4: Light Blue
- 5: Dark Purple
- 6: Salmon Pink
- 7: Medium Blue
- 8: Dark Green
- 9: Magenta
- 10: Slate Blue
- 11: Light Green

---

## Data Models

### scientific.funding

**Technical Name**: `scientific.funding`
**Description**: Funding source tracking
**File Location**: `models/funding.py`
**Inherits**: None
**Views**: None (no UI implementation)

#### Fields

| Field Name | Field Type | Required | Default | Description |
|------------|-----------|----------|---------|-------------|
| `source` | Char | ✓ | - | Funding source name |
| `budget` | Float | ✗ | - | Total budget amount |
| `start_date` | Date | ✗ | - | Funding start date |
| `end_date` | Date | ✗ | - | Funding end date |
| `project_id` | Many2one | ✗ | - | Related project |

#### Relationships

| Field | Related Model | Type | Inverse Field |
|-------|---------------|------|---------------|
| `project_id` | scientific.project | Many2one | `funding` |

---

### scientific.publication

**Technical Name**: `scientific.publication`
**Description**: Publication management
**File Location**: `models/publication.py`
**Inherits**: None
**Views**: None (no UI implementation)

#### Fields

| Field Name | Field Type | Required | Default | Description |
|------------|-----------|----------|---------|-------------|
| `title` | Char | ✓ | - | Publication title |
| `authors_ids` | Many2many | ✗ | - | Publication authors |
| `journal_conference` | Char | ✗ | - | Journal or conference name |
| `doi` | Char | ✗ | - | Digital Object Identifier |
| `project_id` | Many2one | ✗ | - | Related project |
| `experiment_ids` | Many2many | ✗ | - | Related experiments |
| `task_ids` | Many2many | ✗ | - | Related tasks |

#### Relationships

| Field | Related Model | Type | Inverse Field |
|-------|---------------|------|---------------|
| `authors_ids` | scientific.researcher | Many2many | - |
| `project_id` | scientific.project | Many2one | - |
| `experiment_ids` | scientific.experiment | Many2many | - |
| `task_ids` | scientific.task | Many2many | - |

---

### scientific.data_management

**Technical Name**: `scientific.data_management`
**Description**: Research data management
**File Location**: `models/data.py`
**Inherits**: None
**Views**: None (no UI implementation)

#### Fields

| Field Name | Field Type | Required | Default | Description |
|------------|-----------|----------|---------|-------------|
| `data_type` | Selection | ✗ | - | Type of data |
| `storage_location` | Char | ✗ | - | Where data is stored |
| `access_controls` | Char | ✗ | - | Access control settings |
| `project_id` | Many2one | ✗ | - | Related project |

#### Selection Field Values

**data_type**:
- `'raw_data'`: Raw Data
- `'processed_data'`: Processed Data

#### Relationships

| Field | Related Model | Type | Inverse Field |
|-------|---------------|------|---------------|
| `project_id` | scientific.project | Many2one | - |

---

### scientific.partner

**Technical Name**: `scientific.partner`
**Description**: External collaborator/partner management
**File Location**: `models/partner.py`
**Inherits**: None
**Views**: None (no UI implementation)

#### Fields

| Field Name | Field Type | Required | Default | Description |
|------------|-----------|----------|---------|-------------|
| `name` | Char | ✓ | - | Partner name |
| `partner_type` | Selection | ✗ | - | Type of partner |
| `contact_information` | Char | ✗ | - | Contact details |

#### Selection Field Values

**partner_type**:
- `'university'`: University
- `'industry'`: Industry
- `'government'`: Government

---

## Field Types Reference

### Odoo Field Types Used

| Field Type | Python Type | Database Type | Description | Example |
|------------|-------------|---------------|-------------|---------|
| Char | str | VARCHAR | Short text | `name = fields.Char()` |
| Text | str | TEXT | Long text | `notes = fields.Text()` |
| Integer | int | INTEGER | Whole numbers | `amount = fields.Integer()` |
| Float | float | NUMERIC | Decimal numbers | `budget = fields.Float()` |
| Boolean | bool | BOOLEAN | True/False | `raport_created = fields.Boolean()` |
| Date | date | DATE | Date without time | `start_date = fields.Date()` |
| Datetime | datetime | TIMESTAMP | Date with time | `start_time = fields.Datetime()` |
| Binary | bytes | BYTEA | File storage | `file = fields.Binary()` |
| Selection | str | VARCHAR | Dropdown values | `status = fields.Selection([...])` |
| Many2one | int | INTEGER | Foreign key | `project_id = fields.Many2one()` |
| Many2many | list | JOIN TABLE | Many-to-many relation | `tags = fields.Many2many()` |

### Field Attributes

Common attributes used in this module:

| Attribute | Type | Description | Example |
|-----------|------|-------------|---------|
| `string` | str | Field label in UI | `string='Project Name'` |
| `required` | bool | Field must be filled | `required=True` |
| `default` | any | Default value | `default='draft'` |
| `tracking` | bool/str | Track changes in chatter | `tracking=True` |
| `track_visibility` | str | Legacy tracking | `track_visibility='onchange'` |

---

## Methods Reference

### Status Change Methods

Pattern used across models:

```python
def action_status_name(self):
    """
    Change record status to [status_name]

    Called by statusbar buttons in form view
    Updates status field directly
    """
    self.status = 'status_name'
```

**Implementation**:
- `scientific.project`:
  - `action_draft()`: Set status to 'draft'
  - `action_in_progress()`: Set status to 'in_progress'
  - `action_done()`: Set status to 'done'
  - `action_cancelled()`: Set status to 'cancelled'

### Override Methods

#### Researcher Create Override

```python
@api.model_create_multi
def create(self, vals_list):
    """
    Override create to auto-generate Odoo user accounts

    Args:
        vals_list (list): List of value dictionaries for new records

    Returns:
        recordset: Created researcher records with linked users

    Side Effects:
        - Creates res.users record for each researcher
        - Links user via user_id field
        - Uses researcher name as login
        - Uses researcher email for user
    """
```

**Location**: `models/researcher.py:30-45`

---

## Integration Points

### Mail System Integration

Models with chatter integration can use:

```python
# Post a message
self.message_post(
    body="Message content",
    subject="Subject",
    message_type='notification'
)

# Log a note
self.message_post(
    body="Internal note",
    subtype_xmlid='mail.mt_note'
)

# Schedule activity
self.activity_schedule(
    'mail.mail_activity_data_todo',
    summary="Task to do",
    user_id=user.id
)

# Add followers
self.message_subscribe(partner_ids=[partner.id])
```

### User System Integration

Automatic user creation in `scientific.researcher`:

```python
# User is automatically created with:
user_vals = {
    'name': researcher.name,      # Full name
    'login': researcher.name,     # Username for login
    'email': researcher.email,    # Email address
}
```

### Access via XML-RPC/JSON-RPC

External API access example:

```python
import xmlrpc.client

# Connect to Odoo
url = 'http://localhost:8069'
db = 'database_name'
username = 'admin'
password = 'admin'

common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
uid = common.authenticate(db, username, password, {})

models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')

# Search projects
project_ids = models.execute_kw(
    db, uid, password,
    'scientific.project', 'search',
    [[['status', '=', 'in_progress']]]
)

# Read project data
projects = models.execute_kw(
    db, uid, password,
    'scientific.project', 'read',
    [project_ids],
    {'fields': ['name', 'start_date', 'status']}
)
```

### ORM Usage Examples

```python
# Create record
project = self.env['scientific.project'].create({
    'name': 'New Project',
    'status': 'draft',
})

# Search records
projects = self.env['scientific.project'].search([
    ('status', '=', 'in_progress')
])

# Browse by ID
project = self.env['scientific.project'].browse(project_id)

# Update record
project.write({'status': 'done'})

# Delete record
project.unlink()

# Get related records
experiments = project.experiment_ids

# Many2many operations
project.collaborators_ids = [(4, researcher_id)]  # Add
project.collaborators_ids = [(3, researcher_id)]  # Remove
project.collaborators_ids = [(6, 0, [id1, id2])]  # Replace all
```

---

## Security and Access Control

### Access Rights Location

**File**: `security/ir.model.access.csv`

### Current Configuration

All models have full CRUD access with no group restrictions:

| Model | Read | Write | Create | Unlink | Group |
|-------|------|-------|--------|--------|-------|
| All models | ✓ | ✓ | ✓ | ✓ | None |

**Security Implications**: Any authenticated user has full access to all records.

**Recommendation**: Implement security groups for production use. See [SECURITY.md](SECURITY.md) for details.

---

## API Usage Examples

### Python API Examples

#### Create a Complete Project Workflow

```python
# Create project
project = env['scientific.project'].create({
    'name': 'Cancer Research Initiative',
    'start_date': '2025-01-01',
    'end_date': '2026-12-31',
    'description': 'Multi-year cancer research program',
    'status': 'draft',
})

# Create researchers
pi = env['scientific.researcher'].create({
    'name': 'Dr. Jane Smith',
    'type': 'professor',
    'email': 'jane@university.edu',
    'specialization': 'Oncology',
})

# Assign PI
project.principal_investigator_id = pi

# Create experiment
experiment = env['scientific.experiment'].create({
    'name': 'Drug Efficacy Test',
    'project_id': project.id,
    'hypothesis': 'Drug X will reduce tumor size',
    'status': 'planning',
    'assigned_to_ids': [(4, pi.id)],
})

# Book equipment
schedule = env['scientific.schedule'].create({
    'equipment_id': equipment.id,
    'researcher_id': pi.id,
    'experiment_id': experiment.id,
    'start_time': '2025-02-01 09:00:00',
    'end_time': '2025-02-01 17:00:00',
})

# Activate project
project.action_in_progress()
```

#### Search and Filter

```python
# Find all active projects
active_projects = env['scientific.project'].search([
    ('status', '=', 'in_progress')
])

# Complex search
experiments = env['scientific.experiment'].search([
    ('status', '=', 'in_progress'),
    ('start_date', '>=', '2025-01-01'),
    ('project_id.principal_investigator_id.specialization', 'ilike', 'cancer')
])

# Search with limit and order
recent_docs = env['scientific.document'].search(
    [],
    limit=10,
    order='creation_date desc'
)
```

---

## Appendix

### File Locations Quick Reference

```
models/
├── __init__.py
├── project.py              # scientific.project
├── task.py                 # scientific.task
├── experiment.py           # scientific.experiment
├── researcher.py           # scientific.researcher, scientific.tags
├── document.py             # scientific.document
├── equipment.py            # scientific.equipment
├── reagents.py             # scientific.reagent
├── schedule.py             # scientific.schedule
├── funding.py              # scientific.funding
├── publication.py          # scientific.publication
├── data.py                 # scientific.data_management
├── partner.py              # scientific.partner
└── tag.py                  # scientific.tags (duplicate)

views/
├── project.xml             # Project views + main menu
├── task.xml                # Task views
├── experiment.xml          # Experiment views
├── researcher.xml          # Researcher views
├── document.xml            # Document views
├── equipment.xml           # Equipment views
├── reagents.xml            # Reagent views
└── schedule.xml            # Schedule views

security/
└── ir.model.access.csv     # Access control list
```

### Model Relationship Diagram

```
scientific.project (1) ──────< (N) scientific.task
       │
       │ (1)
       ├──────< (N) scientific.experiment ──────< (N) scientific.schedule
       │              │                                   │
       │              │ (N)                               │ (1)
       │              ├────> (N) scientific.equipment <───┘
       │              │
       │              │ (N)
       │              └────> (N) scientific.reagent
       │
       │ (N)
       ├──────> (N) scientific.document
       │              │
       │              │ (N)
       │              └────> (N) scientific.researcher
       │                             │
       │ (N)                         │ (N)
       └──────> (N) ─────────────────┘
       │
       │ (N)
       └──────> (N) scientific.funding
```

---

**Document Version**: 1.0
**Last Updated**: 2025-11-13
**Odoo Version**: 18.0
**Module Version**: 18.0.1.0.0
