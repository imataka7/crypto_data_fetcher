# %%

import sys

sys.path.append("../")

# %%

from crypto_data_fetcher.gmo import GmoFetcher

# %%

import joblib

# %%

memory = joblib.Memory("/tmp/gmo_fetcher_cache", verbose=0)
fetcher = GmoFetcher(memory=memory)
# %%

import pandas as pd

# %%

date = pd.to_datetime("2023-02-11")
date

# %%

market = "BTC_JPY"

# %%

df = fetcher.fetch_trade_csv(market, date)

# %%

df
# %%

interval_sec = 15 * 60  # 15 minutes

# %%

df = fetcher.to_ohlcv(df, interval_sec)
# %%

df
# %%
