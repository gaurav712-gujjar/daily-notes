# Untitled Note - 1330

**Category:** Machine Learning  
**Date:** 2026-11-23 (morning)

---

# Neural Architecture Search

Neural Architecture Search (NAS) automates the design of neural network topologies. Instead of manually choosing the number of layers, types of convolutions, or connectivity patterns, NAS treats the architecture itself as a hyper‑parameter space and searches it with an optimization algorithm (e.g., reinforcement learning, evolutionary strategies, or gradient‑based methods). The goal is to discover high‑performing models within a given computational budget.

**Why use NAS?**  
- **Efficiency:** Saves expert time on trial‑and‑error architecture engineering.  
- **Performance:** Often yields architectures that outperform hand‑crafted baselines on specific tasks (e.g., image classification, language modeling).  
- **Adaptability:** Can tailor models to hardware constraints (latency, memory) by adding cost‑aware objectives.

**Typical workflow**  
1. Define a *search space* (e.g., possible layer types, kernel sizes, skip connections).  
2. Choose a *search strategy* (RL controller, genetic algorithm, differentiable search).  
3. Evaluate sampled architectures on a validation set (often using weight sharing to speed up).  
4. Select the best architecture and train it from scratch.

**Simple example with Keras Tuner (differentiable NAS)**

```python
import tensorflow as tf
from tensorflow import keras
import keras_tuner as kt

def build_model(hp):
    inputs = keras.Input(shape=(32, 32, 3))
    x = inputs
    # search over number of Conv layers and filters
    for i in range(hp.Int('num_layers', 1, 3)):
        filters = hp.Choice(f'filters_{i}', [32, 64, 128])
        kernel = hp.Choice(f'kernel_{i}', [3, 5])
        x = keras.layers.Conv2D(filters, kernel, activation='relu', padding='same')(x)
        if hp.Boolean(f'pool_{i}'):
            x = keras.layers.MaxPooling2D()(x)
    x = keras.layers.Flatten()(x)
    x = keras.layers.Dense(10, activation='softmax')(x)
    model = keras.Model(inputs, x)
    model.compile(
        optimizer=keras.optimizers.Adam(hp.Float('lr', 1e-4, 1e-2, sampling='log')),
        loss='sparse_categorical_crossentropy',
        metrics
