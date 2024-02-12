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

# df2 = fetcher.to_ohlcv(df, interval_sec)
# df2
# %%

# df["timestamp"] = df["timestamp"].dt.floor("{}S".format(interval_sec))
# ohlcv = pd.concat(
#     [
#         df.groupby("timestamp")["price"].nth(0).rename("op"),
#         df.groupby("timestamp")["price"].max().rename("hi"),
#         df.groupby("timestamp")["price"].min().rename("lo"),
#         df.groupby("timestamp")["price"].nth(-1).rename("cl"),
#         df.groupby("timestamp")["size"].sum().rename("volume"),
#     ],
#     axis=1,
# )

df["timestamp"].dt.floor("{}S".format(interval_sec))

# %%

df["timestamp"]

# %%

df_raw = df.copy()

# %%

# df.set_index("timestamp", inplace=True)

# %%

# df.groupby("timestamp").resample("15T").ohlc()
df["timestamp"] = df["timestamp"].dt.floor("{}S".format(interval_sec))

# %%

df

# %%

df.groupby("timestamp")["price"].ohlc()

# %%

df.groupby("timestamp")["size"].sum().rename("volume")
# %%

df.set_index("timestamp", inplace=True)
# %%

x = pd.concat(
    [
        df.groupby("timestamp")["price"].ohlc(),
        df.groupby("timestamp")["size"].sum().rename("volume"),
    ],
    axis=1,
)
x

# %%
y = x.rename(columns={"open": "op", "high": "hi", "low": "lo", "close": "cl"})
y
# %%
