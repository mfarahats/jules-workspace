# Agents.md

This file provides guidance when working with code in this repository.

## Project Overview

This is an Odoo 18 development environment using Docker containers. The project consists of:
- Odoo application server (container: odoo-dev)
- PostgreSQL database (container: odoo-db)
- Custom addons mounted from the local `addons` directory

## Development Commands

### Starting the Development Environment

**Important**: Always use `sudo docker compose` (with space between "docker" and "compose", not "docker-compose") when running Docker Compose commands in this project.

```bash
# Install and test a module (replace 'module_name' with actual module name)
# Always use 'sudo docker compose' (with space, not docker-compose)
sudo docker compose run --rm odoo odoo -i module_name -d postgres --stop-after-init
```

## Architecture

### Container Configuration
- **Odoo Service**: Uses official `odoo:18` image
- **Database Service**: Uses `postgres:15` image
- **Network**: Custom bridge network `odoo-network` connects both containers
- **Volumes**: 
  - `odoo-data`: Persistent Odoo data storage
  - `db-data`: PostgreSQL data persistence
  - `./addons:/mnt/extra-addons`: Local addons mounted into container
  - `./config:/etc/odoo`: Configuration files mounted

### Odoo Configuration (config/odoo.conf)
- Database host: `db` (container name)
- Database credentials: odoo/odoo
- Addons path includes both standard Odoo addons and custom addons from `/mnt/extra-addons/addons`
- Admin password is hashed using pbkdf2-sha512
- Development mode with single worker process
- Database listing is disabled for security

### VSCode Debug Configuration
- Launch configuration available for debugging Odoo server
- Program path: `/usr/bin/odoo`
- Working directory: `/mnt/extra-addons`
- PYTHONPATH includes both standard Odoo libraries and custom addons

## Directory Structure
```
.
├── config/
│   └── odoo.conf          # Odoo server configuration
├── .vscode/
│   └── launch.json        # VSCode debug configuration
├── docker-compose.yml     # Docker services definition
└── addons/                # Custom Odoo addons (to be created)
    └── addons/            # Actual addons directory (referenced in odoo.conf)
```

## Access Points
- **Odoo Web Interface**: http://localhost:8069
- **Database**: localhost:5432 (when containers are running)
- **Admin Credentials**: Configure through web interface on first access

## Important Notes
- The `addons` directory needs to be created for custom Odoo modules
- The addons path in odoo.conf points to `/mnt/extra-addons/addons`, which maps to `./addons/addons` locally
- Configuration changes require container restart
- Database data persists between container restarts via Docker volumes