# Changelog

All notable changes to the Odoo Scientific Project Manager will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [15.0.2.0.0] - 2025-11-13

This release implements major improvements from the comprehensive improvement proposal, focusing on security, missing functionality, code quality, and user experience enhancements.

### Added

#### New Features & Modules
- **Publication Management**: Complete UI implementation with tree, form, kanban, and search views
  - Publication workflow (Draft → Submitted → Under Review → Accepted → Published)
  - Multiple publication types (Journal, Conference, Book, Thesis, etc.)
  - DOI and citation tracking
  - Impact factor management
  - Author collaboration tracking
  - Date validation for submission, acceptance, and publication dates

- **Data Management Module**: Full implementation with comprehensive views
  - Dataset upload and management
  - File size calculation and display
  - Version control system
  - Access level control (Public, Internal, Restricted, Confidential)
  - Data expiry tracking and alerts
  - Metadata and keyword support
  - Checksum validation for file integrity
  - Relationships with projects and experiments

- **Partner/Collaborator Management**: Complete partner management system
  - Organization profiles with full contact information
  - Collaboration type tracking
  - Agreement management with document storage
  - Active agreement status tracking
  - Project relationship tracking
  - Multiple partner types (University, Industry, Government, etc.)

#### Security Enhancements
- **Role-Based Access Control (RBAC)**:
  - **Manager** role: Full access to all features
  - **Principal Investigator (PI)** role: Manage own projects and experiments
  - **User** role: Access to assigned tasks and experiments
  - **Viewer** role: Read-only access

- **Record Rules**: Data isolation based on user roles
  - Projects visible based on PI and collaborator assignment
  - Tasks accessible by assigned researchers
  - Experiments accessible by assigned team members
  - Data access controlled by ownership and confidentiality level

- **Security Groups**: Four distinct security groups with granular permissions
- **Access Rights**: Comprehensive permission matrix for all models

#### Model Enhancements

**Project Model**:
- Added computed fields: `task_count`, `experiment_count`, `publication_count`, `data_count`
- Added `days_remaining` and `is_overdue` computed fields
- Added `completion_percentage` based on task completion
- Added `total_budget` calculation from funding sources
- Added smart button actions for tasks, experiments, and publications
- Date validation constraints

**Task Model**:
- Added `priority` field (Low, Normal, High, Urgent)
- Added computed fields: `assigned_count`, `days_remaining`, `is_overdue`
- Date validation constraints
- Validation requiring assigned researchers for in-progress tasks

**Experiment Model**:
- Added Chatter integration (mail.thread, mail.activity.mixin)
- Added `duration_days`, `days_remaining`, `is_overdue` computed fields
- Added `assigned_researcher_count` and `equipment_count` computed fields
- Added reagents relationship
- Date validation constraints
- Hypothesis validation for in-progress experiments
- Added 'Cancelled' status option

**Schedule Model**:
- Added automatic booking reference generation
- Added `duration_hours` computed field
- **Equipment conflict detection**: Prevents double-booking of equipment
- **Researcher conflict warning**: Logs overlapping researcher bookings
- Time validation (end time must be after start time)
- Status tracking (Scheduled, In Progress, Completed, Cancelled)
- Chatter integration for communication

**Researcher Model**:
- Enhanced user creation with error handling
- Check for existing users before creation
- Email format validation
- Proper logging for user creation success/failures
- Graceful error handling without failing researcher creation

#### Bug Fixes
- **CRITICAL**: Fixed typo in Experiment model: `raport_created` → `report_created`
- **HIGH**: Added comprehensive error handling in Researcher model user creation
- **MEDIUM**: Added email format validation across all models
- **MEDIUM**: Fixed missing inverse relationships in Many2many fields
- **LOW**: Added proper ondelete rules for relationships

#### Data Validation
- Date range validation across all models (start_date < end_date)
- Email format validation using regex patterns
- Version format validation for data management (X.Y or X.Y.Z)
- Agreement date validation for partners
- Publication date logical order validation
- Equipment and researcher conflict detection in scheduling

### Changed

#### Model Improvements
- All major models now inherit from `mail.thread` and `mail.activity.mixin` for better tracking
- Added `_order` specifications for better default sorting
- Enhanced tracking on critical fields
- Improved field descriptions and help text
- Added proper `ondelete` rules for relationships

#### View Enhancements
- Publication views: Tree, Form, Kanban, and Search with comprehensive filters
- Data Management views: Tree, Form, Kanban, and Search with file management
- Partner views: Tree, Form, Kanban, and Search with agreement tracking
- Status badges with color coding across all views
- Ribbon widgets for special statuses (expired data, active agreements)

#### Security
- Updated `ir.model.access.csv` with all models and security groups
- Created `security/security.xml` with group definitions and record rules
- Migrated from open access to role-based access control

#### Manifest
- Updated version to 15.0.2.0.0
- Enhanced description with feature list
- Added security files to data loading
- Added new view files
- Reorganized data loading order (security first, then views)

### Improved

#### Code Quality
- Added comprehensive docstrings to validation methods
- Implemented proper exception handling
- Added logging for important operations
- Consistent code formatting
- Better organization of computed fields

#### User Experience
- Smart buttons on Project form for easy navigation
- Computed fields showing key metrics (counts, percentages, deadlines)
- Visual indicators for overdue items
- Color-coded status badges
- Progress tracking for projects

#### Performance
- Added `store=True` to frequently accessed computed fields
- Proper indexing through `_order` specifications
- Efficient domain filters in record rules

## [15.0.1.0.0] - 2024-11

### Added
- Initial release
- Core project management functionality
- Experiment tracking
- Task management
- Researcher profiles
- Document management
- Equipment and reagent tracking
- Resource scheduling
- Basic views for all models

### Known Issues (Addressed in 15.0.2.0.0)
- No security groups (all users had full access)
- Missing views for Publication, Data Management, and Partner models
- Typo in Experiment model field name
- No data validation constraints
- No conflict detection in scheduling
- Limited computed fields
- No user error handling in researcher creation

## Future Improvements

See [IMPROVEMENT_PROPOSAL.txt](IMPROVEMENT_PROPOSAL.txt) for planned enhancements in future releases:

### Phase 2 (Planned)
- Budget and expense tracking
- Sample inventory management
- Advanced scheduling features
- Dashboard implementation
- Email notifications
- Workflow automation

### Phase 3 (Planned)
- Gantt chart view
- Advanced search and filtering
- Enhanced form layouts
- Mobile optimization
- Custom widgets

### Phase 4 (Planned)
- External system integrations
- Advanced reporting
- API development
- Data import/export tools
- Calendar integration

---

For upgrade instructions, see [README.md](README.md#development--maintenance).

For security information, see [SECURITY.md](odoo/addons/scientific_project/SECURITY.md).
