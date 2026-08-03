import streamlit as st
import streamlit.components.v1 as components
import urllib.parse
from datetime import datetime
import time

# ==========================================
# PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="The Shirt Project | Luxury Bespoke Atelier",
    page_icon="👔",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize Session States
if 'current_quote_idx' not in st.session_state:
    st.session_state.current_quote_idx = 0

if 'last_quote_time' not in st.session_state:
    st.session_state.last_quote_time = time.time()

if 'selected_categories' not in st.session_state:
    st.session_state.selected_categories = ["Shirting"]

if 'config_collar' not in st.session_state:
    st.session_state.config_collar = "Italian Cutaway"

if 'config_cuff' not in st.session_state:
    st.session_state.config_cuff = "French Double Cuff (Cufflinks)"

if 'config_fit' not in st.session_state:
    st.session_state.config_fit = "Slim Bespoke Contour"

# ==========================================
# BRAND AESTHETICS & CUSTOM CSS INJECTION
# ==========================================
custom_css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400;1,600&family=Montserrat:wght@200;300;400;500;600;700&display=swap');

/* Color Variables */
:root {
    --sand: #EAE6DF;
    --sand-light: #F7F5F0;
    --sand-dark: #D4CEBF;
    --charcoal: #1A1D20;
    --charcoal-light: #25292E;
    --gold: #C5A059;
    --gold-bright: #D4AF37;
    --gold-glow: rgba(197, 160, 89, 0.25);
    --white: #FFFFFF;
}

/* Hide default Streamlit elements */
header[data-testid="stHeader"] {
    visibility: hidden;
    height: 0px;
}
footer {
    visibility: hidden;
    height: 0px;
}
.stDeployButton {
    display: none;
}

/* Main Container Adjustments */
#root .block-container {
    padding-top: 1.2rem;
    padding-bottom: 5rem;
    padding-left: 2.5rem;
    padding-right: 2.5rem;
    max-width: 1400px;
/* Global Text Overflow Protection & Responsive Typography */
*, *:before, *:after {
    box-sizing: border-box !important;
}

p, div, h1, h2, h3, h4, h5, h6, span, label, a {
    overflow-wrap: break-word !important;
    word-wrap: break-word !important;
    max-width: 100% !important;
}

/* Typography & Light Page High Contrast Rules */
html, body, [class*="css"], .stMarkdown {
    font-family: 'Montserrat', sans-serif;
    color: #1A1D20 !important;
    -webkit-text-fill-color: #1A1D20 !important;
    background-color: #F7F5F0;
}

h1, h2, h3, h4, h5, h6, .brand-font {
    font-family: 'Cormorant Garamond', serif !important;
    color: #1A1D20 !important;
    -webkit-text-fill-color: #1A1D20 !important;
    letter-spacing: 0.06em;
}

/* Form Input Labels & Descriptions on Light Backgrounds */
label, label p, label span, .stTextInput label p, .stSelectbox label p {
    color: #1A1D20 !important;
    -webkit-text-fill-color: #1A1D20 !important;
    font-weight: 700 !important;
    font-size: 0.98rem !important;
}

/* Metric Display Styling - Golden Brown Labels & Dark Slate Values */
[data-testid="stMetricLabel"], 
[data-testid="stMetricLabel"] p,
[data-testid="stMetricLabel"] span {
    color: #8A6D3B !important;
    -webkit-text-fill-color: #8A6D3B !important;
    font-size: 1.05rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.05em;
}

[data-testid="stMetricValue"], 
[data-testid="stMetricValue"] div,
[data-testid="stMetricValue"] span {
    color: #1A1D20 !important;
    -webkit-text-fill-color: #1A1D20 !important;
    font-size: 2.3rem !important;
    font-weight: 800 !important;
}

/* Selectbox Input Box & Popover Dropdown Menu Styling - Dark Slate & Gold */
[data-baseweb="select"] > div,
div[data-baseweb="select"] *,
div[data-baseweb="select"] span,
div[data-baseweb="select"] div {
    background-color: #1A1D20 !important;
    color: #C5A059 !important;
    -webkit-text-fill-color: #C5A059 !important;
    border-color: #C5A059 !important;
    font-weight: 700 !important;
}

[data-baseweb="popover"],
[data-baseweb="popover"] *,
[data-baseweb="menu"],
[data-baseweb="menu"] *,
ul[role="listbox"],
ul[role="listbox"] *,
li[role="option"] {
    background-color: #1A1D20 !important;
    color: #C5A059 !important;
    -webkit-text-fill-color: #C5A059 !important;
}

li[role="option"] *,
div[role="option"] * {
    color: #C5A059 !important;
    -webkit-text-fill-color: #C5A059 !important;
    font-weight: 600 !important;
}

li[role="option"]:hover,
li[role="option"][aria-selected="true"],
div[role="option"]:hover {
    background-color: #C5A059 !important;
    color: #1A1D20 !important;
    -webkit-text-fill-color: #1A1D20 !important;
}

/* Toast Notifications - Black/Dark Slate Background & Metallic Gold Text */
/* Streamlit Top Header Bar - Solid Pitch Black with Metallic Gold Text */
header,
[data-testid="stHeader"],
.stHeader,
div[data-testid="stHeader"] {
    background-color: #000000 !important;
    background: #000000 !important;
    color: #C5A059 !important;
    -webkit-text-fill-color: #C5A059 !important;
    border-bottom: 2px solid #C5A059 !important;
}

header *,
[data-testid="stHeader"] * {
    color: #C5A059 !important;
    fill: #C5A059 !important;
    -webkit-text-fill-color: #C5A059 !important;
}

[data-testid="stToast"],
div[data-baseweb="toast"],
.stToast,
[data-baseweb="toast"] > div,
[data-baseweb="toast"] * {
    background-color: #1A1D20 !important;
    background: #1A1D20 !important;
    border: 1.5px solid #C5A059 !important;
    color: #C5A059 !important;
    -webkit-text-fill-color: #C5A059 !important;
    box-shadow: 0 10px 30px rgba(0,0,0,0.6) !important;
    border-radius: 10px !important;
    font-family: 'Cormorant Garamond', serif !important;
    font-weight: 700 !important;
    font-size: 1.1rem !important;
}

/* Custom Styled Sidebar with Bright Metallic Gold Text Rules */
[data-testid="stSidebar"],
[data-testid="stSidebar"] div[data-testid="stSidebarUserContent"],
[data-testid="stSidebar"] section {
    --text-color: #C5A059 !important;
    --primary-color: #C5A059 !important;
    background-color: #1A1D20 !important;
    background: #1A1D20 !important;
    border-right: 2px solid #C5A059 !important;
    color: #C5A059 !important;
    -webkit-text-fill-color: #C5A059 !important;
}

[data-testid="stSidebar"] *,
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] span,
[data-testid="stSidebar"] div,
[data-testid="stSidebar"] a,
[data-testid="stSidebar"] li,
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] label p,
[data-testid="stSidebar"] label span,
[data-testid="stSidebar"] strong,
[data-testid="stSidebar"] summary,
[data-testid="stSidebar"] summary *,
[data-testid="stSidebar"] summary span,
[data-testid="stSidebar"] summary div,
[data-testid="stSidebar"] details,
[data-testid="stSidebar"] details *,
[data-testid="stSidebar"] [data-testid="stExpander"],
[data-testid="stSidebar"] [data-testid="stExpander"] *,
[data-testid="stSidebar"] [data-testid="stMarkdownContainer"],
[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] *,
[data-testid="stSidebar"] .stMarkdown,
[data-testid="stSidebar"] .stMarkdown *,
[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3,
[data-testid="stSidebar"] h4,
[data-testid="stSidebar"] h5,
[data-testid="stSidebar"] h6 {
    color: #C5A059 !important;
    fill: #C5A059 !important;
    -webkit-text-fill-color: #C5A059 !important;
    opacity: 1 !important;
    visibility: visible !important;
}

[data-testid="stSidebar"] [data-baseweb="select"] *,
[data-testid="stSidebar"] [data-baseweb="select"] div,
[data-testid="stSidebar"] [data-baseweb="select"] span {
    color: #C5A059 !important;
    -webkit-text-fill-color: #C5A059 !important;
    background-color: #1A1D20 !important;
}

/* Main Navigation Tabs - Dark Emerald & Gold */
.stTabs [data-baseweb="tab-list"] {
    gap: 1rem;
    justify-content: center;
    background-color: #0D2E24 !important;
    padding: 0.8rem 1.2rem;
    border-radius: 12px;
    border: 1.5px solid #C5A059;
    margin-bottom: 2.2rem;
    box-shadow: 0 10px 30px rgba(0,0,0,0.25);
}

.stTabs [data-baseweb="tab"] {
    height: 3.5rem;
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.35rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    color: #C5A059 !important;
    -webkit-text-fill-color: #C5A059 !important;
    background-color: transparent;
    border-radius: 8px;
    padding: 0 1.8rem;
    transition: all 0.3s ease;
}

.stTabs [data-baseweb="tab"]:hover {
    background-color: rgba(197, 160, 89, 0.2) !important;
    color: #FFFFFF !important;
    -webkit-text-fill-color: #FFFFFF !important;
}

.stTabs [aria-selected="true"] {
    background-color: #C5A059 !important;
    color: #0D2E24 !important;
    -webkit-text-fill-color: #0D2E24 !important;
    font-weight: 800 !important;
    box-shadow: 0 6px 22px rgba(197, 160, 89, 0.4) !important;
}

/* Cards & Elevated Glass Elements */
.brand-card {
    background: #FFFFFF;
    border: 1px solid #EAE6DF;
    border-top: 3px solid #C5A059;
    border-radius: 12px;
    padding: 2rem;
    margin-bottom: 1.8rem;
    box-shadow: 0 8px 25px rgba(0,0,0,0.04);
    transition: all 0.35s ease;
}

.brand-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 35px rgba(0,0,0,0.09);
}

.pillar-card {
    background: linear-gradient(145deg, #1A1D20 0%, #24282D 100%) !important;
    color: #C5A059 !important;
    -webkit-text-fill-color: #C5A059 !important;
    padding: 2.2rem 1.4rem;
    border-radius: 12px;
    text-align: center;
    border: 1.5px solid #C5A059;
    height: 100%;
    transition: all 0.35s ease;
    box-shadow: 0 6px 20px rgba(0,0,0,0.2);
}

.pillar-card:hover {
    border-color: #C5A059;
    transform: translateY(-5px);
    box-shadow: 0 12px 30px rgba(197, 160, 89, 0.35);
}

.pillar-card *,
.pillar-icon,
.pillar-title,
.pillar-desc {
    color: #C5A059 !important;
    -webkit-text-fill-color: #C5A059 !important;
    opacity: 1 !important;
}

.pillar-icon {
    font-size: 2.5rem;
    margin-bottom: 1rem;
}

.pillar-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.55rem;
    font-weight: 700;
    letter-spacing: 0.06em;
    margin-bottom: 0.6rem;
}

.pillar-desc {
    font-size: 0.9rem;
    line-height: 1.6;
}

/* Fashion Quote Banner */
.quote-banner {
    background: linear-gradient(135deg, #1A1D20 0%, #2B3037 100%) !important;
    border: 1.5px solid #C5A059 !important;
    padding: 2.5rem 2.2rem;
    border-radius: 14px;
    text-align: center;
    margin: 1rem 0 2.5rem 0;
    position: relative;
    box-shadow: 0 10px 30px rgba(0,0,0,0.35) !important;
}

.quote-symbol {
    font-family: 'Cormorant Garamond', serif;
    font-size: 3.5rem;
    color: #C5A059 !important;
    -webkit-text-fill-color: #C5A059 !important;
    line-height: 0;
    display: block;
    margin-bottom: 1.2rem;
}

.quote-content,
.quote-banner .quote-content {
    font-family: 'Cormorant Garamond', serif !important;
    font-size: 1.85rem !important;
    font-style: italic !important;
    color: #C5A059 !important;
    -webkit-text-fill-color: #C5A059 !important;
    margin-bottom: 0.9rem !important;
    line-height: 1.38 !important;
    opacity: 1 !important;
}

.quote-author,
.quote-banner .quote-author {
    font-family: 'Montserrat', sans-serif !important;
    font-size: 0.95rem !important;
    color: #C5A059 !important;
    -webkit-text-fill-color: #C5A059 !important;
    letter-spacing: 0.25em !important;
    text-transform: uppercase !important;
    font-weight: 700 !important;
    opacity: 1 !important;
}

/* Product Card Styling */
.product-card {
    background: #FFFFFF;
    border-radius: 12px;
    border: 1px solid #EAE6DF;
    overflow: hidden;
    margin-bottom: 1.8rem;
    box-shadow: 0 5px 20px rgba(0,0,0,0.04);
    transition: all 0.35s ease;
    height: 100%;
    display: flex;
    flex-direction: column;
}

.product-card:hover {
    transform: translateY(-6px);
    box-shadow: 0 14px 35px rgba(0,0,0,0.1);
    border-color: #C5A059;
}

.product-img {
    width: 100%;
    height: 250px;
    object-fit: cover;
    border-bottom: 1px solid #EAE6DF;
}

.product-info {
    padding: 1.5rem;
    flex-grow: 1;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.product-tag {
    font-size: 0.75rem;
    font-weight: 700;
    color: #C5A059;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    margin-bottom: 0.4rem;
}

.product-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.6rem;
    font-weight: 700;
    color: #1A1D20;
    margin-bottom: 0.5rem;
    line-height: 1.2;
}

.product-desc {
    font-size: 0.88rem;
    color: #555555;
    line-height: 1.55;
    margin-bottom: 1.2rem;
}

.product-meta {
    font-size: 0.8rem;
    color: #888888;
    border-top: 1px dashed #EAE6DF;
    padding-top: 0.8rem;
    margin-bottom: 1.2rem;
}

/* Custom Buttons Styling - Clean Single Outer Gold Border & Perfect Equal Alignment */
.stButton > button {
    background-color: #1A1D20 !important;
    background: #1A1D20 !important;
    color: #C5A059 !important;
    -webkit-text-fill-color: #C5A059 !important;
    border: 1.5px solid #C5A059 !important;
    font-family: 'Montserrat', sans-serif !important;
    font-size: 0.88rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.08em !important;
    text-transform: uppercase !important;
    padding: 0.9rem 1.4rem !important;
    border-radius: 8px !important;
    transition: all 0.35s ease !important;
    width: 100%;
    white-space: normal !important;
    word-break: keep-all !important;
    line-height: 1.35 !important;
    box-shadow: 0 4px 15px rgba(0,0,0,0.2) !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    min-height: 3.8rem !important;
    text-align: center !important;
}

.stButton > button *,
.stButton > button p,
.stButton > button span,
.stButton > button div {
    border: none !important;
    background: transparent !important;
    box-shadow: none !important;
    outline: none !important;
    color: #C5A059 !important;
    -webkit-text-fill-color: #C5A059 !important;
}

.stButton > button:hover {
    background-color: #C5A059 !important;
    background: #C5A059 !important;
    border-color: #C5A059 !important;
    box-shadow: 0 6px 22px rgba(197, 160, 89, 0.45) !important;
    transform: translateY(-2px);
}

.stButton > button:hover *,
.stButton > button:hover p,
.stButton > button:hover span {
    color: #1A1D20 !important;
    -webkit-text-fill-color: #1A1D20 !important;
}

/* Expanders Styling */
.stExpander,
[data-testid="stExpander"],
[data-testid="stExpander"] details,
[data-testid="stExpander"] summary,
[data-testid="stExpander"] summary *,
[data-testid="stExpander"] p,
[data-testid="stExpander"] span {
    color: #C5A059 !important;
    -webkit-text-fill-color: #C5A059 !important;
    font-weight: 700 !important;
    opacity: 1 !important;
}

/* Form Controls & Inquiry Box Typed Text Styling - Metallic Gold */
.stTextInput input, 
.stTextArea textarea, 
.stSelectbox > div > div,
input[type="text"],
textarea,
div[data-baseweb="input"] input,
div[data-baseweb="textarea"] textarea {
    border: 1.5px solid #C5A059 !important;
    background-color: #1A1D20 !important;
    color: #C5A059 !important;
    -webkit-text-fill-color: #C5A059 !important;
    border-radius: 6px !important;
    font-family: 'Montserrat', sans-serif !important;
    font-weight: 600 !important;
    font-size: 1rem !important;
}

.stTextInput input::placeholder,
.stTextArea textarea::placeholder,
input::placeholder,
textarea::placeholder {
    color: rgba(197, 160, 89, 0.65) !important;
    -webkit-text-fill-color: rgba(197, 160, 89, 0.65) !important;
}

.stTextInput input:focus, 
.stTextArea textarea:focus {
    border-color: #C5A059 !important;
    box-shadow: 0 0 12px rgba(197, 160, 89, 0.45) !important;
}

/* WhatsApp Direct Button */
.whatsapp-direct-btn {
    display: block;
    width: 100%;
    background-color: #25D366;
    color: #FFFFFF !important;
    text-align: center;
    padding: 1rem 1.5rem;
    font-family: 'Montserrat', sans-serif;
    font-size: 0.98rem;
    font-weight: 700;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    text-decoration: none !important;
    border-radius: 6px;
    margin-top: 1.4rem;
    box-shadow: 0 5px 20px rgba(37, 211, 102, 0.38);
    transition: all 0.35s ease;
}

.whatsapp-direct-btn:hover {
    background-color: #1EBE57;
    color: #FFFFFF !important;
    transform: translateY(-3px);
    box-shadow: 0 8px 25px rgba(37, 211, 102, 0.5);
}

/* Configurator Preview Box - Sleek Single Luxury Card */
.configurator-preview {
    background: #1A1D20 !important;
    border: 1.5px solid #C5A059 !important;
    border-radius: 12px !important;
    padding: 1.8rem 1.5rem !important;
    text-align: center !important;
    margin-bottom: 1.8rem !important;
    box-shadow: 0 10px 30px rgba(0,0,0,0.3) !important;
}

.configurator-preview div,
.configurator-preview span,
.configurator-preview strong {
    border: none !important;
    background: transparent !important;
    outline: none !important;
    box-shadow: none !important;
}

.configurator-badge {
    display: inline-block !important;
    background: transparent !important;
    border: 1px solid #C5A059 !important;
    color: #C5A059 !important;
    -webkit-text-fill-color: #C5A059 !important;
    font-weight: 700 !important;
    font-size: 0.8rem !important;
    letter-spacing: 0.18em !important;
    text-transform: uppercase !important;
    padding: 0.35rem 1.2rem !important;
    border-radius: 50px !important;
    margin-bottom: 1rem !important;
}
    padding: 0.3rem 0.8rem;
    border-radius: 20px;
    text-transform: uppercase;
    letter-spacing: 0.15em;
    margin-bottom: 0.8rem;
}

/* Summary Badge */
.summary-badge {
    background: #F7F5F0;
    border-left: 5px solid #C5A059;
    padding: 1.4rem 1.6rem;
    border-radius: 8px;
    margin: 1rem 0;
    box-shadow: 0 4px 15px rgba(0,0,0,0.03);
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Helper function for Sartorial Genie AI Style Assistant
def query_sartorial_genie(prompt):
    prompt_lower = prompt.lower()
    if any(w in prompt_lower for w in ["summer", "linen", "hot", "breathable", "casual", "beach"]):
        return "🌿 **Summer & Casual Luxury Recommendation:**\nFor warm weather or resort elegance, we highly recommend our **100% Pure Vintage Irish Linen** or **200s Giza Egyptian Cotton** shirts paired with **Custom Linen Drawstring Pants**."
    elif any(w in prompt_lower for w in ["wedding", "gala", "tuxedo", "party", "formal", "suit", "groom"]):
        return "🎩 **Gala & Wedding Recommendation:**\nFor grand evening galas or weddings, opt for our **Classic Black Tie Tuxedo** with satin peak lapels or a **Custom Raw Silk Nehru Jacket** with hand-embroidered monogramming."
    elif any(w in prompt_lower for w in ["time", "duration", "days", "how long", "fitting", "stitch"]):
        return "⏱️ **Bespoke Timeline & Fitting Guide:**\nOur master tailors take 2 to 3 weeks for 30-point pattern drafting, hand-cutting, and pick-stitching. Urgent gala requests can be expedited in **7-Day Express Bespoke**."
    elif any(w in prompt_lower for w in ["contact", "jatin", "founder", "address", "location", "jammu", "phone", "number"]):
        return "👑 **Founder Concierge Info:**\nReach **Founder Mr. Jatin Gupta** directly at **+91 8717070570** or visit **264-A, Raj Tilak Road, Jammu**."
    else:
        return "👔 **Sartorial Genie Guidance:**\nEvery garment at *The Shirt Project* is 100% custom-crafted. Explore our **Sartorial Vault** catalog or use our **Bespoke Design Suite** live configurator to customize your collar, cuff, and contour fit!"

# ==========================================
# SIDEBAR NAVIGATION & QUICK ACTIONS TOGGLE
# ==========================================
with st.sidebar:
    st.markdown("""
    <div style="background: #1A1D20; border-radius: 12px; padding: 1.5rem 1rem; margin-bottom: 1.5rem; border: 1.5px solid #C5A059; text-align: center; box-shadow: 0 8px 25px rgba(0,0,0,0.35);">
        <svg viewBox="0 0 300 170" width="160" height="90" xmlns="http://www.w3.org/2000/svg" style="margin-bottom: 0.3rem;">
            <!-- Golden Coat Hanger Hook -->
            <path d="M 150 18 C 132 18 122 35 138 55 C 145 65 148 71 150 82" fill="none" stroke="#C5A059" stroke-width="6" stroke-linecap="round"/>
            <!-- Golden Outer Hanger Frame -->
            <path d="M 150 82 L 45 125 C 32 130 32 145 45 150 L 105 150 M 150 82 L 255 125 C 268 130 268 145 255 150 L 195 150" fill="none" stroke="#C5A059" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>
            <!-- Golden Monogram TSP -->
            <path d="M 130 118 C 112 108 112 132 138 140 C 152 145 142 165 125 158 C 112 154 108 143 108 143" fill="none" stroke="#C5A059" stroke-width="5" stroke-linecap="round"/>
            <path d="M 152 115 C 178 115 182 138 152 145 L 152 165" fill="none" stroke="#C5A059" stroke-width="5" stroke-linecap="round"/>
            <path d="M 138 110 L 162 110 M 150 110 L 150 165" fill="none" stroke="#C5A059" stroke-width="5" stroke-linecap="round"/>
        </svg>
        <div style="font-family: 'Cormorant Garamond', serif; font-size: 1.65rem; font-weight: 700; color: #C5A059 !important; -webkit-text-fill-color: #C5A059 !important; letter-spacing: 0.12em; margin-top: 0.2rem; display: block;">The Shirt Project</div>
        <div style="font-family: 'Montserrat', sans-serif; font-size: 0.68rem; font-weight: 700; color: #C5A059 !important; -webkit-text-fill-color: #C5A059 !important; letter-spacing: 0.18em; text-transform: uppercase; margin-top: 0.4rem; display: block;">FOUNDED &amp; CREATED BY JATIN GUPTA</div>
    </div>
    """, unsafe_allow_html=True)

    # Sartorial Genie Assistant Expander in Sidebar
    with st.expander("🧞 Sartorial Genie (Quick Q&A Assistant)", expanded=False):
        genie_input = st.text_input("Ask Genie a question:", placeholder="e.g. Best suit for summer wedding?", key="sb_genie")
        if genie_input:
            st.info(query_sartorial_genie(genie_input))

    # Category Filter Choice Selector in Sidebar
    st.markdown("""
    <div style="border-top: 1px dashed rgba(197, 160, 89, 0.4); padding-top: 1rem; margin-top: 1rem;">
        <span style="font-family: 'Cormorant Garamond', serif; font-size: 1.35rem; font-weight: 700; color: #C5A059 !important; -webkit-text-fill-color: #C5A059 !important; display: block; margin-bottom: 0.4rem;">✂️ Filter Lookbook by Category</span>
    </div>
    """, unsafe_allow_html=True)

    sb_filter_choice = st.selectbox(
        "Select Collection Category:",
        ["All Collections", "Shirting", "Suiting & Tuxedos", "Trousers & Bottoms", "Style Statements"],
        key="sidebar_collection_filter"
    )
    if sb_filter_choice != "All Collections":
        if st.session_state.get("last_sb_choice") != sb_filter_choice:
            st.session_state.selected_categories = [sb_filter_choice]
            st.session_state.switch_to_catalog = True
            st.session_state.last_sb_choice = sb_filter_choice
    else:
        st.session_state.selected_categories = ["Shirting", "Suiting & Tuxedos", "Trousers & Bottoms", "Style Statements"]

    st.markdown("""
    <div style="border-top: 1px dashed rgba(197, 160, 89, 0.4); padding-top: 1rem; margin-top: 1.2rem;">
        <span style="font-family: 'Cormorant Garamond', serif; font-size: 1.4rem; font-weight: 700; color: #C5A059 !important; -webkit-text-fill-color: #C5A059 !important; display: block; margin-bottom: 0.5rem;">👑 Founder Atelier</span>
        <div style="font-size: 0.92rem; line-height: 1.6;">
            <strong style="color: #C5A059 !important; -webkit-text-fill-color: #C5A059 !important;">Mr. Jatin Gupta</strong><br>
            <span style="color: #C5A059 !important; -webkit-text-fill-color: #C5A059 !important; font-style: italic;">Founder</span><br>
            <span style="color: #C5A059 !important; -webkit-text-fill-color: #C5A059 !important;">📍 264-A, Raj Tilak Road, Jammu</span><br>
            <span style="color: #C5A059 !important; -webkit-text-fill-color: #C5A059 !important;">📞 +91 8717070570</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    wa_direct_quick = f"https://wa.me/918717070570?text={urllib.parse.quote('Hello, I would like to inquire about bespoke tailoring for The Shirt Project.')}"
    st.markdown(f"""
    <div style="border-top: 1px dashed rgba(197, 160, 89, 0.4); padding-top: 1rem; margin-top: 1.2rem;">
        <span style="font-family: 'Cormorant Garamond', serif; font-size: 1.4rem; font-weight: 700; color: #C5A059 !important; -webkit-text-fill-color: #C5A059 !important; display: block; margin-bottom: 0.4rem;">💬 Direct WhatsApp Concierge</span>
        <span style="font-size: 0.88rem; color: #C5A059 !important; -webkit-text-fill-color: #C5A059 !important; display: block; line-height: 1.5; margin-bottom: 0.8rem;">Need instant fabric guidance or custom pricing?</span>
        <a href="{wa_direct_quick}" target="_blank" style="display:block; text-align:center; background:#25D366; color:white !important; -webkit-text-fill-color:white !important; padding:0.75rem 1rem; border-radius:6px; font-weight:700; text-decoration:none !important; font-size:0.9rem; letter-spacing: 0.05em; box-shadow: 0 4px 15px rgba(37, 211, 102, 0.35);">
            💬 Chat With Us on WhatsApp
        </a>
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# BRAND HEADER BANNER
# ==========================================
st.markdown("""
<div style="background-color: #000000 !important; background: #000000 !important; border-radius: 16px; border: 2px solid #C5A059; padding: 2.8rem 2rem; text-align: center; box-shadow: 0 14px 40px rgba(0,0,0,0.6), 0 0 25px rgba(197, 160, 89, 0.25); margin-bottom: 2.2rem;">
    <svg viewBox="0 0 300 160" width="200" height="106" xmlns="http://www.w3.org/2000/svg" style="margin-bottom: 0.6rem; display: block; margin-left: auto; margin-right: auto; filter: drop-shadow(0 4px 12px rgba(197, 160, 89, 0.35));">
        <!-- Coat Hanger Hook -->
        <path d="M 150 18 C 132 18 122 35 138 55 C 145 65 148 71 150 80" fill="none" stroke="#C5A059" stroke-width="6" stroke-linecap="round"/>
        <!-- Outer Hanger -->
        <path d="M 150 80 L 45 125 C 32 130 32 145 45 150 L 105 150 M 150 80 L 255 125 C 268 130 268 145 255 150 L 195 150" fill="none" stroke="#C5A059" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>
        <!-- Monogram SP -->
        <path d="M 130 118 C 112 108 112 132 138 140 C 152 145 142 165 125 158 C 112 154 108 143 108 143" fill="none" stroke="#C5A059" stroke-width="5" stroke-linecap="round"/>
        <path d="M 152 115 C 178 115 182 138 152 145 L 152 165" fill="none" stroke="#C5A059" stroke-width="5" stroke-linecap="round"/>
        <path d="M 138 110 L 162 110 M 150 110 L 150 165" fill="none" stroke="#C5A059" stroke-width="5" stroke-linecap="round"/>
    </svg>
    <div style="font-family: 'Cormorant Garamond', serif !important; font-size: 3.2rem !important; font-weight: 700 !important; color: #C5A059 !important; -webkit-text-fill-color: #C5A059 !important; letter-spacing: 0.15em !important; text-transform: uppercase !important; margin-top: 0.4rem !important; line-height: 1.2 !important; display: block !important; visibility: visible !important; opacity: 1 !important; text-shadow: 0 2px 10px rgba(0,0,0,0.9);">The Shirt Project</div>
    <div style="font-family: 'Montserrat', sans-serif !important; font-size: 0.88rem !important; font-weight: 700 !important; color: #C5A059 !important; -webkit-text-fill-color: #C5A059 !important; letter-spacing: 0.22em !important; text-transform: uppercase !important; margin-top: 0.6rem !important; display: block !important; visibility: visible !important; opacity: 1 !important;">FOUNDED &amp; CREATED BY JATIN GUPTA</div>
    <div style="font-family: 'Cormorant Garamond', serif !important; font-size: 1.3rem !important; font-style: italic !important; color: #C5A059 !important; -webkit-text-fill-color: #C5A059 !important; letter-spacing: 0.08em !important; margin-top: 0.6rem !important; display: block !important; visibility: visible !important; opacity: 1 !important;">Crafted to Measure. Tailored for Distinction.</div>
</div>
""", unsafe_allow_html=True)

# ==========================================
# MAIN NAVIGATION TABS & AUTOMATIC REDIRECTION
# ==========================================
if st.session_state.get("switch_to_catalog", False):
    components.html("""
    <script>
    setTimeout(function() {
        const mainTabs = window.parent.document.querySelectorAll('div.stTabs button[data-baseweb="tab"]');
        if (mainTabs && mainTabs.length >= 2) {
            mainTabs[1].click();
        }
    }, 150);
    </script>
    """, height=1)
    st.session_state.switch_to_catalog = False

if st.session_state.get("switch_to_studio", False):
    components.html("""
    <script>
    setTimeout(function() {
        const mainTabs = window.parent.document.querySelectorAll('div.stTabs button[data-baseweb="tab"]');
        if (mainTabs && mainTabs.length >= 3) {
            mainTabs[2].click();
        }
    }, 150);
    </script>
    """, height=1)
    st.session_state.switch_to_studio = False

tab_atelier, tab_catalog, tab_studio, tab_contact = st.tabs([
    "🏛️ The Grand Atelier",
    "✨ The Sartorial Vault",
    "✂️ Bespoke Design Suite",
    "📍 VIP Concierge & Founder"
])

# ==========================================
# SECTION 1: THE GRAND ATELIER (HOME PAGE)
# ==========================================
with tab_atelier:
    # Rotating Style Quotes System with Timed Auto-Flip (Every 4 Seconds)
    if 'last_quote_time' not in st.session_state:
        st.session_state.last_quote_time = time.time()

    quotes = [
        {"quote": "Style is a way to say who you are without having to speak.", "author": "Rachel Zoe"},
        {"quote": "Elegance is not standing out, but being remembered.", "author": "Giorgio Armani"},
        {"quote": "A well-tailored suit is to women what lingerie is to men.", "author": "Bespoke Fitting Maxim"},
        {"quote": "Dressing well is a form of good manners.", "author": "Tom Ford"},
        {"quote": "Fashion fades, only style remains the same.", "author": "Coco Chanel"}
    ]

    # Auto-flip quote every 4 seconds
    if time.time() - st.session_state.last_quote_time > 4:
        st.session_state.current_quote_idx = (st.session_state.current_quote_idx + 1) % len(quotes)
        st.session_state.last_quote_time = time.time()

    current = quotes[st.session_state.current_quote_idx]
    st.markdown(f"""
    <div class="quote-banner">
        <span class="quote-symbol">“</span>
        <div class="quote-content">{current['quote']}</div>
        <div class="quote-author">— {current['author']}</div>
    </div>
    """, unsafe_allow_html=True)

    # Introduction Narrative
    st.markdown("""
    <div style="text-align: center; max-width: 880px; margin: 0 auto 2.5rem auto;">
        <h2 style="font-family: 'Cormorant Garamond', serif; font-size: 2.5rem; color: #1A1D20; margin-bottom: 1.2rem;">
            Where Master Craftsmanship Meets Modern Elegance
        </h2>
        <p style="font-size: 1.02rem; color: #555555; line-height: 1.85;">
            Founded by <strong>Mr. Jatin Gupta</strong>, <strong>The Shirt Project</strong> rejects mass production in favor of individual sartorial excellence. 
            Every shirt, suit, and garment is drafted from a unique paper pattern created exclusively for your body measurements. 
            Combining royal Indian heritage with centuries-old Savile Row traditions, we deliver garments of unmatched precision, comfort, and timeless prestige.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # 🧞 Sartorial Genie Smart Q&A Assistant Section
    st.markdown("""
    <div class="brand-card" style="border-top: 3px solid #C5A059; background: #FFFFFF; padding: 2rem; border-radius: 12px; margin-bottom: 3rem;">
        <div style="display: flex; align-items: center; gap: 0.8rem; margin-bottom: 0.5rem;">
            <span style="font-size: 2rem;">🧞</span>
            <div>
                <h3 style="font-family: 'Cormorant Garamond', serif; font-size: 2rem; color: #1A1D20; margin: 0;">Sartorial Genie — Quick Q&A & Style Assistant</h3>
                <p style="color: #666666; font-size: 0.88rem; margin: 0;">Ask any question about fabrics, outfit choices, bespoke timelines, or founder consultations.</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Preset Quick Questions (2 clean aligned rows)
    genie_query = ""

    r1_col1, r1_col2 = st.columns(2)
    with r1_col1:
        if st.button("🌿 Summer Shirting Fabrics", key="g_btn1"):
            genie_query = "Summer Shirting Fabrics"
    with r1_col2:
        if st.button("🎩 Wedding & Gala Suits", key="g_btn2"):
            genie_query = "Wedding & Gala Suits"

    st.markdown("<div style='margin-top: 0.8rem;'></div>", unsafe_allow_html=True)

    r2_col1, r2_col2 = st.columns(2)
    with r2_col1:
        if st.button("⏱️ Bespoke Stitching Timeline", key="g_btn3"):
            genie_query = "Bespoke Stitching Timeline"
    with r2_col2:
        if st.button("👑 Founder Consultation", key="g_btn4"):
            genie_query = "Founder Consultation"

    user_genie_input = st.text_input("Or type your custom question here:", value=genie_query, placeholder="e.g. What fabric is best for summer business formal?", key="main_genie")

    if user_genie_input:
        st.success(query_sartorial_genie(user_genie_input))

    st.markdown("<br>", unsafe_allow_html=True)

    # Brand Pillars (4 Cards)
    st.markdown("<h3 style='text-align: center; font-family: \"Cormorant Garamond\", serif; font-size: 2.2rem; margin-bottom: 1.8rem;'>The Four Pillars of Our Craft</h3>", unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="pillar-card">
            <div class="pillar-icon">📏</div>
            <div class="pillar-title">Bespoke Fitting</div>
            <div class="pillar-desc">Comprehensive 30-point measurement blueprint ensuring an absolute custom silhouette engineered for your posture.</div>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class="pillar-card">
            <div class="pillar-icon">🧵</div>
            <div class="pillar-title">Handpicked Fabrics</div>
            <div class="pillar-desc">Sourced directly from legendary mills in Italy, Egypt, & Ireland — 200s Giza cottons, Loro Piana wools, & crisp linens.</div>
        </div>
        """, unsafe_allow_html=True)
        
    with col3:
        st.markdown("""
        <div class="pillar-card">
            <div class="pillar-icon">🪡</div>
            <div class="pillar-title">Artisanal Stitching</div>
            <div class="pillar-desc">Hand-finished buttonholes, mother-of-pearl buttons, reinforced single-needle French seams, & pick stitching.</div>
        </div>
        """, unsafe_allow_html=True)
        
    with col4:
        st.markdown("""
        <div class="pillar-card">
            <div class="pillar-icon">👑</div>
            <div class="pillar-title">Personal Style</div>
            <div class="pillar-desc">Private 1-on-1 consultations with Founder Mr. Jatin Gupta for wedding galas, executive wardrobes, & casual luxury.</div>
        </div>
        """, unsafe_allow_html=True)

    # Craft Metrics Banner
    st.markdown("<br><hr style='border: none; border-top: 1px solid #EAE6DF; margin: 2.5rem 0;'>", unsafe_allow_html=True)
    
    m1, m2, m3, m4 = st.columns(4)
    m1.metric(label="Handcraft Steps", value="50+", delta="Precision Hand Work")
    m2.metric(label="Fabric Collection", value="500+", delta="Exclusive Weaves")
    m3.metric(label="Bespoke Garments", value="10,000+", delta="Delivered Worldwide")
    m4.metric(label="Fitting Satisfaction", value="100%", delta="Lifetime Alteration Guarantee")


# ==========================================
# SECTION 2: THE SARTORIAL VAULT (CATALOG)
# ==========================================
with tab_catalog:
    st.markdown("""
    <div style="text-align: center; margin-bottom: 2rem;">
        <h2 style="font-family: 'Cormorant Garamond', serif; font-size: 2.6rem; color: #1A1D20;">The Bespoke Collection Catalog</h2>
        <p style="color: #666666; font-size: 0.98rem;">Select a category to explore our signature weaves, cuts, and custom style statement pieces.</p>
    </div>
    """, unsafe_allow_html=True)

    cat_shirting, cat_suiting, cat_trousers, cat_statements = st.tabs([
        "👔 Shirting Collection",
        "🧥 Suiting & Tuxedos",
        "👖 Trousers & Bottoms",
        "✨ Style Statements"
    ])

    # Fallback Fashion Placeholder Images (High quality curated Unsplash menswear URLs)
    IMG_SHIRT_1 = "https://images.unsplash.com/photo-1602810318383-e386cc2a3ccf?auto=format&fit=crop&w=600&q=80"
    IMG_SHIRT_2 = "https://images.unsplash.com/photo-1596755094514-f87e34085b2c?auto=format&fit=crop&w=600&q=80"
    IMG_SHIRT_3 = "https://images.unsplash.com/photo-1598033129183-c4f50c736f10?auto=format&fit=crop&w=600&q=80"
    IMG_SUIT_1  = "https://images.unsplash.com/photo-1594938298603-c8148c4dae35?auto=format&fit=crop&w=600&q=80"
    IMG_SUIT_2  = "https://images.unsplash.com/photo-1507679799987-c73779587ccf?auto=format&fit=crop&w=600&q=80"
    IMG_SUIT_3  = "https://images.unsplash.com/photo-1507679799987-c73779587ccf?auto=format&fit=crop&w=600&q=80"
    IMG_PANTS_1 = "https://images.unsplash.com/photo-1479064555552-3ef4979f8908?auto=format&fit=crop&w=600&q=80"
    IMG_PANTS_2 = "https://images.unsplash.com/photo-1624378439575-d8705ad7ae80?auto=format&fit=crop&w=600&q=80"
    IMG_NEHRU   = "https://images.unsplash.com/photo-1507679799987-c73779587ccf?auto=format&fit=crop&w=600&q=80"

    # Helper function to render catalog items
    def render_catalog_item(title, category_tag, desc, fabric, img_url):
        st.markdown(f"""
        <div class="product-card">
            <img src="{img_url}" class="product-img" alt="{title}">
            <div class="product-info">
                <div>
                    <div class="product-tag">{category_tag}</div>
                    <div class="product-title">{title}</div>
                    <div class="product-desc">{desc}</div>
                </div>
                <div class="product-meta"><strong>Fabric:</strong> {fabric}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Sub-Category 1: Shirting
    with cat_shirting:
        c1, c2, c3 = st.columns(3)
        with c1:
            render_catalog_item(
                "Pure Egyptian Cotton Formal",
                "Shirting • Business Formal",
                "Crisp 200s Giza Egyptian Cotton with cutaway collar and convertible barrel cuffs.",
                "100% Giza 45 Egyptian Cotton",
                IMG_SHIRT_1
            )
            if st.button("Inquire Shirting", key="btn_sh1"):
                st.session_state.selected_categories = ["Shirting"]
                st.session_state.switch_to_studio = True
                st.toast("✨ Redirecting to Bespoke Design Suite...", icon="✂️")
                st.rerun()

        with c2:
            render_catalog_item(
                "Premium Irish Linen Resort Shirt",
                "Shirting • Casual Luxury",
                "Breathable organic Irish linen with soft spread collar for effortless warm-weather elegance.",
                "100% Pure Vintage Irish Linen",
                IMG_SHIRT_2
            )
            if st.button("Inquire Shirting", key="btn_sh2"):
                st.session_state.selected_categories = ["Shirting"]
                st.session_state.switch_to_studio = True
                st.toast("✨ Redirecting to Bespoke Design Suite...", icon="✂️")
                st.rerun()

        with c3:
            render_catalog_item(
                "Hand-Embroidered Monogrammed Party Shirt",
                "Shirting • Evening Wear",
                "Lustrous royal twill weave featuring hand-embroidered monogram initials on the left wrist cuff.",
                "Royal Twill Silk Blend",
                IMG_SHIRT_3
            )
            if st.button("Inquire Shirting", key="btn_sh3"):
                st.session_state.selected_categories = ["Shirting"]
                st.session_state.switch_to_studio = True
                st.toast("✨ Redirecting to Bespoke Design Suite...", icon="✂️")
                st.rerun()

    # Sub-Category 2: Suiting & Tuxedos
    with cat_suiting:
        c1, c2, c3 = st.columns(3)
        with c1:
            render_catalog_item(
                "2-Piece & 3-Piece Bespoke Suit",
                "Suiting • Executive & Formal",
                "Sculpted waistline, hand-canvassed chest piece, pick-stitched lapels, and horn buttons.",
                "Super 150s Italian Merino Wool",
                IMG_SUIT_1
            )
            if st.button("Inquire Suiting", key="btn_suit1"):
                st.session_state.selected_categories = ["Suiting & Tuxedos"]
                st.session_state.switch_to_studio = True
                st.toast("✨ Redirecting to Bespoke Design Suite...", icon="✂️")
                st.rerun()

        with c2:
            render_catalog_item(
                "Classic Black Tie Tuxedo",
                "Suiting • Black Tie Gala",
                "Timeless black tuxedo with satin peak lapels, silk-braided trouser side seams, and satin waist button.",
                "Barathea Wool & Silk Satin",
                IMG_SUIT_2
            )
            if st.button("Inquire Tuxedo", key="btn_suit2"):
                st.session_state.selected_categories = ["Suiting & Tuxedos"]
                st.session_state.switch_to_studio = True
                st.toast("✨ Redirecting to Bespoke Design Suite...", icon="✂️")
                st.rerun()

        with c3:
            render_catalog_item(
                "Italian Cut Cashmere Blazer",
                "Suiting • Smart Casual",
                "Soft shoulder, unlined Italian blazer offering lightweight elegance and effortless drape.",
                "Cashmere & Virgin Wool Blend",
                IMG_SUIT_3
            )
            if st.button("Inquire Blazer", key="btn_suit3"):
                st.session_state.selected_categories = ["Suiting & Tuxedos"]
                st.session_state.switch_to_studio = True
                st.toast("✨ Redirecting to Bespoke Design Suite...", icon="✂️")
                st.rerun()

    # Sub-Category 3: Trousers & Bottoms
    with cat_trousers:
        c1, c2, c3 = st.columns(3)
        with c1:
            render_catalog_item(
                "Tailored Formal Trousers",
                "Trousers • Business Formal",
                "Flat-front slim formal trousers with side brass adjusters and extended waistband button enclosure.",
                "Super 120s Fine Wool Twill",
                IMG_PANTS_1
            )
            if st.button("Inquire Trousers", key="btn_tr1"):
                st.session_state.selected_categories = ["Trousers & Bottoms"]
                st.session_state.switch_to_studio = True
                st.toast("✨ Redirecting to Bespoke Design Suite...", icon="✂️")
                st.rerun()

        with c2:
            render_catalog_item(
                "Gurkha & Double-Pleated Pants",
                "Trousers • Heritage Style",
                "High-waisted Gurkha trouser featuring double forward pleats and dual buckle waistband straps.",
                "Heavyweight Cotton Drill & Wool",
                IMG_PANTS_2
            )
            if st.button("Inquire Gurkha Pants", key="btn_tr2"):
                st.session_state.selected_categories = ["Trousers & Bottoms"]
                st.session_state.switch_to_studio = True
                st.toast("✨ Redirecting to Bespoke Design Suite...", icon="✂️")
                st.rerun()

        with c3:
            render_catalog_item(
                "Custom Linen Drawstring Pants",
                "Trousers • Casual Luxe",
                "Relaxed fit trousers with elasticated drawstring waist, deep slant pockets, and breathable drape.",
                "Organic Irish Linen",
                IMG_SHIRT_2
            )
            if st.button("Inquire Linen Pants", key="btn_tr3"):
                st.session_state.selected_categories = ["Trousers & Bottoms"]
                st.session_state.switch_to_studio = True
                st.toast("✨ Redirecting to Bespoke Design Suite...", icon="✂️")
                st.rerun()

    # Sub-Category 4: Style Statements
    with cat_statements:
        c1, c2, c3 = st.columns(3)
        with c1:
            render_catalog_item(
                "Custom Raw Silk Nehru Jacket",
                "Style Statement • Bandhgala",
                "Structured mandarin collar jacket crafted from handloom raw silk with antiqued brass buttons.",
                "100% Handloom Raw Silk",
                IMG_NEHRU
            )
            if st.button("Inquire Nehru Jacket", key="btn_st1"):
                st.session_state.selected_categories = ["Style Statements (Nehru Jacket / Waistcoat)"]
                st.session_state.switch_to_studio = True
                st.toast("✨ Redirecting to Bespoke Design Suite...", icon="✂️")
                st.rerun()

        with c2:
            render_catalog_item(
                "Tuxedo Silk Waistcoat",
                "Style Statement • Formal Vests",
                "Low-cut double-breasted tuxedo waistcoat designed to pair with black-tie suits.",
                "Pure Mulberry Silk Satin",
                IMG_SUIT_2
            )
            if st.button("Inquire Waistcoat", key="btn_st2"):
                st.session_state.selected_categories = ["Style Statements (Nehru Jacket / Waistcoat)"]
                st.session_state.switch_to_studio = True
                st.toast("✨ Redirecting to Bespoke Design Suite...", icon="✂️")
                st.rerun()

        with c3:
            render_catalog_item(
                "Bespoke Monogramming Details",
                "Style Statement • Personalization",
                "Signature hand-stitched monogram embroidery for cuffs, collar bands, lining pockets, or handkerchiefs.",
                "Silk Thread Custom Embroidery",
                IMG_SHIRT_3
            )
            if st.button("Inquire Monogramming", key="btn_st3"):
                st.session_state.selected_categories = ["Bespoke Monogramming & Details"]
                st.session_state.switch_to_studio = True
                st.toast("✨ Redirecting to Bespoke Design Suite...", icon="✂️")
                st.rerun()


# ==========================================
# SECTION 3: BESPOKE DESIGN SUITE (CUSTOM QUOTE & CONFIGURATOR)
# ==========================================
with tab_studio:
    st.markdown("""
    <div style="text-align: center; margin-bottom: 2rem;">
        <h2 style="font-family: 'Cormorant Garamond', serif; font-size: 2.6rem; color: #1A1D20;">Bespoke Design & Interactive Studio</h2>
        <p style="color: #666666; font-size: 0.98rem;">Configure your shirt cut preferences or submit custom stitching requests directly to Founder Mr. Jatin Gupta.</p>
    </div>
    """, unsafe_allow_html=True)

    # Interactive Live Visual Configurator Widget
    st.markdown("<h3 style='font-family: \"Cormorant Garamond\", serif; font-size: 1.8rem; border-bottom: 2px solid #C5A059; padding-bottom: 0.4rem;'>🎨 Interactive Sartorial Configurator</h3>", unsafe_allow_html=True)
    
    cfg1, cfg2, cfg3, cfg4 = st.columns(4)
    with cfg1:
        st.session_state.config_collar = st.selectbox(
            "1. Select Collar Style",
            ["Italian Cutaway", "Classic Spread", "Bandhgala / Mandarin", "Button-Down Casual", "Tuxedo Wingtip"]
        )
    with cfg2:
        st.session_state.config_cuff = st.selectbox(
            "2. Select Cuff Style",
            ["French Double Cuff (Cufflinks)", "Single Barrel Convertible", "2-Button Mitred Cuff", "Neapolitan Soft Cuff"]
        )
    with cfg3:
        st.session_state.config_fit = st.selectbox(
            "3. Select Contour Fit",
            ["Slim Bespoke Contour", "Classic Tailored Fit", "Relaxed Heritage Fit"]
        )
    with cfg4:
        config_monogram = st.selectbox(
            "4. Monogram Placement",
            ["Left Cuff Embroidery", "Collar Band Inside", "Shirt Pocket Edge", "No Monogram"]
        )

    # Configurator Live Preview Summary Box
    st.markdown(f"""
    <div class="configurator-preview">
        <span class="configurator-badge">✨ Live Bespoke Silhouette Blueprint</span>
        <div style="font-family: 'Cormorant Garamond', serif; font-size: 1.65rem; font-weight: 700; color: #C5A059 !important; -webkit-text-fill-color: #C5A059 !important; margin-bottom: 0.6rem; line-height: 1.3;">
            {st.session_state.config_fit} &bull; {st.session_state.config_collar} Collar &bull; {st.session_state.config_cuff}
        </div>
        <div style="font-family: 'Montserrat', sans-serif; font-size: 0.9rem; color: #C5A059 !important; -webkit-text-fill-color: #C5A059 !important; border-top: 1px dashed rgba(197, 160, 89, 0.35) !important; padding-top: 0.8rem; margin-top: 0.8rem;">
            Monogram Detail: <strong style="color: #C5A059 !important; -webkit-text-fill-color: #C5A059 !important;">{config_monogram}</strong> &nbsp;|&nbsp; Estimated Handcraft Time: <strong style="color: #C5A059 !important; -webkit-text-fill-color: #C5A059 !important;">18-24 Precision Hours</strong>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    form_col, info_col = st.columns([3, 2])

    with form_col:
        st.markdown('<div class="brand-card">', unsafe_allow_html=True)
        st.markdown("<h3 style='font-family: \"Cormorant Garamond\", serif; font-size: 1.8rem; border-bottom: 2px solid #C5A059; padding-bottom: 0.5rem;'>Client & Customization Request</h3>", unsafe_allow_html=True)

        client_name = st.text_input("Full Name *", placeholder="e.g. Lord Alexander Sterling")
        
        c_mob, c_email = st.columns(2)
        with c_mob:
            client_phone = st.text_input("WhatsApp / Mobile Number *", placeholder="+91 8717070570")
        with c_email:
            client_email = st.text_input("Email Address *", placeholder="alexander@sterling.com")

        category_options = [
            "Shirting",
            "Suiting & Tuxedos",
            "Trousers & Bottoms",
            "Style Statements (Nehru Jacket / Waistcoat)",
            "Bespoke Monogramming & Details"
        ]

        default_cats = [c for c in st.session_state.selected_categories if c in category_options]
        if not default_cats:
            default_cats = [category_options[0]]

        selected_cats = st.multiselect(
            "Category Selection (Multi-select) *",
            options=category_options,
            default=default_cats
        )

        fabric_notes = st.text_area(
            "Preferred Fabric & Customization Notes",
            placeholder=f"Configured: {st.session_state.config_collar} collar with {st.session_state.config_cuff}. Add specific fabric weight, pattern choices, initial letters for monogramming, or event dates...",
            height=130
        )

        uploaded_files = st.file_uploader(
            "Upload Photo / Style Inspiration (PNG, JPG, JPEG)",
            type=["png", "jpg", "jpeg"],
            accept_multiple_files=True,
            help="Upload images of suits, shirts, or collars you want Founder Mr. Jatin Gupta to replicate."
        )

        submit_quote = st.button("✨ Request Bespoke Quote")
        st.markdown('</div>', unsafe_allow_html=True)

    with info_col:
        st.markdown("""
        <div class="pillar-card" style="text-align: left; padding: 2rem;">
            <div style="color: #C5A059; font-size: 1.8rem; margin-bottom: 0.5rem;">👑 Direct Founder Concierge</div>
            <h4 style="font-family: 'Cormorant Garamond', serif; font-size: 1.6rem; color: #FFFFFF;">What Happens Next?</h4>
            <ol style="color: #D0D4D9; font-size: 0.9rem; line-height: 1.8; padding-left: 1.2rem;">
                <li><strong>Founder Review:</strong> Founder Mr. Jatin Gupta personally reviews your fabric & fit preferences.</li>
                <li><strong>WhatsApp Swatches:</strong> Direct high-resolution digital fabric swatches & price estimates sent straight to your WhatsApp.</li>
                <li><strong>Private Atelier Fitting:</strong> Visit our Jammu Heritage Atelier or schedule a private consultation.</li>
            </ol>
            <div style="border-top: 1px dashed #C5A059; margin-top: 1.5rem; padding-top: 1rem; color: #C5A059; font-size: 0.85rem;">
                👑 <strong>Founder:</strong> Mr. Jatin Gupta<br>
                ⚡ <strong>Direct WhatsApp:</strong> +91 8717070570<br>
                ✉️ <strong>VIP Booking:</strong> jatin.gupta@live.com
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Submission Action & WhatsApp Generator
    if submit_quote:
        if not client_name or not client_phone:
            st.error("Please provide at least your Full Name and WhatsApp / Mobile Number to generate your bespoke quote link.")
        else:
            cats_str = ", ".join(selected_cats) if selected_cats else "General Bespoke Inquiry"
            file_count_str = f" ({len(uploaded_files)} inspiration files attached in studio)" if uploaded_files else ""
            
            # Format WhatsApp Message
            wa_text = f"""*BESPOKE INQUIRY - THE SHIRT PROJECT*
---------------------------------------
*Client Name:* {client_name}
*Contact Phone:* {client_phone}
*Email:* {client_email if client_email else 'Not provided'}
*Requested Categories:* {cats_str}

*Sartorial Configuration:*
- Fit: {st.session_state.config_fit}
- Collar: {st.session_state.config_collar}
- Cuff: {st.session_state.config_cuff}
- Monogram: {config_monogram}

*Customization Notes:*
{fabric_notes if fabric_notes else 'Standard Bespoke Consultation requested.'}{file_count_str}
---------------------------------------
Sent via The Shirt Project Web Studio
"""
            # Encode for WhatsApp URL (using Founder Mr. Jatin Gupta's WhatsApp number +91 8717070570)
            business_wa_number = "918717070570"
            encoded_text = urllib.parse.quote(wa_text)
            wa_link = f"https://wa.me/{business_wa_number}?text={encoded_text}"

            st.success("🎉 Bespoke Request Form Created Successfully!")
            
            st.markdown(f"""
            <div class="summary-badge">
                <h4 style="font-family: 'Cormorant Garamond', serif; font-size: 1.55rem; color: #1A1D20; margin: 0 0 0.5rem 0;">
                    Bespoke Request Summary for {client_name}
                </h4>
                <p style="margin: 0; font-size: 0.92rem; color: #333333; line-height: 1.6;">
                    <strong>Configuration:</strong> {st.session_state.config_fit} | {st.session_state.config_collar} Collar | {st.session_state.config_cuff}<br>
                    <strong>Categories:</strong> {cats_str}<br>
                    <strong>Contact:</strong> {client_phone} | {client_email if client_email else 'N/A'}<br>
                    <strong>Customization Details:</strong> {fabric_notes if fabric_notes else 'Default fit'}
                </p>
                <a href="{wa_link}" target="_blank" class="whatsapp-direct-btn">
                    💬 Click Here to Send Direct WhatsApp Inquiry to Founder
                </a>
            </div>
            """, unsafe_allow_html=True)


# ==========================================
# SECTION 4: VIP CONCIERGE & FOUNDER
# ==========================================
with tab_contact:
    st.markdown("""
    <div style="text-align: center; margin-bottom: 2rem;">
        <h2 style="font-family: 'Cormorant Garamond', serif; font-size: 2.6rem; color: #1A1D20;">The Royal Atelier & VIP Concierge</h2>
        <p style="color: #666666; font-size: 0.98rem;">Book a private fitting appointment or reach Founder Mr. Jatin Gupta directly.</p>
    </div>
    """, unsafe_allow_html=True)

    col_loc, col_book = st.columns([1, 1])

    with col_loc:
        st.markdown("""
        <div class="brand-card">
            <h3 style="font-family: 'Cormorant Garamond', serif; font-size: 1.8rem; color: #1A1D20; border-bottom: 2px solid #C5A059; padding-bottom: 0.5rem;">
                The Royal Jammu Atelier
            </h3>
            <p style="font-size: 0.95rem; line-height: 1.85; color: #444444;">
                <strong>The Shirt Project Atelier</strong><br>
                👑 <strong>Founder:</strong> Mr. Jatin Gupta<br>
                📍 <strong>Address:</strong> 264-A, Raj Tilak Road, Jammu<br><br>
                🕒 <strong>Atelier Hours:</strong><br>
                Monday – Saturday: 10:00 AM – 8:00 PM<br>
                Sunday: By Private VIP Appointment Only<br><br>
                📞 <strong>Direct Contact No:</strong> +91 8717070570<br>
                💬 <strong>WhatsApp Concierge:</strong> +91 8717070570<br>
                ✉️ <strong>VIP Booking:</strong> jatin.gupta@live.com
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col_book:
        st.markdown("<h3 style='font-family: \"Cormorant Garamond\", serif; font-size: 1.8rem; border-bottom: 2px solid #C5A059; padding-bottom: 0.5rem; color: #1A1D20; margin-top: 0;'>Schedule Private Fitting Session</h3>", unsafe_allow_html=True)

        app_name = st.text_input("Your Full Name", placeholder="e.g. Marcus Vance")
        app_date = st.date_input("Preferred Date", value=datetime.today())
        app_time = st.selectbox("Preferred Time Slot", ["10:30 AM", "12:00 PM", "02:30 PM", "04:30 PM", "06:30 PM"])
        app_tailor = st.selectbox("Preferred Master Stylist / Fitter", ["Mr. Jatin Gupta (Founder)", "Senior Bespoke Stylist", "Master Fitter & Cutter"])

        if st.button("📅 Confirm Fitting Reservation"):
            if app_name:
                st.success(f"Appointment reserved for {app_name} on {app_date.strftime('%B %d, %Y')} at {app_time} with {app_tailor}. Our concierge will contact you shortly!")
            else:
                st.warning("Please provide your name to confirm the reservation.")

    # FAQ Accordion Section
    st.markdown("<br><h3 style='text-align: center; font-family: \"Cormorant Garamond\", serif; font-size: 2.2rem;'>Frequently Asked Bespoke Questions</h3>", unsafe_allow_html=True)
    
    with st.expander("❓ How long does a bespoke shirt or suit take to craft?"):
        st.write("Each garment requires approximately 2 to 3 weeks for master pattern drafting, hand cutting, and stitching. For urgent gala events, expedited 7-day express bespoke service is available upon request.")

    with st.expander("❓ Can I select custom monogram styles and collar designs?"):
        st.write("Yes! We offer over 15 collar styles (Italian cutaway, spread, club, mandarin, wingtip), 8 cuff styles, and hand-embroidered monogramming in silk thread with your initials or family crest.")

    with st.expander("❓ What happens if my body weight or posture changes?"):
        st.write("All 'The Shirt Project' bespoke garments come with our signature Lifetime Alteration Guarantee. You may bring your garment back to our atelier at any time for adjustments.")

# ==========================================
# FOOTER
# ==========================================
st.markdown("""
<div style="text-align: center; border-top: 1px solid #EAE6DF; margin-top: 4rem; padding-top: 2rem; color: #888888; font-size: 0.82rem; letter-spacing: 0.12em;">
    © 2026 THE SHIRT PROJECT • FOUNDED BY MR. JATIN GUPTA • CRAFTED TO MEASURE. TAILORED FOR DISTINCTION.
</div>
""", unsafe_allow_html=True)
