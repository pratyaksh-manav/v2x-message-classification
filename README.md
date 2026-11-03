# V2X Message Multi-Label Classification: Neural Cyber-Defense Suite

[![IEEE Document](https://img.shields.io/badge/IEEE%20Xplore-11308890-blue.svg)](https://ieeexplore.ieee.org/document/11308890)
[![Accuracy](https://img.shields.io/badge/Top%20Accuracy-97.80%25%20(KAN--GRU)-success.svg)](#-benchmarking-results)
[![Python](https://img.shields.io/badge/Python-3.11+-informational.svg)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-red.svg)](https://pytorch.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-green.svg)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-18.2-blue.svg)](https://react.dev/)

A state-of-the-art deep learning cyber-defense and multi-label message classification platform for **Vehicle-To-Everything (V2X) Communications Security**, expanding on the IEEE baseline study ([IEEE Document 11308890](https://ieeexplore.ieee.org/document/11308890)) with advanced architectures including **Kolmogorov-Arnold Networks (KAN)** and hybrid **KAN-GRU**.

---

## 👥 Authors & Affiliation

* **Pratyaksh Manav** (`manavpratyaksh@gmail.com`)
* **Abhayraj Verma**
* **Arnav Tomar**

*Bachelor of Technology in Computer Science & Engineering (Specialization in Artificial Intelligence)*  
*School of Computer Science and Technology, Bennett University, Greater Noida, India*  
*Faculty Reference / Guide: **Dr. Kumar Saurabh***

---

## 📌 Problem & Purpose

Connected and Autonomous Vehicles (CAVs) communicate wirelessly using standardized V2X protocols (`BSM`, `CAM`, `DENM`, `SPAT`, `MAP`, `RSA`) to coordinate collision avoidance, speed harmonization, and intersection traversal. 

Malicious nodes or adversaries can compromise vehicular networks via:
- 👻 **Sybil Attacks**: Broadcasting fake "ghost" vehicle identities to manipulate traffic.
- 📍 **Location Tampering**: Injecting false GPS offsets to induce phantom collisions.
- 🔄 **Replay Attacks**: Re-transmitting expired timestamps and recycled authentication keys.
- ⚠️ **False Information Injection**: Broadcasting fabricated emergency alerts and fake road hazards.

This suite provides real-time, multi-label anomaly detection on incoming message payloads, separating legitimate traffic from multi-vector cyber attacks with up to **97.80% accuracy** in under 10 milliseconds.

---

## 📊 Benchmarking Results (7 Architectures)

All 7 models have been trained and benchmarked under identical splits on 6,000 IEEE-standard synthetic V2X payloads:

| Rank | Model Architecture | Accuracy | Precision | Recall | F1-Score | Loss | Key Highlight |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| 👑 **1** | **KAN-GRU** *(Top Fused)* | **97.80%** | **99.45%** | **96.80%** | **98.10%** | **0.14** | Fused KAN Spline + BiGRU + Attention |
| 🥈 **2** | **CNN-BRNN** | **96.50%** | **99.12%** | **95.20%** | **97.10%** | **0.18** | Dual Conv1D ($k=3, 5$) + BiGRU + Attention |
| 🥉 **3** | **KAN** | **94.80%** | **98.20%** | **93.50%** | **95.80%** | **0.22** | Pure Kolmogorov-Arnold Network (SiLU Splines) |
| **4** | **BRNN** | **93.80%** | **97.60%** | **92.40%** | **94.90%** | **0.25** | Deep Bidirectional GRU + Attention Pooling |
| **5** | **GRU** | **93.10%** | **97.10%** | **91.80%** | **94.30%** | **0.27** | Multi-Layer Unidirectional GRU + Attention |
| **6** | **CNN-BLSTM** | **92.40%** | **96.80%** | **90.80%** | **93.70%** | **0.29** | Dual Conv1D + BiLSTM + Attention |
| **7** | **BLSTM** | **90.60%** | **95.20%** | **88.50%** | **91.70%** | **0.34** | Baseline Bidirectional LSTM + Attention |

> **Comparison to Baseline Paper**: The original IEEE study achieved a maximum of 90.00% accuracy with CNN-BRNN, while BLSTM scored 81.20%. Our architectural refinements (dual convolutions, KAN edge activations, attention pooling, AdamW, and label smoothing) lifted **every single model above 90%**, with KAN-GRU setting the new high-water mark at **97.80%**.

---

## 📁 Repository Structure

```
v2x-message-classification/
├── README.md                           # Master project guide
├── requirements.txt                     # Python dependencies
├── data/                               # Explicit train, val, and test splits
│   ├── train.csv                       # Training dataset (75%, 4,499 samples)
│   ├── val.csv                         # Validation dataset (10%, 601 samples)
│   ├── test.csv                        # Test evaluation dataset (15%, 900 samples)
│   └── v2x_dataset.csv                 # Consolidated IEEE DataPort dataset (6,000 samples)
├── src/                                # Backend inference & training engine
│   ├── data_generator.py               # IEEE DataPort payload synthesizer
│   ├── preprocessing.py                # Tokenizer, post-padding (len=50) & MLB
│   ├── models.py                       # PyTorch implementations of all 7 models
│   ├── train_evaluate.py               # Training loop with AdamW, Cosine LR & metrics
│   └── server.py                       # FastAPI REST backend (<10ms inference)
├── frontend/                           # Futuristic Cyberpunk Web Dashboard
│   ├── src/
│   │   ├── App.jsx                     # Interactive HUD, playground, telemetry & graphs
│   │   ├── main.jsx                    # Entrypoint
│   │   └── index.css                   # Cyber grid theme & keyframe glow styling
│   ├── index.html
│   └── package.json
├── models_saved/                       # Trained PyTorch weights & vocabulary state
│   ├── preprocessor_state.json
│   ├── kan_gru_model.pt
│   ├── cnn_brnn_model.pt
│   ├── kan_model.pt
│   ├── brnn_model.pt
│   ├── gru_model.pt
│   ├── cnn_blstm_model.pt
│   ├── blstm_model.pt
│   └── benchmark_results.json
├── papers/                             # Complete Research Literature & Publications
│   ├── Our_Research_Paper_KAN_GRU_IEEE_Two_Column.pdf # Group's compiled IEEE research paper (9 Pages)
│   ├── Base_Paper_IEEE_11308890_V2X_Classification.pdf # Base study (Lazaga et al., 2025)
│   └── Reference_Paper_HMS_IDS_Saurabh_et_al_2025.pdf   # Faculty guide paper (Dr. Kumar Saurabh et al., 2025)
├── paper/                              # IEEE Two-Column Research Paper Source & Assets
│   ├── V2X_KAN_GRU_Research_Paper.pdf  # Compiled publication-ready PDF (Overleaf)
│   ├── main.tex                        # LaTeX manuscript source (IEEEtran format)
│   ├── V2X_Overleaf_Project.zip        # Complete Overleaf LaTeX bundle (main.tex + figures)
│   ├── fig1_v2x_ecosystem.png          # Fig 1: V2X Ecosystem & Communication Modes
│   ├── fig2_threat_taxonomy.png        # Fig 2: Comprehensive Threat Taxonomy
│   ├── fig3_process_flowchart.png      # Fig 3: End-to-End Deep Learning Process Flowchart
│   ├── fig4_kangru_architecture.png    # Fig 4: Proposed KAN-GRU Topology Blueprint
│   ├── fig5_epoch_convergence.png      # Fig 5: Epoch-by-Epoch Metric Progression
│   ├── fig6_model_benchmark.png        # Fig 6: Comparative Benchmark vs Base Paper
│   ├── fig7_classwise_metrics.png      # Fig 7: Per-Class F1-Score Breakdown (11 Classes)
│   ├── fig1_v2x_ecosystem.drawio       # Editable Draw.io XML vector diagram
│   ├── fig2_threat_taxonomy.drawio     # Editable Draw.io XML vector diagram
│   ├── fig3_process_flowchart.drawio   # Editable Draw.io XML vector diagram
│   └── fig4_kangru_architecture.drawio # Editable Draw.io XML vector diagram
├── presentation/                       # Presentation & Defense Deliverables
│   ├── V2X_KAN_GRU_Presentation.pptx   # 13-Slide PowerPoint deck with embedded diagrams
│   └── presentation_slides.md          # Markdown presentation source
└── docs/
    └── ARCHITECTURE_AND_EVALUATION.md  # Mathematical formulations & layer diagrams
```

---

## 🚀 Quick Start Guide

### 1. Python Environment Setup

```bash
# Clone repository
git clone https://github.com/<your-username>/v2x-message-classification.git
cd v2x-message-classification

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Dataset Generation & Splitting (Pre-generated Dataset Included)

```bash
# Generate full synthetic dataset (6,000 samples)
python3 src/data_generator.py --samples 6000 --output data/v2x_dataset.csv
```

### 3. Model Training & Benchmarking

```bash
# Train all 7 architectures and output evaluation summary
python3 src/train_evaluate.py --epochs 8
```

### 4. Start FastAPI REST Backend

```bash
python3 src/server.py
# REST API documentation available at: http://localhost:8000/docs
```

### 5. Launch React Futuristic Web Dashboard

```bash
cd frontend
npm install
npm run dev
# Dashboard opens at: http://localhost:5173
```

---

## 🛰️ API Endpoints

- `GET /` — Service health and active top model summary.
- `GET /api/benchmarks` — Performance metrics for all 7 architectures.
- `GET /api/samples` — Preset attack and benign V2X payloads.
- `POST /api/predict` — Real-time multi-label classification:
  ```json
  {
    "raw_text": "MSG_TYPE:BSM VEH_ID:SYBIL_GHOST_88 LAT:37.779100 LON:-122.411100 ...",
    "model_name": "KAN-GRU",
    "threshold": 0.40
  }
  ```
- `GET /api/telemetry-stream` — Real-time simulated CAV telemetry stream.

---

## 📜 Citations & References

```bibtex
@inproceedings{lazaga2025v2x,
  author={Lazaga, Chrisjonpane F. and Rosales, Marife A. and Tan, Gerhard P.},
  booktitle={2025 1st International Conference on Artificial Intelligence Technology (ICoAIT)},
  title={V2X Message Multi-Label Classification: A Deep Learning Approach},
  year={2025},
  pages={1--6},
  doi={10.1109/ICoAIT67446.2025.11308890}
}

@article{saurabh2025hmsids,
  author={Saurabh, Kumar and Sharma, Vishal and Singh, Umesh and Khondoker, Rahamatullah and Vyas, Rajeev and Vyas, O. P.},
  title={HMS-IDS: Threat Intelligence Integration for Zero-Day Exploits and Advanced Persistent Threats in IIoT},
  journal={Arabian Journal for Science and Engineering},
  volume={50},
  pages={1307--1327},
  year={2025},
  doi={10.1007/s13369-024-08935-5}
}
```