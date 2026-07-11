#!/usr/bin/env bash
set -e

# Example pipeline: download data -> run LSTM -> run VaR -> backtest -> sensitivity
bash scripts/download_data.sh

python -m src.energy_var_backtesting.cli.main run-lstm \
  --base-cfg config/base.yaml \
  --data-cfg config/data.yaml \
  --lstm-cfg config/model_lstm.yaml

python -m src.energy_var_backtesting.cli.main run-var \
  --base-cfg config/base.yaml \
  --data-cfg config/data.yaml \
  --var-cfg config/var.yaml

python -m src.energy_var_backtesting.cli.main run-backtest \
  --base-cfg config/base.yaml \
  --data-cfg config/data.yaml \
  --var-cfg config/var.yaml \
  --backtest-cfg config/backtest.yaml

python -m src.energy_var_backtesting.cli.main run-sensitivity \
  --base-cfg config/base.yaml \
  --data-cfg config/data.yaml \
  --var-cfg config/var.yaml \
  --backtest-cfg config/backtest.yaml
