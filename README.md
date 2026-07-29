<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=220&section=header&text=Data%20Analyzer%20and%20Transformer&fontSize=38&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Functional%20Programming%20in%20Python%20%7C%20Red%20and%20White%20Skill%20Education&descAlignY=58&descSize=18" width="100%"/>

<br/>

<img src="https://readme-typing-svg.demolab.com/?font=Fira+Code&weight=600&size=24&duration=3000&pause=800&color=F75C7E&center=true&vCenter=true&width=650&lines=Analyze+1D+and+2D+Arrays+Like+a+Pro+%F0%9F%93%8A;Built+with+Recursion%2C+Lambdas+and+kwargs+%F0%9F%90%8D;Menu-Driven+%7C+Clean+%7C+Beginner-Friendly+%E2%9C%A8" alt="Typing SVG" />

<br/><br/>

<p>
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Made%20with-%E2%9D%A4-red?style=for-the-badge" />
</p>

<p>
  <img src="https://img.shields.io/github/stars/PalAnghan/Functional-Treat-RedandWhite-Python?style=social" />
  <img src="https://img.shields.io/github/forks/PalAnghan/Functional-Treat-RedandWhite-Python?style=social" />
  <img src="https://img.shields.io/github/watchers/PalAnghan/Functional-Treat-RedandWhite-Python?style=social" />
</p>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=25&section=header" width="100%"/>

</div>

<br/>

## 📋 Table of Contents

- [About the Project](#-about-the-project)
- [Demo Video](#-demo-video)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [How It Works](#-how-it-works)
- [Concepts Demonstrated](#-concepts-demonstrated)
- [Contributing](#-contributing)
- [Author](#-author)
- [License](#-license)

<br/>

## 📖 About the Project

> **Data Analyzer and Transformer** is a menu-driven Python console program built to demonstrate core **functional programming concepts** — built-in functions, user-defined functions, recursion, lambdas, `*args`/`**kwargs`, and the `global` keyword — all wrapped inside a clean, interactive data analysis tool.

This project was built as part of the **"Functional Treat"** assignment at **Red and White Skill Education**, and takes raw **1D** and **2D** array data and lets the user **analyze**, **filter**, and **sort** it — all from a single terminal menu.

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=25&section=header" width="100%"/>
</div>

<br/>

## 🎥 Demo Video

<div align="center">

<!-- 🎬 Paste your demo video link below once it's ready — YouTube link works great here! -->
<!-- Example: [![Watch the demo](https://img.youtube.com/vi/VIDEO_ID/0.jpg)](https://www.youtube.com/watch?v=VIDEO_ID) -->

> 🎬 **Demo video coming soon!** — will be added right here once recorded.

<img src="https://img.shields.io/badge/Video-Coming%20Soon-orange?style=for-the-badge&logo=youtube&logoColor=white" />

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=25&section=header" width="100%"/>

</div>

<br/>

## ✨ Features

<table>
<tr>
<td width="50%" valign="top">

### 🧮 Data Handling
- 📥 Input **1D** or **2D** array data
- 📊 Instant dataset summary (min, max, sum, avg)
- 🔁 Recursive factorial calculator
- 🧹 Filter data above/below a threshold with `lambda`

</td>
<td width="50%" valign="top">

### ⚙️ Under the Hood
- 🧩 User-defined functions for every task
- 📌 `global` keyword for shared state
- 🎒 `*args` and `**kwargs` powered statistics
- 🔀 Ascending / Descending sorting
- 📚 `__doc__` powered self-describing menu

</td>
</tr>
</table>

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=25&section=header" width="100%"/>
</div>

<br/>

## 🛠 Tech Stack

<div align="center">
  <img src="https://skillicons.dev/icons?i=python,git,github" />
</div>

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=25&section=header" width="100%"/>
</div>

<br/>

## 📂 Project Structure

```
Functional-Treat-RedandWhite-Python/
│
├── Functional Treat/
│   └── index.py        # Main program — all logic lives here
│
└── README.md            # You are here 👋
```

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=25&section=header" width="100%"/>
</div>

<br/>

## 🚀 Getting Started

### Prerequisites
- Python **3.10+** installed (uses `match-case`, added in 3.10)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/PalAnghan/Functional-Treat-RedandWhite-Python.git

# 2. Move into the project folder
cd "Functional-Treat-RedandWhite-Python/Functional Treat"

# 3. Run the program
python index.py
```

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=25&section=header" width="100%"/>
</div>

<br/>

## 🧭 How It Works

The program boots into a **main menu** loop where you choose a numbered option:

```
Menu:
1. Input Data
2. Display Data
3. Calculate Factorial
4. Filter Data
5. Sort Data
6. Display Dataset Statistics
7. Exit Program
```

Each option maps to a dedicated function, documented inline with a `__doc__` string that's printed the moment you select it — so the tool literally explains itself as you use it.

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=25&section=header" width="100%"/>
</div>

<br/>

## 🧠 Concepts Demonstrated

| Concept | Where It's Used |
|---|---|
| **Built-in Functions** | `len()`, `sum()`, `min()`, `max()` for instant stats |
| **User-Defined Functions** | Every menu option is its own dedicated function |
| **`*args` and `**kwargs`** | `display_dataset()` for flexible statistics printing |
| **`__doc__`** | Every function self-documents inside the menu |
| **Recursion** | `calculate_factorial()` |
| **Lambda Functions** | Threshold filtering with `filter()` |
| **`global` keyword** | Shared `OneDArray` / `TwoDArray` state across functions |
| **Sorting** | `sorted()` with ascending/descending toggle |
| **1D and 2D Collections** | `array` module for 1D, nested lists for 2D |

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=25&section=header" width="100%"/>
</div>

<br/>

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

```bash
1. Fork the project
2. Create your feature branch (git checkout -b feature/AmazingFeature)
3. Commit your changes (git commit -m 'Add some AmazingFeature')
4. Push to the branch (git push origin feature/AmazingFeature)
5. Open a Pull Request
```

<br/>

## 👤 Author

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=160&section=header" width="100%"/>

<img src="https://github.com/PalAnghan.png" width="110" style="border-radius:50%;border:3px solid #F75C7E;margin-top:-90px;"/>

### **Pal Anghan**

<img src="https://readme-typing-svg.demolab.com/?font=Fira+Code&weight=500&size=16&duration=2500&pause=700&color=888888&center=true&vCenter=true&width=420&lines=Final-Year+BCA+Student;Aspiring+AI-ML+Developer;Building+one+function+at+a+time" alt="Typing SVG" />

<br/>

<p>
  <a href="https://www.linkedin.com/in/pal-anghan"><img src="https://img.shields.io/badge/LinkedIn-Connect%20with%20me-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
  <a href="https://github.com/PalAnghan"><img src="https://img.shields.io/badge/GitHub-Follow%20me-181717?style=for-the-badge&logo=github&logoColor=white"/></a>
</p>

> *"Turning raw data into readable stories, one array at a time."*

<br/>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=100&section=footer&text=Thanks%20for%20Visiting&fontSize=18&fontColor=ffffff&animation=twinkling" width="100%"/>

</div>

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=25&section=header" width="100%"/>
</div>

<br/>

## 📄 License

This project is licensed under the **MIT License** — feel free to use, modify, and learn from it.

<br/>

<div align="center">

### ⭐ If this project helped you, consider giving it a star!

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=120&section=footer" width="100%"/>

</div>
