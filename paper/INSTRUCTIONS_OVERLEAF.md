# Overleaf Submission & Compilation Guide for IEEE Research Paper

This folder contains the complete, publication-ready **IEEE Two-Column Research Paper** in LaTeX format (`main.tex`), structured in direct compliance with IEEE conference standards, the base paper, and faculty guide reference literature.

---

## 🎯 Key Manuscript Specifications

1. **Authors & Affiliation**:
   - **Pratyaksh Manav, Abhayraj Verma, and Arnav Tomar**
   - **School of Computer Science and Engineering (Specialization in Artificial Intelligence)**
   - **Bennett University, Greater Noida, India**
   - Formatted side-by-side with shared department/university affiliation in IEEE two-column format.

2. **Visual Parity with Base Paper (All 7 Figures & Diagrams Included)**:
   - **Fig. 1**: Architecture & Communication Modes in the V2X Ecosystem (`fig1_v2x_ecosystem.png`).
   - **Fig. 2**: Comprehensive Security Threat Taxonomy (`fig2_threat_taxonomy.png`).
   - **Fig. 3**: End-to-End Deep Learning Process Flowchart (`fig3_process_flowchart.png`).
   - **Fig. 4**: Architectural Blueprint of Proposed KAN-GRU Framework (`fig4_kangru_architecture.png`).
   - **Fig. 5**: Epoch-by-Epoch Metric Progression & Loss Attenuation (`fig5_epoch_convergence.png`).
   - **Fig. 6**: Consolidated Comparative Benchmark Across 7 Models vs. Base Study (`fig6_model_benchmark.png`).
   - **Fig. 7**: Per-Class Multi-Label F1-Score Breakdown across all 11 classes (`fig7_classwise_metrics.png`).

3. **Citations & Literature Review**:
   - **Faculty Reference Paper Cited**: Ref [7] *K. Saurabh, V. Sharma, U. Singh, R. Khondoker, R. Vyas, and O. P. Vyas, "HMS-IDS: Threat Intelligence Integration for Zero-Day Exploits and Advanced Persistent Threats in IIoT", Arabian Journal for Science and Engineering, vol. 50, pp. 1307–1327, 2025*.
   - **Base Research Paper Cited**: Ref [12] *"V2X Message Multi-Label Classification: A Deep Learning Approach", IEEE Xplore, Document ID: 11308890, 2025*.
   - Comparative Literature Review Synthesis (Table 1 emulating the comparative analysis table of HMS-IDS).

4. **Methodology & Mathematical Rigor**:
   - Complete mathematical equations for:
     - Learnable Kolmogorov-Arnold Network (KAN) B-spline & SiLU edge activation functions.
     - Bidirectional Gated Recurrent Unit (BiGRU) temporal gates (update, reset, candidate hidden state).
     - Parameterized Self-Attention Weight Pooling mechanism.
   - Algorithmic pseudocode (Algorithm 1: KAN-GRU Multi-Label Training and Classification).
   - Theoretical computational runtime complexity analysis ($\mathcal{O}(B \cdot L \cdot (D_{in}D_{out} + D_{gru}^2))$).

5. **Experimental Findings**:
   - Comprehensive benchmarks comparing all 7 models: **KAN-GRU (97.80%)**, **CNN-BRNN (96.50%)**, **KAN (94.80%)**, **BRNN (93.80%)**, **GRU (93.10%)**, **CNN-BLSTM (92.40%)**, and **BLSTM (90.60%)**.
   - Substantial improvement over the base paper's maximum accuracy (90.00% $\to$ 97.80%) and F1-score (84.49% $\to$ 98.10%).
   - Latency evaluation demonstrating 7.82 ms average inference time for real-time DSRC/C-V2X onboard execution.

---

## 🚀 How to Compile in Overleaf (Two Easy Methods)

### Method 1: Upload the ZIP file directly (Recommended - 1 Click!)
1. Go to your Overleaf dashboard: [https://www.overleaf.com/project](https://www.overleaf.com/project)
2. Click the green button **"New Project"** $\rightarrow$ select **"Upload Project"**.
3. Select or drag-and-drop the file:
   `V2X_Overleaf_Project.zip`
4. Overleaf automatically extracts all files (`main.tex` and all 7 figures) and immediately compiles the paper with all diagrams rendered!

### Method 2: If you already have a project open in Overleaf
1. Replace all text in `main.tex` on Overleaf with the updated code from `paper/main.tex`.
2. On the left sidebar (under "File tree"), click the **Upload** icon (tray with arrow pointing up).
3. Drag and drop all 7 image files:
   - `fig1_v2x_ecosystem.png`
   - `fig2_threat_taxonomy.png`
   - `fig3_process_flowchart.png`
   - `fig4_kangru_architecture.png`
   - `fig5_epoch_convergence.png`
   - `fig6_model_benchmark.png`
   - `fig7_classwise_metrics.png`
4. Click **"Recompile"** (or hit `Cmd + Enter` / `Ctrl + Enter`).
5. Click **"Download PDF"** to get your official submission PDF!
