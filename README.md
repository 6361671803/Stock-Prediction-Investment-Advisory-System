# 📈 Stock Prediction & Investment Advisory System

## 🧠 Overview

The **Stock Prediction & Investment Advisory System** is a machine learning-based application designed to help users make better investment decisions. The system analyzes historical stock data using a **Neural Network model (MLPClassifier)** and predicts whether a stock price is likely to increase or decrease.

In addition to prediction, the system provides:

* 📊 Investment suggestions
* 📈 Graph visualization
* 🧾 Graph explanation (trend, volatility, price levels)
* 📉 RSI (Relative Strength Index) analysis

This makes the system useful for both beginners and intermediate users.

---

## 🎯 Objectives

* Predict stock price movement (Up/Down)
* Provide investment recommendation (Buy / Do Not Buy)
* Calculate approximate number of shares based on budget
* Analyze stock trends using indicators:

  * Moving Average (MA)
  * Relative Strength Index (RSI)
* Display stock trends using graphs
* Explain graph and RSI values in simple language

---

## ⚙️ Technologies Used

* **Python** – Core programming language
* **Streamlit** – Web UI framework
* **Pandas** – Data processing
* **Scikit-learn** – Machine learning (Neural Network)
* **Matplotlib** – Graph visualization

---

## 🏗️ System Architecture

The system follows this workflow:

```
Data Collection → Data Preprocessing → Feature Engineering → Model Training → Prediction → Investment Suggestion → Visualization → Explanation
```

---

## 🔍 Methodology

### 1. Data Collection

Historical stock data is collected in CSV format. The main attribute used is the **closing price**, which reflects the final value of a stock for a given day.

### 2. Data Preprocessing

* Removes missing values
* Converts data into numerical format
* Selects relevant columns

### 3. Feature Engineering

#### 📊 Moving Average (MA)

* Calculates average price over a fixed period
* Helps identify trend direction

#### 📉 Relative Strength Index (RSI)

* Measures momentum of price movement
* Values range from 0 to 100

  * RSI < 30 → Oversold (Buy signal)
  * RSI > 70 → Overbought (Sell signal)

### 4. Model Training

* Uses **MLPClassifier (Neural Network)**
* Input features: RSI, Moving Average
* Target:

  * 1 → Price increases
  * 0 → Price decreases

### 5. Prediction

The model predicts whether the stock will:

* 📈 Increase → BUY
* 📉 Decrease → DO NOT BUY

### 6. Investment Suggestion

* Suggests a sample investment amount (₹10000)
* Calculates number of shares based on current price

### 7. Visualization

* Uses a **line graph**
* X-axis → Time
* Y-axis → Stock price

### 8. Graph Explanation

The system explains:

* Trend (up/down)
* Highest & lowest price
* Current price position
* Volatility (risk level)

### 9. RSI Interpretation

Displays current RSI value and explains:

* Oversold → Good buying opportunity
* Overbought → Risk of price drop
* Normal → Stable

---

## 📁 Project Structure

```
StockPrediction/
│
├── app.py                # Main application
├── AAPL.csv              # Apple dataset
├── TSLA.csv              # Tesla dataset
├── RELIANCE.csv          # Reliance dataset
├── GOOGL.csv             # Google dataset
├── requirements.txt      # Dependencies
└── README.md             # Project documentation
```

---

## ▶️ How to Run the Project

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/stock-prediction-advisor.git
cd stock-prediction-advisor
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Application

```bash
streamlit run app.py
```

### 4. Open in Browser

```
http://localhost:8501
```

---

## 📊 Output

The system provides:

* 📈 Prediction Result (Buy / Do Not Buy)
* 💰 Investment Suggestion
* 📊 Stock Price Graph
* 📌 Graph Explanation
* 📉 RSI Value with Meaning

---

## 🧪 Example Output

```
Decision: BUY  
Investment: ₹10000 → 20 shares  
Trend: Uptrend  
RSI Value: 65 → Normal Range  
```

---

## 🚀 Features

* ✔ Neural Network-based prediction
* ✔ Real-time user interaction (Streamlit UI)
* ✔ Graph + explanation (not just visualization)
* ✔ RSI interpretation
* ✔ Investment guidance

---

## 🔮 Future Scope

* Integration with real-time stock APIs
* Use of advanced deep learning models (LSTM)
* Add more indicators (MACD, Bollinger Bands)
* Deployment as web/mobile application
* Personalized investment recommendations

---

## 👨‍💻 Author

**Your Name**:mohammed fahad
Stock Prediction & Investment Advisory System Project

---

## 📌 Conclusion

This project demonstrates how machine learning can be applied to financial data to assist in decision-making. By combining prediction, visualization, and explanation, the system makes stock analysis simple, understandable, and practical.

---

⭐ If you like this project, consider giving it a star on GitHub!
