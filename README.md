# loki-lab-04-template

Template repo for **Lab-04: Babysitting GitHub CI/CD with Loki and Claude Code Skills**.

This is the **CI source**. Fork this into your own GitHub account so workflow runs are billed to you and the repository secrets / webhook point at *your* Poridhi VM.

## Layout

```
.github/
├── workflows/
│   ├── build-and-test.yml   # unit-tests job; flaky test inside
│   ├── deploy-staging.yml   # always-fails on feature/payments
│   └── lint-and-scan.yml    # secret-scan tripwire on commit messages
└── actions/
    └── push-to-loki/
        └── action.yml       # composite action every job calls
src/
└── checkout.py              # tiny module under test
tests/
└── test_checkout.py         # one test is deliberately flaky (~15%)
pyproject.toml               # pytest pythonpath config
requirements.txt             # pytest
```

## Required repository secrets

Set these in **Settings → Secrets and variables → Actions → New repository secret**:

| Name | Value |
|---|---|
| `LOKI_URL` | `https://<your-poridhi-public-url>/loki/api/v1/push` |
| `LOKI_USER` | The user printed by `setup.sh` on the VM (default: `ci`) |
| `LOKI_PASSWORD` | The password printed by `setup.sh` on the VM |

Without these, the composite action emits a workflow warning and skips the push (the rest of the workflow still runs).

## Required webhook

Add one webhook in **Settings → Webhooks**:

- **Payload URL**: `https://<your-poridhi-public-url>/webhook`
- **Content type**: `application/json`
- **Secret**: the `WEBHOOK_SECRET` printed by `setup.sh` on the VM
- **Events**: select **Workflow runs** and **Workflow jobs** only

## Built-in failure modes

| Where | Failure | Trigger |
|---|---|---|
| `tests/test_checkout.py::test_total_flaky` | ~15% random fail | Just push commits — flakes accumulate |
| `deploy-staging.yml` | Deterministic exit 1 | Push to `feature/payments` |
| `build-and-test.yml::install-deps` | +8s sleep | Any branch matching `feature/*` |
| `lint-and-scan.yml::secret-scan` | exit 1 | Commit message contains `TODO: api_key` |

These are the four shapes the Claude Code Skills in `loki-lab-04-code` are written to find.
# notes
# notes
# notes
