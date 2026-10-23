
import json
import time
from pathlib import Path
from datetime import datetime

BASELINE = {
    "firewall_enabled": True,
    "mfa_enabled": True,
    "admin_access": False,
    "ssh_root_login": False
}

# Risk Scoring Lens: weighted security risks
RISK_POINTS = {
    "firewall_enabled": 40,
    "mfa_enabled": 35,
    "admin_access": 15,
    "ssh_root_login": 10
}

FILE = Path(__file__).with_name("current_config.json")

def save_config(config):
    FILE.write_text(json.dumps(config, indent=4))

def assess_risk(current):
    findings = []
    score = 0

    for setting, expected in BASELINE.items():
        actual = current.get(setting, "MISSING")

        if actual != expected:
            points = RISK_POINTS[setting]
            score += points
            findings.append((setting, expected, actual, points))

    if score >= 70:
        level = "CRITICAL"
    elif score >= 40:
        level = "HIGH"
    elif score >= 15:
        level = "MEDIUM"
    elif score > 0:
        level = "LOW"
    else:
        level = "SECURE"

    return findings, score, level

def main():
    print("=" * 50)
    print("         DRIFT SENTRY - RISK SCORING LENS")
    print("=" * 50)

    if not FILE.exists():
        save_config(BASELINE)

    print("[OK] Secure baseline loaded")
    print("[OK] Risk scoring enabled")
    print("[OK] Monitoring every 2 seconds\n")

    last_state = None
    cycle = 0

    try:
        while True:
            cycle += 1

            try:
                current = json.loads(FILE.read_text())
                if not isinstance(current, dict):
                    raise ValueError("Configuration must be an object")
            except (ValueError, OSError) as error:
                print("[ERROR]", error)
                time.sleep(2)
                continue

            findings, score, level = assess_risk(current)
            state = (tuple(str(f) for f in findings), score)
            timestamp = datetime.now().strftime("%H:%M:%S")

            if state != last_state:
                print(f"\n[{timestamp}] SECURITY ASSESSMENT")
                print("-" * 50)

                for setting, expected, actual, points in findings:
                    print(f"[DRIFT] {setting}")
                    print(f"  Expected: {expected}")
                    print(f"  Actual:   {actual}")
                    print(f"  Risk Contribution: +{points} points")

                print("\nRISK SCORING LENS")
                print(f"Risk Score: {score}/100")
                print(f"Risk Level: {level}")

                calculation = " + ".join(
                    str(f[3]) for f in findings
                ) or "0"

                print(f"Score Derivation: {calculation} = {score}")

                if findings:
                    print("ALERT: Risky configuration drift detected!")
                else:
                    print("STATUS: Secure baseline maintained")

                last_state = state

            # Automatic demo
            if cycle == 3:
                print("\n[DEMO] Disabling firewall and MFA...")
                current["firewall_enabled"] = False
                current["mfa_enabled"] = False
                save_config(current)

            if cycle == 6:
                print("\n[DEMO] Restoring secure settings...")
                save_config(BASELINE)

            time.sleep(2)

    except KeyboardInterrupt:
        print("\n[STOPPED] Monitoring ended")

if __name__ == "__main__":
    main()
