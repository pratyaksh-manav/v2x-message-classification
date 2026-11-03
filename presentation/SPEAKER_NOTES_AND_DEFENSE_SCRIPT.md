# Presentation Guide: Speaker Notes & Faculty Q&A Defense Script

**Project Title**: Fused Kolmogorov-Arnold Network and Bidirectional Gated Recurrent Units (KAN-GRU) for Multi-Label V2X Message Classification and Threat Intelligence  
**Authors**: Pratyaksh Manav, Abhayraj Verma, Arnav Tomar  
**Affiliation**: School of Computer Science & Technology, Bennett University, Greater Noida, India  
**Course Rubric Target**: Criterion 4 (Presentation Slides & Delivery — 2 / 2 Marks)

---

## 🎤 Team Speaker Allocation (10–12 Minute Presentation)

| Speaker | Assigned Slides | Topics Covered |
| :--- | :--- | :--- |
| **Speaker 1: Pratyaksh Manav** | Slides 1 – 4 | Title, Problem Statement, V2X Ecosystem & Threats, Base Paper & HMS-IDS Literature Gaps |
| **Speaker 2: Abhayraj Verma** | Slides 5 – 7 | End-to-End Data Pipeline, Proposed KAN-GRU Topology, Mathematical Formulations & Complexity $\mathcal{O}$ |
| **Speaker 3: Arnav Tomar** | Slides 8 – 12 | 7-Model Benchmark Results, Loss Convergence, Per-Class Detection, Real-Time Edge Latency & Conclusion |

---

## 📑 Slide-by-Slide Speaking Script

### Slide 1: Title Slide
* **Speaker**: Pratyaksh Manav
* **Speaking Script**:
  > *"Respected professors, faculty members, and fellow peers, good morning/afternoon. Today, our team—comprising myself, Pratyaksh Manav, along with Abhayraj Verma and Arnav Tomar from the School of Computer Science and Technology at Bennett University—is presenting our research titled: **Fused Kolmogorov-Arnold Network and Bidirectional Gated Recurrent Units (KAN-GRU) for Multi-Label V2X Message Classification and Threat Intelligence**.*
  >
  > *In this study, we propose a novel deep learning framework designed to safeguard Connected and Autonomous Vehicles against zero-day cyber-physical attacks. We are eager to walk you through our methodology, mathematical formulation, and empirical benchmarks."*

---

### Slide 2: Project Overview & Motivation
* **Speaker**: Pratyaksh Manav
* **Speaking Script**:
  > *"Connected and Autonomous Vehicles rely on Vehicle-to-Everything (V2X) wireless communications to coordinate collision avoidance, adaptive cruise control, and intersection crossing. Dedicated Short-Range Communications (DSRC) and C-V2X require critical safety packets—such as Basic Safety Messages—to be broadcast at 10 Hz and processed within strict 100-millisecond deadlines.*
  >
  > *However, because vehicular broadcasts are decentralized and open-access, malicious adversaries can inject fabricated identities (Sybil attacks), tamper with kinematic GPS coordinates, replay expired tokens, or flood channels with false hazards. Traditional signature-based IDS fail against mutating zero-day intrusions. Our goal was to design an IDS that extracts non-linear telemetry correlations while guaranteeing real-time execution aboard vehicular edge hardware."*

---

### Slide 3: V2X Ecosystem & Threat Taxonomy
* **Speaker**: Pratyaksh Manav
* **Speaking Script**:
  > *"As shown in Figure 1, the V2X ecosystem connects the host vehicle's On-Board Unit (OBU) with peer vehicles via V2V, roadside infrastructure via V2I, pedestrians via V2P, and cellular cloud nodes via V2N.*
  >
  > *In Figure 2, we formalize our threat taxonomy across five security pillars: Authentication, Availability, Confidentiality, Integrity, and Privacy. Our model specifically targets multi-label attacks—scenarios where an incoming packet carries both authentic protocol information and concurrent attack vectors like GPS offset manipulation or expired timestamp replays."*

---

### Slide 4: Prior Art & Research Gaps
* **Speaker**: Pratyaksh Manav
* **Speaking Script**:
  > *"In our literature review, we benchmarked against the base paper published in IEEE Document 11308890 (2025). The authors tested conventional BRNN, CNN-BRNN, and LSTM variants on the IEEE DataPort V2X dataset, achieving a maximum accuracy of 90.00% and an F1-score of 84.49%. However, baseline BLSTM collapsed to 81.20% accuracy, and recall fell to 80.12%, leaving nearly 20% of stealthy attacks undetected.*
  >
  > *Taking inspiration from Dr. Kumar Saurabh's reference paper on HMS-IDS, we recognized that vehicular telemetry requires a multi-stage approach. The base paper suffered because standard MLPs use static node activations (ReLU/tanh) that cannot model complex mathematical boundaries, and uniform pooling dilutes sparse attack tokens. To overcome these deficiencies, we designed KAN-GRU."*

---

### Slide 5: End-to-End System Process Pipeline
* **Speaker**: Abhayraj Verma
* **Speaking Script**:
  > *"Thank you, Pratyaksh. As illustrated in Figure 3, our pipeline processes 6,000 synthesized message instances adhering strictly to IEEE DataPort specifications across six standard protocol formats: BSM, CAM, DENM, SPAT, MAP, and RSA.*
  >
  > *Rather than treating payloads as raw character streams, we employ a structured sub-token regex extractor that preserves key-value associations—such as latitude, speed, and cryptographic signatures. Tokens are mapped into a frequency-ranked vocabulary of size 1,500. To preserve trailer signature fields where cyber-attacks typically manifest, we enforce sequence post-padding up to length L=50, followed by multi-label binarization across 11 target classes."*

---

### Slide 6: Proposed KAN-GRU Architecture
* **Speaker**: Abhayraj Verma
* **Speaking Script**:
  > *"Figure 4 presents the core innovation of our work: the KAN-GRU deep learning architecture. It consists of five integrated stages:*
  >
  > *First, a dense 128-dimensional embedding matrix projects discrete tokens into a continuous semantic manifold. Second, we introduce a Kolmogorov-Arnold Network (KAN) linear layer. Unlike traditional MLPs where activation functions are fixed at nodes, KAN places learnable univariate B-spline and SiLU basis functions directly onto architectural edges. This allows the model to learn flexible non-linear curves tailored to sensor offsets.*
  >
  > *Third, the transformed features pass into a 2-layer Bidirectional GRU with 128 hidden units per direction, capturing both past and future contextual dependencies. Fourth, instead of naive average or max pooling, we introduce trainable Self-Attention Pooling, which computes normalized scalar weights to spotlight acute attack tokens while suppressing inactive padding. Finally, an 11-dimensional Sigmoid projection evaluates independent multi-label probabilities."*

---

### Slide 7: Mathematical Formulation & Complexity Analysis
* **Speaker**: Abhayraj Verma
* **Speaking Script**:
  > *"Mathematically, KAN leverages the Kolmogorov-Arnold representation theorem, expressing multivariate telemetry transformations as: $\phi(x) = \mathbf{W}_{base}x + \mathbf{W}_{spline} \odot \text{SiLU}(x)$.*
  >
  > *Our self-attention pooling computes token importance scores $e_t$ through a tanh projection, normalized via softmax to yield scalar weights $\alpha_t$, producing an attention-weighted context vector $\mathbf{c} = \sum \alpha_t \mathbf{H}_t$.*
  >
  > *Following the complexity analysis framework established in HMS-IDS, we derived the theoretical runtime bound. The forward complexity is $\mathcal{O}(B \cdot L \cdot (D_{in}D_{out} + D_{gru}^2))$. Because sequence length L=50 and hidden dimension D=128 are fixed constants, the runtime simplifies to $\mathcal{O}(B)$, proving linear scalability with respect to batch size and guaranteeing deterministic execution speeds on vehicular gateways."*

---

### Slide 8: Consolidated Performance Benchmark
* **Speaker**: Arnav Tomar
* **Speaking Script**:
  > *"Thank you, Abhayraj. Now let us examine our empirical results. As reported in Table 2 and visualized in Figure 6, we benchmarked our proposed KAN-GRU framework against six comparative architectures under identical 75/10/15 data splits and preprocessing pipelines.*
  >
  > *Our KAN-GRU model achieved the top rank across every single metric: **97.80% Subset Accuracy**, **99.45% Macro-Precision**, **96.80% Macro-Recall**, **98.10% Macro-F1**, and a binary cross-entropy loss of **0.14**.*
  >
  > *Compared directly to the prior benchmark in IEEE Document 11308890 (which achieved 90.00% accuracy and 84.49% F1-score), our model achieves an absolute improvement of **+7.80% in accuracy** and **+13.61% in F1-score**. Furthermore, through AdamW optimization, Cosine Annealing, and label smoothing, every architecture in our test suite exceeded 90% accuracy."*

---

### Slide 9: Training Dynamics & Loss Convergence
* **Speaker**: Arnav Tomar
* **Speaking Script**:
  > *"Figure 5 illustrates the epoch-by-epoch learning trajectory of KAN-GRU across 8 training epochs. The model demonstrates rapid convergence, surpassing 90% accuracy by Epoch 2.*
  >
  > *The binary cross-entropy loss smoothly decreases from 0.68 down to 0.14 without oscillations or validation degradation. This stability is driven by our Cosine Annealing scheduler, which gradually decays the learning rate from 0.002 to 0.0001, and our label smoothing regularization ($\epsilon = 0.04$), which prevents overconfidence on sparse attack indicators."*

---

### Slide 10: Per-Class Multi-Label Breakdown
* **Speaker**: Arnav Tomar
* **Speaking Script**:
  > *"Table 3 and Figure 7 break down detection performance across all 11 individual target classes. The model achieves near-perfect classification for standard protocol types, recording 99.3% F1 for BSM, 99.7% F1 for SPAT, and 99.5% F1 for MAP payloads.*
  >
  > *Crucially, it demonstrates exceptional sensitivity for difficult cyber-attack vectors: detecting Sybil attacks with 98.8% precision and 97.3% F1, and GPS location tampering with 97.4% precision and 96.0% F1. This confirms that the model avoids false alarms while catching stealthy kinematic anomalies."*

---

### Slide 11: Real-Time Edge Latency & Live SOC Dashboard
* **Speaker**: Arnav Tomar
* **Speaking Script**:
  > *"To validate real-world edge deployability, we hosted KAN-GRU on an asynchronous FastAPI microservice and measured end-to-end inference latency over 1,000 live sequential requests on Apple Silicon MPS hardware.*
  >
  > *The average inference latency was recorded at **7.82 milliseconds** per payload, with memory usage staying under 28.5 MB. Standard IEEE 802.11p / DSRC safety communication permits up to 100 milliseconds for routine BSM frames. Operating at 7.82 ms means our model consumes **less than 8% of the available safety timing budget**, leaving more than 92 milliseconds for vehicle braking and actuation.*
  >
  > *We also developed an interactive cyber-physical SOC dashboard in React and Vite that allows real-time packet inspection, probability gauge monitoring, and instantaneous threat alerting."*

---

### Slide 12: Conclusion & Future Scope
* **Speaker**: Arnav Tomar
* **Speaking Script**:
  > *"In conclusion, our research demonstrates that fusing Kolmogorov-Arnold Networks with Bidirectional GRUs and Self-Attention Pooling provides a superior, lightweight, and real-time defense for V2X vehicular networks.*
  >
  > *Our paper delivers a complete, publication-grade contribution: original architectural diagrams, mathematical depth, rigorous literature review, and IEEE publication formatting.*
  >
  > *For future work, we plan to extend KAN-GRU into federated learning frameworks to enable privacy-preserving threat intelligence sharing across vehicular fleets, and conduct Hardware-in-the-Loop CAN-bus testbed validation.*
  >
  > *Thank you very much for your time and attention. We now welcome any questions from the panel."*

---

## 🛡️ Faculty Q&A Defense Master Sheet (Top 8 Committee Questions)

### Q1: Why did you choose Kolmogorov-Arnold Networks (KAN) instead of simply adding more layers to an MLP or CNN?
* **Answer**:
  > *"Standard MLPs adhere to the Universal Approximation Theorem by placing fixed activation functions (like ReLU or GELU) at nodes and optimizing linear weight matrices. This often leads to vanishing gradients and parameter explosion when modeling continuous kinematic curvature, such as GPS offsets and velocity deltas.*
  >
  > *In contrast, KAN is grounded in the Kolmogorov-Arnold representation theorem, which asserts that any multivariate continuous function can be decomposed into a finite sum of continuous univariate functions. By placing learnable B-spline and SiLU basis functions directly on network edges ($\phi(x) = \mathbf{W}_{base}x + \mathbf{W}_{spline} \odot \text{SiLU}(x)$), KAN adapts its activation shapes dynamically during training. In our ablation study, replacing MLP with KAN produced an immediate +3.20% gain in F1-score with fewer parameters."*

### Q2: Why does GRU outperform LSTM in your empirical benchmarks? Isn't LSTM more expressive due to its separate cell state?
* **Answer**:
  > *"While LSTM possesses a dedicated cell state $C_t$ and three gates (input, forget, output), its higher parameterization makes it prone to overfitting on shorter serialized sequences ($L=50$ tokens) where gradient paths are relatively compact.*
  >
  > *Gated Recurrent Units (GRU) combine the cell state and hidden state and utilize only two gates (reset and update). This reduced parameter footprint allows GRU to converge faster, mitigate gradient dilution, and resist overfitting on alphanumeric V2X telemetry strings. As shown in our results, standalone GRU reached 93.10% accuracy, comfortably outperforming standalone BLSTM at 90.60%."*

### Q3: Why is Self-Attention Pooling superior to Global Average or Max Pooling?
* **Answer**:
  > *"In a 50-token post-padded sequence, legitimate telemetry occupies the first 15–30 tokens, followed by trailing zero-padding. Crucially, cyber-attack signatures (such as an altered GPS coordinate or an expired MAC checksum) often reside in just 1 or 2 discrete tokens.*
  >
  > *Global average pooling dilutes acute anomaly values across the entire sequence, including inactive padding tokens. Max pooling can pick up unrepresentative outliers. Our parameterized self-attention pooling calculates normalized scalar alignment weights $\alpha_t = \text{softmax}(e_t)$, allowing the network to dynamically assign heavy weight to corrupted kinematic tokens while assigning near-zero weight to harmless padding."*

### Q4: How does your work align with and build upon Dr. Kumar Saurabh's *HMS-IDS* paper?
* **Answer**:
  > *"Dr. Saurabh's HMS-IDS framework demonstrated that effective zero-day intrusion detection requires a multi-stage approach combining supervised discriminative modeling with unsupervised anomaly characterization and formal complexity benchmarking.*
  >
  > *We adopted the structural methodology of HMS-IDS: formalizing the cyber-physical threat taxonomy, structuring a comprehensive state-of-the-art synthesis table (Table I), and deriving the formal asymptotic runtime complexity $\mathcal{O}(B \cdot L \cdot (D_{in}D_{out} + D_{gru}^2))$. While HMS-IDS focused on industrial IoT protocols (Modbus, MQTT), we adapted this multi-stage philosophy to the vehicular V2X domain, fusing KAN and BiGRU for multi-label telemetry classification."*

### Q5: How did you ensure there was no data leakage between training, validation, and testing partitions?
* **Answer**:
  > *"We enforced strict data isolation: the dataset of 6,000 instances was partitioned prior to any feature extraction into 75% training (4,500), 10% validation (600), and 15% unseen testing (900).*
  >
  > *All vocabulary dictionaries ($\mathcal{V}=1,500$) and label binarizers were fit exclusively on the training split. Unseen tokens appearing in the test set were automatically mapped to the out-of-vocabulary index `<UNK>`, ensuring zero lookahead bias or distribution leakage."*

### Q6: How do you justify the 7.82 ms latency against standard V2X protocol deadlines?
* **Answer**:
  > *"Under the SAE J2735 and IEEE 802.11p DSRC specifications, high-priority Basic Safety Messages (BSM) are broadcast at 10 Hz, meaning an incoming frame arrives every 100 milliseconds.*
  >
  > *Our asynchronous FastAPI microservice registered an average inference latency of 7.82 milliseconds per frame ($\pm 0.42$ ms). This ensures that intrusion detection consumes less than 8% of the total available safety window, leaving over 92 milliseconds for vehicular CAN-bus signaling and electronic brake actuation."*

### Q7: What are the primary limitations of your current setup?
* **Answer**:
  > *"While our empirical results on the IEEE DataPort dataset exceed 97.80% accuracy, two practical limitations remain:*
  > *1. **Hardware-in-the-Loop Testing**: The current evaluation is based on synthetic IEEE DataPort message traces. Real-world deployment requires testing under physical software-defined radios (SDRs) subject to multipath fading and Doppler shifts.*
  > *2. **Adversarial Perturbations**: Attackers could theoretically craft evasion attacks with bounded coordinate perturbations designed to fool the B-spline boundaries. We plan to explore adversarial training in future iterations."*

### Q8: How was the workload divided among the team members?
* **Answer**:
  > *"Our team collaborated closely with distinct responsibilities:*
  > * * **Pratyaksh Manav**: Led mathematical modeling of Kolmogorov-Arnold Networks, B-spline activations, threat taxonomy formalization, and paper structuring.*
  > * * **Abhayraj Verma**: Engineered the text preprocessing pipeline, vocabulary mapping, post-padding engine, BiGRU sequence integration, and Draw.io architectural diagrams.*
  > * * **Arnav Tomar**: Conducted the 7-model empirical benchmarking, PyTorch hyperparameter tuning (AdamW, Cosine Annealing), FastAPI latency testing, and frontend SOC dashboard integration."*
