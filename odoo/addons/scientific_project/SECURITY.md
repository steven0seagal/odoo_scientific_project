# Scientific Project Manager - Security Guide

## Table of Contents

1. [Current Security Configuration](#current-security-configuration)
2. [Security Model Overview](#security-model-overview)
3. [Recommended Security Implementation](#recommended-security-implementation)
4. [Security Groups Configuration](#security-groups-configuration)
5. [Record Rules (Row-Level Security)](#record-rules-row-level-security)
6. [Field-Level Security](#field-level-security)
7. [Implementation Guide](#implementation-guide)
8. [Best Practices](#best-practices)
9. [Audit and Compliance](#audit-and-compliance)
10. [Troubleshooting Security Issues](#troubleshooting-security-issues)

---

## Current Security Configuration

### Overview

**⚠️ WARNING**: The current security configuration provides **full unrestricted access** to all users.

### Access Rights File

**Location**: `security/ir.model.access.csv`

### Current Configuration

```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_scientific_project,scientific.project,model_scientific_project,"",1,1,1,1
access_scientific_task,scientific.task,model_scientific_task,"",1,1,1,1
access_scientific_document,scientific.document,model_scientific_document,"",1,1,1,1
access_scientific_experiment,scientific.experiment,model_scientific_experiment,"",1,1,1,1
access_scientific_researcher,scientific.researcher,model_scientific_researcher,"",1,1,1,1
access_scientific_tag,scientific.tags,model_scientific_tags,"",1,1,1,1
access_scientific_equipment,scientific.equipment,model_scientific_equipment,"",1,1,1,1
access_scientific_reagent,scientific.reagent,model_scientific_reagent,"",1,1,1,1
access_scientific_schedule,scientific.schedule,model_scientific_schedule,"",1,1,1,1
```

### What This Means

| Model | Read | Write | Create | Delete | Restricted To |
|-------|------|-------|--------|--------|---------------|
| **All Models** | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes | ❌ No restrictions |

**Implications**:
- ✅ **Advantage**: Easy to use, no permission issues during development/testing
- ⚠️ **Risk**: Any authenticated user can:
  - View all research data (including confidential projects)
  - Modify any project, experiment, or document
  - Delete critical research records
  - Access sensitive equipment schedules
  - View all researcher information

### Suitable For

- ✅ Development environment
- ✅ Testing environment
- ✅ Small research teams with full trust
- ✅ Single-user installations

### NOT Suitable For

- ❌ Production environments
- ❌ Multi-department institutions
- ❌ Environments with confidential research
- ❌ Installations requiring audit trails
- ❌ Compliance-regulated organizations (HIPAA, GDPR, etc.)

---

## Security Model Overview

### Odoo Security Layers

Odoo provides four layers of security:

```
1. Access Rights (CRUD permissions per model per group)
        ↓
2. Record Rules (Row-level filtering)
        ↓
3. Field-Level Access (Field visibility per group)
        ↓
4. View-Level Security (UI element visibility)
```

### Security Concepts

#### 1. Security Groups

**Definition**: Collections of users with similar access needs

**Examples**:
- Scientific Project Manager
- Scientific Project User
- Scientific Project Viewer
- Principal Investigator
- Lab Technician

#### 2. Access Rights (CRUD)

**Definition**: Model-level permissions

**Operations**:
- **Create**: Can create new records
- **Read**: Can view records
- **Update**: Can modify existing records
- **Delete**: Can delete records

#### 3. Record Rules

**Definition**: Row-level security (which records a user can access)

**Examples**:
- Users can only see their own projects
- PIs can see all projects they lead
- Managers can see all projects

#### 4. Inherited Groups

**Common Odoo Base Groups**:
- `base.group_user`: Internal User
- `base.group_system`: Administrator
- `base.group_portal`: Portal User

---

## Recommended Security Implementation

### Proposed Security Groups

#### 1. Scientific Project Manager
**Technical Name**: `group_scientific_project_manager`
**Description**: Full access to all features
**Members**: Lab managers, research directors, administrators

**Permissions**:
- ✅ Create, Read, Update, Delete all records
- ✅ Access all projects regardless of ownership
- ✅ Manage researchers and equipment
- ✅ View confidential documents
- ✅ Configure system settings

#### 2. Principal Investigator
**Technical Name**: `group_scientific_project_pi`
**Description**: Lead researchers with project management capabilities
**Members**: Principal investigators, project leads

**Permissions**:
- ✅ Create projects where they are PI
- ✅ Full access to their own projects
- 👁️ Read-only access to other projects
- ✅ Create and assign tasks
- ✅ Create experiments
- ✅ Book equipment
- ✅ Upload documents
- ❌ Cannot delete other users' projects

#### 3. Scientific Project User
**Technical Name**: `group_scientific_project_user`
**Description**: Regular researchers and lab members
**Members**: Researchers, post-docs, lab technicians

**Permissions**:
- 👁️ Read all non-confidential projects
- ✅ Full access to assigned tasks
- ✅ Update experiments they're assigned to
- ✅ Book equipment
- ✅ Create documents
- ❌ Cannot create projects
- ❌ Cannot delete experiments
- ❌ Cannot view confidential documents

#### 4. Scientific Project Viewer
**Technical Name**: `group_scientific_project_viewer`
**Description**: Read-only access for stakeholders
**Members**: Students, observers, visiting researchers

**Permissions**:
- 👁️ Read public projects only
- 👁️ Read public documents
- 👁️ View equipment availability
- ❌ Cannot create or modify anything
- ❌ Cannot view confidential information

### Group Hierarchy

```
base.group_system (Odoo Administrator)
        ↓
group_scientific_project_manager
        ↓
group_scientific_project_pi
        ↓
group_scientific_project_user
        ↓
group_scientific_project_viewer
```

**Inheritance**: Each lower group inherits the permissions of groups above it.

---

## Security Groups Configuration

### Implementation Files

#### 1. Create Security Groups XML

**File**: `security/security_groups.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <data>
        <!-- Category for Scientific Project groups -->
        <record id="module_category_scientific_project" model="ir.module.category">
            <field name="name">Scientific Project</field>
            <field name="description">Manage scientific research projects</field>
            <field name="sequence">20</field>
        </record>

        <!-- Viewer Group -->
        <record id="group_scientific_project_viewer" model="res.groups">
            <field name="name">Viewer</field>
            <field name="category_id" ref="module_category_scientific_project"/>
            <field name="implied_ids" eval="[(4, ref('base.group_user'))]"/>
            <field name="comment">Read-only access to public projects and documents</field>
        </record>

        <!-- User Group -->
        <record id="group_scientific_project_user" model="res.groups">
            <field name="name">User</field>
            <field name="category_id" ref="module_category_scientific_project"/>
            <field name="implied_ids" eval="[(4, ref('group_scientific_project_viewer'))]"/>
            <field name="comment">Regular researchers with task and experiment access</field>
        </record>

        <!-- Principal Investigator Group -->
        <record id="group_scientific_project_pi" model="res.groups">
            <field name="name">Principal Investigator</field>
            <field name="category_id" ref="module_category_scientific_project"/>
            <field name="implied_ids" eval="[(4, ref('group_scientific_project_user'))]"/>
            <field name="comment">Project leads with full project management capabilities</field>
        </record>

        <!-- Manager Group -->
        <record id="group_scientific_project_manager" model="res.groups">
            <field name="name">Manager</field>
            <field name="category_id" ref="module_category_scientific_project"/>
            <field name="implied_ids" eval="[(4, ref('group_scientific_project_pi'))]"/>
            <field name="comment">Full access to all scientific project features</field>
        </record>
    </data>
</odoo>
```

#### 2. Update Access Rights

**File**: `security/ir.model.access.csv`

```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink

# Manager - Full Access
access_scientific_project_manager,scientific.project.manager,model_scientific_project,group_scientific_project_manager,1,1,1,1
access_scientific_task_manager,scientific.task.manager,model_scientific_task,group_scientific_project_manager,1,1,1,1
access_scientific_document_manager,scientific.document.manager,model_scientific_document,group_scientific_project_manager,1,1,1,1
access_scientific_experiment_manager,scientific.experiment.manager,model_scientific_experiment,group_scientific_project_manager,1,1,1,1
access_scientific_researcher_manager,scientific.researcher.manager,model_scientific_researcher,group_scientific_project_manager,1,1,1,1
access_scientific_tag_manager,scientific.tags.manager,model_scientific_tags,group_scientific_project_manager,1,1,1,1
access_scientific_equipment_manager,scientific.equipment.manager,model_scientific_equipment,group_scientific_project_manager,1,1,1,1
access_scientific_reagent_manager,scientific.reagent.manager,model_scientific_reagent,group_scientific_project_manager,1,1,1,1
access_scientific_schedule_manager,scientific.schedule.manager,model_scientific_schedule,group_scientific_project_manager,1,1,1,1

# Principal Investigator
access_scientific_project_pi,scientific.project.pi,model_scientific_project,group_scientific_project_pi,1,1,1,0
access_scientific_task_pi,scientific.task.pi,model_scientific_task,group_scientific_project_pi,1,1,1,1
access_scientific_document_pi,scientific.document.pi,model_scientific_document,group_scientific_project_pi,1,1,1,0
access_scientific_experiment_pi,scientific.experiment.pi,model_scientific_experiment,group_scientific_project_pi,1,1,1,0
access_scientific_researcher_pi,scientific.researcher.pi,model_scientific_researcher,group_scientific_project_pi,1,0,0,0
access_scientific_tag_pi,scientific.tags.pi,model_scientific_tags,group_scientific_project_pi,1,0,0,0
access_scientific_equipment_pi,scientific.equipment.pi,model_scientific_equipment,group_scientific_project_pi,1,1,0,0
access_scientific_reagent_pi,scientific.reagent.pi,model_scientific_reagent,group_scientific_project_pi,1,1,1,0
access_scientific_schedule_pi,scientific.schedule.pi,model_scientific_schedule,group_scientific_project_pi,1,1,1,1

# User
access_scientific_project_user,scientific.project.user,model_scientific_project,group_scientific_project_user,1,0,0,0
access_scientific_task_user,scientific.task.user,model_scientific_task,group_scientific_project_user,1,1,0,0
access_scientific_document_user,scientific.document.user,model_scientific_document,group_scientific_project_user,1,1,1,0
access_scientific_experiment_user,scientific.experiment.user,model_scientific_experiment,group_scientific_project_user,1,1,0,0
access_scientific_researcher_user,scientific.researcher.user,model_scientific_researcher,group_scientific_project_user,1,0,0,0
access_scientific_tag_user,scientific.tags.user,model_scientific_tags,group_scientific_project_user,1,0,0,0
access_scientific_equipment_user,scientific.equipment.user,model_scientific_equipment,group_scientific_project_user,1,0,0,0
access_scientific_reagent_user,scientific.reagent.user,model_scientific_reagent,group_scientific_project_user,1,0,0,0
access_scientific_schedule_user,scientific.schedule.user,model_scientific_schedule,group_scientific_project_user,1,1,1,0

# Viewer
access_scientific_project_viewer,scientific.project.viewer,model_scientific_project,group_scientific_project_viewer,1,0,0,0
access_scientific_task_viewer,scientific.task.viewer,model_scientific_task,group_scientific_project_viewer,1,0,0,0
access_scientific_document_viewer,scientific.document.viewer,model_scientific_document,group_scientific_project_viewer,1,0,0,0
access_scientific_experiment_viewer,scientific.experiment.viewer,model_scientific_experiment,group_scientific_project_viewer,1,0,0,0
access_scientific_researcher_viewer,scientific.researcher.viewer,model_scientific_researcher,group_scientific_project_viewer,1,0,0,0
access_scientific_tag_viewer,scientific.tags.viewer,model_scientific_tags,group_scientific_project_viewer,1,0,0,0
access_scientific_equipment_viewer,scientific.equipment.viewer,model_scientific_equipment,group_scientific_project_viewer,1,0,0,0
access_scientific_reagent_viewer,scientific.reagent.viewer,model_scientific_reagent,group_scientific_project_viewer,1,0,0,0
access_scientific_schedule_viewer,scientific.schedule.viewer,model_scientific_schedule,group_scientific_project_viewer,1,0,0,0
```

#### 3. Update Manifest

**File**: `__manifest__.py`

Add security files to data section:

```python
'data': [
    'security/security_groups.xml',  # Add this line FIRST
    'security/ir.model.access.csv',
    'views/project.xml',
    # ... other view files
],
```

**⚠️ IMPORTANT**: `security_groups.xml` must be loaded BEFORE `ir.model.access.csv`

---

## Record Rules (Row-Level Security)

### Overview

Record rules filter which specific records a user can access based on conditions.

### Implementation File

**File**: `security/record_rules.xml`

### Example Record Rules

```xml
<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <data noupdate="1">

        <!-- Project Rules -->

        <!-- Manager: All Projects -->
        <record id="rule_project_manager" model="ir.rule">
            <field name="name">Scientific Project: Manager sees all</field>
            <field name="model_id" ref="model_scientific_project"/>
            <field name="groups" eval="[(4, ref('group_scientific_project_manager'))]"/>
            <field name="domain_force">[(1, '=', 1)]</field>
        </record>

        <!-- PI: Own Projects and Collaborations -->
        <record id="rule_project_pi" model="ir.rule">
            <field name="name">Scientific Project: PI sees own projects</field>
            <field name="model_id" ref="model_scientific_project"/>
            <field name="groups" eval="[(4, ref('group_scientific_project_pi'))]"/>
            <field name="domain_force">['|', ('principal_investigator_id.user_id', '=', user.id), ('collaborators_ids.user_id', 'in', [user.id])]</field>
        </record>

        <!-- User: Assigned Projects Only -->
        <record id="rule_project_user" model="ir.rule">
            <field name="name">Scientific Project: User sees assigned projects</field>
            <field name="model_id" ref="model_scientific_project"/>
            <field name="groups" eval="[(4, ref('group_scientific_project_user'))]"/>
            <field name="domain_force">[('collaborators_ids.user_id', 'in', [user.id])]</field>
        </record>

        <!-- Viewer: Public Projects Only -->
        <record id="rule_project_viewer" model="ir.rule">
            <field name="name">Scientific Project: Viewer sees public projects</field>
            <field name="model_id" ref="model_scientific_project"/>
            <field name="groups" eval="[(4, ref('group_scientific_project_viewer'))]"/>
            <field name="domain_force">[('status', '!=', 'draft')]</field>
            <field name="perm_read" eval="True"/>
            <field name="perm_write" eval="False"/>
            <field name="perm_create" eval="False"/>
            <field name="perm_unlink" eval="False"/>
        </record>

        <!-- Task Rules -->

        <!-- Manager: All Tasks -->
        <record id="rule_task_manager" model="ir.rule">
            <field name="name">Scientific Task: Manager sees all</field>
            <field name="model_id" ref="model_scientific_task"/>
            <field name="groups" eval="[(4, ref('group_scientific_project_manager'))]"/>
            <field name="domain_force">[(1, '=', 1)]</field>
        </record>

        <!-- User: Assigned Tasks -->
        <record id="rule_task_user" model="ir.rule">
            <field name="name">Scientific Task: User sees assigned tasks</field>
            <field name="model_id" ref="model_scientific_task"/>
            <field name="groups" eval="[(4, ref('group_scientific_project_user'))]"/>
            <field name="domain_force">[('assigned_to_ids.user_id', 'in', [user.id])]</field>
        </record>

        <!-- Document Rules -->

        <!-- Manager: All Documents -->
        <record id="rule_document_manager" model="ir.rule">
            <field name="name">Scientific Document: Manager sees all</field>
            <field name="model_id" ref="model_scientific_document"/>
            <field name="groups" eval="[(4, ref('group_scientific_project_manager'))]"/>
            <field name="domain_force">[(1, '=', 1)]</field>
        </record>

        <!-- PI: Documents from Own Projects -->
        <record id="rule_document_pi" model="ir.rule">
            <field name="name">Scientific Document: PI sees own documents</field>
            <field name="model_id" ref="model_scientific_document"/>
            <field name="groups" eval="[(4, ref('group_scientific_project_pi'))]"/>
            <field name="domain_force">['|', ('author_ids.user_id', '=', user.id), ('project_id.principal_investigator_id.user_id', '=', user.id)]</field>
        </record>

        <!-- User: Non-Confidential Documents -->
        <record id="rule_document_user" model="ir.rule">
            <field name="name">Scientific Document: User sees non-confidential</field>
            <field name="model_id" ref="model_scientific_document"/>
            <field name="groups" eval="[(4, ref('group_scientific_project_user'))]"/>
            <field name="domain_force">['|', ('confidentiality_level', 'in', ['public', 'internal']), ('author_ids.user_id', '=', user.id)]</field>
        </record>

        <!-- Viewer: Public Documents Only -->
        <record id="rule_document_viewer" model="ir.rule">
            <field name="name">Scientific Document: Viewer sees public only</field>
            <field name="model_id" ref="model_scientific_document"/>
            <field name="groups" eval="[(4, ref('group_scientific_project_viewer'))]"/>
            <field name="domain_force">[('confidentiality_level', '=', 'public')]</field>
            <field name="perm_read" eval="True"/>
            <field name="perm_write" eval="False"/>
            <field name="perm_create" eval="False"/>
            <field name="perm_unlink" eval="False"/>
        </record>

        <!-- Experiment Rules -->

        <!-- Manager: All Experiments -->
        <record id="rule_experiment_manager" model="ir.rule">
            <field name="name">Scientific Experiment: Manager sees all</field>
            <field name="model_id" ref="model_scientific_experiment"/>
            <field name="groups" eval="[(4, ref('group_scientific_project_manager'))]"/>
            <field name="domain_force">[(1, '=', 1)]</field>
        </record>

        <!-- User: Assigned Experiments -->
        <record id="rule_experiment_user" model="ir.rule">
            <field name="name">Scientific Experiment: User sees assigned</field>
            <field name="model_id" ref="model_scientific_experiment"/>
            <field name="groups" eval="[(4, ref('group_scientific_project_user'))]"/>
            <field name="domain_force">[('assigned_to_ids.user_id', 'in', [user.id])]</field>
        </record>

    </data>
</odoo>
```

### Domain Syntax

Common domain patterns:

```python
# All records
[(1, '=', 1)]

# Current user is the owner
[('user_id', '=', user.id)]

# Current user is in many2many field
[('researcher_ids.user_id', 'in', [user.id])]

# OR condition
['|', (condition1), (condition2)]

# AND condition (default)
[(condition1), (condition2)]

# Nested field access
[('project_id.principal_investigator_id.user_id', '=', user.id)]
```

---

## Field-Level Security

### Implementation

Add `groups` attribute to sensitive fields:

```python
# In models/project.py
class Project(models.Model):
    _name = 'scientific.project'

    name = fields.Char(string='Name', required=True)

    # Only managers can see funding
    funding = fields.Many2many(
        'scientific.funding',
        string='Funding',
        groups='scientific_project.group_scientific_project_manager'
    )

    # Only PI and managers can see confidential notes
    confidential_notes = fields.Text(
        string='Confidential Notes',
        groups='scientific_project.group_scientific_project_pi,scientific_project.group_scientific_project_manager'
    )
```

### View-Level Security

Hide UI elements based on groups:

```xml
<!-- In views/project.xml -->
<record id="project_form_view" model="ir.ui.view">
    <field name="name">project.form</field>
    <field name="model">scientific.project</field>
    <field name="arch" type="xml">
        <form>
            <sheet>
                <group>
                    <field name="name"/>

                    <!-- Only visible to managers -->
                    <field name="funding" groups="scientific_project.group_scientific_project_manager"/>

                    <!-- Only visible to PI and managers -->
                    <notebook>
                        <page string="Confidential" groups="scientific_project.group_scientific_project_pi,scientific_project.group_scientific_project_manager">
                            <field name="confidential_notes"/>
                        </page>
                    </notebook>
                </group>
            </sheet>
        </form>
    </field>
</record>
```

---

## Implementation Guide

### Step-by-Step Implementation

#### Phase 1: Backup Current System

```bash
# Backup database
pg_dump database_name > backup_before_security.sql

# Backup code
git commit -am "Backup before implementing security"
git tag backup-before-security
```

#### Phase 2: Create Security Files

1. **Create security group file**:
   ```bash
   touch security/security_groups.xml
   ```

2. **Add group definitions** (use XML above)

3. **Update access rights CSV** (use CSV above)

4. **Create record rules file**:
   ```bash
   touch security/record_rules.xml
   ```

5. **Add record rules** (use XML above)

#### Phase 3: Update Manifest

```python
# In __manifest__.py
'data': [
    'security/security_groups.xml',      # FIRST
    'security/ir.model.access.csv',      # SECOND
    'security/record_rules.xml',         # THIRD
    'views/project.xml',                 # Then views
    # ... other files
],
```

#### Phase 4: Install/Update Module

```bash
# Method 1: Via UI
# Settings → Apps → Scientific Project Manager → Upgrade

# Method 2: Via Command Line
odoo-bin -u scientific_project -d database_name
```

#### Phase 5: Assign Users to Groups

1. Go to **Settings → Users & Companies → Users**
2. Open each user
3. Go to **Access Rights** tab
4. Find **Scientific Project** section
5. Select appropriate group:
   - Manager
   - Principal Investigator
   - User
   - Viewer

#### Phase 6: Test Security

Test each group:

```python
# Test as different users
# Login as manager → should see everything
# Login as PI → should see own projects
# Login as user → should see assigned tasks
# Login as viewer → should only read public data
```

### Migration from Current System

**Problem**: Current system has no restrictions, new system will restrict access.

**Solution**: Assign all existing users to Manager group initially, then gradually move them to appropriate groups.

```xml
<!-- In security/security_groups.xml -->
<!-- Automatically add all users to User group on upgrade -->
<record id="auto_add_users_to_group" model="ir.rule">
    <field name="name">Auto-assign existing users</field>
    <!-- Implementation depends on requirements -->
</record>
```

---

## Best Practices

### 1. Principle of Least Privilege

- Grant minimum necessary permissions
- Start restrictive, loosen as needed
- Regular access reviews

### 2. Group Assignment

- Assign users to lowest appropriate group
- Document group membership reasons
- Review group membership quarterly

### 3. Sensitive Data

- Mark confidential projects explicitly
- Use confidentiality_level field consistently
- Restrict funding information visibility
- Protect researcher personal information

### 4. Audit Trail

All core models use `tracking=True`:

```python
# Tracked changes appear in chatter
description = fields.Text(tracking=True)
status = fields.Selection(tracking=True)
```

**View audit trail**:
1. Open record
2. Scroll to chatter
3. See "Description changed from X to Y by User on Date"

### 5. Password Policy

Configure strong password requirements:

```python
# In odoo.conf or via Settings → Technical → Parameters → System Parameters
auth_password_policy_minlength = 12
auth_password_policy_uppercase = True
auth_password_policy_lowercase = True
auth_password_policy_number = True
auth_password_policy_special = True
```

### 6. Two-Factor Authentication

Enable 2FA for sensitive accounts:

1. Go to **Settings → Users & Companies → Users**
2. Open user
3. Enable **Two-Factor Authentication**

### 7. Session Security

Configure session timeout:

```python
# In odoo.conf
limit_time_real = 1800  # 30 minutes
limit_time_cpu = 600    # 10 minutes
```

### 8. Database Backup

Regular automated backups:

```bash
# Daily backup script
#!/bin/bash
DATE=$(date +%Y%m%d)
pg_dump database_name | gzip > /backup/odoo_$DATE.sql.gz

# Keep only last 30 days
find /backup -name "odoo_*.sql.gz" -mtime +30 -delete
```

---

## Audit and Compliance

### GDPR Compliance

For researcher personal data:

1. **Data Minimization**:
   - Only collect necessary researcher information
   - Remove unused fields

2. **Right to Access**:
   - Researchers can view their own data
   - Export functionality available

3. **Right to Erasure**:
   - Implement data deletion procedures
   - Archive before delete for audit trail

4. **Data Portability**:
   - Export researcher data in standard format
   - Use Odoo's built-in export feature

### HIPAA Compliance (If Handling Health Data)

⚠️ **WARNING**: This module does NOT include HIPAA-required features by default.

Required additions:
- Encryption at rest
- Encryption in transit (HTTPS)
- Audit logs for all data access
- Automatic logoff
- Data integrity checks
- Emergency access procedures

### ISO 27001 Compliance

Security controls checklist:

- [ ] Access control policy documented
- [ ] User access reviews performed quarterly
- [ ] Security groups properly configured
- [ ] Audit trails enabled on all models
- [ ] Database backups automated and tested
- [ ] Password policy enforced
- [ ] Two-factor authentication available
- [ ] Security incident response plan documented

### Audit Logs

Enable detailed audit logging:

```python
# Custom audit model
class AuditLog(models.Model):
    _name = 'scientific.audit_log'
    _description = 'Audit Log'

    user_id = fields.Many2one('res.users', 'User')
    model = fields.Char('Model')
    record_id = fields.Integer('Record ID')
    action = fields.Selection([
        ('create', 'Create'),
        ('write', 'Update'),
        ('unlink', 'Delete'),
        ('read', 'Read'),
    ], 'Action')
    timestamp = fields.Datetime('Timestamp', default=fields.Datetime.now)
    details = fields.Text('Details')
```

---

## Troubleshooting Security Issues

### Common Issues

#### Issue 1: User Cannot See Any Records

**Symptoms**: User logs in, sees empty lists

**Causes**:
- Not assigned to any security group
- Record rules too restrictive
- Not a collaborator/assignee on any records

**Solutions**:
1. Check user's group membership
   ```
   Settings → Users & Companies → Users → [User] → Access Rights Tab
   ```

2. Check record rules
   ```
   Settings → Technical → Security → Record Rules
   Filter by model, check domains
   ```

3. Add user as collaborator to at least one project

#### Issue 2: Manager Cannot Create Records

**Symptoms**: "Access Denied" error when creating

**Causes**:
- Missing create permission in ir.model.access.csv
- Conflicting record rule

**Solutions**:
1. Verify access rights:
   ```csv
   access_scientific_project_manager,...,1,1,1,1
   # Last 4 numbers: read,write,create,unlink
   ```

2. Check for restrictive record rules on create

#### Issue 3: PI Cannot See Own Projects

**Symptoms**: PI doesn't see projects they lead

**Causes**:
- researcher.user_id not set correctly
- Record rule domain incorrect

**Solutions**:
1. Verify researcher has linked user:
   ```python
   researcher = env['scientific.researcher'].search([('name', '=', 'PI Name')])
   print(researcher.user_id)  # Should not be empty
   ```

2. Fix researcher-user link:
   ```python
   researcher.user_id = user
   ```

#### Issue 4: Access Errors After Security Update

**Symptoms**: Errors after implementing security

**Causes**:
- Groups not loaded before access rights
- XML ID references incorrect
- Module not fully upgraded

**Solutions**:
1. Correct manifest order:
   ```python
   'data': [
       'security/security_groups.xml',  # FIRST
       'security/ir.model.access.csv',  # SECOND
   ],
   ```

2. Fully upgrade module:
   ```bash
   odoo-bin -u scientific_project -d database_name --stop-after-init
   ```

3. Check XML IDs:
   ```sql
   SELECT * FROM ir_model_data WHERE module = 'scientific_project' AND model = 'res.groups';
   ```

### Debug Mode

Enable debug mode to see security information:

1. Activate developer mode:
   ```
   Settings → Activate Developer Mode
   ```

2. See technical info:
   - View metadata (bug icon)
   - See record access rules
   - Check user groups

### Testing Security

Test script:

```python
# Run in Odoo shell: odoo-bin shell -d database_name

# Test as different user
def test_as_user(user_login):
    user = env['res.users'].search([('login', '=', user_login)])

    # Projects visible
    projects = env['scientific.project'].with_user(user).search([])
    print(f"{user_login} sees {len(projects)} projects")

    # Can create?
    try:
        project = env['scientific.project'].with_user(user).create({
            'name': 'Test Project'
        })
        print(f"{user_login} can create projects")
        project.unlink()
    except:
        print(f"{user_login} CANNOT create projects")

# Test each role
test_as_user('manager_user')
test_as_user('pi_user')
test_as_user('regular_user')
test_as_user('viewer_user')
```

---

## Security Checklist

### Pre-Production Checklist

- [ ] Security groups defined and documented
- [ ] Access rights CSV configured for all models
- [ ] Record rules implemented and tested
- [ ] Field-level security applied to sensitive fields
- [ ] All users assigned to appropriate groups
- [ ] Password policy configured
- [ ] Two-factor authentication enabled for admins
- [ ] Session timeout configured
- [ ] HTTPS enabled (SSL certificate installed)
- [ ] Database backups automated
- [ ] Audit logging enabled
- [ ] Security documentation reviewed
- [ ] Security training completed for all users
- [ ] Incident response plan documented
- [ ] Regular security review scheduled

### Regular Security Review (Quarterly)

- [ ] Review user group assignments
- [ ] Audit access logs for anomalies
- [ ] Test backup restoration
- [ ] Review and update password policy
- [ ] Check for Odoo security updates
- [ ] Review record rules effectiveness
- [ ] Update security documentation
- [ ] Conduct security awareness training

---

## Additional Resources

### Odoo Security Documentation

- [Official Security Guide](https://www.odoo.com/documentation/18.0/developer/reference/backend/security.html)
- [Access Rights](https://www.odoo.com/documentation/18.0/developer/reference/backend/security.html#access-rights)
- [Record Rules](https://www.odoo.com/documentation/18.0/developer/reference/backend/security.html#record-rules)

### Security Standards

- **ISO 27001**: Information security management
- **GDPR**: General Data Protection Regulation (EU)
- **HIPAA**: Health Insurance Portability and Accountability Act (US)
- **NIST**: National Institute of Standards and Technology guidelines

### Support

For security concerns:
- Review this documentation
- Check Odoo community forums
- Consult security professionals for compliance requirements
- Contact Odoo security team for critical issues

---

## Conclusion

Implementing proper security is essential for production use of the Scientific Project Manager. This guide provides:

1. ✅ Analysis of current (insecure) configuration
2. ✅ Recommended security architecture
3. ✅ Complete implementation code
4. ✅ Step-by-step implementation guide
5. ✅ Troubleshooting procedures
6. ✅ Compliance considerations

**Next Steps**:
1. Review this document with stakeholders
2. Plan security implementation
3. Test in development environment
4. Deploy to production
5. Train users on new security model

---

**Document Version**: 1.0
**Last Updated**: 2025-11-13
**Odoo Version**: 18.0
**Security Level**: Production-Ready Reference
