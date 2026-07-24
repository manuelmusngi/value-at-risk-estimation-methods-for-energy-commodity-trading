#### Backtesting Value‑at‑Risk (VaR) Estimation Methods for Energy Commodity Trading

📈 Overview

This repository provides a complete, production‑ready implementation of the research paper: 

*Backtesting of Value at Risk Estimation Methods for Energy Commodity Trading: Evaluating Performance and Identifying the Optimal Approach*

It delivers an end‑to‑end workflow for:

- Natural Gas price ingestion (NYMEX NG & TTF)
- LSTM‑based forward price forecasting
- Multiple VaR estimation engines
- Comprehensive backtesting (QPS, Kupiec)
- Sensitivity analysis across horizons & confidence levels
- Automated reporting & CLI execution

This project is designed for quantitative researchers, energy traders, risk managers, and developers building real‑world risk analytics systems.

🚀 Key Feature

- Modular, extensible architecture
- Config‑driven execution using YAML
- LSTM forecasting pipeline for forward curves
- Three VaR engines:
  - Variance–Covariance
  - Historical Simulation
  - Monte Carlo Simulation
- Backtesting suite:
  - Quadratic Probability Score (QPS)
  - Exception counting
  - Kupiec test
- Sensitivity analysis across:
  - Confidence levels (95%, 99%)
  - Horizons (1‑day, 10‑day)
  - Portfolio compositions
- CLI automation for reproducibility
- Full test suite for reliability

📁 Project Architecture

energy-var-backtesting/\
├── README.md\
├── pyproject.toml            # or setup.cfg / requirements.txt\
├── .env.example              # environment variables template\
├── config/\
│   ├── base.yaml             # base configuration\
│   ├── data.yaml             # data sources, paths\
│   ├── model_lstm.yaml       # LSTM hyperparameters\
│   ├── var.yaml              # VaR settings (confidence, horizon)\
│   └── backtest.yaml         # backtesting & sensitivity settings\
├── data/\
│   ├── raw/\
│   │   ├── nymex_ng.csv\
│   │   └── ttf_ng.csv\
│   ├── interim/\
│   └── processed/\
├── notebooks/\
│   ├── 01_exploratory_data_analysis.ipynb\
│   ├── 02_lstm_forward_price_demo.ipynb\
│   └── 03_var_method_comparison.ipynb\
├── src/\
│   ├── energy_var_backtesting/\
│   │   ├── __init__.py\
│   │   ├── config.py\
│   │   ├── logging_utils.py\
│   │   ├── data/\
│   │   │   ├── loader.py\
│   │   │   ├── preprocessing.py\
│   │   │   └── portfolio_builder.py\
│   │   ├── models/\
│   │   │   ├── lstm_model.py\
│   │   │   └── lstm_pipeline.py\
│   │   ├── risk/\
│   │   │   ├── var_base.py\
│   │   │   ├── var_variance_covariance.py\
│   │   │   ├── var_historical.py\
│   │   │   ├── var_monte_carlo.py\
│   │   │   └── sensitivity.py\
│   │   ├── backtesting/\
│   │   │   ├── qps.py\
│   │   │   ├── exceptions.py\
│   │   │   └── runner.py\
│   │   ├── cli/\
│   │   │   ├── main.py\
│   │   │   └── commands/\
│   │   │       ├── run_lstm.py\
│   │   │       ├── run_var.py\
│   │   │       ├── run_backtest.py\
│   │   │       └── run_sensitivity.py\
│   │   └── reports/\
│   │       ├── plots.py\
│   │       └── summary.py\
├── tests/\
│   ├── test_data_loader.py\
│   ├── test_lstm_model.py\
│   ├── test_var_methods.py\
│   ├── test_qps.py\
│   └── test_backtest_runner.py\
└── scripts/\
    ├── download_data.sh\
    └── run_all.sh\

📚 Research Reference

- [Backtesting of value at risk estimation methods for energy commodity trading: evaluating performance and identifying the optimal approach](https://www.researchgate.net/publication/384365458_Backtesting_of_value_at_risk_estimation_methods_for_energy_commodity_trading_evaluating_performance_and_identifying_the_optimal_approach)

#### License
This project is licensed under the [MIT License](LICENSE).  

