# Fluentbit Doctor Linux

Fluentbit Doctor Linux simplifies the setup, configuration, and upkeep of Fluent Bit on Linux systems. This toolkit provides Python scripts and a YAML configuration file to streamline installation, automate checks, and optimize Fluent Bit's performance.

## Files Overview

- **configuration.py**: Manages configuration settings for Fluent Bit.
- **connectivity.py**: Validates connectivity crucial for Fluent Bit’s functionality.
- **installation.py**: Automates Fluent Bit installation on Linux.
- **meta_data.py**: Collects and processes metadata for Fluent Bit operations.
- **config.yml**: Contains YAML configurations for Fluent Bit setups.
- **health_checks.py**: Performs health checks to ensure Fluent Bit runs optimally.
- **performance_metrics.py**: Monitors and logs Fluent Bit performance metrics.
- **run.py**: Main executable script integrating all functionalities.

## Getting Started

To begin with Fluentbit Doctor Linux:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-repo/fluentbit-doctor-linux.git
   cd fluentbit-doctor-linux
   ```
2. **Run the main script:**
   ```bash
   python3 run.py
   ```
Ensure Python 3 is installed. Adjust `config.yml` to match your environment's requirements.

## Requirements

- Python 3.6+
- PyYAML (for handling YAML files)

Install required Python packages via pip:

```bash
pip install packagename

```
