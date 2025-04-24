# 🌇️ Mumbai Residential Real Estate Intelligence System

This is a complete Data Science + NLP-powered project focused on **Mumbai’s residential property market**. It consists of **three powerful modules**: price prediction, advanced analytics, and a smart chatbot — all tied together with a modern Streamlit frontend.

---

## 📌 Problem Statement

The Mumbai real estate market is vast and highly dynamic. Buyers often struggle to:
- Get accurate price estimates
- Explore meaningful trends (like price by locality, age, BHK)
- Find answers to their questions quickly

---

## ✅ Proposed Solution

We propose an intelligent real estate system that:
- Predicts property prices using machine learning
- Visualizes important property patterns and trends
- Answers user queries using an AI chatbot trained on real data

All these components are unified in a clean, interactive Streamlit dashboard.

---

## 🧠 Project Workflow

### 📂 Dataset Used

We used `mumbaipropdataset.csv`, a structured dataset containing:
- Property details like `AREA`, `BHK`, `FACING`, `AGE`, `PRICE`, `DESCRIPTION`, `LAT`, `LONG`, etc.
- Listings from across **Mumbai residential sectors**

---

## 💪 Modules Description

### 1️⃣ Price Prediction (ML)
- Built using **Random Forest Regressor (n=500)**
- Achieved **91% accuracy**
- Input: Property features like area, locality, BHK, age, etc.
- Output: Predicted property price

### 2️⃣ Analytics (Data Visualization)
- Built with **Plotly** inside **Streamlit**
- Shows:
  - Scatter plots: Area vs Price
  - Sunburst: City → Locality → BHK
  - Radial charts: Price by Facing
  - Line charts: Price vs Age
  - Word cloud from descriptions
  - Pie charts: BHK filtered by locality

### 3️⃣ Chatbot (NLP-Powered Assistant)
- Powered by a lightweight **LLM/chatbot interface**
- Trained over `mumbaipropdataset.csv`
- Handles both Q&A and visualization queries
- **Hosted on Colab with GPU**, integrated with Streamlit via an API

---

## ⚙️ Implementation Steps

### ✅ 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### ✅ 2. Launch Chatbot on Google Colab

- Open `RealEstateChatbot.ipynb` on **Colab (T4 GPU)**
- Run all cells — an **API link** will be generated
- Copy this API URL

### ✅ 3. Link chatbot to Streamlit frontend

- Go to:
  ```bash
  pages/RealtEase.py
  ```
- **Paste the API URL at line 12**
  ```python
  url = "https://your-colab-api.ngrok-free.app"
  ```

️⚠️ *Note*: The chatbot will keep working **until your Colab session is live**.

---

## ▶️ Running the App Locally(For Windows)

1. **Create your environment** (e.g., `dslab`) and install dependencies:

```bash
pip install virtualenv
```

```bash
virtualenv dslab
```

```bash
cd dslab/Scripts && activate
```

2. **Install the required packages:**

```bash
pip install -r requirements.txt
```

3. **Launch the Streamlit app:**

```bash
streamlit run Real_Estate_Project.py
```

🎉 That's it! Your Mumbai Real Estate Intelligence App is now live.

---

## 🛠️ Tech Stack

| Component     | Tools Used                                      |
|---------------|-------------------------------------------------|
| Language      | Python                                          |
| Visualization | Plotly, Matplotlib, Seaborn                     |
| Web App       | Streamlit                                       |
| ML Model      | Scikit-learn (Random Forest Regressor)          |
| NLP           | TF-IDF, NLTK                                    |
| LLM API       | Colab + custom Python Flask/NLP logic           |
| Hosting       | Local + Colab API for GPU-based chatbot         |

---

## 🚧 Future Scope

- Replace RF with **XGBoost or CatBoost**
- Improve chatbot with **LLM fine-tuning** or **LangChain**
- Deploy chatbot via WhatsApp/Telegram

---

## 🙏 Acknowledgements

- **Guide**: Ms. Sonal Balpande  
- **Institute**: A.P. Shah Institute of Technology, Mumbai  
- Built as part of the academic mini project (TE IT - 2024-25)

---

## 📜 License

This project is for academic and research purposes only.

---

