# Positional Encoding in Transformers

**Category:** AI/ML Concepts  
**Date:** 2026-09-26 (afternoon)

---

# Positional Encoding in Transformers

Transformers process sequences without recurrence, relying on self‑attention to relate tokens. However, self‑attention alone is permutation‑invariant; it cannot distinguish *where* a token appears. Positional encoding injects deterministic or learned vectors that represent each token’s position, allowing the model to capture order information.

Two common schemes are:

* **Sinusoidal encoding** – uses sine and cosine functions of varying frequencies, ensuring that any relative offset can be expressed as a linear combination of encodings.
* **Learned embeddings** – treats positions like vocabulary items, learning a unique vector for each index during training.

These encodings are added to the token embeddings before feeding them to the attention layers. In practice, positional encodings are crucial for tasks such as language modeling, machine translation, and time‑series forecasting where order matters.

```python
import torch
import math

def sinusoidal_pos_enc(seq_len, d_model):
    """Return [seq_len, d_model] sinusoidal positional encodings."""
    pos = torch.arange(seq_len).unsqueeze(1)          # (seq_len, 1)
    i   = torch.arange(d_model).unsqueeze(0)         # (1, d_model)
    angle_rates = 1 / (10000 ** (2 * (i // 2) / d_model))
    angle_rads = pos * angle_rates                    # (seq_len, d_model)

    # apply sin to even indices, cos to odd indices
    enc = torch.zeros_like(angle_rads)
    enc[:, 0::2] = torch.sin(angle_rads[:, 0::2])
    enc[:, 1::2] = torch.cos(angle_rads[:, 1::2])
    return enc

# Example usage
seq_len, d_model = 10, 64
pos_enc = sinusoidal_pos_enc(seq_len, d_model)  # (10, 64)
```

The resulting matrix can be added to token embeddings (`emb + pos_enc`) to provide each token with a sense of its position in the sequence.
