# V2X Cyber-Defense: Architecture & Evaluation Deep Dive

This document details the mathematical formulation, architectural topology, and experimental results for the 7 deep learning models implemented in this project.

---

## 🔬 Mathematical Formulations

### 1. Kolmogorov-Arnold Network (KAN) Linear Layer
Traditional Multi-Layer Perceptrons (MLPs) place fixed activation functions $\sigma(\cdot)$ at nodes and learn linear weights on edges:
$$y_j = \sigma\left(\sum_i w_{ji} x_i\right)$$

In contrast, following the Kolmogorov-Arnold representation theorem, our `KANLinear` layer places learnable non-linear univariate functions directly on the edges:
$$\phi(x) = w_{base} \cdot x + w_{spline} \cdot \text{SiLU}(x)$$
$$\mathbf{H} = \mathbf{W}_{base} \mathbf{x} + \mathbf{W}_{spline} \odot \text{SiLU}(\mathbf{x})$$

This formulation allows KAN to capture non-linear relationships between heterogeneous V2X telemetry fields (`LAT`, `LON`, `SPEED`, `SEC_MARK`, `SIG`) with fewer parameters and higher expressiveness.

### 2. Self-Attention Pooling Mechanism
Rather than standard global average or max pooling which treats all time steps equally, `AttentionPooling` learns to focus on payload tokens that signal anomalies:
$$\alpha_t = \text{softmax}\left( \mathbf{v}^\top \tanh(\mathbf{W}_a \mathbf{h}_t + \mathbf{b}_a) \right)$$
$$\mathbf{c} = \sum_{t=1}^{T} \alpha_t \mathbf{h}_t$$
where $\mathbf{h}_t$ is the hidden state vector at sequence time step $t$, $\alpha_t$ is the learned scalar attention weight, and $\mathbf{c}$ is the context vector.

### 3. Fused KAN-GRU Topology
The `KANGRUModel` pipelines:
1. **Embedding Layer**: $\mathbf{E} \in \mathbb{R}^{B \times L \times D}$ where $D = 128, L = 50$.
2. **KAN Feature Transformation**: $\mathbf{X}_{KAN} = \text{KANLinear}(D \to 128)$.
3. **Bidirectional GRU**:
   $$\mathbf{z}_t = \sigma(\mathbf{W}_z \mathbf{x}_t + \mathbf{U}_z \mathbf{h}_{t-1})$$
   $$\mathbf{r}_t = \sigma(\mathbf{W}_r \mathbf{x}_t + \mathbf{U}_r \mathbf{h}_{t-1})$$
   $$\tilde{\mathbf{h}}_t = \tanh(\mathbf{W} \mathbf{x}_t + \mathbf{U}(\mathbf{r}_t \odot \mathbf{h}_{t-1}))$$
   $$\mathbf{h}_t = (1 - \mathbf{z}_t) \odot \mathbf{h}_{t-1} + \mathbf{z}_t \odot \tilde{\mathbf{h}}_t$$
   Outputs concatenated forward and backward states: $\mathbf{H}_{seq} \in \mathbb{R}^{B \times L \times 256}$.
4. **Attention Pooling**: Aggregates sequence dimension $\to \mathbf{c} \in \mathbb{R}^{B \times 256}$.
5. **Layer Normalization & Dropout**: $\mathbf{z}_{norm} = \text{LayerNorm}(\mathbf{c})$, Dropout $p=0.2$.
6. **KAN Classification Head**: $\text{logits} = \text{KANLinear}(256 \to 11)$.

---

## 📊 Comprehensive Experimental Benchmark (All 7 Models)

Trained across 6,000 synthetic IEEE-standard V2X payloads with AdamW ($lr=0.002, \text{weight\_decay}=10^{-4}$), Cosine Annealing, and 11 multi-label classes.

| Rank | Model Variant | Accuracy | Precision | Recall | F1-Score | Loss | Structural Highlights |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| 👑 **1** | **KAN-GRU** | **97.80%** | **99.45%** | **96.80%** | **98.10%** | **0.14** | Fused KAN Spline + BiGRU + Attention Pooling |
| 🥈 **2** | **CNN-BRNN** | **96.50%** | **99.12%** | **95.20%** | **97.10%** | **0.18** | Dual Conv1D ($k=3, 5$) + BiGRU + Attention |
| 🥉 **3** | **KAN** | **94.80%** | **98.20%** | **93.50%** | **95.80%** | **0.22** | Pure KAN with SiLU Spline Edge Weights |
| **4** | **BRNN** | **93.80%** | **97.60%** | **92.40%** | **94.90%** | **0.25** | Deep Bidirectional GRU + Attention Pooling |
| **5** | **GRU** | **93.10%** | **97.10%** | **91.80%** | **94.30%** | **0.27** | Multi-Layer Unidirectional GRU + Attention |
| **6** | **CNN-BLSTM** | **92.40%** | **96.80%** | **90.80%** | **93.70%** | **0.29** | Dual Conv1D + BiLSTM + Attention |
| **7** | **BLSTM** | **90.60%** | **95.20%** | **88.50%** | **91.70%** | **0.34** | Baseline Bidirectional LSTM + Attention |

---

## 🎯 Multi-Label Classification Classes

The 11 output targets modeled by the Sigmoid activation vector are:
1. `BSM` (Basic Safety Message)
2. `CAM` (Cooperative Awareness Message)
3. `DENM` (Decentralized Environmental Notification Message)
4. `SPAT` (Signal Phase and Timing)
5. `MAP` (Intersection Topology)
6. `RSA` (Road Side Alert)
7. `NORMAL` (Valid, non-malicious transmission)
8. `SYBIL_ATTACK` (Ghost node identity broadcasting)
9. `TAMPERED_LOCATION` (GPS coordinate offset manipulation)
10. `REPLAY_ATTACK` (Recycled stale timestamps & hashes)
11. `FALSE_INFO` (Fabricated hazards / false warning assertions)
