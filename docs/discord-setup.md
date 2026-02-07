# Discord Setup Guide

How to create and configure the Stardew Helper bot in the Discord Developer Portal.

## 1) Create application
- Go to https://discord.com/developers/applications
- New Application → name it “Stardew Helper” (or your variant) → create.
- Branding: add avatar (e.g., green Junimo-like blob), optional banner/description.
- Public? Yes (for invites). No need for message content intent.

## 2) Create Bot user
- In the left navigation: *Bot* → *Add Bot*.
- Copy the Bot Token (store in `.env` and GitHub Secrets, never commit).
- Privileged Intents: leave Message Content disabled. No presence/member intents needed for MVP.

## 3) Permissions
- Scopes: `applications.commands`, `bot`
- Bot permissions: Send Messages, Embed Links, Read Message History (optional), Use Application Commands.
- No admin/mod permissions required.

## 4) Generate invite link
- OAuth2 → URL Generator → select scopes + permissions above.
- Copy the invite URL to add the bot to servers.

## 5) Environment
- Set `DISCORD_TOKEN` in `.env` (and in GitHub Actions secrets for deploys).
- Optional: `GUILD_ID` for faster dev command sync on a single server.
- Optional: `UPDATE_CHANNEL_ID` where deploy notifications should appear.

## 6) Testing commands
- Run locally (`uv run stardew-bot`) and use `/help` in your dev server.
- If commands don’t appear immediately, check the dev guild sync (`GUILD_ID`) and bot permissions.

## 7) Non-affiliation / safety
- Add to the bot description: “Community-made; not affiliated with or endorsed by ConcernedApe.”
- Keep minimal permissions to reassure server admins.
