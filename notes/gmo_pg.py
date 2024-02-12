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
