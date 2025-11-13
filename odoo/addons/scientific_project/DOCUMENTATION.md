# Scientific Project Manager - Comprehensive Documentation

## Table of Contents

1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
3. [Core Modules](#core-modules)
   - [Projects](#projects)
   - [Tasks](#tasks)
   - [Experiments](#experiments)
   - [Researchers](#researchers)
4. [Supporting Modules](#supporting-modules)
   - [Documents](#documents)
   - [Equipment](#equipment)
   - [Reagents](#reagents)
   - [Scheduling](#scheduling)
5. [Views and Navigation](#views-and-navigation)
6. [Workflows](#workflows)
7. [Integration Features](#integration-features)
8. [Best Practices](#best-practices)
9. [Troubleshooting](#troubleshooting)

---

## Introduction

The **Scientific Project Manager** is a comprehensive Odoo addon designed to streamline research project management in scientific institutions. This documentation provides detailed information about all features, views, and capabilities.

### Key Concepts

- **Projects**: Top-level organizational units for research initiatives
- **Tasks**: Actionable items within projects
- **Experiments**: Detailed experimental procedures following the scientific method
- **Researchers**: Personnel involved in research activities
- **Documents**: All documentation related to research
- **Equipment**: Laboratory equipment and instruments
- **Reagents**: Chemicals, materials, and consumables
- **Schedule**: Time-based resource allocation

---

## Getting Started

### First Login

After installation, access the module through the main menu:

**Main Menu → Scientific Project**

### Initial Setup Checklist

1. ✅ **Add Researchers** - Create profiles for all team members
2. ✅ **Configure Tags** - Set up categorization tags for researchers
3. ✅ **Add Equipment** - Register all laboratory equipment
4. ✅ **Set Up Reagents** - Enter inventory of chemicals and materials
5. ✅ **Create Projects** - Initialize your research projects
6. ✅ **Configure Security** - Set up user groups and permissions (See SECURITY.md)

### Navigation Overview

```
Scientific Project (Main Menu)
├── Projects
├── Tasks
├── Experiments
├── Researchers
├── Documents
├── Equipment
├── Reagents
└── Schedule
```

---

## Core Modules

### Projects

Projects are the top-level organizational units for research initiatives.

#### Key Features

- **Status Tracking**: Draft → In Progress → Done/Cancelled
- **Team Management**: Assign principal investigators and collaborators
- **Funding Tracking**: Link multiple funding sources
- **Document Repository**: Attach and organize project documents
- **Activity Tracking**: Built-in chatter for communication and activities

#### Available Views

##### 1. Tree View (List View)
**Location**: `views/project.xml:project_tree_view`

Displays projects in a table format with columns:
- Name
- Start Date
- End Date
- Status
- Principal Investigator

**Features**:
- Click column headers to sort
- Use filters in the search bar
- Multi-select for batch operations

##### 2. Form View
**Location**: `views/project.xml:project_form_view`

Detailed project form with organized tabs:

**General Tab**:
- Project name (required)
- Start and end dates
- Status with clickable buttons (Draft, In Progress, Done, Cancelled)
- Principal Investigator (dropdown)
- Collaborators (multi-select)
- Description (rich text)

**Documents Tab**:
- Many2many widget to attach documents
- Quick create option for new documents

**Funding Tab**:
- Many2many widget for funding sources
- Track multiple grants/funding streams

**Notes Tab**:
- Free-form text area for project notes
- Support for internal comments

**Activity Tab** (Chatter):
- Log notes and messages
- Schedule activities
- Track followers
- Email integration

##### 3. Kanban View
**Location**: `views/project.xml:project_kanban_view`

Visual card-based interface grouped by status:

**Card Information**:
- Project name
- Date range
- Status indicator
- Quick action buttons

**Features**:
- Drag and drop between status columns
- Color-coded status indicators
- Quick edit capability
- Compact project overview

##### 4. Calendar View
**Location**: `views/project.xml:project_calendar_view`

Timeline view of projects:

**Display**:
- Monthly calendar layout
- Projects displayed by start/end date
- Color-coded by status
- Click to open project details

**Use Cases**:
- Resource planning
- Timeline visualization
- Deadline tracking
- Conflict identification

#### Field Reference

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | Char | Yes | Project name |
| `start_date` | Date | No | Project start date |
| `end_date` | Date | No | Project end date |
| `description` | Text | No | Detailed project description |
| `status` | Selection | Yes | Current status (draft/in_progress/done/cancelled) |
| `document_id` | Many2many | No | Related documents |
| `funding` | Many2many | No | Funding sources |
| `principal_investigator_id` | Many2one | No | Lead researcher |
| `collaborators_ids` | Many2many | No | Team members |
| `notes` | Text | No | Additional notes |

#### Workflows

**Project Lifecycle**:
```
Draft → In Progress → Done
              ↓
          Cancelled
```

**State Change Methods**:
- `action_draft()`: Reset to draft status
- `action_in_progress()`: Mark as in progress
- `action_done()`: Complete the project
- `action_cancelled()`: Cancel the project

#### Usage Examples

**Example 1: Creating a New Research Project**

1. Navigate to **Scientific Project → Projects**
2. Click **Create**
3. Fill in:
   - Name: "Cancer Biomarker Discovery"
   - Start Date: 2025-01-01
   - End Date: 2026-12-31
   - Status: Draft
   - Principal Investigator: Dr. Smith
   - Description: "Research project to identify novel cancer biomarkers..."
4. Click **Save**
5. Switch to **Documents** tab and attach:
   - Research proposal
   - Ethical approval
   - Study protocol
6. Switch to **Funding** tab and add grant information
7. Click **In Progress** button to activate the project

**Example 2: Monitoring Project Portfolio**

1. Go to **Scientific Project → Projects**
2. Switch to **Kanban View**
3. View all projects grouped by status
4. Drag projects between columns to update status
5. Switch to **Calendar View** to see timeline
6. Identify scheduling conflicts or resource overlaps

---

### Tasks

Tasks are actionable items within projects, allowing detailed work breakdown.

#### Key Features

- **Multi-researcher Assignment**: Assign tasks to multiple team members
- **Status Tracking**: Planning → In Progress → Completed/Cancelled
- **Project Linkage**: Connect tasks to parent projects
- **Document Attachment**: Link relevant documentation
- **Activity Tracking**: Chatter integration for updates

#### Available Views

##### 1. Tree View
**Location**: `views/task.xml:task_tree_view`

Columns:
- Task name
- Start date
- End date
- Status
- Assigned researchers
- Related project

##### 2. Form View
**Location**: `views/task.xml:task_form_view`

**General Tab**:
- Task name (required)
- Description
- Assigned to (multi-select researchers)
- Start and end dates
- Status (with clickable buttons)
- Parent project

**Documents Tab**:
- Attach supporting documents
- Link to protocols and procedures

**Notes Tab**:
- Additional task notes
- Implementation details

**Activity Tab**:
- Chatter for communication
- Activity scheduling
- Follower management

##### 3. Kanban View
**Location**: `views/task.xml:task_kanban_view`

Grouped by status: Planning, In Progress, Completed, Cancelled

Features:
- Visual workflow management
- Drag-and-drop status updates
- Quick task overview
- Priority indicators

##### 4. Calendar View
**Location**: `views/task.xml:task_calendar_view`

Monthly calendar showing tasks by date range.

#### Field Reference

| Field | Type | Required | Tracking | Description |
|-------|------|----------|----------|-------------|
| `name` | Char | Yes | Yes | Task name |
| `description` | Text | No | Yes | Detailed description |
| `assigned_to_ids` | Many2many | No | Yes | Assigned researchers |
| `start_date` | Date | No | Yes | Task start date |
| `end_date` | Date | No | Yes | Task deadline |
| `status` | Selection | Yes | Yes | Current status |
| `project_id` | Many2one | No | Yes | Parent project |
| `document_id` | Many2many | No | Yes | Related documents |
| `notes` | Text | No | Yes | Additional notes |

#### Usage Examples

**Example 1: Creating and Assigning Tasks**

1. Navigate to **Scientific Project → Tasks**
2. Click **Create**
3. Enter:
   - Name: "Literature Review - Cancer Biomarkers"
   - Status: Planning
   - Project: Select parent project
   - Assigned to: Select researchers
   - Start Date: 2025-01-15
   - End Date: 2025-02-15
4. In **Description**, add detailed instructions
5. Save and notify team members

**Example 2: Task Management Workflow**

1. Open task in Kanban view
2. Drag from "Planning" to "In Progress" when work begins
3. Team members add updates in chatter
4. Attach completed documents in Documents tab
5. Move to "Completed" when finished
6. Review in Calendar view to track deadlines

---

### Experiments

Experiments follow the scientific method with structured sections for complete documentation.

#### Key Features

- **Scientific Method Structure**: Introduction, Hypothesis, Methodology, Results, Conclusion
- **Resource Assignment**: Link researchers, equipment, and reagents
- **Status Tracking**: Planning → In Progress → Completed
- **Project Integration**: Connect experiments to parent projects
- **Documentation**: Attach protocols, data, and reports

#### Available Views

##### 1. Tree View
**Location**: `views/experiment.xml:experiment_tree_view`

Displays:
- Experiment name
- Status
- Project
- Start date
- End date
- Assigned researchers

##### 2. Form View
**Location**: `views/experiment.xml:experiment_form_view`

**General Information Section**:
- Experiment name (required)
- Description
- Start and end dates
- Status (Planning/In Progress/Completed)
- Parent project
- Assigned researchers

**Scientific Method Tabs**:

1. **Introduction Tab**:
   - Background information
   - Research context
   - Literature review summary

2. **Hypothesis Tab**:
   - Research question
   - Hypothesis statement
   - Expected outcomes

3. **Methodology Tab**:
   - Experimental design
   - Procedures
   - Materials and methods
   - Equipment and reagents needed

4. **Results Tab**:
   - Experimental findings
   - Data analysis
   - Observations

5. **Conclusion Tab**:
   - Interpretation of results
   - Comparison with hypothesis
   - Future directions

**Equipment Tab**:
- Many2many widget to assign equipment
- Track equipment usage

**Documents Tab**:
- Attach protocols, data files, images
- Link to ethical approvals

**Notes Tab**:
- Additional observations
- Troubleshooting notes

##### 3. Kanban View
**Location**: `views/experiment.xml:experiment_kanban_view`

Default Odoo kanban view grouped by status.

#### Field Reference

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | Char | Yes | Experiment name |
| `description` | Text | No | Brief description |
| `start_date` | Date | No | Start date |
| `end_date` | Date | No | Completion date |
| `status` | Selection | No | Planning/In Progress/Completed |
| `project_id` | Many2one | No | Parent project |
| `introduction` | Text | No | Background and context |
| `hypothesis` | Text | No | Research hypothesis |
| `methodology` | Text | No | Experimental procedures |
| `results` | Text | No | Findings and data |
| `conclusion` | Text | No | Analysis and interpretation |
| `raport_created` | Boolean | No | Report generation flag |
| `notes` | Text | No | Additional notes |
| `document_id` | Many2many | No | Related documents |
| `assigned_to_ids` | Many2many | No | Researchers |
| `equipment_ids` | Many2many | No | Required equipment |

#### Usage Examples

**Example 1: Documenting a Complete Experiment**

1. Create new experiment:
   - Name: "Effect of Drug X on Cancer Cell Lines"
   - Project: Link to parent research project
   - Status: Planning
   - Assign researchers

2. Fill Introduction tab:
   ```
   Background: Cancer cell line MCF-7 shows resistance to current treatments...
   Research Context: Previous studies have shown...
   ```

3. Write Hypothesis:
   ```
   Drug X will reduce cell viability of MCF-7 cells by >50% at 10μM concentration
   within 48 hours of treatment.
   ```

4. Document Methodology:
   ```
   Materials:
   - MCF-7 cell line
   - Drug X (10μM, 50μM, 100μM)
   - MTT assay kit

   Procedure:
   1. Seed cells at 10,000 cells/well in 96-well plate
   2. Treat with Drug X at various concentrations
   3. Incubate for 48 hours
   4. Perform MTT assay
   5. Measure absorbance at 570nm
   ```

5. Assign Equipment:
   - Cell culture incubator
   - Microplate reader
   - Biosafety cabinet

6. Update status to "In Progress"

7. After completion, record Results:
   ```
   Drug X reduced cell viability:
   - 10μM: 55% reduction
   - 50μM: 78% reduction
   - 100μM: 92% reduction
   IC50: ~8.5μM
   ```

8. Write Conclusion:
   ```
   Hypothesis confirmed. Drug X shows potent cytotoxic effect on MCF-7 cells.
   The IC50 value of 8.5μM suggests promise for further development...
   ```

9. Attach documents:
   - Raw data files
   - Analysis scripts
   - Images/graphs

10. Mark as "Completed"

---

### Researchers

Researcher profiles manage personnel information and track involvement in projects, tasks, and experiments.

#### Key Features

- **Complete Profiles**: Contact information, specialization, affiliations
- **Categorization**: Student, Professor, Researcher types
- **Tag System**: Flexible tagging with color coding
- **Automatic User Creation**: Creates Odoo user account on researcher creation
- **Activity Overview**: See all assigned projects, tasks, experiments, documents

#### Available Views

##### 1. Tree View
**Location**: `views/researcher.xml:researcher_tree_view`

Columns:
- Profile image
- Name
- Email
- Phone
- Type
- Specialization

##### 2. Form View
**Location**: `views/researcher.xml:researcher_form_view`

**Header Section**:
- Profile image (upload photo)
- Name (required)
- Tags (multi-select with colors)

**Contact Information Section**:
- Email
- Phone
- Type (Student/Professor/Researcher)
- Title (Dr., Prof., etc.)
- Affiliation (institution/department)
- Specialization

**Address Section**:
- Street
- Street 2
- City
- Zip Code
- Country

**Activity Tabs**:

1. **Projects Tab**:
   - Many2many widget showing all projects
   - Both as PI and collaborator

2. **Tasks Tab**:
   - All assigned tasks
   - Quick navigation to task details

3. **Experiments Tab**:
   - All assigned experiments
   - Track experimental involvement

4. **Documents Tab**:
   - All authored or related documents

5. **Comment Tab**:
   - Notes about the researcher
   - Administrative information

##### 3. Kanban View
**Location**: `views/researcher.xml:researcher_kanban_view`

Grouped by projects.

Card shows:
- Profile image
- Name
- Tags with colors
- Contact information

#### Field Reference

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `user_id` | Many2one | No | Linked Odoo user account |
| `name` | Char | Yes | Researcher name |
| `type` | Selection | No | Student/Professor/Researcher |
| `title` | Char | No | Academic title |
| `affiliation` | Char | No | Institution/department |
| `specialization` | Char | No | Research area |
| `tags` | Many2many | No | Categorization tags |
| `image` | Binary | No | Profile photo |
| `street` | Char | No | Street address |
| `street2` | Char | No | Street address line 2 |
| `city` | Char | No | City |
| `zip_code` | Char | No | Postal code |
| `country` | Char | No | Country |
| `phone` | Char | No | Phone number |
| `email` | Char | No | Email address |
| `comment` | Text | No | Notes |
| `projects` | Many2many | No | Associated projects |
| `tasks` | Many2many | No | Assigned tasks |
| `experiments` | Many2many | No | Assigned experiments |
| `documents` | Many2many | No | Authored documents |

#### Automatic User Creation

When a researcher is created, the system automatically:
1. Creates an Odoo user account
2. Sets login as researcher name
3. Sets email from researcher email
4. Links user to researcher record

**Code Reference**: `models/researcher.py:30-45`

#### Tags System

**Tag Model**: `scientific.tags`

Fields:
- `name`: Tag name
- `color`: Color index (0-11 for Odoo color palette)
- `researcher_ids`: Linked researchers

**Usage**:
- Create tags for departments, skills, or projects
- Assign colors for visual identification
- Use in kanban view for grouping

#### Usage Examples

**Example 1: Adding a New Researcher**

1. Navigate to **Scientific Project → Researchers**
2. Click **Create**
3. Fill information:
   - Name: "Dr. Jane Smith"
   - Email: "jane.smith@university.edu"
   - Phone: "+1-555-0123"
   - Type: Professor
   - Title: "Ph.D."
   - Affiliation: "University of Science - Biology Dept"
   - Specialization: "Molecular Biology"
4. Add address information
5. Upload profile photo
6. Add tags: "Molecular Biology", "Cancer Research"
7. Save - user account created automatically

**Example 2: Viewing Researcher Activity**

1. Open researcher profile
2. Switch to **Projects** tab to see all projects
3. Switch to **Tasks** tab to see assigned tasks
4. Review **Experiments** tab for experimental involvement
5. Check **Documents** tab for authored publications

---

## Supporting Modules

### Documents

Document management system for all research documentation with version control and confidentiality settings.

#### Key Features

- **Multiple Document Types**: Research papers, reports, proposals, ethical approvals, protocols
- **Status Workflow**: Draft → Submitted → Approved → Published
- **File Upload**: Binary file storage
- **Confidentiality Levels**: Public, Internal, Confidential
- **Multi-author Support**: Link multiple researchers as authors
- **Version Tracking**: Track document versions
- **Relationship Mapping**: Link to projects, tasks, experiments

#### Available Views

##### 1. Tree View
**Location**: `views/document.xml:document_tree_view`

Displays:
- Title
- Document type
- Status
- File name
- Authors
- Creation date

##### 2. Form View
**Location**: `views/document.xml:document_form_view`

**Document Information**:
- Title (required)
- Document type (dropdown)
- Status (dropdown with workflow)
- File upload widget
- File name

**Metadata Section**:
- Authors (multi-select researchers)
- Keywords
- Version
- Description

**Dates Section**:
- Creation date
- Last modified date
- Review date

**Security Section**:
- Confidentiality level (Public/Internal/Confidential)

**Relationships**:
- Projects (many2many)
- Tasks (many2one)
- Experiments (many2many)

**Notes**:
- Comments and additional information

#### Field Reference

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `title` | Char | Yes | Document title |
| `file_name` | Char | No | Name of uploaded file |
| `file` | Binary | No | File content |
| `document_type` | Selection | No | Type of document |
| `author_ids` | Many2many | No | Document authors |
| `description` | Text | No | Document description |
| `version` | Char | No | Version number |
| `status` | Selection | No | Document status |
| `creation_date` | Date | No | Date created |
| `last_modified_date` | Date | No | Last modification date |
| `review_date` | Date | No | Date for review |
| `confidentiality_level` | Selection | No | Access level |
| `project_id` | Many2many | No | Related projects |
| `task_id` | Many2one | No | Related task |
| `associated_experiment_id` | Many2many | No | Related experiments |
| `keywords` | Char | No | Search keywords |
| `comments` | Text | No | Additional notes |

#### Document Types

1. **Research Paper**: Manuscripts, publications
2. **Report**: Progress reports, final reports
3. **Proposal**: Grant proposals, project proposals
4. **Ethical Approval**: IRB approvals, ethics documents
5. **Experimental Protocol**: SOPs, procedures

#### Confidentiality Levels

- **Public**: Accessible to anyone
- **Internal**: Accessible within organization
- **Confidential**: Restricted access

#### Usage Examples

**Example 1: Uploading an Experimental Protocol**

1. Navigate to **Scientific Project → Documents**
2. Click **Create**
3. Enter:
   - Title: "Cell Culture Protocol - MCF-7"
   - Type: Experimental Protocol
   - Status: Draft
4. Click **Upload** and select protocol PDF
5. Add authors who wrote the protocol
6. Set confidentiality: Internal
7. Link to relevant experiments
8. Add keywords: "cell culture, MCF-7, protocol"
9. Change status to Published when finalized

---

### Equipment

Equipment management for tracking laboratory instruments, maintenance, and usage.

#### Key Features

- **Equipment Inventory**: Comprehensive equipment database
- **Status Tracking**: Available, In Use, Maintenance
- **Maintenance Scheduling**: Track maintenance dates
- **Care Taker Assignment**: Assign responsible personnel
- **Location Tracking**: Know where equipment is located
- **Usage Tracking**: Link to experiments using the equipment

#### Available Views

##### 1. Tree View
**Location**: `views/equipment.xml:equipment_tree_view`

Columns:
- Equipment name
- Type
- Location
- Status
- Maintenance schedule
- Care taker

##### 2. Form View
**Location**: `views/equipment.xml:equipment_form_view`

**Equipment Details**:
- Name (required)
- Equipment type
- Location
- Status (dropdown)
- Maintenance schedule (date picker)
- Care taker (researcher)

**Related Records Tabs**:
- **Experiments**: All experiments using this equipment
- **Documents**: Manuals, calibration certificates
- **Notes**: Maintenance logs, troubleshooting

##### 3. Kanban View
**Location**: `views/equipment.xml:equipment_kanban_view`

Grouped by equipment type.

Cards show:
- Equipment name
- Location
- Status indicator
- Maintenance date

#### Field Reference

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | Char | Yes | Equipment name |
| `equipment_type` | Char | No | Type/category |
| `location` | Char | No | Physical location |
| `status` | Selection | No | Available/In Use/Maintenance |
| `maintenance_schedule` | Date | No | Next maintenance date |
| `notes` | Text | No | Additional information |
| `care_taker_id` | Many2one | No | Responsible researcher |
| `document_id` | Many2many | No | Related documents |
| `experiment_id` | Many2many | No | Experiments using equipment |

#### Status Options

- **Available**: Ready for use
- **In Use**: Currently being used
- **Maintenance**: Under maintenance, not available

#### Usage Examples

**Example 1: Registering New Equipment**

1. Go to **Scientific Project → Equipment**
2. Click **Create**
3. Enter:
   - Name: "Microplate Reader - BioTek Epoch 2"
   - Type: "Spectrophotometer"
   - Location: "Lab 3A, Bench 5"
   - Status: Available
   - Maintenance Schedule: 2025-06-01
   - Care Taker: Select responsible researcher
4. Attach documents:
   - User manual
   - Calibration certificate
5. Add notes about usage guidelines

**Example 2: Tracking Equipment Maintenance**

1. Filter equipment by upcoming maintenance dates
2. Change status to "Maintenance" when servicing
3. Update notes with maintenance performed
4. Update maintenance schedule for next service
5. Change status back to "Available"

---

### Reagents

Inventory management for chemicals, reagents, and consumables.

#### Key Features

- **Inventory Tracking**: Track quantities and units
- **Location Management**: Know where reagents are stored
- **Status Monitoring**: Available, Not Available, In Delivery
- **Experiment Linkage**: Track reagent usage in experiments
- **Type Categorization**: Organize by reagent type

#### Available Views

##### 1. Tree View
**Location**: `views/reagents.xml:reagent_tree_view`

Columns:
- Reagent name
- Type
- Amount
- Units
- Location
- Status

##### 2. Form View
**Location**: `views/reagents.xml:reagent_form_view`

**Reagent Information**:
- Reagent name (required)
- Type
- Status (dropdown)
- Amount (numeric)
- Units (text)
- Location
- Related experiment
- Notes

##### 3. Kanban View
**Location**: `views/reagents.xml:reagent_kanban_view`

Grouped by type.

Cards display:
- Reagent name
- Amount and units
- Location
- Status indicator

#### Field Reference

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | Char | Yes | Reagent name |
| `type` | Char | No | Reagent category |
| `location` | Char | No | Storage location |
| `status` | Selection | No | Availability status |
| `amount` | Integer | No | Quantity |
| `units` | Char | No | Unit of measurement |
| `experiment_id` | Many2one | No | Related experiment |
| `notes` | Text | No | Additional information |

#### Status Options

- **Available**: In stock and available
- **Not Available**: Out of stock
- **In Delivery**: On order, arriving soon

#### Usage Examples

**Example 1: Adding Reagent to Inventory**

1. Navigate to **Scientific Project → Reagents**
2. Click **Create**
3. Enter:
   - Reagent: "DMSO (Dimethyl sulfoxide)"
   - Type: "Solvent"
   - Amount: 500
   - Units: "mL"
   - Location: "Chemical Storage Room, Shelf A3"
   - Status: Available
4. Add notes: "High purity, Cell culture grade"

**Example 2: Managing Reagent Consumption**

1. Open reagent record
2. Update amount when used
3. Change status to "Not Available" when depleted
4. Change to "In Delivery" when reordered
5. Update amount and status when received

---

### Scheduling

Resource scheduling system for equipment booking and researcher time allocation.

#### Key Features

- **Equipment Booking**: Schedule equipment usage
- **Researcher Assignment**: Allocate researcher time
- **Experiment Linkage**: Connect bookings to experiments
- **Time Slot Management**: Define start and end times
- **Conflict Prevention**: Visual calendar to avoid double booking

#### Available Views

##### 1. Tree View
**Location**: `views/schedule.xml:schedule_tree_view`

Columns:
- Equipment
- Researcher
- Experiment
- Start time
- End time

##### 2. Form View
**Location**: `views/schedule.xml:schedule_form_view`

**Booking Information**:
- Equipment (dropdown)
- Researcher (dropdown)
- Experiment (dropdown)
- Start time (datetime picker)
- End time (datetime picker)
- Notes

##### 3. Kanban View
**Location**: `views/schedule.xml:schedule_kanban_view`

Grouped by equipment.

Cards show:
- Researcher name
- Experiment
- Time slot
- Duration

##### 4. Calendar View
**Location**: `views/schedule.xml:schedule_calendar_view`

Weekly calendar layout:
- Time slots shown vertically
- Equipment bookings displayed
- Color-coded by equipment
- Click to create new booking
- Drag to reschedule

#### Field Reference

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `equipment_id` | Many2one | No | Equipment to book |
| `researcher_id` | Many2one | No | Assigned researcher |
| `start_time` | Datetime | No | Booking start |
| `end_time` | Datetime | No | Booking end |
| `notes` | Text | No | Additional information |
| `experiment_id` | Many2one | No | Related experiment |

#### Usage Examples

**Example 1: Booking Equipment**

1. Navigate to **Scientific Project → Schedule**
2. Switch to **Calendar View**
3. Click on desired time slot
4. Fill in:
   - Equipment: "Microplate Reader"
   - Researcher: Select user
   - Experiment: Link to experiment
   - Start Time: 2025-01-15 09:00
   - End Time: 2025-01-15 11:00
5. Save booking

**Example 2: Managing Schedules**

1. View weekly calendar
2. Identify available time slots
3. Check for conflicts
4. Drag bookings to reschedule
5. Color-code by equipment type

---

## Views and Navigation

### View Types

#### 1. Tree Views (List Views)

**Purpose**: Display multiple records in table format

**Features**:
- Sortable columns
- Searchable and filterable
- Multi-select for batch operations
- Export to Excel/CSV
- Customizable columns

**Best For**:
- Reviewing many records
- Comparing data
- Bulk operations
- Reporting

#### 2. Form Views

**Purpose**: Detailed single record view

**Features**:
- Organized with tabs/notebooks
- Rich text editors
- File uploads
- Related record widgets
- Status bars with actions
- Chatter integration

**Best For**:
- Creating new records
- Editing detailed information
- Viewing all related data
- Communication via chatter

#### 3. Kanban Views

**Purpose**: Visual card-based workflow management

**Features**:
- Drag-and-drop functionality
- Grouped by categories
- Quick card editing
- Color indicators
- Progress tracking

**Best For**:
- Workflow management
- Visual project tracking
- Status updates
- Team coordination

#### 4. Calendar Views

**Purpose**: Time-based visualization

**Features**:
- Monthly/weekly/daily views
- Click to create
- Drag to reschedule
- Color-coded events
- Conflict detection

**Best For**:
- Schedule planning
- Timeline visualization
- Resource allocation
- Deadline tracking

### Navigation Tips

**Quick Search**: Use the search bar with filters:
- Click filter icon for predefined filters
- Use "Group By" for categorization
- Save custom filters for reuse

**Breadcrumbs**: Use breadcrumb navigation to return to previous views

**Action Menu**: Access via "Action" dropdown:
- Export records
- Duplicate records
- Delete records
- Custom actions

**Keyboard Shortcuts**:
- `Alt + C`: Create new record
- `Alt + S`: Save record
- `Alt + K`: Discard changes
- `Ctrl + K`: Open command palette

---

## Workflows

### Project Workflow

```
1. Create Project (Draft)
   ↓
2. Add Funding and Team
   ↓
3. Activate Project (In Progress)
   ↓
4. Create Tasks and Experiments
   ↓
5. Track Progress
   ↓
6. Complete or Cancel (Done/Cancelled)
```

### Experiment Workflow

```
1. Plan Experiment
   - Write introduction
   - Formulate hypothesis
   - Design methodology
   ↓
2. Prepare Resources
   - Book equipment
   - Order reagents
   - Assign researchers
   ↓
3. Execute Experiment (In Progress)
   - Follow protocols
   - Record observations
   - Collect data
   ↓
4. Analyze and Conclude (Completed)
   - Analyze results
   - Draw conclusions
   - Create report
```

### Document Workflow

```
Draft → Submitted → Approved → Published
```

---

## Integration Features

### Chatter Integration

All core models (Projects, Tasks) include Odoo's chatter functionality:

**Features**:
- **Messages**: Post updates, comments, notes
- **Activities**: Schedule meetings, calls, todos
- **Followers**: Add team members to receive notifications
- **Email Integration**: Send and receive emails
- **File Attachments**: Share files via chatter

**Usage**:
1. Open any project or task
2. Scroll to chatter section at bottom
3. Click "Log note" for internal messages
4. Click "Send message" for notifications to followers
5. Click "Schedule Activity" for task scheduling

### Field Tracking

Key fields are tracked for audit trail:
- Status changes
- Assignment modifications
- Date updates
- Description edits

**Viewing Changes**:
1. Open record
2. Check chatter for "Status changed from Draft to In Progress"
3. Click timestamp to see who made the change

### User Integration

Researcher records automatically create Odoo user accounts:
- Username = Researcher name
- Email synced
- Automatic linking

---

## Best Practices

### Project Management

1. **Always set dates**: Helps with timeline visualization
2. **Assign PI early**: Clarifies responsibility
3. **Use status correctly**: Keep status updated for accurate reporting
4. **Leverage chatter**: Communicate within project context
5. **Attach funding**: Track budget and resources

### Experiment Documentation

1. **Complete all sections**: Use the full scientific method structure
2. **Write hypothesis clearly**: Specific, testable hypotheses
3. **Detail methodology**: Enough detail for reproduction
4. **Update results promptly**: Record findings while fresh
5. **Link resources**: Connect equipment, reagents, documents

### Task Management

1. **Break down work**: Create specific, actionable tasks
2. **Assign clearly**: Ensure everyone knows their tasks
3. **Set realistic deadlines**: Allow adequate time
4. **Update status regularly**: Keep team informed
5. **Use calendar view**: Visualize workload

### Document Management

1. **Choose correct type**: Proper categorization aids searching
2. **Set confidentiality**: Protect sensitive information
3. **Version documents**: Track changes over time
4. **Add keywords**: Improve searchability
5. **Link relationships**: Connect to projects/experiments

### Equipment and Reagents

1. **Keep inventory updated**: Accurate quantities
2. **Schedule maintenance**: Preventive maintenance prevents breakdowns
3. **Track locations**: Know where everything is
4. **Assign care takers**: Clear responsibility
5. **Book equipment**: Prevent scheduling conflicts

### Researcher Management

1. **Complete profiles**: Full contact information
2. **Use tags effectively**: Organize by skills/departments
3. **Keep specializations updated**: Know expertise
4. **Link activities**: See full picture of involvement

---

## Troubleshooting

### Common Issues

#### Issue: Cannot create researcher
**Solution**: Check that required field (name) is filled. Check user permissions.

#### Issue: Equipment shows as "In Use" but not being used
**Solution**: Update status manually or check for orphaned schedule entries.

#### Issue: Cannot see documents in project
**Solution**: Ensure documents are linked via Many2many relationship in Documents tab.

#### Issue: Calendar view not showing events
**Solution**: Check that date fields (start_date, end_date) are populated.

#### Issue: Status buttons not working
**Solution**: Check that status methods exist in model and are called correctly.

### Performance Tips

1. **Use filters**: Narrow down large datasets
2. **Archive old records**: Keep active data manageable
3. **Optimize searches**: Use specific search terms
4. **Limit calendar range**: Don't load too much at once

### Getting Help

1. Check this documentation
2. Review API_REFERENCE.md for field details
3. Check SECURITY.md for permission issues
4. Contact system administrator
5. Submit issues on GitHub

---

## Conclusion

The Scientific Project Manager provides a comprehensive solution for research project management. By following this documentation and best practices, your team can effectively manage projects, experiments, resources, and documentation.

For technical details about models and fields, see [API_REFERENCE.md](API_REFERENCE.md).

For security configuration, see [SECURITY.md](SECURITY.md).

For installation and quick start, see [README.md](README.md).

---

**Document Version**: 1.0
**Last Updated**: 2025-11-13
**Odoo Version**: 15.0
