# Security Policy

## Supported Versions
This project is experimental. Security fixes are handled on a best-effort basis on `main` and the latest tagged release.

## Reporting a Vulnerability
- Please mail security reports to the repository maintainers or open a private security advisory on GitHub.
- Do not disclose vulnerabilities publicly until a fix is available.
- Include reproduction steps, impact, and suggested mitigations when possible.

## Secrets & Tokens
- Never commit Discord tokens or API keys.
- Use local `.env` files for development; use GitHub Secrets for CI/CD.
- Oracle VM deployments should keep secrets in the server `.env` or secure secret stores, not in the repository.

## Discord App Permissions
- Minimal permissions: Send Messages, Embed Links, Read Message History (optional), Use Application Commands.
- No message content intent is required or enabled by default.
