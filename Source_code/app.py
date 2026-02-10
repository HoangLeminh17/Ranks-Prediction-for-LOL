import streamlit as st
import numpy as np


# --- LOAD DATA & MODELS ---
Ranks = {0: 'Iron', 1:'Bronze', 2:'Silver', 3:'Gold', 4:'Platinum', 
         5:'Diamond', 6:'Master', 7:'Grand Master', 8:'Challenger'}
theta = np.load('model.npy')
x_min = np.load('data_min.npy')
x_max = np.load('data_max.npy')

def predict_rank(input_data, theta, x_min, x_max):
    k, d, a, gold_raw, m = input_data
    passive_gold_estimate = 3000
    min_gold_calculated = (k * 250) + (a * 100) + (m * 18) + passive_gold_estimate
    gold_corrected = max(gold_raw, min_gold_calculated)
    corrected_input = np.array([k, d, a, gold_corrected, m])
    
    clean_input = np.clip(corrected_input, x_min, x_max)
    features = [1.0]
    features.extend(clean_input)
    n = len(clean_input)
    for i in range(n):
        for j in range(i, n):
            features.append(clean_input[i] * clean_input[j])
            
    prediction = np.array(features) @ theta
    if d > 12:
        prediction -= (d - 12) * 0.1
        
    return max(0.0, min(8.0, prediction))

# --- STREAMLIT UI ---
st.set_page_config(page_title="League Rank Predictor", page_icon="🎮")

st.title("🎮 Rank Prediction Dashboard")
st.markdown("Enter your match statistics to see your predicted Rank level.")

# Sidebar for inputs
st.sidebar.header("Player Statistics")
kills = st.sidebar.slider("Average Kills", 0, 40, 10)
deaths = st.sidebar.slider("Average Deaths", 0, 30, 5)
assists = st.sidebar.slider("Average Assists", 0, 40, 10)
gold = st.sidebar.number_input("Average Total Gold", min_value=0, max_value=50000, value=12000)
minions = st.sidebar.number_input("Average Minions (CS)", min_value=0, max_value=500, value=150)

# Predict Button
if st.button("Predict My Rank"):
    input_data = [kills, deaths, assists, gold, minions]
    
    score = predict_rank(input_data, theta, x_min, x_max)
    rank_idx = int(score)
    
    # Display Results
    st.divider()
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric(label="Predicted Rank", value=Ranks[rank_idx])
        st.write(f"Raw Model Score: **{score:.2f}**")
        
    with col2:
        if rank_idx < 8:
            progress = (score - rank_idx)
            st.write(f"Road to **{Ranks[rank_idx+1]}**")
            st.progress(progress)
            st.write(f"{progress*100:.1f}% completed")
        else:
            st.balloons()
            st.success("You are at the peak: Challenger!")

    # Logic Warning
    if gold < (kills * 250 + minions * 18 + 3000):
        st.warning("⚠️ Note: Your input gold was too low for these stats. The model used a corrected minimum gold value for logic consistency.")