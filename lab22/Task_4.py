"""
AI-Based ECG Arrhythmia Detection (Educational Use Only)
---------------------------------------------------------
⚠️ Disclaimer:
This program is for **learning and research purposes only** — not for clinical or diagnostic use.

Features:
✅ Automatically generates dummy ECG data if none exists
✅ Trains a simple 1D CNN model using TensorFlow/Keras
✅ Demonstrates human oversight importance in healthcare AI
"""

import os
import numpy as np
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow.keras import layers, models, callbacks, utils
import matplotlib.pyplot as plt

# --------------------------
# CONFIGURATION
# --------------------------
RANDOM_SEED = 42
np.random.seed(RANDOM_SEED)
tf.random.set_seed(RANDOM_SEED)

SAMPLE_LENGTH = 256     # samples per ECG beat
NUM_CLASSES = 5         # e.g., Normal, PVC, AF, etc.
DATA_PATH = "prepared_ecg.npz"

# --------------------------
# STEP 1: CREATE DUMMY DATA (if not available)
# --------------------------
def create_dummy_ecg_dataset(file_path=DATA_PATH, samples=1000):
    """
    Creates a synthetic ECG-like dataset for testing.
    """
    print("⚙️ No dataset found — generating dummy ECG data...")
    X = np.zeros((samples, SAMPLE_LENGTH), dtype=np.float32)

    for i in range(samples):
        freq = np.random.uniform(0.5, 5.0)
        phase = np.random.uniform(0, 2 * np.pi)
        noise = np.random.normal(0, 0.1, SAMPLE_LENGTH)
        signal = np.sin(np.linspace(0, 2 * np.pi * freq, SAMPLE_LENGTH) + phase) + noise
        X[i] = signal

    y = np.random.randint(0, NUM_CLASSES, samples)
    np.savez(file_path, X=X, y=y)
    print(f"✅ Dummy dataset created: {file_path}")
    print(f"🩺 X shape: {X.shape}, y shape: {y.shape}")

# --------------------------
# STEP 2: LOAD DATA
# --------------------------
def load_prepared_dataset(npz_path):
    if not os.path.exists(npz_path):
        create_dummy_ecg_dataset(npz_path)
    data = np.load(npz_path)
    return data["X"], data["y"]

# --------------------------
# STEP 3: PREPARE DATA SPLITS
# --------------------------
def prepare_splits(npz_path):
    X, y = load_prepared_dataset(npz_path)
    X = X.astype(np.float32)
    X = (X - np.mean(X, axis=1, keepdims=True)) / (np.std(X, axis=1, keepdims=True) + 1e-8)
    X = X[..., np.newaxis]
    y_cat = utils.to_categorical(y, num_classes=NUM_CLASSES)

    X_train, X_temp, y_train, y_temp = train_test_split(X, y_cat, test_size=0.3, random_state=RANDOM_SEED, stratify=y)
    X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=RANDOM_SEED,
                                                    stratify=np.argmax(y_temp, axis=1))
    return X_train, y_train, X_val, y_val, X_test, y_test

# --------------------------
# STEP 4: BUILD MODEL
# --------------------------
def make_1d_cnn(input_shape=(SAMPLE_LENGTH, 1), num_classes=NUM_CLASSES):
    model = models.Sequential([
        layers.Conv1D(32, kernel_size=7, padding="same", activation="relu", input_shape=input_shape),
        layers.BatchNormalization(),
        layers.MaxPool1D(2),

        layers.Conv1D(64, kernel_size=5, padding="same", activation="relu"),
        layers.BatchNormalization(),
        layers.MaxPool1D(2),

        layers.Conv1D(128, kernel_size=3, padding="same", activation="relu"),
        layers.BatchNormalization(),
        layers.GlobalAveragePooling1D(),

        layers.Dense(64, activation="relu"),
        layers.Dropout(0.4),
        layers.Dense(num_classes, activation="softmax")
    ])

    model.compile(optimizer=tf.keras.optimizers.Adam(1e-3),
                  loss="categorical_crossentropy",
                  metrics=["accuracy"])
    return model

# --------------------------
# STEP 5: TRAIN AND EVALUATE
# --------------------------
def train_and_evaluate(npz_path, model_save_path="ecg_cnn_model.h5"):
    X_train, y_train, X_val, y_val, X_test, y_test = prepare_splits(npz_path)
    model = make_1d_cnn(input_shape=X_train.shape[1:], num_classes=y_train.shape[1])

    print("\n🧠 Model Summary:")
    model.summary()

    cb = [
        callbacks.EarlyStopping(monitor="val_loss", patience=5, restore_best_weights=True),
        callbacks.ModelCheckpoint(model_save_path, monitor="val_loss", save_best_only=True)
    ]

    history = model.fit(X_train, y_train,
                        validation_data=(X_val, y_val),
                        epochs=15,
                        batch_size=64,
                        callbacks=cb,
                        verbose=1)

    print("\n📊 Evaluating model on test data...")
    test_metrics = model.evaluate(X_test, y_test, verbose=2)
    print(f"\n✅ Test Loss: {test_metrics[0]:.4f}, Test Accuracy: {test_metrics[1]*100:.2f}%")

    model.save(model_save_path)
    print(f"💾 Model saved as: {model_save_path}")

    # Plot training history
    plt.figure(figsize=(8, 4))
    plt.plot(history.history["accuracy"], label="Train Accuracy")
    plt.plot(history.history["val_accuracy"], label="Val Accuracy")
    plt.xlabel("Epoch")
    plt.ylabel("Accuracy")
    plt.title("ECG CNN Training Performance")
    plt.legend()
    plt.show()

# --------------------------
# MAIN PROGRAM
# --------------------------
if __name__ == "__main__":
    print("🩺 ECG Arrhythmia Detection — Educational Demo\n")

    dataset_path = input("📂 Enter full path to ECG dataset (.npz) or press Enter to use default: ").strip()
    if dataset_path == "":
        dataset_path = DATA_PATH

    train_and_evaluate(dataset_path, model_save_path="ecg_cnn_model.h5")
