#!/usr/bin/env python3
"""
V2X Deep Learning Model Architectures (PyTorch Implementation with Fused KAN-GRU)
Implements:
1. KAN-GRU   - Fused Kolmogorov-Arnold Network + Gated Recurrent Unit (Spline Edge + BiGRU + Attention)
2. KAN       - Kolmogorov-Arnold Network (Spline/Learnable Edge Activation Network)
3. GRU       - Gated Recurrent Unit Network
4. BRNN      - Bidirectional Recurrent Neural Network + Attention Pooling
5. CNN-BRNN  - Multi-Kernel Conv1D + Bidirectional GRU (Top Performer)
6. BLSTM     - Bidirectional Long Short-Term Memory
7. CNN-BLSTM - Multi-Kernel Conv1D + Bidirectional LSTM
"""

import torch
import torch.nn as nn
import torch.nn.functional as F

class KANLinear(nn.Module):
    """
    Kolmogorov-Arnold Network (KAN) Linear Layer
    Replaces fixed node activation functions with learnable edge basis functions (SiLU + Spline Weights).
    """
    def __init__(self, in_features, out_features):
        super(KANLinear, self).__init__()
        self.in_features = in_features
        self.out_features = out_features
        
        # Base linear transformation weight
        self.base_weight = nn.Parameter(torch.randn(out_features, in_features) * 0.05)
        # Learnable spline activation weight
        self.spline_weight = nn.Parameter(torch.randn(out_features, in_features) * 0.05)
        self.scale_base = nn.Parameter(torch.ones(out_features, in_features))
        self.scale_spline = nn.Parameter(torch.ones(out_features, in_features))
        self.silu = nn.SiLU()

    def forward(self, x):
        base_act = F.linear(x, self.base_weight)
        spline_act = F.linear(self.silu(x), self.spline_weight)
        return base_act + spline_act

class AttentionPooling(nn.Module):
    """Self-Attention Pooling over time dimension."""
    def __init__(self, in_dim):
        super(AttentionPooling, self).__init__()
        self.attn = nn.Sequential(
            nn.Linear(in_dim, in_dim // 2),
            nn.Tanh(),
            nn.Linear(in_dim // 2, 1)
        )

    def forward(self, x):
        attn_weights = F.softmax(self.attn(x), dim=1)
        context = torch.sum(x * attn_weights, dim=1)
        return context

class KANGRUModel(nn.Module):
    """
    Fused Kolmogorov-Arnold Network + Gated Recurrent Unit (KAN-GRU)
    Fuses KAN spline non-linear feature transformation with Bidirectional GRU sequence encoding
    and Trainable Self-Attention Weight Pooling.
    Target Performance: >97.5% Accuracy, >99.2% Precision
    """
    def __init__(self, vocab_size=1500, embed_dim=128, hidden_dim=128, num_classes=11, dropout=0.2):
        super(KANGRUModel, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim, padding_idx=0)
        self.kan_feat = KANLinear(embed_dim, hidden_dim)
        self.gru = nn.GRU(hidden_dim, hidden_dim, batch_first=True, bidirectional=True, num_layers=2, dropout=dropout)
        self.attention = AttentionPooling(hidden_dim * 2)
        self.norm = nn.LayerNorm(hidden_dim * 2)
        self.dropout = nn.Dropout(dropout)
        self.kan_classifier = KANLinear(hidden_dim * 2, num_classes)

    def forward(self, x):
        embedded = self.embedding(x)                 # (batch, seq_len, embed_dim)
        kan_encoded = self.kan_feat(embedded)        # (batch, seq_len, hidden_dim)
        gru_out, _ = self.gru(kan_encoded)           # (batch, seq_len, hidden_dim * 2)
        pooled = self.attention(gru_out)             # (batch, hidden_dim * 2)
        normed = self.norm(pooled)
        logits = self.kan_classifier(self.dropout(normed))
        return logits

class KANModel(nn.Module):
    """Kolmogorov-Arnold Network (KAN) for V2X Multi-Label Classification"""
    def __init__(self, vocab_size=1500, embed_dim=128, hidden_dim=128, num_classes=11, dropout=0.2):
        super(KANModel, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim, padding_idx=0)
        self.kan_layer1 = KANLinear(embed_dim, hidden_dim)
        self.kan_layer2 = KANLinear(hidden_dim, hidden_dim)
        self.attention = AttentionPooling(hidden_dim)
        self.norm = nn.LayerNorm(hidden_dim)
        self.dropout = nn.Dropout(dropout)
        self.kan_classifier = KANLinear(hidden_dim, num_classes)

    def forward(self, x):
        embedded = self.embedding(x)
        h1 = self.kan_layer1(embedded)
        h2 = self.kan_layer2(h1)
        pooled = self.attention(h2)
        normed = self.norm(pooled)
        logits = self.kan_classifier(self.dropout(normed))
        return logits

class GRUModel(nn.Module):
    """Gated Recurrent Unit (GRU) Model for V2X Message Classification"""
    def __init__(self, vocab_size=1500, embed_dim=128, hidden_dim=128, num_classes=11, dropout=0.2):
        super(GRUModel, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim, padding_idx=0)
        self.gru = nn.GRU(embed_dim, hidden_dim, batch_first=True, num_layers=2, dropout=dropout)
        self.attention = AttentionPooling(hidden_dim)
        self.norm = nn.LayerNorm(hidden_dim)
        self.fc = nn.Sequential(
            nn.Dropout(dropout),
            nn.Linear(hidden_dim, hidden_dim // 2),
            nn.ReLU(),
            nn.Linear(hidden_dim // 2, num_classes)
        )

    def forward(self, x):
        embedded = self.embedding(x)
        out, _ = self.gru(embedded)
        pooled = self.attention(out)
        normed = self.norm(pooled)
        logits = self.fc(normed)
        return logits

class BRNNModel(nn.Module):
    """Bidirectional Recurrent Neural Network (BRNN) with Attention Pooling"""
    def __init__(self, vocab_size=1500, embed_dim=128, hidden_dim=128, num_classes=11, dropout=0.2):
        super(BRNNModel, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim, padding_idx=0)
        self.rnn = nn.GRU(embed_dim, hidden_dim, batch_first=True, bidirectional=True, num_layers=2, dropout=dropout)
        self.attention = AttentionPooling(hidden_dim * 2)
        self.norm = nn.LayerNorm(hidden_dim * 2)
        self.fc = nn.Sequential(
            nn.Dropout(dropout),
            nn.Linear(hidden_dim * 2, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, num_classes)
        )

    def forward(self, x):
        embedded = self.embedding(x)
        out, _ = self.rnn(embedded)
        pooled = self.attention(out)
        normed = self.norm(pooled)
        logits = self.fc(normed)
        return logits

class CNNBRNNModel(nn.Module):
    """Convolutional - Bidirectional Recurrent Neural Network (CNN-BRNN)"""
    def __init__(self, vocab_size=1500, embed_dim=128, num_filters=128, hidden_dim=128, num_classes=11, dropout=0.2):
        super(CNNBRNNModel, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim, padding_idx=0)
        
        self.conv_k3 = nn.Conv1d(in_channels=embed_dim, out_channels=num_filters // 2, kernel_size=3, padding=1)
        self.conv_k5 = nn.Conv1d(in_channels=embed_dim, out_channels=num_filters // 2, kernel_size=5, padding=2)
        self.bn = nn.BatchNorm1d(num_filters)
        self.pool = nn.MaxPool1d(kernel_size=2)
        
        self.rnn = nn.GRU(num_filters, hidden_dim, batch_first=True, bidirectional=True, num_layers=2, dropout=dropout)
        self.attention = AttentionPooling(hidden_dim * 2)
        self.norm = nn.LayerNorm(hidden_dim * 2)
        
        self.fc = nn.Sequential(
            nn.Dropout(dropout),
            nn.Linear(hidden_dim * 2, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, num_classes)
        )

    def forward(self, x):
        embedded = self.embedding(x)
        embedded_perm = embedded.permute(0, 2, 1)
        
        c3 = F.relu(self.conv_k3(embedded_perm))
        c5 = F.relu(self.conv_k5(embedded_perm))
        conv_cat = torch.cat([c3, c5], dim=1)
        conv_bn = self.bn(conv_cat)
        pooled = self.pool(conv_bn)
        
        pooled_perm = pooled.permute(0, 2, 1)
        rnn_out, _ = self.rnn(pooled_perm)
        
        attn_pooled = self.attention(rnn_out)
        normed = self.norm(attn_pooled)
        logits = self.fc(normed)
        return logits

class BLSTMModel(nn.Module):
    """Bidirectional Long Short-Term Memory (BLSTM) with Attention Pooling"""
    def __init__(self, vocab_size=1500, embed_dim=128, hidden_dim=128, num_classes=11, dropout=0.2):
        super(BLSTMModel, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim, padding_idx=0)
        self.lstm = nn.LSTM(embed_dim, hidden_dim, batch_first=True, bidirectional=True, num_layers=2, dropout=dropout)
        self.attention = AttentionPooling(hidden_dim * 2)
        self.norm = nn.LayerNorm(hidden_dim * 2)
        self.fc = nn.Sequential(
            nn.Dropout(dropout),
            nn.Linear(hidden_dim * 2, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, num_classes)
        )

    def forward(self, x):
        embedded = self.embedding(x)
        out, _ = self.lstm(embedded)
        pooled = self.attention(out)
        normed = self.norm(pooled)
        logits = self.fc(normed)
        return logits

class CNNBLSTMModel(nn.Module):
    """Convolutional - Bidirectional Long Short-Term Memory (CNN-BLSTM)"""
    def __init__(self, vocab_size=1500, embed_dim=128, num_filters=128, hidden_dim=128, num_classes=11, dropout=0.2):
        super(CNNBLSTMModel, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim, padding_idx=0)
        
        self.conv_k3 = nn.Conv1d(in_channels=embed_dim, out_channels=num_filters // 2, kernel_size=3, padding=1)
        self.conv_k5 = nn.Conv1d(in_channels=embed_dim, out_channels=num_filters // 2, kernel_size=5, padding=2)
        self.bn = nn.BatchNorm1d(num_filters)
        self.pool = nn.MaxPool1d(kernel_size=2)
        
        self.lstm = nn.LSTM(num_filters, hidden_dim, batch_first=True, bidirectional=True, num_layers=2, dropout=dropout)
        self.attention = AttentionPooling(hidden_dim * 2)
        self.norm = nn.LayerNorm(hidden_dim * 2)
        
        self.fc = nn.Sequential(
            nn.Dropout(dropout),
            nn.Linear(hidden_dim * 2, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, num_classes)
        )

    def forward(self, x):
        embedded = self.embedding(x)
        embedded_perm = embedded.permute(0, 2, 1)
        
        c3 = F.relu(self.conv_k3(embedded_perm))
        c5 = F.relu(self.conv_k5(embedded_perm))
        conv_cat = torch.cat([c3, c5], dim=1)
        conv_bn = self.bn(conv_cat)
        pooled = self.pool(conv_bn)
        
        pooled_perm = pooled.permute(0, 2, 1)
        lstm_out, _ = self.lstm(pooled_perm)
        attn_pooled = self.attention(lstm_out)
        normed = self.norm(attn_pooled)
        logits = self.fc(normed)
        return logits

def get_model(model_name, vocab_size=1500, embed_dim=128, hidden_dim=128, num_classes=11):
    """Factory function to build deep learning models by name."""
    name_upper = model_name.upper().replace("-", "_")
    if name_upper in ["KAN_GRU", "KANGRU", "KAN-GRU"]:
        return KANGRUModel(vocab_size=vocab_size, embed_dim=embed_dim, hidden_dim=hidden_dim, num_classes=num_classes)
    elif name_upper in ["KAN", "KAN_MODEL"]:
        return KANModel(vocab_size=vocab_size, embed_dim=embed_dim, hidden_dim=hidden_dim, num_classes=num_classes)
    elif name_upper in ["GRU", "GRU_MODEL"]:
        return GRUModel(vocab_size=vocab_size, embed_dim=embed_dim, hidden_dim=hidden_dim, num_classes=num_classes)
    elif name_upper in ["BRNN"]:
        return BRNNModel(vocab_size=vocab_size, embed_dim=embed_dim, hidden_dim=hidden_dim, num_classes=num_classes)
    elif name_upper in ["CNN_BRNN", "CNNBRNN"]:
        return CNNBRNNModel(vocab_size=vocab_size, embed_dim=embed_dim, hidden_dim=hidden_dim, num_classes=num_classes)
    elif name_upper in ["BLSTM"]:
        return BLSTMModel(vocab_size=vocab_size, embed_dim=embed_dim, hidden_dim=hidden_dim, num_classes=num_classes)
    elif name_upper in ["CNN_BLSTM", "CNNBLSTM"]:
        return CNNBLSTMModel(vocab_size=vocab_size, embed_dim=embed_dim, hidden_dim=hidden_dim, num_classes=num_classes)
    else:
        raise ValueError(f"Unknown model architecture: {model_name}. Options: KAN-GRU, KAN, GRU, BRNN, CNN-BRNN, BLSTM, CNN-BLSTM")
