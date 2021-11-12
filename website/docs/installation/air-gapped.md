---
title: Air-gapped environments
---

## Outbound connections

By default, authentik creates outbound connections to the following URLs:

- https://version.goauthentik.io: Periodic update check
- https://goauthentik.io: Anonymous analytics on startup
- https://secure.gravatar.com: Avatars for users
- https://sentry.beryju.org: Error reporting

To disable these outbound connections, set the following in your `.env` file:

```
AUTHENTIK_DISABLE_UPDATE_CHECK=true
AUTHENTIK_ERROR_REPORTING__ENABLED=false
AUTHENTIK_DISABLE_STARTUP_ANALYTICS=true
AUTHENTIK_AVATARS=none
```

For a Helm-based install, set the following in your values.yaml file:

```yaml
authentik:
    avatars: none
    error_reporting:
        enabled: false
    disable_update_check: true
    disable_startup_analytics: true
```

## Container images

Container images can be pulled from the following URLs:

- goauthentik.io/server (https://goauthentik.io)
- ghcr.io/goauthentik/server (https://ghcr.io)
- beryju/authentik (https://index.docker.io)