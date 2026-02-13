// Replace placeholders once you have real IDs/URLs
const INVITE_URL = 'https://discord.com/api/oauth2/authorize?client_id=YOUR_CLIENT_ID&permissions=274877910016&scope=bot%20applications.commands';
const REPO_URL = 'https://github.com/etondo/stardew-discord-bot';
const SETUP_URL = 'https://github.com/etondo/stardew-discord-bot/blob/master/docs/getting-started.md';

document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('[data-href="invite"]').forEach(el => el.href = INVITE_URL);
  document.querySelectorAll('[data-href="repo"]').forEach(el => el.href = REPO_URL);
  document.querySelectorAll('[data-href="setup"]').forEach(el => el.href = SETUP_URL);
});
