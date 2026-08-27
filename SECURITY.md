# Security and Public-Safety Policy

Visual Presentation Studio's public distribution must not be used to store or exchange credentials, private project material, or sensitive personal/professional information.

## Reporting a possible security problem

Do not report secrets by pasting them into a public issue, pull request, discussion, screenshot, or comment.

If you discover a credential or other sensitive value, describe the **type of exposure and safe file/path reference only**. Do not quote the value. The repository owner can then coordinate remediation through an appropriate private channel.

## What must never be committed

- passwords, API keys, tokens, session cookies, SSH/private keys, PEM/private keys, signing keys, cloud/database credentials, or credential-bearing connection strings;
- `.env` files containing real values or credential-store configuration;
- private presentations, documents, screenshots, source assets, datasets, prompts, transcripts, logs, or evaluation evidence;
- private professional identities/data, internal identifiers, private personal data, or non-public endpoints;
- material of unknown provenance or rights when public redistribution cannot be established.

`SECRET` and `UNKNOWN` classifications fail closed.

## If an exposure occurs

Treat a committed credential as compromised. Stop release activity, rotate or revoke the credential, remove the exposure safely (including public history when applicable), and re-run the complete public-safety audit before proceeding.

For private information that is not a credential, stop release activity until it has been removed from all public surfaces and the remaining content has passed semantic review.

## Defense in depth

Automated scanning catches common secret-shaped content and risky file classes, but a clean scan does not prove that content is semantically safe. Human review of provenance, context, and confidentiality remains required.
