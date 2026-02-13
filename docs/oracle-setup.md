# Oracle Cloud (Always Free) Setup

This guide assumes you already have an Oracle Cloud account and will deploy Stardew Helper on an Always Free VM (Ampere A1). Repo default branch: `master`.

## 1) Create the VM
- Choose **Ampere A1** (ARM) with the Always Free shape.
- OS: Ubuntu/Debian preferred (supports Docker easily).
- Open ports in security lists: `22/tcp` (SSH), `443/tcp` (if reverse proxy), optional `80/tcp`.

## 2) Harden the VM
- Create an SSH keypair; disable password SSH.
- Keep the system updated:
  ```bash
  sudo apt-get update && sudo apt-get upgrade -y
  ```
- Optional: set up a non-root deploy user with `docker` group membership.

## 3) Install Docker + docker compose plugin
```bash
sudo apt-get install -y ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

## 4) Prepare deployment directory
```bash
sudo mkdir -p /opt/stardew-bot
sudo chown $USER:$USER /opt/stardew-bot
cd /opt/stardew-bot
```

Place these files (synced from the repo or copied manually, branch `master`):
- `docker-compose.yml`
- `.env` (never commit this; fill with Discord token, logging, locale, etc.)

## 5) Test locally on the VM
```bash
cd /opt/stardew-bot
docker compose pull   # once images are published
docker compose up -d
docker compose logs -f
```

## 6) Discord Bot Setup (one-time)
- Create an application at https://discord.com/developers/applications
- Add a Bot user, copy the token (store in `.env` and GitHub Secrets).
- Scopes: `bot`, `applications.commands`
- Permissions: Send Messages, Embed Links, Read Message History (optional), Use Application Commands
- No Message Content Intent required.

## 7) Security reminders
- Keep the VM firewall/security lists tight (SSH + proxy ports only).
- Rotate the bot token if leaked.
- Keep `.env` permissions restrictive (`chmod 600 .env`).
- Enable automatic security updates if possible.
