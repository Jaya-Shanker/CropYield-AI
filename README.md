# 🌾 Indian Crop Yield Prediction - Deployment Guide

This repository contains the end-to-end Machine Learning pipeline and web application for predicting agricultural crop yields across Indian states.

## 📊 Model Overview
- **Target Variable:** `Yield` (Tonnes per Hectare)
- **Data Leakage Prevention:** `Production` was excluded from the feature set because `Production / Area` directly leaks the target `Yield`.
- **Features Used:** `Year`, `State`, `Crop`, `Season`, `Area`, `Annual_Rainfall`, `Fertilizer`, `Pesticide`
- **Best Model:** `ExtraTreesRegressor` ($R^2 = 0.9776$, $\text{MAE} = 11.56$, $\text{RMSE} = 152.79$)

---

## 🚀 Step-by-Step Deployment Instructions

### Step 1: Generate the Saved Model (`.pkl`)
Place your `train-00000-of-00001.parquet` file in this folder and run:
```bash
pip install -r requirements.txt
python train_and_save_model.py
```
This will generate `crop_yield_model.pkl` and `metadata.pkl`.

### Step 2: Test the Web App Locally
Run the Streamlit app on your computer:
```bash
streamlit run app.py
```

### Step 3: Push to Your GitHub (`https://github.com/Jaya-Shanker`)
1. Create a new repository on your GitHub account (e.g., `crop-yield-prediction`).
2. Initialize Git and push your files:
```bash
git init
git add app.py train_and_save_model.py requirements.txt Dockerfile api.py README.md crop_yield_model.pkl metadata.pkl
git commit -m "Add Crop Yield ML deployment files"
git branch -M main
git remote add origin https://github.com/Jaya-Shanker/crop-yield-prediction.git
git push -u origin main
```
*(Note: If `crop_yield_model.pkl` is larger than 100MB, either use [Git LFS](https://git-lfs.com/) or increase `min_samples_leaf=5` / reduce `n_estimators=100` in `train_and_save_model.py` to shrink the file size under 25MB).*

### Step 4: Deploy Live for Free (Streamlit Community Cloud)
1. Go to [share.streamlit.io](https://share.streamlit.io/) and sign in with your **Jaya-Shanker** GitHub account.
2. Click **"New app"**.
3. Select your repository (`Jaya-Shanker/crop-yield-prediction`), branch (`main`), and main file path (`app.py`).
4. Click **"Deploy!"** — Your live public URL will be ready in ~2 minutes!
