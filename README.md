# 🔢 Name Numerology App (Chaldean System)

A simple web application built using **Streamlit** that calculates:

- 🔮 Name Numerology Number (Chaldean System)
- 🌟 Destiny Number (Based on Birth Date)

This project demonstrates Python logic implementation, Streamlit UI development, and optional Docker-based deployment.

---

## 🚀 Features

- Accepts user name input
- Accepts birth date (day, month, year)
- Calculates Name Numerology Number
- Calculates Destiny Number
- Reduces numbers to a single digit (1–9)
- Displays styled results

---

## 🛠️ Tech Stack

- Python 3.x
- Streamlit
- Docker (optional)

---

## 🔢 Numerology Logic

### 1️⃣ Chaldean Numerology Chart

| Number | Letters |
|--------|----------|
| 1 | A, I, J, Q, Y |
| 2 | B, K, R |
| 3 | C, G, L, S |
| 4 | D, M, T |
| 5 | E, H, N, X |
| 6 | U, V, W |
| 7 | O, Z |
| 8 | F, P |

---

### 2️⃣ Name Number Calculation

1. Convert name to uppercase  
2. Map each character to numeric value  
3. Sum all values  
4. Reduce result to a single digit  

---

### 3️⃣ Destiny Number Calculation

1. Add birth date + month + year  
2. Reduce repeatedly until a single digit is obtained  

---

## 📂 Project Structure

```
StreamlitNumerology/
│
├── app.py
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/Numerology-app.git
cd Numerology-app/StreamlitNumerology
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Run the App

```bash
streamlit run app.py
```

Open in browser:

```
http://localhost:8501
```

---

## 🐳 Run Using Docker (Optional)

### Build Docker Image

```bash
docker build -t numerology-app .
```

### Run Container

```bash
docker run -p 8501:8501 numerology-app
```

---

## 📦 requirements.txt

```
streamlit
```

---

## 🧠 Core Function

```python
def reduce_to_single_digit(number):
    total = sum(int(d) for d in str(number))
    while total > 9:
        total = sum(int(d) for d in str(total))
    return total
```

---

## ⚠️ Important Note

For correct Destiny Number calculation, ensure birth inputs are converted to integers before addition:

```python
bnum = reduce_to_single_digit(int(bdate) + int(bmonth) + int(byear))
```

---

## 🔮 Possible Improvements

- Add input validation
- Use date picker instead of text input
- Add numerology meaning descriptions
- Improve UI styling
- Add error handling
- Deploy on Streamlit Cloud

---

## 📄 License

This project is open source and available under the MIT License.

---

## 👩‍💻 Author

Prachi Ballal  

---

⭐ If you found this project useful, consider giving it a star!
