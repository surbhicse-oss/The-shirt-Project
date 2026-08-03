import streamlit as st
import urllib.parse
from datetime import datetime

# ==========================================
# PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="The Shirt Project | Bespoke Men's Apparel",
    page_icon="👔",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Initialize Session States
if 'current_quote_idx' not in st.session_state:
    st.session_state.current_quote_idx = 0

if 'selected_categories' not in st.session_state:
    st.session_state.selected_categories = ["Shirting"]

if 'active_tab' not in st.session_state:
    st.session_state.active_tab = 0

# ==========================================
# BRAND AESTHETICS & CUSTOM CSS INJECTION
# ==========================================
custom_css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,600&family=Montserrat:wght@300;400;500;600;700&display=swap');

/* Color Variables */
:root {
    --sand: #EAE6DF;
    --sand-light: #F7F5F0;
    --charcoal: #1A1D20;
    --charcoal-light: #2A2E33;
    --gold: #C5A059;
    --gold-dark: #A3803C;
    --white: #FFFFFF;
    --border-color: #D6D0C4;
}

/* Hide default Streamlit headers, footers, & adjust padding */
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
#root .block-container {
    padding-top: 1rem;
    padding-bottom: 4rem;
    padding-left: 2.5rem;
    padding-right: 2.5rem;
    max-width: 1350px;
}

/* Typography Overrides */
html, body, [class*="css"], .stMarkdown {
    font-family: 'Montserrat', sans-serif;
    color: #1A1D20;
}

h1, h2, h3, h4, h5, h6, .brand-font {
    font-family: 'Cormorant Garamond', serif !important;
    letter-spacing: 0.05em;
}

/* Luxury Header Bar */
.brand-header-banner {
    background: linear-gradient(135deg, #1A1D20 0%, #25292E 100%);
    border-bottom: 3px solid #C5A059;
    padding: 2.5rem 1.5rem;
    border-radius: 12px;
    text-align: center;
    color: #EAE6DF;
    margin-bottom: 2rem;
    box-shadow: 0 12px 35px rgba(26, 29, 32, 0.25);
    position: relative;
    overflow: hidden;
}

.brand-header-banner::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background: radial-gradient(circle at center, rgba(197, 160, 89, 0.08) 0%, transparent 70%);
    pointer-events: none;
}

.brand-logo-svg {
    width: 65px;
    height: 65px;
    margin-bottom: 0.5rem;
}

.brand-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: 3.5rem;
    font-weight: 700;
    letter-spacing: 0.18em;
    color: #FFFFFF;
    text-transform: uppercase;
    margin: 0;
    line-height: 1;
}

.brand-tagline {
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.35rem;
    font-style: italic;
    letter-spacing: 0.15em;
    color: #C5A059;
    margin-top: 0.6rem;
}

/* Luxury Tabs Styling */
.stTabs [data-baseweb="tab-list"] {
    gap: 1rem;
    justify-content: center;
    background-color: #EAE6DF;
    padding: 0.6rem 0.8rem;
    border-radius: 8px;
    border: 1px solid #D6D0C4;
    margin-bottom: 2rem;
}

.stTabs [data-baseweb="tab"] {
    height: 3.2rem;
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.3rem;
    font-weight: 600;
    letter-spacing: 0.08em;
    color: #1A1D20;
    background-color: transparent;
    border-radius: 6px;
    padding: 0 1.5rem;
    transition: all 0.3s ease;
}

.stTabs [aria-selected="true"] {
    background-color: #1A1D20 !important;
    color: #C5A059 !important;
    box-shadow: 0 4px 12px rgba(26, 29, 32, 0.15);
}

/* Cards & Containers */
.brand-card {
    background: #FFFFFF;
    border: 1px solid #EAE6DF;
    border-top: 3px solid #C5A059;
    border-radius: 10px;
    padding: 1.8rem;
    margin-bottom: 1.5rem;
    box-shadow: 0 6px 20px rgba(0,0,0,0.03);
    transition: all 0.3s ease;
}

.brand-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 30px rgba(0,0,0,0.08);
}

.pillar-card {
    background: #1A1D20;
    color: #EAE6DF;
    padding: 2rem 1.2rem;
    border-radius: 10px;
    text-align: center;
    border: 1px solid #C5A059;
    height: 100%;
    transition: all 0.3s ease;
}

.pillar-card:hover {
    border-color: #FFFFFF;
    transform: translateY(-3px);
}

.pillar-icon {
    font-size: 2.2rem;
    color: #C5A059;
    margin-bottom: 0.8rem;
}

.pillar-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.45rem;
    color: #FFFFFF;
    font-weight: 600;
    letter-spacing: 0.06em;
    margin-bottom: 0.5rem;
}

.pillar-desc {
    font-size: 0.88rem;
    color: #B5BAC0;
    line-height: 1.5;
}

/* Fashion Quote Card */
.quote-banner {
    background: linear-gradient(135deg, #1A1D20 0%, #292D33 100%);
    border: 1px solid #C5A059;
    padding: 2.2rem 2rem;
    border-radius: 12px;
    text-align: center;
    color: #EAE6DF;
    margin: 1.5rem 0 2.5rem 0;
    position: relative;
    box-shadow: 0 8px 25px rgba(0,0,0,0.1);
}

.quote-symbol {
    font-family: 'Cormorant Garamond', serif;
    font-size: 3rem;
    color: #C5A059;
    line-height: 0;
    display: block;
    margin-bottom: 1rem;
}

.quote-content {
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.75rem;
    font-style: italic;
    color: #FFFFFF;
    margin-bottom: 0.8rem;
    line-height: 1.35;
}

.quote-author {
    font-family: 'Montserrat', sans-serif;
    font-size: 0.82rem;
    color: #C5A059;
    letter-spacing: 0.25em;
    text-transform: uppercase;
    font-weight: 600;
}

/* Product Card Styling */
.product-card {
    background: #FFFFFF;
    border-radius: 10px;
    border: 1px solid #EAE6DF;
    overflow: hidden;
    margin-bottom: 1.8rem;
    box-shadow: 0 4px 15px rgba(0,0,0,0.03);
    transition: all 0.3s ease;
    height: 100%;
    display: flex;
    flex-direction: column;
}

.product-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 28px rgba(0,0,0,0.09);
    border-color: #C5A059;
}

.product-img {
    width: 100%;
    height: 240px;
    object-fit: cover;
    border-bottom: 1px solid #EAE6DF;
}

.product-info {
    padding: 1.4rem;
    flex-grow: 1;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.product-tag {
    font-size: 0.72rem;
    font-weight: 700;
    color: #C5A059;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    margin-bottom: 0.4rem;
}

.product-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.5rem;
    font-weight: 700;
    color: #1A1D20;
    margin-bottom: 0.5rem;
    line-height: 1.2;
}

.product-desc {
    font-size: 0.85rem;
    color: #555555;
    line-height: 1.5;
    margin-bottom: 1rem;
}

.product-meta {
    font-size: 0.78rem;
    color: #888888;
    border-top: 1px dashed #EAE6DF;
    padding-top: 0.8rem;
    margin-bottom: 1rem;
}

/* Custom Buttons Styling */
.stButton > button {
    background-color: #1A1D20 !important;
    color: #C5A059 !important;
    border: 1px solid #C5A059 !important;
    font-family: 'Montserrat', sans-serif !important;
    font-size: 0.82rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.15em !important;
    text-transform: uppercase !important;
    padding: 0.65rem 1.2rem !important;
    border-radius: 4px !important;
    transition: all 0.3s ease !important;
    width: 100%;
}

.stButton > button:hover {
    background-color: #C5A059 !important;
    color: #1A1D20 !important;
    border-color: #C5A059 !important;
    box-shadow: 0 4px 15px rgba(197, 160, 89, 0.4) !important;
}

/* Form Controls Styling */
.stTextInput > div > div > input, 
.stTextArea > div > div > textarea, 
.stSelectbox > div > div {
    border: 1px solid #C5A059 !important;
    background-color: #FFFFFF !important;
    color: #1A1D20 !important;
    border-radius: 4px !important;
    font-family: 'Montserrat', sans-serif !important;
}

.stTextInput > div > div > input:focus, 
.stTextArea > div > div > textarea:focus {
    border-color: #C5A059 !important;
    box-shadow: 0 0 8px rgba(197, 160, 89, 0.3) !important;
}

/* WhatsApp Direct Button */
.whatsapp-direct-btn {
    display: block;
    width: 100%;
    background-color: #25D366;
    color: #FFFFFF !important;
    text-align: center;
    padding: 0.9rem 1.5rem;
    font-family: 'Montserrat', sans-serif;
    font-size: 0.95rem;
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    text-decoration: none !important;
    border-radius: 6px;
    margin-top: 1.2rem;
    box-shadow: 0 4px 18px rgba(37, 211, 102, 0.35);
    transition: all 0.3s ease;
}

.whatsapp-direct-btn:hover {
    background-color: #1EBE57;
    color: #FFFFFF !important;
    transform: translateY(-2px);
    box-shadow: 0 6px 22px rgba(37, 211, 102, 0.45);
}

/* Summary Badge */
.summary-badge {
    background: #F7F5F0;
    border-left: 4px solid #C5A059;
    padding: 1.2rem 1.5rem;
    border-radius: 6px;
    margin: 1rem 0;
}

</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# ==========================================
# BRAND HEADER BANNER
# ==========================================
st.markdown("""
<div class="brand-header-banner">
    <svg class="brand-logo-svg" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M50 15 C45 15 42 19 44 24 C45.5 27.5 49 29 50 30 C51 29 54.5 27.5 56 24 C58 19 55 15 50 15 Z" stroke="#C5A059" stroke-width="2.5" stroke-linecap="round"/>
        <path d="M50 30 L10 50 L35 50 C40 45 42 45 50 45 C58 45 60 45 65 50 L90 50 Z" stroke="#C5A059" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"/>
        <path d="M38 52 C38 65 42 70 50 70 C58 70 62 65 62 52" stroke="#C5A059" stroke-width="2" stroke-linecap="round"/>
        <path d="M44 58 L56 58" stroke="#C5A059" stroke-width="2"/>
    </svg>
    <h1 class="brand-title">The Shirt Project</h1>
    <div class="brand-tagline">Crafted to Measure. Tailored for Distinction.</div>
</div>
""", unsafe_allow_html=True)

# ==========================================
# MAIN NAVIGATION TABS
# ==========================================
tab_atelier, tab_catalog, tab_studio, tab_contact = st.tabs([
    "🏛️ The Grand Atelier",
    "✨ The Sartorial Vault",
    "✂️ Bespoke Design Suite",
    "📍 VIP Concierge & Founder"
])

# ==========================================
# SECTION 1: THE ATELIER (HOME PAGE)
# ==========================================
with tab_atelier:
    # Rotating Style Quotes System
    quotes = [
        {"quote": "Style is a way to say who you are without having to speak.", "author": "Rachel Zoe"},
        {"quote": "Elegance is not standing out, but being remembered.", "author": "Giorgio Armani"},
        {"quote": "A well-tailored suit is to women what lingerie is to men.", "author": "Bespoke Fitting Maxim"},
        {"quote": "Dressing well is a form of good manners.", "author": "Tom Ford"},
        {"quote": "Fashion fades, only style remains the same.", "author": "Coco Chanel"}
    ]

    col_quote_content, col_quote_btn = st.columns([5, 1])
    
    with col_quote_content:
        current = quotes[st.session_state.current_quote_idx]
        st.markdown(f"""
        <div class="quote-banner">
            <span class="quote-symbol">“</span>
            <div class="quote-content">{current['quote']}</div>
            <div class="quote-author">— {current['author']}</div>
        </div>
        """, unsafe_allow_html=True)
        
    with col_quote_btn:
        st.markdown("<br><br>", unsafe_allow_html=True)
        if st.button("✨ Next Quote"):
            st.session_state.current_quote_idx = (st.session_state.current_quote_idx + 1) % len(quotes)
            st.rerun()

    # Introduction Narrative
    st.markdown("""
    <div style="text-align: center; max-width: 850px; margin: 0 auto 3rem auto;">
        <h2 style="font-family: 'Cormorant Garamond', serif; font-size: 2.3rem; color: #1A1D20; margin-bottom: 1rem;">
            Where Master Craftsmanship Meets Modern Elegance
        </h2>
        <p style="font-size: 1rem; color: #555555; line-height: 1.8;">
            At <strong>The Shirt Project</strong>, we reject mass production in favor of individual sartorial excellence. 
            Every shirt, suit, and garment is drafted from a unique paper pattern created exclusively for your body measurements. 
            Using centuries-old Savile Row traditions combined with handpicked European textiles, we deliver garments of unmatched precision, comfort, and timeless prestige.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Brand Pillars (4 Cards)
    st.markdown("<h3 style='text-align: center; font-family: \"Cormorant Garamond\", serif; font-size: 2rem; margin-bottom: 1.5rem;'>The Four Pillars of Our Craft</h3>", unsafe_allow_html=True)
    
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
            <div class="pillar-title">Personal Style Consultation</div>
            <div class="pillar-desc">Private 1-on-1 consultations with our master stylists for wedding galas, executive wardrobes, & casual luxury.</div>
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
# SECTION 2: INTERACTIVE CATALOG (CATEGORIES)
# ==========================================
with tab_catalog:
    st.markdown("""
    <div style="text-align: center; margin-bottom: 2rem;">
        <h2 style="font-family: 'Cormorant Garamond', serif; font-size: 2.5rem; color: #1A1D20;">The Bespoke Collection Catalog</h2>
        <p style="color: #666666; font-size: 0.95rem;">Select a category to explore our signature weaves, cuts, and custom style statement pieces.</p>
    </div>
    """, unsafe_allow_html=True)

    cat_shirting, cat_suiting, cat_trousers, cat_statements = st.tabs([
        "👔 Shirting",
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
                st.info("Added to Bespoke Studio request form! Switch to the Bespoke Studio tab to complete your request.")

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
                st.info("Added to Bespoke Studio request form! Switch to the Bespoke Studio tab to complete your request.")

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
                st.info("Added to Bespoke Studio request form! Switch to the Bespoke Studio tab to complete your request.")

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
                st.info("Added to Bespoke Studio request form!")

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
                st.info("Added to Bespoke Studio request form!")

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
                st.info("Added to Bespoke Studio request form!")

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
                st.info("Added to Bespoke Studio request form!")

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
                st.info("Added to Bespoke Studio request form!")

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
                st.info("Added to Bespoke Studio request form!")

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
                st.info("Added to Bespoke Studio request form!")

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
                st.info("Added to Bespoke Studio request form!")

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
                st.info("Added to Bespoke Studio request form!")


# ==========================================
# SECTION 3: BESPOKE STUDIO (CUSTOM QUOTE FORM)
# ==========================================
with tab_studio:
    st.markdown("""
    <div style="text-align: center; margin-bottom: 2rem;">
        <h2 style="font-family: 'Cormorant Garamond', serif; font-size: 2.5rem; color: #1A1D20;">Bespoke Design & Quote Request Studio</h2>
        <p style="color: #666666; font-size: 0.95rem;">Submit your custom stitching preferences, fabric desires, or inspiration images to receive a personalized quote from our master tailors.</p>
    </div>
    """, unsafe_allow_html=True)

    form_col, info_col = st.columns([3, 2])

    with form_col:
        st.markdown('<div class="brand-card">', unsafe_allow_html=True)
        st.markdown("<h3 style='font-family: \"Cormorant Garamond\", serif; font-size: 1.8rem; border-bottom: 2px solid #C5A059; padding-bottom: 0.5rem;'>Client & Customization Details</h3>", unsafe_allow_html=True)

        client_name = st.text_input("Full Name *", placeholder="e.g. Lord Alexander Sterling")
        
        c_mob, c_email = st.columns(2)
        with c_mob:
            client_phone = st.text_input("WhatsApp / Mobile Number *", placeholder="+1 (555) 019-2834")
        with c_email:
            client_email = st.text_input("Email Address *", placeholder="alexander@sterling.com")

        category_options = [
            "Shirting",
            "Suiting & Tuxedos",
            "Trousers & Bottoms",
            "Style Statements (Nehru Jacket / Waistcoat)",
            "Bespoke Monogramming & Details"
        ]

        # Ensure default selected category is valid
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
            placeholder="Specify collar preferences (e.g. Italian cutaway, button-down), cuffs (single barrel, French cuff), fabric weights, pattern choices, initial monograms, or event dates...",
            height=140
        )

        uploaded_files = st.file_uploader(
            "Upload Photo / Style Inspiration (PNG, JPG, JPEG)",
            type=["png", "jpg", "jpeg"],
            accept_multiple_files=True,
            help="Upload images of suits, shirts, or collars you want our master tailor to replicate."
        )

        submit_quote = st.button("✨ Request Bespoke Quote")
        st.markdown('</div>', unsafe_allow_html=True)

    with info_col:
        st.markdown("""
        <div class="pillar-card" style="text-align: left; padding: 2rem;">
            <div style="color: #C5A059; font-size: 1.8rem; margin-bottom: 0.5rem;">👑 Direct Founder Concierge</div>
            <h4 style="font-family: 'Cormorant Garamond', serif; font-size: 1.6rem; color: #FFFFFF;">What Happens Next?</h4>
            <ol style="color: #D0D4D9; font-size: 0.9rem; line-height: 1.8; padding-left: 1.2rem;">
                <li><strong>Founder Review:</strong> Founder & Master Couturier Mr. Jatin Gupta personally reviews your fabric & fit preferences.</li>
                <li><strong>WhatsApp Swatches:</strong> Direct high-resolution digital fabric swatches & price estimates sent straight to your WhatsApp.</li>
                <li><strong>Private Atelier Fitting:</strong> Visit our Jammu Heritage Atelier or schedule a private consultation.</li>
            </ol>
            <div style="border-top: 1px dashed #C5A059; margin-top: 1.5rem; padding-top: 1rem; color: #C5A059; font-size: 0.85rem;">
                👑 <strong>Founder:</strong> Mr. Jatin Gupta<br>
                ⚡ <strong>Direct WhatsApp:</strong> +91 8717070570<br>
                ✉️ <strong>VIP Booking:</strong> concierge@theshirtproject.com
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

*Customization & Fabric Notes:*
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
                <h4 style="font-family: 'Cormorant Garamond', serif; font-size: 1.5rem; color: #1A1D20; margin: 0 0 0.5rem 0;">
                    Bespoke Request Summary for {client_name}
                </h4>
                <p style="margin: 0; font-size: 0.9rem; color: #333333;">
                    <strong>Categories:</strong> {cats_str}<br>
                    <strong>Contact:</strong> {client_phone} | {client_email if client_email else 'N/A'}<br>
                    <strong>Customization Details:</strong> {fabric_notes if fabric_notes else 'Default fit'}
                </p>
                <a href="{wa_link}" target="_blank" class="whatsapp-direct-btn">
                    💬 Click Here to Send Direct WhatsApp Inquiry
                </a>
            </div>
            """, unsafe_allow_html=True)


# ==========================================
# SECTION 4: CONTACT & CONCIERGE
# ==========================================
with tab_contact:
    st.markdown("""
    <div style="text-align: center; margin-bottom: 2rem;">
        <h2 style="font-family: 'Cormorant Garamond', serif; font-size: 2.5rem; color: #1A1D20;">The Royal Atelier & VIP Concierge</h2>
        <p style="color: #666666; font-size: 0.95rem;">Book a private fitting appointment or reach Founder Mr. Jatin Gupta directly.</p>
    </div>
    """, unsafe_allow_html=True)

    col_loc, col_book = st.columns([1, 1])

    with col_loc:
        st.markdown("""
        <div class="brand-card">
            <h3 style="font-family: 'Cormorant Garamond', serif; font-size: 1.8rem; color: #1A1D20; border-bottom: 2px solid #C5A059; padding-bottom: 0.5rem;">
                The Royal Jammu Atelier
            </h3>
            <p style="font-size: 0.95rem; line-height: 1.8; color: #444444;">
                <strong>The Shirt Project Atelier</strong><br>
                👑 <strong>Founder & Master Couturier:</strong> Mr. Jatin Gupta<br>
                📍 <strong>Address:</strong> 264-A, Raj Tilak Road, Jammu<br><br>
                🕒 <strong>Atelier Hours:</strong><br>
                Monday – Saturday: 10:00 AM – 8:00 PM<br>
                Sunday: By Private VIP Appointment Only<br><br>
                📞 <strong>Direct Contact No:</strong> +91 8717070570<br>
                💬 <strong>WhatsApp Concierge:</strong> +91 8717070570<br>
                ✉️ <strong>VIP Booking:</strong> concierge@theshirtproject.com
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col_book:
        st.markdown('<div class="brand-card">', unsafe_allow_html=True)
        st.markdown("<h3 style='font-family: \"Cormorant Garamond\", serif; font-size: 1.8rem; border-bottom: 2px solid #C5A059; padding-bottom: 0.5rem;'>Schedule Private Fitting Session</h3>", unsafe_allow_html=True)

        app_name = st.text_input("Your Full Name", placeholder="e.g. Marcus Vance")
        app_date = st.date_input("Preferred Date", value=datetime.today())
        app_time = st.selectbox("Preferred Time Slot", ["10:30 AM", "12:00 PM", "02:30 PM", "04:30 PM", "06:30 PM"])
        app_tailor = st.selectbox("Preferred Master Stylist / Fitter", ["Mr. Jatin Gupta (Founder & Master Couturier)", "Senior Bespoke Stylist", "Master Fitter & Cutter"])

        if st.button("📅 Confirm Fitting Reservation"):
            if app_name:
                st.success(f"Appointment reserved for {app_name} on {app_date.strftime('%B %d, %Y')} at {app_time} with {app_tailor}. Our concierge will contact you shortly!")
            else:
                st.warning("Please provide your name to confirm the reservation.")
        st.markdown('</div>', unsafe_allow_html=True)

    # FAQ Accordion Section
    st.markdown("<br><h3 style='text-align: center; font-family: \"Cormorant Garamond\", serif; font-size: 2rem;'>Frequently Asked Bespoke Questions</h3>", unsafe_allow_html=True)
    
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
<div style="text-align: center; border-top: 1px solid #EAE6DF; margin-top: 4rem; padding-top: 2rem; color: #888888; font-size: 0.8rem; letter-spacing: 0.1em;">
    © 2026 THE SHIRT PROJECT. CRAFTED TO MEASURE. TAILORED FOR DISTINCTION. ALL RIGHTS RESERVED.
</div>
""", unsafe_allow_html=True)
