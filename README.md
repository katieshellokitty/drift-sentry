# 🛡️ Drift Sentry

### Python-Based Security Configuration Monitoring

A cybersecurity project developed for the **Build or Bust** challenge.

Drift Sentry is a Python-based security monitoring prototype designed to detect risky configuration changes early and calculate their potential security impact.

## Features

- 🔍 Automatic configuration drift detection
- 🛡️ Secure baseline comparison
- ⏱️ Monitoring every 2 seconds
- 🚨 Security risk alerts
- 📊 Weighted risk scoring (0–100)
- ✅ Detection of restored security settings

## Risk Scoring Lens

Each security issue contributes to the overall risk score.

| Security Risk | Points |
|---|---:|
| Firewall disabled | 40 |
| MFA disabled | 35 |
| Unauthorized admin access | 15 |
| SSH root login enabled | 10 |

**Example:**

Firewall Disabled (+40) + MFA Disabled (+35) = **75/100 — Critical Risk**

## Technologies

- Python
- JSON
- Visual Studio Code

## How to Run

1. Download the project.
2. Open the project folder in VS Code.
3. Run:

```bash
python drift_sentry.py
```

4. Observe the simulated security changes and risk alerts.

## Project Results

Drift Sentry successfully demonstrated:

- Detection of risky configuration changes
- Automatic risk score calculation
- Transparent score derivation
- Recovery detection when settings return to normal

## Future Improvements

- Monitor real operating system security settings
- Add a web-based dashboard
- Implement email notifications
- Store historical security alerts
- Protect baseline configurations against unauthorized changes

## Disclaimer

This project is a proof of concept using simulated security configuration data. It does not currently monitor or modify actual firewall, MFA, or system permissions.

---

Developed by Katie & Luca
