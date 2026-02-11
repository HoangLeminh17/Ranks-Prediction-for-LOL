# 🎮 League of Legends Rank Prediction (v2.0)

An AI-powered rank prediction system using **Multivariate Polynomial Regression** with advanced game-logic validation and an interactive dashboard.

<p align="center">
  <img src="images/demo.gif" width="600">
</p>


## What's New in v2.0?

In this version, we moved beyond pure mathematics to incorporate **Domain Knowledge** (League of Legends mechanics) to solve the "illogical input" problem.

### Key Improvements:
* **Smart Gold Correction (Heuristic):** Prevents impossible scenarios (e.g., 15 kills with only 2000 gold) by calculating a "Minimum Realistic Gold" threshold based on passive income, kills, and minions.
* **Feature Clipping:** Utilizes $X_{min}$ and $X_{max}$ from the training set to prevent **unstable extrapolation** when users input extreme values.
* **Death Penalty Logic:** Implements a post-processing penalty for high death counts (>12 deaths) to accurately reflect the impact of "feeding" on player rank.
* **Interactive UI:** A fully functional dashboard built with **Streamlit** for real-time rank estimation.

---

## Project Structure

```text
Ranks-Prediction-for-LOL/
├── Processed_Final_Data/      # Individual processed text files for each rank
├── Raw_Ranks_data/           # Original raw data crawled via Riot API
├── Source_code/
│   ├── config.py             # Configuration and constants
│   ├── retrieve_data_step1.ipynb        # Data crawling script (Step 1)
│   ├── retrieve_process_data_step2.ipynb # Data cleaning script (Step 2)
│   ├── computer_project_step3.ipynb     # Model training & analysis logic (Step 3)
│   ├── app.py                # Main Streamlit web application (Step 4)
│   ├── model.npy             # Trained model weights (Theta)
│   ├── data_min.npy          # Feature minimums for clipping/scaling
│   ├── data_max.npy          # Feature maximums for clipping/scaling
│   └── .gitignore            
├── data.csv                  # Aggregated dataset from folder Processed_Final_Data
├── LICENSE                   # Project license (MIT)
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
└── Slide_MAI_Computing_...   # Project presentation slide (PDF - VNM)
```

### Installation & Usage
```text
git clone https://github.com/HoangLeminh17/Ranks-Prediction-for-LOL.git
cd Ranks-Prediction-for-LOL/Source_code
```
### 1. Create virtual environment
```text
conda create -n rank-prediction-LOL python=3.10
conda activate rank-prediction-LOL
```

### 2. Install Dependencies
```text
pip install -r requirements.txt
```

### 3. Run the Demo
```text
streamlit run app.py
```

### 📈 Methodology
The model utilizes a **2nd-degree Polynomial Design Matrix** to capture non-linear relationships between player statistics:

$$y = \theta_0 + \sum_{i=1}^{n} \theta_i x_i + \sum_{i=1}^{n} \sum_{j=i}^{n} \theta_{ij} x_i x_j$$

* **Inputs:** Kills, Deaths, Assists, Total Gold, Minions (CS).
* **Output:** Continuous Rank Score $[0.0 - 8.0]$ (Iron to Challenger).

---

### 🛠 Technical Highlights

| Feature | Description |
| :--- | :--- |
| **Input Validation** | Heuristic: $Gold_{min} = (K \times 250) + (A \times 100) + (M \times 18) + 3000$ |
| **Optimization** | Gradient Descent on a Quadratic Feature Space. |
| **Stability** | `np.clip` based on training distribution to handle outliers. |
| **UX** | Progress bar visualization for "Road to next Rank". |

---

### 📜 License
Distributed under the MIT License. See `LICENSE` for more information.

## 👥 Contributors

* **Hoang Le Minh** ([@HoangLeminh17](https://github.com/HoangLeminh17)) - Demo streamlit, improve model for Version 2.0, Crawling and processing data for Version 1.0
* **Ngọc Bảo** ([@ngocbaoo](https://github.com/ngocbaoo)) - Data Processing, Crawling data for Version 1.0
* **Nguyễn Đức Hoàng Phúc** ([@Nguyễn Đức Hoàng Phúc](https://github.com/somene112)) - Develop model for Version 1.0
* **Vũ Hải Đăng** ([@Vũ Hải Đăng](https://github.com/vudang142)) - Develop model for Version 1.0

Project Link: [https://github.com/HoangLeminh17/Ranks-Prediction-for-LOL](https://github.com/HoangLeminh17/Ranks-Prediction-for-LOL)
