# 🛡️ Mini SIEM Log Monitoring with Wazuh

A minimal Security Information and Event Management (SIEM) demo using Wazuh for log monitoring and alert parsing.

## 🔍 Features
- Wazuh installation guide for single-node
- Sample logs from `/var/log/auth.log`
- Custom JSON alerts for simulation/testing
- Python script to parse Wazuh alerts for basic reporting

## 📁 Structure

- `log-sample/` – Example logs and alerts
- `scripts/` – Python tools to parse and analyze logs
- `wazuh-installation.md` – Installation and config guide

## 🚀 Getting Started

1. Install Wazuh using `wazuh-installation.md`
2. Copy logs into `/var/ossec/logs/`
3. Run `parse_alerts.py` to extract and analyze important alerts
   (python3 parse_alerts.py --live --csv <name>.csv) (result in csv)

## ⚠️ Disclaimer

This is a learning project and not intended for production use
