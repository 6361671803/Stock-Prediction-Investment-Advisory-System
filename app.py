# --------------------------------------------
# IMPORT LIBRARIES
# --------------------------------------------

import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
import matplotlib.pyplot as plt


# --------------------------------------------
# APP TITLE
# --------------------------------------------

st.title("📈 Stock Prediction & Investment Advisor")


# --------------------------------------------
# COMPANY DATA FILES
# --------------------------------------------

company_files = {
    "Apple": "apple stock.csv",
    "Tesla": "tesla stock.csv",
    "Reliance": "reliance stock.csv",
    "Google": "google stock.csv"
}

company = st.selectbox("Select Company", list(company_files.keys()))


# --------------------------------------------
# MAIN FUNCTION
# --------------------------------------------

def run_model(file):

    data = pd.read_csv(file)

    if 'Adj Close' in data.columns:
        data['Close'] = data['Adj Close']
    elif 'Close/Last' in data.columns:
        data['Close'] = data['Close/Last']
    elif 'close' in data.columns:
        data['Close'] = data['close']

    if isinstance(data['Close'], pd.DataFrame):
        data['Close'] = data['Close'].iloc[:, 0]

    data['Close'] = pd.to_numeric(data['Close'], errors='coerce')
    data = data.dropna()


    # FEATURE ENGINEERING
    data['MA'] = data['Close'].rolling(5).mean()

    data['Change'] = data['Close'].diff()
    data['Gain'] = data['Change'].apply(lambda x: x if x > 0 else 0)
    data['Loss'] = data['Change'].apply(lambda x: -x if x < 0 else 0)

    avg_gain = data['Gain'].rolling(5).mean()
    avg_loss = data['Loss'].rolling(5).mean()

    rs = avg_gain / avg_loss
    data['RSI'] = 100 - (100 / (1 + rs))

    data['Target'] = (data['Close'].shift(-1) > data['Close']).astype(int)

    data = data.dropna()


    # MODEL
    X = data[['RSI', 'MA']]
    y = data['Target']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = MLPClassifier(hidden_layer_sizes=(10,10), max_iter=500)
    model.fit(X_train, y_train)

    accuracy = round(model.score(X_test, y_test) * 100, 2)


    # PREDICTION
    latest = X.iloc[-1:]
    prediction = model.predict(latest)[0]

    if prediction == 1:
        decision = "📈 BUY"
    else:
        decision = "📉 DO NOT BUY"


    # INVESTMENT
    latest_price = data['Close'].iloc[-1]

    if prediction == 1:
        invest_amount = 10000
        shares = int(invest_amount / latest_price)
        investment_msg = f"You can invest ₹{invest_amount} and buy approx {shares} shares."
    else:
        investment_msg = "Not recommended to invest now."


    # TREND
    trend = "Uptrend 📈" if data['Close'].iloc[-1] > data['Close'].iloc[0] else "Downtrend 📉"

    high = round(data['Close'].max(), 2)
    low = round(data['Close'].min(), 2)


    # GRAPH EXPLANATION
    start_price = data['Close'].iloc[0]
    end_price = data['Close'].iloc[-1]
    max_price = data['Close'].max()
    min_price = data['Close'].min()
    current_price = data['Close'].iloc[-1]

    volatility = data['Close'].std()

    if end_price > start_price:
        graph_explanation = "📈 The stock price has generally increased over time."
    else:
        graph_explanation = "📉 The stock price has generally decreased over time."

    graph_explanation += f"\n\n🔝 Highest price: {round(max_price,2)}"
    graph_explanation += f"\n🔻 Lowest price: {round(min_price,2)}"

    if current_price > (max_price * 0.8):
        graph_explanation += "\n\n📊 Current price is near highest (expensive)."
    elif current_price < (min_price * 1.2):
        graph_explanation += "\n\n📊 Current price is near lowest (good buying chance)."
    else:
        graph_explanation += "\n\n📊 Current price is moderate."

    if volatility > 50:
        graph_explanation += "\n\n⚠️ High fluctuation (risky)."
    else:
        graph_explanation += "\n\n✅ Stable stock."

    graph_explanation += "\n\n💡 This graph shows how stock price changes over time."

    return data, accuracy, decision, investment_msg, trend, high, low, graph_explanation


# --------------------------------------------
# BUTTON
# --------------------------------------------

if st.button("Predict"):

    data, accuracy, decision, investment_msg, trend, high, low, graph_explanation = run_model(company_files[company])

    st.subheader(company)

    # GRAPH
    fig, ax = plt.subplots()
    ax.plot(data['Close'])
    ax.set_title("Stock Price Trend")
    ax.set_xlabel("Time (Days)")
    ax.set_ylabel("Stock Price")
    st.pyplot(fig)

    # AXIS EXPLANATION
    st.write("### 📌 Graph Axis Explanation")
    st.write("""
- X-axis → Time (days)
- Y-axis → Stock price
""")

    # RESULTS
    st.write("### 📊 Prediction Result")
    st.write(decision)

    st.write("### 💰 Investment Suggestion")
    st.write(investment_msg)

    st.write("### 📈 Analysis")
    st.write(f"Accuracy: {accuracy}%")
    st.write(f"Trend: {trend}")
    st.write(f"Highest Price: {high}")
    st.write(f"Lowest Price: {low}")

    st.write("### 📊 Graph Explanation")
    st.write(graph_explanation)

    # ==========================================================
    # 🆕 CURRENT RSI VALUE + MEANING (ADDED ONLY)
    # ==========================================================

    latest_rsi = data['RSI'].iloc[-1]

    st.write("### 📊 Current RSI Analysis")
    st.write(f"RSI Value: {round(latest_rsi,2)}")

    # Explain meaning of RSI value
    if latest_rsi < 30:
        st.write("📈 This value indicates the stock is OVERSOLD → price may increase → good time to buy.")
    elif latest_rsi > 70:
        st.write("📉 This value indicates the stock is OVERBOUGHT → price may decrease → be careful.")
    else:
        st.write("⚖️ This value indicates the stock is in NORMAL range → no strong buy/sell signal.")