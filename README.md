# 👔 The Shirt Project — Bespoke Men's Apparel Web App

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **"Crafted to Measure. Tailored for Distinction."**

**The Shirt Project** is a luxury, high-end bespoke men's fashion Streamlit application designed for elite bespoke tailors and luxury apparel houses. Built with custom CSS fashion catalog aesthetics, warm greige and deep slate palettes, gold accents, an interactive product catalog, a bespoke design studio with instant WhatsApp direct quote generation, and an atelier concierge booking widget.

---

## ✨ Features & Highlights

### 🎨 1. Luxury Brand Theme & Aesthetics
- **Curated Color Palette**: Warm Greige (`#EAE6DF`), Deep Slate (`#1A1D20`), Muted Gold (`#C5A059`), and Pure White (`#FFFFFF`).
- **Typography**: Google Fonts `@import` for **Cormorant Garamond** (Serif headers) and **Montserrat** (Modern body font).
- **Custom CSS Overrides**: Clean borderless Streamlit layout, custom tabs, luxury product cards, custom inputs, and button hover states.

### 🏛️ 2. The Atelier (Home Page)
- **SVG Brand Logo & Tagline Banner**.
- **Rotating Style Quotes Card**: Curated menswear quotes from Rachel Zoe, Giorgio Armani, Tom Ford, and Coco Chanel with an interactive **✨ Next Quote** button.
- **Brand Pillars Grid**: 4 feature cards (*Bespoke Fitting*, *Handpicked Fabrics*, *Artisanal Stitching*, *Personal Style Consultation*).
- **Craftsmanship Metrics**: Displaying 50+ handcraft steps, 500+ fabric options, and lifetime alteration guarantee.

### 👔 3. Interactive Apparel Catalog
Organized into sub-category tabs:
1. **Shirting**: Pure Egyptian Cotton, Premium Irish Linen, Executive Formals, Party Wear, Hand-Embroidered & Monogrammed.
2. **Suiting & Tuxedos**: 2-Piece & 3-Piece Bespoke Suits, Classic Black Tie Tuxedos, Italian Cut Blazers, Winter Wool Coats.
3. **Trousers & Bottoms**: Tailored Formal Trousers, Gurkha & Pleated Pants, Luxury Casual Chinos, Custom Linen Drawstring Pants.
4. **Style Statements**: Custom Nehru Jackets, Tuxedo Waistcoats, Bespoke Monogramming Details.
- Each item features high-resolution imagery, fabric details, and an **"Inquire"** button that pre-selects categories in the Bespoke Studio.

### ✂️ 4. Bespoke Studio (Custom Quote & WhatsApp Direct Generator)
- Interactive quote form collecting client name, WhatsApp number, email, multi-select categories, and preferred fabric notes.
- `st.file_uploader` for clients to upload photos or style inspiration.
- **Instant Direct WhatsApp Generator**: Automatically formats a structured bespoke request message and generates a direct `https://wa.me/` link for 1-click messaging to WhatsApp Business.

### 📍 5. Contact & Concierge
- Flagship Atelier details (Savile Row Mayfair Suite).
- Interactive fitting appointment reservation scheduler.
- Bespoke Care FAQ accordion.

---

## 📁 Repository Structure

```text
The Shirt Project/
├── .github/
│   └── workflows/
│       └── ci.yml              # CI/CD Python syntax check workflow
├── .streamlit/
│   └── config.toml           # Custom Streamlit theme configuration
├── app.py                     # Main Streamlit application
├── requirements.txt           # Python dependencies
├── Dockerfile                 # Container deployment specification
├── .dockerignore              # Docker build ignore rules
├── .gitignore                 # Git ignore rules
├── LICENSE                    # MIT License
└── README.md                  # Project documentation
```

---

## 🚀 Quick Start (Local Setup)

### Prerequisites
- Python 3.8+ installed on your system.

### 1. Clone or Download Repository
```bash
git clone https://github.com/your-username/the-shirt-project.git
cd the-shirt-project
```

### 2. Create Virtual Environment (Optional but recommended)
```bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit Application
```bash
streamlit run app.py
```
Open your browser at `http://localhost:8501`.

---

## ☁️ How to Deploy on GitHub & Streamlit Community Cloud (Free)

### Step 1: Push Project to GitHub

1. Initialize Git repository and commit files:
   ```bash
   git init
   git add .
   git commit -m "Initial commit - The Shirt Project Bespoke App"
   ```

2. Create a new repository on [GitHub](https://github.com/new) named `the-shirt-project`.

3. Connect local repo and push to GitHub:
   ```bash
   git remote add origin https://github.com/YOUR_GITHUB_USERNAME/the-shirt-project.git
   git branch -M main
   git push -u origin main
   ```

### Step 2: Deploy on Streamlit Community Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io/) and log in with your GitHub account.
2. Click **New app**.
3. Select your repository `YOUR_GITHUB_USERNAME/the-shirt-project`.
4. Set **Main file path** to `app.py`.
5. Click **Deploy!** 🎉

Your luxury website will be live with an SSL certificate (`https://<your-app-name>.streamlit.app`).

---

## 🐳 Docker Deployment

To build and run using Docker:

```bash
# Build Docker image
docker build -t the-shirt-project .

# Run Docker container
docker run -p 8501:8501 the-shirt-project
```

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

Crafted with ❤️ for **The Shirt Project**.
