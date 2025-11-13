# Frequently Asked Questions

## General Questions

### What is Scientific Project Manager?

Scientific Project Manager is an Odoo 15.0 addon designed specifically for managing scientific research projects, experiments, researchers, equipment, and documentation in research institutions and laboratories.

### Who is it for?

- Research institutions and universities
- Corporate R&D departments
- Clinical research organizations
- Laboratory managers
- Principal investigators
- Research teams

### What Odoo version is required?

Odoo 15.0 or higher is required. The module is built for Odoo 15.0 specifically.

### Is it free?

Yes, the module is open source and licensed under LGPL-3. You can use, modify, and distribute it freely.

## Installation & Setup

### How do I install the module?

See the [Installation Guide](getting-started/installation.md) for detailed instructions. Basic steps:

1. Copy module to Odoo addons directory
2. Update apps list
3. Install "Scientific Project Manager"

### Do I need any additional Python packages?

No, all dependencies are standard Odoo modules (`base` and `mail`).

### Can I use it with Docker?

Yes! We provide a `docker-compose.yml` for easy deployment. See [Docker Setup](getting-started/docker-setup.md).

### How do I upgrade to a new version?

```bash
# Backup first!
pg_dump database > backup.sql

# Pull latest code
git pull

# Upgrade module
odoo-bin -u scientific_project -d database_name
```

## Features & Usage

### Can I customize fields?

Yes! You can add custom fields, modify views, and extend the module. See [Developer Guide](developer-guide/architecture.md).

### Does it support multiple languages?

Odoo supports multi-language out of the box. Translate strings via Settings → Translations.

### Can I export data?

Yes, use Odoo's built-in export feature:
1. Select records (tree view)
2. Action menu → Export
3. Choose fields and format

### How do I delete data?

Select records and use Action menu → Delete. Note: Some deletions may be restricted by security settings.

### Can researchers self-register?

By default, researchers are created by administrators. You can enable portal access for self-registration with custom development.

## Projects & Experiments

### What's the difference between a project and an experiment?

- **Project**: High-level research initiative with funding, timeline, and team
- **Experiment**: Specific scientific procedure following the scientific method

Projects contain multiple experiments.

### Can one experiment belong to multiple projects?

No, each experiment belongs to one project. However, you can link related experiments via documents and notes.

### How do I track project progress?

Use status fields, kanban boards, and calendar views. Check the [Projects Guide](user-guide/core-modules/projects.md).

### Can I template experiments?

Not built-in, but you can duplicate experiments (Action menu → Duplicate) and modify as needed.

## Researchers & Teams

### Are user accounts created automatically?

Yes! When you create a researcher record, an Odoo user account is automatically created.

### How do I manage permissions?

See the [Security Guide](security/overview.md) for setting up security groups and access rights.

### Can external collaborators access the system?

Yes, using Odoo's portal feature. Configure portal users with limited access.

### How do I assign tasks to multiple people?

Tasks have a many2many relationship with researchers. Select multiple researchers in the "Assigned to" field.

## Equipment & Resources

### How does equipment scheduling work?

Use the Schedule module to book equipment time slots. View in calendar or kanban format. See [Scheduling Guide](user-guide/supporting-modules/scheduling.md).

### Can I prevent double-booking?

Use the calendar view to visually check availability before booking. Custom validation can be added via development.

### How do I track equipment maintenance?

Set maintenance schedule dates on equipment records. Use filters to find equipment due for maintenance.

### Can I track reagent quantities?

Yes, the reagent model includes amount and units fields. Update manually as reagents are used.

## Documents & Data

### What file types can I upload?

Any file type. Use the binary field to upload PDFs, images, data files, etc.

### Is there version control for documents?

Basic version tracking via the version field. For advanced version control, integrate with external systems.

### How do I set document confidentiality?

Use the confidentiality_level field: Public, Internal, or Confidential. Combine with security rules for enforcement.

### Can I link documents to multiple projects?

Yes, the project field is many2many, allowing documents to link to multiple projects.

## Security & Access

### Is my data secure?

Security depends on your configuration. Review the [Security Guide](security/overview.md) for best practices.

### What's the default security setting?

⚠️ Default is open access (all users have full permissions). Configure security groups for production!

### How do I restrict access to confidential projects?

Use record rules to filter projects based on user groups or ownership. See [Record Rules](security/record-rules.md).

### Can I audit who accessed data?

Enable audit logging via Odoo's audit trail module or implement custom logging.

## Performance & Scalability

### How many projects can it handle?

Depends on your server resources. Properly configured, it can handle thousands of projects and experiments.

### Does it work with large teams?

Yes, designed for teams of 10-1000+ users. Use security groups to organize large teams.

### How do I optimize performance?

- Use database indexing
- Archive old records
- Optimize queries
- Use filters to reduce data loading

### Can I use it across multiple locations?

Yes, track locations in equipment and reagent models. Use Odoo's multi-company feature for separate institutions.

## Integration

### Can I integrate with laboratory instruments?

Custom development required. Use Odoo's API to connect external systems.

### Does it integrate with LIMS?

Not out of the box. Can be customized to interface with LIMS systems via API.

### Can I export to Excel?

Yes, use Odoo's built-in export feature. Exports to XLS, CSV, and other formats.

### Is there an API?

Yes, Odoo provides XML-RPC and JSON-RPC APIs. See [API Reference](api-reference/overview.md).

## Troubleshooting

### I can't see any records

Check:
1. User security group assignment
2. Record rules filtering your view
3. Filters in search bar

See [Troubleshooting Guide](troubleshooting.md).

### Equipment shows "In Use" but isn't being used

Update the status manually or check for orphaned schedule entries.

### Researcher user account wasn't created

Check:
1. Email field is filled
2. No duplicate users exist
3. User creation permissions

### Module installation fails

Check:
1. Odoo logs for errors
2. Module dependencies are installed
3. File permissions are correct

## Compliance & Regulations

### Is it HIPAA compliant?

No, additional security measures required for HIPAA compliance. See [Compliance Guide](security/compliance.md).

### Is it GDPR compliant?

Basic GDPR features available (data export, deletion). Review with legal team for full compliance.

### Can I use it for clinical trials?

Yes, but additional validation and 21 CFR Part 11 compliance may be required. Consult regulatory experts.

### Are audit trails included?

Basic change tracking via chatter. Advanced audit trails require additional modules or customization.

## Support

### Where can I get help?

- This documentation
- [GitHub Issues](https://github.com/steven0seagal/odoo_scientific_project/issues)
- Odoo community forums
- Commercial support (contact us)

### How do I report bugs?

[Open an issue on GitHub](https://github.com/steven0seagal/odoo_scientific_project/issues) with:
- Description of the bug
- Steps to reproduce
- Expected vs actual behavior
- Odoo version and module version

### Can I request features?

Yes! Open a feature request on GitHub or contribute via pull request.

### Is training available?

- Self-paced: This documentation
- Videos: Coming soon
- Commercial training: Contact us

## Contributing

### How can I contribute?

- Report bugs
- Suggest features
- Improve documentation
- Submit pull requests

See [Contributing Guide](developer-guide/contributing.md).

### What's the development process?

1. Fork repository
2. Create feature branch
3. Make changes with tests
4. Submit pull request
5. Code review and merge

### Where's the roadmap?

See the main [README](index.md#roadmap) for planned features.

---

**Don't see your question?** Check the [Troubleshooting Guide](troubleshooting.md) or [open an issue](https://github.com/steven0seagal/odoo_scientific_project/issues).
