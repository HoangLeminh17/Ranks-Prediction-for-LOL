# 🎮 League of Legends Rank Prediction (v2.0)

An AI-powered rank prediction system using **Multivariate Polynomial Regression** with advanced game-logic validation and an interactive dashboard.



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
├── Source_code/
│   ├── app.py              # Streamlit Web Application
│   ├── model_logic.py      # Core prediction & logic functions
│   └── weights/            # Saved theta, x_min, x_max (.npy files)
├── Data/                   # Aggregated dataset from Processed_Final_Data
├── README.md               # Documentation
└── requirements.txt        # Python dependencies

### Installation & Usage
`git clone [https://github.com/your-username/Ranks-Prediction-for-LOL.git](https://github.com/your-username/Ranks-Prediction-for-LOL.git)
cd Ranks-Prediction-for-LOL/Source_code`

### 2. Install Dependencies
`pip install -r ../requirements.txt`

### 3. Run the Demo
`streamlit run app.py`

### Methodology
The model uses a 2nd-degree Polynomial Design Matrix to capture the non-linear relationship between player stats:$$y = \theta_0 + \sum \theta_i x_i + \sum \theta_{ij} x_i x_j$$Inputs: Kills, Deaths, Assists, Total Gold, Minions (CS).Output: Continuous Rank Score [0.0 - 8.0] (Iron to Challenger).

### Technical Highlights
Feature,Description
Input Validation,Heuristic formula: Goldmin​=(K×250)+(A×100)+(M×18)+3000
Optimization,Gradient Descent on a Quadratic Feature Space.
Stability,np.clip based on training distribution to handle outliers.
UX,"Progress bar visualization for ""Road to next Rank""."

📝 Author
Hoang - Initial work & v2.0 Logic - @HoangLeminh17
