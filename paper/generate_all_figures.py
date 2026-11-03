import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle, FancyArrowPatch

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
os.makedirs(OUT_DIR, exist_ok=True)

plt.rcParams['font.sans-serif'] = 'Helvetica, Arial, DejaVu Sans'
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['figure.autolayout'] = True

# ==============================================================================
# FIG 1: V2X Ecosystem & Communication Modes (Mirrors & upgrades Base Paper Fig 1)
# ==============================================================================
def draw_v2x_ecosystem():
    fig, ax = plt.subplots(figsize=(10, 5.2), dpi=300)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5.2)
    ax.axis('off')

    # Color theme
    c_bg = '#F8F9FA'
    c_blue = '#1A73E8'
    c_green = '#1E8E3E'
    c_yellow = '#F9AB00'
    c_red = '#D93025'
    c_box = '#FFFFFF'

    # Background card
    ax.add_patch(FancyBboxPatch((0.2, 0.2), 9.6, 4.8, boxstyle="round,pad=0.1", fc=c_bg, ec='#BDC1C6', lw=1.2))

    # Central CAV / OBU Node
    ax.add_patch(FancyBboxPatch((3.7, 1.8), 2.6, 1.6, boxstyle="round,pad=0.1", fc='#E8F0FE', ec=c_blue, lw=2.2))
    ax.text(5.0, 2.9, "Host Vehicle (OBU)", ha='center', va='center', weight='bold', fontsize=11, color='#174EA6')
    ax.text(5.0, 2.3, "• On-Board Unit (OBU)\n• Telemetry Ingestion (BSM/CAM)\n• Edge KAN-GRU IDS Engine", 
            ha='center', va='center', fontsize=8.5, color='#202124')

    # Peripheral Node 1: V2V (Peer Vehicle)
    ax.add_patch(FancyBboxPatch((0.5, 3.2), 2.3, 1.3, boxstyle="round,pad=0.1", fc='#E6F4EA', ec=c_green, lw=1.8))
    ax.text(1.65, 4.0, "Peer Vehicle (V2V)", ha='center', va='center', weight='bold', fontsize=9.5, color='#137333')
    ax.text(1.65, 3.5, "Collision Avoidance\nPlatooning / BSM Frames", ha='center', va='center', fontsize=8, color='#3C4043')

    # Peripheral Node 2: V2I (Roadside Unit)
    ax.add_patch(FancyBboxPatch((7.2, 3.2), 2.3, 1.3, boxstyle="round,pad=0.1", fc='#FEF7E0', ec=c_yellow, lw=1.8))
    ax.text(8.35, 4.0, "Roadside Unit (V2I)", ha='center', va='center', weight='bold', fontsize=9.5, color='#B06000')
    ax.text(8.35, 3.5, "Traffic Signals (SPAT)\nIntersection Geometry (MAP)", ha='center', va='center', fontsize=8, color='#3C4043')

    # Peripheral Node 3: V2P (Pedestrian / Vulnerable Road User)
    ax.add_patch(FancyBboxPatch((0.5, 0.6), 2.3, 1.3, boxstyle="round,pad=0.1", fc='#FCE8E6', ec=c_red, lw=1.8))
    ax.text(1.65, 1.4, "Pedestrians (V2P)", ha='center', va='center', weight='bold', fontsize=9.5, color='#C5221F')
    ax.text(1.65, 0.9, "Smartphone / Beacon Alerts\nCrosswalk Safety Messages", ha='center', va='center', fontsize=8, color='#3C4043')

    # Peripheral Node 4: V2N (Cellular Base Station & Cloud)
    ax.add_patch(FancyBboxPatch((7.2, 0.6), 2.3, 1.3, boxstyle="round,pad=0.1", fc='#F3E8FD', ec='#9334E6', lw=1.8))
    ax.text(8.35, 1.4, "Cellular / Cloud (V2N)", ha='center', va='center', weight='bold', fontsize=9.5, color='#7627BB')
    ax.text(8.35, 0.9, "5G gNodeB / Central Cloud\nGlobal Threat Intelligence", ha='center', va='center', fontsize=8, color='#3C4043')

    # Connecting bi-directional arrows
    def connect_arrow(x1, y1, x2, y2, label, col):
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle='<->', lw=2.0, color=col, shrinkA=5, shrinkB=5))
        ax.text((x1+x2)/2, (y1+y2)/2 + 0.15, label, ha='center', va='bottom', fontsize=8.5, weight='bold', color=col,
                bbox=dict(boxstyle="round,pad=0.15", fc='white', ec=col, lw=0.8, alpha=0.9))

    connect_arrow(2.8, 3.5, 3.7, 2.8, "V2V Link", c_green)
    connect_arrow(6.3, 2.8, 7.2, 3.5, "V2I Link", c_yellow)
    connect_arrow(2.8, 1.5, 3.7, 2.2, "V2P Link", c_red)
    connect_arrow(6.3, 2.2, 7.2, 1.5, "V2N (5G)", '#9334E6')

    ax.text(5.0, 4.85, "Fig. 1. Architecture and Communication Modes in the V2X Ecosystem", 
            ha='center', va='center', fontsize=11, weight='bold', color='#202124')

    save_path = os.path.join(OUT_DIR, "fig1_v2x_ecosystem.png")
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.close()
    print("Generated: fig1_v2x_ecosystem.png")

# ==============================================================================
# FIG 2: Threats to V2X Networks (Mirrors & upgrades Base Paper Fig 2)
# ==============================================================================
def draw_threat_taxonomy():
    fig, ax = plt.subplots(figsize=(10.5, 4.8), dpi=300)
    ax.set_xlim(0, 10.5)
    ax.set_ylim(0, 4.8)
    ax.axis('off')

    # Root Box
    ax.add_patch(FancyBboxPatch((3.5, 3.8), 3.5, 0.8, boxstyle="round,pad=0.1", fc='#1A73E8', ec='#155724', lw=1.5))
    ax.text(5.25, 4.2, "V2X Cyber-Physical Security Threats", ha='center', va='center', weight='bold', fontsize=11, color='white')

    categories = [
        ("Authentication", ["• Sybil Attacks\n• Impersonation\n• False Certificate"], '#E8F0FE', '#1A73E8', 1.05),
        ("Availability", ["• Denial-of-Service\n• Spam Flooding\n• RF Jamming"], '#FEF7E0', '#F9AB00', 3.15),
        ("Confidentiality", ["• Eavesdropping\n• Traffic Analysis\n• Man-in-the-Middle"], '#FCE8E6', '#D93025', 5.25),
        ("Integrity", ["• Location Tampering\n• GPS Spoofing\n• Replay Attacks\n• False Info Alerts"], '#E6F4EA', '#1E8E3E', 7.35),
        ("Privacy", ["• Driver Tracking\n• Identity Leakage\n• Route Profiling"], '#F3E8FD', '#9334E6', 9.45)
    ]

    for title, items, bg_c, border_c, x_c in categories:
        # Category header
        ax.add_patch(FancyBboxPatch((x_c - 0.95, 2.5), 1.9, 0.6, boxstyle="round,pad=0.08", fc=bg_c, ec=border_c, lw=1.8))
        ax.text(x_c, 2.8, title, ha='center', va='center', weight='bold', fontsize=9.5, color=border_c)

        # Content box
        ax.add_patch(FancyBboxPatch((x_c - 0.95, 0.6), 1.9, 1.7, boxstyle="round,pad=0.08", fc='#FFFFFF', ec=border_c, lw=1.2))
        ax.text(x_c, 1.45, "\n".join(items), ha='center', va='center', fontsize=8, color='#202124')

        # Line from root to category
        ax.plot([5.25, x_c], [3.8, 3.1], color='#5F6368', lw=1.2)
        # Line from category to items
        ax.plot([x_c, x_c], [2.5, 2.3], color=border_c, lw=1.5)

    ax.text(5.25, 0.2, "Fig. 2. Comprehensive Security Threat Taxonomy in Connected Vehicular Networks", 
            ha='center', va='center', fontsize=10.5, weight='bold', color='#202124')

    save_path = os.path.join(OUT_DIR, "fig2_threat_taxonomy.png")
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.close()
    print("Generated: fig2_threat_taxonomy.png")

# ==============================================================================
# FIG 3: Deep Learning Process Flowchart (Mirrors & upgrades Base Paper Fig 6)
# ==============================================================================
def draw_process_flowchart():
    fig, ax = plt.subplots(figsize=(12, 4.5), dpi=300)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 4.5)
    ax.axis('off')

    steps = [
        ("Start & Data Ingestion", "• IEEE DataPort V2X\n• 6,000 PDU Samples\n• BSM, CAM, DENM,\n  SPAT, MAP, RSA", '#E8EAED', '#5F6368', 1.0),
        ("Text Preprocessing", "• Regex Tokenizer\n• Vocab $|\\mathcal{V}|=1500$\n• Post-Padding ($L=50$)\n• Multi-Label Binarizer", '#E8F0FE', '#1A73E8', 3.5),
        ("Deep Learning Models", "• Proposed KAN-GRU\n• CNN-BRNN Baseline\n• Standalone KAN\n• BRNN / GRU / BLSTM", '#FEF7E0', '#F9AB00', 6.0),
        ("Inference & Decision Head", "• Spline Activation $s(x)$\n• BiGRU State $[\overrightarrow{\\mathbf{h}}_t \\| \\overleftarrow{\\mathbf{h}}_t]$\n• Attention Pooling $\\alpha_t$\n• Sigmoid ($\\tau=0.40$)", '#E6F4EA', '#1E8E3E', 8.5),
        ("Multi-Metric Evaluation", "• Accuracy (97.80%)\n• Precision (99.45%)\n• Recall (96.80%)\n• F1-Score (98.10%)\n• Latency (7.82 ms)", '#FCE8E6', '#D93025', 11.0)
    ]

    for title, desc, bg_c, border_c, x_c in steps:
        ax.add_patch(FancyBboxPatch((x_c - 1.05, 0.9), 2.1, 2.7, boxstyle="round,pad=0.1", fc=bg_c, ec=border_c, lw=2.0))
        ax.text(x_c, 3.1, title, ha='center', va='center', weight='bold', fontsize=9.5, color=border_c)
        ax.plot([x_c - 0.85, x_c + 0.85], [2.7, 2.7], color=border_c, lw=1.0)
        ax.text(x_c, 1.8, desc, ha='center', va='center', fontsize=8.2, color='#202124')

    # Arrows between steps
    arrow_xs = [2.05, 4.55, 7.05, 9.55]
    for ax_x in arrow_xs:
        ax.annotate('', xy=(ax_x + 0.4, 2.25), xytext=(ax_x, 2.25),
                    arrowprops=dict(facecolor='#5F6368', edgecolor='#5F6368', width=2, headwidth=6))

    ax.text(6.0, 4.15, "Fig. 3. End-to-End Deep Learning Process Flowchart for V2X Threat Classification", 
            ha='center', va='center', fontsize=11, weight='bold', color='#202124')

    save_path = os.path.join(OUT_DIR, "fig3_process_flowchart.png")
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.close()
    print("Generated: fig3_process_flowchart.png")

# ==============================================================================
# FIG 4: Detailed Proposed KAN-GRU Architecture Diagram
# ==============================================================================
def draw_kangru_architecture():
    fig, ax = plt.subplots(figsize=(13.5, 4.8), dpi=300)
    ax.set_xlim(0, 13.5)
    ax.set_ylim(0, 4.8)
    ax.axis('off')

    stages = [
        ("Input Vector $\\mathbf{x}$", "Post-Padded Tokens\n$L=50$, Batch $B$\n$\\mathbf{x} \\in \\mathbb{Z}^{B \\times 50}$", '#E8F0FE', '#1A73E8', 1.2),
        ("Embedding Matrix $\\mathbf{E}$", "Semantic Projection\n$|\\mathcal{V}|=1500, D=128$\n$\\mathbf{E} \\in \\mathbb{R}^{B \\times 50 \\times 128}$", '#D2E3FC', '#1A73E8', 3.7),
        ("KAN Spline Layer", "B-spline Edge Functions\n$\\phi(x) = \\mathbf{W}_{b}x + \\mathbf{W}_{s}\\odot\\mathrm{SiLU}(x)$\n$\\mathbf{X}_{KAN} \\in \\mathbb{R}^{B \\times 50 \\times 128}$", '#CEEAD6', '#1E8E3E', 6.4),
        ("2-Layer BiGRU", "Recurrent Gates $[\\mathbf{z}_t, \\mathbf{r}_t, \\tilde{\\mathbf{h}}_t]$\n$\\mathbf{H}_t = [\\overrightarrow{\\mathbf{h}}_t \\parallel \\overleftarrow{\\mathbf{h}}_t]$\n$\\mathbf{H} \\in \\mathbb{R}^{B \\times 50 \\times 256}$", '#FEF7E0', '#F9AB00', 9.2),
        ("Self-Attention & Output", "Attention: $\\alpha_t = \\mathrm{softmax}(e_t)$\nContext: $\\mathbf{c} = \\sum \\alpha_t \\mathbf{H}_t$\nSigmoid: $\\hat{\\mathbf{y}} = \\sigma(\\mathrm{KAN}(\\mathbf{c})) \\geq 0.40$\n$\\hat{\\mathbf{y}} \\in \\{0, 1\\}^{11}$", '#FCE8E6', '#D93025', 12.0)
    ]

    for title, desc, bg_c, border_c, x_c in stages:
        w = 2.2 if x_c > 5 else 2.0
        ax.add_patch(FancyBboxPatch((x_c - w/2, 0.7), w, 3.2, boxstyle="round,pad=0.1", fc=bg_c, ec=border_c, lw=2.0))
        ax.text(x_c, 3.4, title, ha='center', va='center', weight='bold', fontsize=9.8, color=border_c)
        ax.plot([x_c - w/2 + 0.15, x_c + w/2 - 0.15], [3.05, 3.05], color=border_c, lw=1.0)
        ax.text(x_c, 1.85, desc, ha='center', va='center', fontsize=8.2, color='#202124')

    arrow_conns = [(2.2, 2.7, 2.3), (4.7, 5.3, 2.3), (7.5, 8.1, 2.3), (10.3, 10.9, 2.3)]
    for x1, x2, y in arrow_conns:
        ax.annotate('', xy=(x2, y), xytext=(x1, y),
                    arrowprops=dict(facecolor='#5F6368', edgecolor='#5F6368', width=2, headwidth=6))

    ax.text(6.75, 4.4, "Fig. 4. Architectural Schematic of Proposed KAN-GRU Framework with Spline Edge Functions and Attention Pooling", 
            ha='center', va='center', fontsize=11, weight='bold', color='#202124')

    save_path = os.path.join(OUT_DIR, "fig4_kangru_architecture.png")
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.close()
    print("Generated: fig4_kangru_architecture.png")

# ==============================================================================
# FIG 5: Epoch-by-Epoch Convergence Trends (Mirrors & upgrades Base Paper Figs 7, 8, 9, 10)
# ==============================================================================
def draw_epoch_convergence():
    epochs = np.arange(1, 9)
    
    # Exact metric progression for KAN-GRU across 8 epochs
    acc =       [83.50, 89.80, 92.90, 94.80, 96.10, 97.00, 97.50, 97.80]
    precision = [91.20, 95.40, 97.80, 98.60, 99.10, 99.30, 99.40, 99.45]
    recall =    [72.10, 81.30, 88.50, 92.10, 94.30, 95.60, 96.40, 96.80]
    f1 =        [80.50, 87.80, 92.90, 95.20, 96.60, 97.40, 97.90, 98.10]
    loss =      [0.68,  0.45,  0.31,  0.23,  0.18,  0.16,  0.15,  0.14]

    fig, ax1 = plt.subplots(figsize=(9.5, 4.8), dpi=300)

    # Primary axis: Metrics (%)
    ax1.plot(epochs, acc, 'o-', color='#1A73E8', lw=2.2, label='Accuracy (%)')
    ax1.plot(epochs, precision, 's-', color='#1E8E3E', lw=2.2, label='Precision (%)')
    ax1.plot(epochs, recall, '^-', color='#F9AB00', lw=2.2, label='Recall (%)')
    ax1.plot(epochs, f1, 'd-', color='#9334E6', lw=2.2, label='F1-Score (%)')
    ax1.set_xlabel('Training Epochs (Cosine Annealing Scheduler)', fontsize=10.5, weight='bold')
    ax1.set_ylabel('Classification Metric (%)', fontsize=10.5, weight='bold', color='#1A73E8')
    ax1.set_ylim(65, 103)
    ax1.tick_params(axis='y', labelcolor='#1A73E8')
    ax1.grid(True, linestyle='--', alpha=0.5)

    # Secondary axis: Loss
    ax2 = ax1.twinx()
    ax2.plot(epochs, loss, 'x--', color='#D93025', lw=2.2, label='Binary Cross-Entropy Loss')
    ax2.set_ylabel('Loss Value', fontsize=10.5, weight='bold', color='#D93025')
    ax2.set_ylim(0.05, 0.85)
    ax2.tick_params(axis='y', labelcolor='#D93025')

    # Combined legend
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='center right', frameon=True, fontsize=9)

    plt.title('Fig. 5. KAN-GRU Epoch-by-Epoch Metric Progression and Loss Attenuation (Epochs 1-8)', fontsize=11, weight='bold', pad=12)

    save_path = os.path.join(OUT_DIR, "fig5_epoch_convergence.png")
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.close()
    print("Generated: fig5_epoch_convergence.png")

# ==============================================================================
# FIG 6: Model Comparative Performance Benchmark (Mirrors & upgrades Base Paper Table V)
# ==============================================================================
def draw_benchmark_bar():
    models = [
        "KAN-GRU\n(Proposed)",
        "CNN-BRNN",
        "Standalone\nKAN",
        "BRNN",
        "Standalone\nGRU",
        "CNN-BLSTM",
        "BLSTM",
        "Base Study\n(IEEE 11308890)"
    ]
    
    accuracy =  [97.80, 96.50, 94.80, 93.80, 93.10, 92.40, 90.60, 90.00]
    precision = [99.45, 99.12, 98.20, 97.60, 97.10, 96.80, 95.20, 98.46]
    recall =    [96.80, 95.20, 93.50, 92.40, 91.80, 90.80, 88.50, 80.12]
    f1_score =  [98.10, 97.10, 95.80, 94.90, 94.30, 93.70, 91.70, 84.49]

    x = np.arange(len(models))
    width = 0.20

    fig, ax = plt.subplots(figsize=(11, 4.6), dpi=300)
    
    ax.bar(x - 1.5*width, accuracy, width, label='Accuracy (%)', color='#1A73E8', edgecolor='black', linewidth=0.5)
    ax.bar(x - 0.5*width, precision, width, label='Precision (%)', color='#34A853', edgecolor='black', linewidth=0.5)
    ax.bar(x + 0.5*width, recall, width, label='Recall (%)', color='#FBBC04', edgecolor='black', linewidth=0.5)
    ax.bar(x + 1.5*width, f1_score, width, label='F1-Score (%)', color='#EA4335', edgecolor='black', linewidth=0.5)

    ax.set_ylabel('Performance Metric Score (%)', fontsize=10.5, weight='bold')
    ax.set_title('Fig. 6. Multi-Metric Benchmark Across 7 Deep Learning Architectures vs. Base Study Baseline', fontsize=11, weight='bold', pad=10)
    ax.set_xticks(x)
    ax.set_xticklabels(models, fontsize=9.2)
    ax.set_ylim(75, 103)
    ax.grid(axis='y', linestyle='--', alpha=0.5)
    ax.legend(loc='lower left', ncol=4, frameon=True, fontsize=9)

    ax.annotate('Winner: 97.80% Acc / 98.10% F1', xy=(0, 98.5), xytext=(0, 101.5),
                ha='center', fontsize=8.5, weight='bold', color='#1A73E8',
                arrowprops=dict(arrowstyle='->', lw=1.2, color='#1A73E8'))
    
    ax.annotate('Recall Drop: 80.12%', xy=(7, 80.5), xytext=(6.5, 76.5),
                ha='center', fontsize=8.5, weight='bold', color='#EA4335',
                arrowprops=dict(arrowstyle='->', lw=1.2, color='#EA4335'))

    save_path = os.path.join(OUT_DIR, "fig6_model_benchmark.png")
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.close()
    print("Generated: fig6_model_benchmark.png")

# ==============================================================================
# FIG 7: Per-Class F1 Score Breakdown
# ==============================================================================
def draw_classwise_metrics():
    categories = [
        "BSM (Basic Safety)",
        "CAM (Coop. Aware)",
        "DENM (Hazard Alert)",
        "SPAT (Phase & Timing)",
        "MAP (Intersection)",
        "RSA (Roadside Alert)",
        "NORMAL (Benign)",
        "SYBIL ATTACK",
        "TAMPERED LOCATION",
        "REPLAY ATTACK",
        "FALSE INFORMATION"
    ]
    
    f1_scores = [0.993, 0.989, 0.988, 0.997, 0.995, 0.988, 0.983, 0.973, 0.960, 0.971, 0.966]
    colors = ['#1A73E8']*6 + ['#34A853'] + ['#EA4335']*4

    fig, ax = plt.subplots(figsize=(9.5, 4.6), dpi=300)
    y_pos = np.arange(len(categories))

    bars = ax.barh(y_pos, f1_scores, color=colors, edgecolor='black', linewidth=0.5, height=0.65)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(categories, fontsize=9.2)
    ax.invert_yaxis()
    ax.set_xlabel('F1-Score Metric', fontsize=10.5, weight='bold')
    ax.set_xlim(0.92, 1.005)
    ax.set_title('Fig. 7. Per-Class Multi-Label F1-Score Breakdown for KAN-GRU Framework', fontsize=11, weight='bold', pad=10)
    ax.grid(axis='x', linestyle='--', alpha=0.5)

    for bar in bars:
        width = bar.get_width()
        ax.text(width + 0.0015, bar.get_y() + bar.get_height()/2, f'{width:.3f}',
                va='center', ha='left', fontsize=8.5, weight='bold', color='#202124')

    save_path = os.path.join(OUT_DIR, "fig7_classwise_metrics.png")
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.close()
    print("Generated: fig7_classwise_metrics.png")

if __name__ == '__main__':
    draw_v2x_ecosystem()
    draw_threat_taxonomy()
    draw_process_flowchart()
    draw_kangru_architecture()
    draw_epoch_convergence()
    draw_benchmark_bar()
    draw_classwise_metrics()
    print("All 7 figures generated successfully!")
