# ⚡ WattWise AI

WattWise AI is an AI-powered electricity consumption analyzer built using Streamlit and Google Gemini AI. It helps users estimate electricity usage, calculate monthly bills, analyze energy consumption, and receive personalized energy-saving suggestions.

## 🌍 Project Objective

The main goal of WattWise AI is to promote energy conservation by helping users understand their electricity usage and reduce unnecessary power consumption.

This project supports:

- SDG 7 – Affordable and Clean Energy
- SDG 13 – Climate Action

---

## Demo
https://wattwise-ai-n7r3boexvi5adrqsdv3avd.streamlit.app/

## ✨ Features

- 🔐 User Login & Registration
- ⚡ Appliance Energy Calculator
- 💰 Monthly Electricity Bill Estimator
- 📊 Energy Usage Comparison Dashboard
- 🏆 Energy Efficiency Score
- 🤖 AI-powered Energy Saving Suggestions
- 📋 AI Energy Report Generator
- 💡 Appliance-specific Energy Saving Tips
- 📈 Interactive Charts

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- Google Gemini AI API
- CSV Dataset

---

## 📂 Project Structure

```
WattWise-AI/
│
├── app.py
├── appliances.csv
├── energy_tips.csv
├── users.csv
├── requirements.txt
├── README.md
└── .streamlit/
    └── secrets.toml
```

---

## 📊 Dataset

### appliances.csv

Contains appliance names and power consumption.

Example:

| Appliance | Watts |
|-----------|------:|
| Fan | 75 |
| LED Bulb | 10 |
| AC | 1500 |
| Refrigerator | 200 |

---

### energy_tips.csv

Contains appliance-wise electricity saving tips.

Example:

| Appliance | Tip |
|-----------|-----|
| Fan | Clean fan blades regularly |
| AC | Set temperature between 24–26°C |

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/WattWise-AI.git
```

Go to the project folder

```bash
cd WattWise-AI
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 🔑 Gemini API Setup

Create a Gemini API Key from Google AI Studio.

Create a `.streamlit/secrets.toml` file:

```toml
GOOGLE_API_KEY="YOUR_GEMINI_API_KEY"
```

Configure it in Python:

```python
import os
import google.generativeai as genai

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
```

---

## 📈 How It Works

1. Register/Login
2. Select an appliance
3. Enter daily usage hours
4. View monthly energy consumption
5. Estimate electricity bill
6. Compare previous and current usage
7. Generate AI-powered energy-saving suggestions
8. Generate a complete AI Energy Report

---

## 🎯 Future Enhancements

- PDF Report Download
- Monthly Usage History
- Smart Home IoT Integration
- Voice Assistant
- Dark Mode
- Renewable Energy Suggestions

- ## Thank you 

