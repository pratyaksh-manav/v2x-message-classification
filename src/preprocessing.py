#!/usr/bin/env python3
"""
V2X Text Preprocessing & Tokenization Engine (Optimized)
Applies:
1. Tokenization & Vocabulary mapping
2. Sequence Post-padding (padding='post')
3. Multi-Label One-Hot Binarization
"""

import json
import re
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MultiLabelBinarizer

DEFAULT_CLASSES = ['BSM', 'CAM', 'DENM', 'SPAT', 'MAP', 'RSA', 'NORMAL', 'SYBIL_ATTACK', 'TAMPERED_LOCATION', 'REPLAY_ATTACK', 'FALSE_INFO']

class V2XTextPreprocessor:
    def __init__(self, max_vocab_size=1500, max_sequence_length=50):
        self.max_vocab_size = max_vocab_size
        self.max_sequence_length = max_sequence_length
        self.word2idx = {"<PAD>": 0, "<UNK>": 1}
        self.idx2word = {0: "<PAD>", 1: "<UNK>"}
        self.mlb = MultiLabelBinarizer(classes=DEFAULT_CLASSES)
        self.mlb.fit([[c] for c in DEFAULT_CLASSES])
        self.is_fitted = False

    def tokenize_text(self, text):
        """Clean and tokenize V2X payload string into word/key-value tokens."""
        text = text.upper()
        # Preserve structured tokens like LAT:37.77, SPEED:12.5, 0x0000, etc.
        tokens = re.findall(r'[A-Z0-9_\-\.\:\[\]]+', text)
        return tokens

    def fit(self, texts, label_lists=None):
        """Build vocabulary from texts and fit MultiLabelBinarizer."""
        freq = {}
        for text in texts:
            tokens = self.tokenize_text(text)
            for token in tokens:
                freq[token] = freq.get(token, 0) + 1
        
        # Sort tokens by frequency
        sorted_tokens = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        for token, _ in sorted_tokens[:self.max_vocab_size - 2]:
            if token not in self.word2idx:
                idx = len(self.word2idx)
                self.word2idx[token] = idx
                self.idx2word[idx] = token
                
        if label_lists is not None:
            self.mlb.fit(label_lists)

        self.is_fitted = True

    def transform_texts(self, texts):
        """Convert list of texts into post-padded sequence array."""
        sequences = []
        for text in texts:
            tokens = self.tokenize_text(text)
            seq = [self.word2idx.get(token, 1) for token in tokens] # 1 is UNK
            
            # Apply post-padding / truncation
            if len(seq) < self.max_sequence_length:
                seq = seq + [0] * (self.max_sequence_length - len(seq)) # Post-padding with 0
            else:
                seq = seq[:self.max_sequence_length]
            sequences.append(seq)

        return np.array(sequences, dtype=np.int32)

    def transform_labels(self, label_lists):
        """One-hot binarize multi-label targets."""
        return self.mlb.transform(label_lists)

    def inverse_transform_labels(self, binary_matrix, threshold=0.40):
        """Convert probability output array back to label list."""
        binary_pred = (binary_matrix >= threshold).astype(int)
        return self.mlb.inverse_transform(binary_pred)

    def save_state(self, filepath):
        """Save preprocessor parameters to JSON."""
        state = {
            "max_vocab_size": self.max_vocab_size,
            "max_sequence_length": self.max_sequence_length,
            "word2idx": self.word2idx,
            "classes": self.mlb.classes_.tolist()
        }
        with open(filepath, "w") as f:
            json.dump(state, f, indent=2)

    @classmethod
    def load_state(cls, filepath):
        """Load preprocessor from JSON file."""
        with open(filepath, "r") as f:
            state = json.load(f)
        obj = cls(max_vocab_size=state["max_vocab_size"], max_sequence_length=state["max_sequence_length"])
        obj.word2idx = state["word2idx"]
        obj.idx2word = {int(v): k for k, v in state["word2idx"].items()}
        obj.mlb = MultiLabelBinarizer(classes=state["classes"])
        obj.mlb.fit([[c] for c in state["classes"]])
        obj.is_fitted = True
        return obj

def load_and_preprocess_dataset(csv_path, test_size=0.15, val_size=0.10, max_len=50):
    """Load V2X CSV dataset, fit preprocessor, and return train/val/test splits."""
    df = pd.read_csv(csv_path)
    df['label_list'] = df['multi_labels'].apply(lambda s: s.split() if isinstance(s, str) else [])
    
    preprocessor = V2XTextPreprocessor(max_sequence_length=max_len)
    preprocessor.fit(df['raw_text'].values, df['label_list'].values)
    
    X = preprocessor.transform_texts(df['raw_text'].values)
    y = preprocessor.transform_labels(df['label_list'].values)
    
    X_train_val, X_test, y_train_val, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
    val_relative = val_size / (1.0 - test_size)
    X_train, X_val, y_train, y_val = train_test_split(X_train_val, y_train_val, test_size=val_relative, random_state=42)
    
    return {
        "X_train": X_train, "y_train": y_train,
        "X_val": X_val, "y_val": y_val,
        "X_test": X_test, "y_test": y_test,
        "preprocessor": preprocessor
    }

def load_explicit_splits(train_path="data/train.csv", val_path="data/val.csv", test_path="data/test.csv", max_len=50):
    """Load explicit train, validation, and test CSV splits and transform with preprocessor."""
    train_df = pd.read_csv(train_path)
    val_df = pd.read_csv(val_path)
    test_df = pd.read_csv(test_path)

    for df in [train_df, val_df, test_df]:
        df['label_list'] = df['multi_labels'].apply(lambda s: s.split() if isinstance(s, str) else [])

    preprocessor = V2XTextPreprocessor(max_sequence_length=max_len)
    preprocessor.fit(train_df['raw_text'].values, train_df['label_list'].values)

    return {
        "X_train": preprocessor.transform_texts(train_df['raw_text'].values),
        "y_train": preprocessor.transform_labels(train_df['label_list'].values),
        "X_val": preprocessor.transform_texts(val_df['raw_text'].values),
        "y_val": preprocessor.transform_labels(val_df['label_list'].values),
        "X_test": preprocessor.transform_texts(test_df['raw_text'].values),
        "y_test": preprocessor.transform_labels(test_df['label_list'].values),
        "preprocessor": preprocessor
    }
