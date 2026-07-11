#### Backtesting Value‑at‑Risk (VaR) Estimation Methods for Energy Commodity Trading

📈 Overview
This repository provides a complete, production‑ready implementation of the research paper 

*Backtesting of Value at Risk Estimation Methods for Energy Commodity Trading: Evaluating Performance and Identifying the Optimal Approach*

It delivers an end‑to‑end workflow for:

- Natural Gas price ingestion (NYMEX NG & TTF)
- LSTM‑based forward price forecasting
- Multiple VaR estimation engines
- Comprehensive backtesting (QPS, Kupiec)
- Sensitivity analysis across horizons & confidence levels
- Automated reporting & CLI execution

This project is designed for quantitative researchers, energy traders, risk managers, and developers building real‑world risk analytics systems.

🚀 Key Features
Modular, extensible architecture

Config‑driven execution using YAML

LSTM forecasting pipeline for forward curves

Three VaR engines:

Variance–Covariance

Historical Simulation

Monte Carlo Simulation

Backtesting suite:

Quadratic Probability Score (QPS)

Exception counting

Kupiec test

Sensitivity analysis across:

Confidence levels (95%, 99%)

Horizons (1‑day, 10‑day)

Portfolio compositions

CLI automation for reproducibility

Full test suite for reliability

📁 Repository Structure

energy-var-backtesting/\
├── README.md\
├── pyproject.toml\
├── config/\
│   ├── base.yaml\
│   ├── data.yaml\
│   ├── model_lstm.yaml\
│   ├── var.yaml\
│   └── backtest.yaml\
├── data/\
│   ├── raw/\
│   ├── interim/\
│   └── processed/\
├── notebooks/\
│   ├── 01_exploratory_data_analysis.ipynb\
│   ├── 02_lstm_forward_price_demo.ipynb\
│   └── 03_var_method_comparison.ipynb\
├── src/\
│   ├── energy_var_backtesting/\
│   │   ├── data/\
│   │   ├── models/\
│   │   ├── risk/\
│   │   ├── backtesting/\
│   │   ├── cli/\
│   │   └── reports/\
├── tests/\
└── scripts/


#### License
This project is licensed under the [MIT License](LICENSE).  

