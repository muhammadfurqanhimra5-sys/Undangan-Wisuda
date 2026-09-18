import streamlit as st

# Konfigurasi Halaman
st.set_page_config(
    page_title="Undangan Wisuda - Muhammad Furqan Himra, S.T.",
    page_icon="🎓",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Sistem Penanganan Parameter URL yang Kebal Bug
# Mengatasi perubahan tipe data query_params di berbagai versi Streamlit
try:
    raw_to = st.query_params.get("to", None)
except Exception:
    raw_to = None

if isinstance(raw_to, list):
    nama_tamu = raw_to[0] if len(raw_to) > 0 else "Tamu Kehormatan"
elif raw_to is not None and str(raw_to).strip() != "":
    nama_tamu = str(raw_to)
else:
    nama_tamu = "Tamu Kehormatan"

# Mengembalikan karakter '+' menjadi spasi asli
nama_tamu = nama_tamu.replace("+", " ").strip()
if not nama_tamu:
    nama_tamu = "Tamu Kehormatan"

# CSS Editorial Haute Luxury (Obsidian & Platinum Bronze)
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;0,700;1,400&family=Montserrat:wght@200;300;400;500;600&display=swap');

    /* Latar Belakang Obsidian Minimalis */
    .stApp {
        background-color: #0c0d0e;
        background-image: radial-gradient(#1e2024 0.65px, transparent 0.65px);
        background-size: 24px 24px;
        color: #d1d5db;
        font-family: 'Montserrat', sans-serif;
    }

    /* Hilangkan ornamen default Streamlit */
    header, #MainMenu, footer {visibility: hidden;}

    /* Kartu Geometris & Garis Presisi */
    .luxury-card {
        background: rgba(18, 20, 23, 0.75);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 4px;
        padding: 32px 24px;
        margin: 20px 0;
        box-shadow: 0 20px 40px -15px rgba(0, 0, 0, 0.8);
        backdrop-filter: blur(16px);
        position: relative;
    }

    /* Aksen Sudut Tipis Arsitektural */
    .luxury-card::before {
        content: "";
        position: absolute;
        top: 0; left: 0; width: 14px; height: 14px;
        border-top: 1.5px solid #d4af37;
        border-left: 1.5px solid #d4af37;
    }
    .luxury-card::after {
        content: "";
        position: absolute;
        bottom: 0; right: 0; width: 14px; height: 14px;
        border-bottom: 1.5px solid #d4af37;
        border-right: 1.5px solid #d4af37;
    }

    .text-center { text-align: center; }
    .text-left { text-align: left; }

    /* Label Editorial Kecil */
    .editorial-tag {
        font-family: 'Montserrat', sans-serif;
        font-size: 0.65rem;
        font-weight: 500;
        letter-spacing: 5px;
        color: #9ca3af;
        text-transform: uppercase;
        margin-bottom: 8px;
    }

    /* Judul Utama */
    .main-heading {
        font-family: 'Cormorant Garamond', serif;
        font-size: 2.8rem;
        font-weight: 400;
        letter-spacing: 3px;
        color: #f9fafb;
        margin: 4px 0 10px 0;
        text-transform: uppercase;
    }

    .sub-heading-italic {
        font-family: 'Cormorant Garamond', serif;
        font-style: italic;
        font-size: 1.15rem;
        color: #9ca3af;
        letter-spacing: 0.5px;
        margin-bottom: 24px;
    }

    .recipient-name {
        font-family: 'Cormorant Garamond', serif;
        font-size: 2rem;
        font-weight: 600;
        letter-spacing: 1.5px;
        color: #ffffff;
        margin-top: 6px;
    }

    .graduate-name {
        font-family: 'Cormorant Garamond', serif;
        font-size: 2.3rem;
        font-weight: 600;
        letter-spacing: 1.5px;
        color: #f3f4f6;
        line-height: 1.25;
        margin: 12px 0 16px 0;
    }

    .tag-degree {
        display: inline-block;
        border: 1px solid rgba(212, 175, 55, 0.4);
        background: transparent;
        color: #e5e7eb;
        padding: 5px 22px;
        border-radius: 2px;
        font-size: 0.72rem;
        letter-spacing: 3px;
        text-transform: uppercase;
        margin-bottom: 10px;
    }

    .univ-subtitle {
        color: #9ca3af;
        font-size: 0.85rem;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin: 0;
    }

    /* Format Detail Acara */
    .meta-title {
        font-size: 0.65rem;
        letter-spacing: 3.5px;
        color: #d4af37;
        text-transform: uppercase;
        font-weight: 500;
        margin-bottom: 4px;
    }

    .meta-content {
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.45rem;
        color: #f9fafb;
        margin-bottom: 18px;
        letter-spacing: 0.5px;
    }

    hr.divider {
        border: none;
        border-top: 1px solid rgba(255, 255, 255, 0.08);
        margin: 28px 0;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 1. Header Pembuka
st.markdown(
    """
    <div class="text-center" style="margin-top: 20px;">
        <div class="editorial-tag">Official Commencement Notice</div>
        <h1 class="main-heading">Graduation</h1>
        <div class="sub-heading-italic">Menandai akhir dedikasi akademik dan perayaan sebuah permulaan baru.</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# 2. Kartu Tamu Kehormatan
st.markdown(
    f"""
    <div class="luxury-card text-center">
        <div class="editorial-tag">Special Invitation For</div>
        <div class="recipient-name">{nama_tamu}</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# 3. Kartu Wisudawan
st.markdown(
    """
    <div class="luxury-card text-center">
        <div class="editorial-tag">The Graduate</div>
        <div class="graduate-name">Muhammad Furqan Himra, S.T.</div>
        <div><span class="tag-degree">Sarjana Teknik Industri</span></div>
        <p class="univ-subtitle">Departemen Teknik Industri · Universitas Andalas</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("<hr class='divider'>", unsafe_allow_html=True)

# 4. Detail Acara
st.markdown(
    """
    <div class="luxury-card text-left">
        <div class="editorial-tag" style="text-align: center; margin-bottom: 24px; color: #d4af37;">Rincian Agenda Acara</div>
        <div class="meta-title">Hari & Tanggal</div>
        <div class="meta-content">Sabtu, 19 September 2026</div>
        <div class="meta-title">Waktu Pelaksanaan</div>
        <div class="meta-content">12.30 – 14.30 WIB</div>
        <div class="meta-title">Tempat & Ruangan</div>
        <div style="font-family: 'Cormorant Garamond', serif; font-size: 1.45rem; color: #ffffff;">Gedung Jurusan Teknik Industri</div>
        <div style="font-size: 0.82rem; color: #9ca3af; letter-spacing: 0.5px; margin-top: 4px;">Fakultas Teknik, Universitas Andalas, Limau Manis, Padang</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# 5. Lokasi Interaktif (Google Maps)
st.markdown("<div class='editorial-tag'>Titik Koordinat & Navigasi</div>", unsafe_allow_html=True)
maps_url = "https://maps.google.com/?q=Jurusan+Teknik+Industri+Universitas+Andalas"

st.markdown(
    f"""
    <div style="border: 1px solid rgba(255,255,255,0.1); border-radius: 2px; overflow: hidden; margin-bottom: 12px;">
        <iframe src="https://maps.google.com/maps?q=Jurusan+Teknik+Industri+Universitas+Andalas&t=&z=16&ie=UTF8&iwloc=&output=embed" 
        width="100%" height="270" style="border:0; filter: invert(90%) hue-rotate(180deg);" allowfullscreen="" loading="lazy"></iframe>
    </div>
    <div style="text-align: center; margin-bottom: 24px;">
        <a href="{maps_url}" target="_blank" style="color: #d4af37; text-decoration: none; font-size: 0.72rem; letter-spacing: 2px; text-transform: uppercase;">
            Buka Petunjuk Arah Google Maps ↗
        </a>
    </div>
    """,
    unsafe_allow_html=True,
)

# 6. Kutipan Filosofis
st.markdown(
    """
    <div class="luxury-card text-center" style="padding: 36px 24px;">
        <p style="font-family: 'Cormorant Garamond', serif; font-style: italic; font-size: 1.25rem; color: #f3f4f6; line-height: 1.7; margin: 0;">
            “Setiap ikhtiar dan proses panjang selalu berlabuh pada pencapaian yang bermakna. Terima kasih telah menjadi bagian tak terpisahkan dalam perjalanan ini.”
        </p>
        <p style="font-size: 0.68rem; letter-spacing: 3px; color: #9ca3af; text-transform: uppercase; margin-top: 18px;">
            — Muhammad Furqan Himra, S.T.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("<hr class='divider'>", unsafe_allow_html=True)

# 7. Penutup Editorial
st.markdown(
    """
    <div class="text-center" style="margin-top: 40px; margin-bottom: 50px;">
        <div style="font-family: 'Cormorant Garamond', serif; font-size: 1.25rem; font-style: italic; color: #ffffff; margin-bottom: 8px;">
            Kehadiran Rekan-Rekan Melengkapi Rasa Syukur Kami
        </div>
        <div style="font-size: 0.7rem; letter-spacing: 3px; color: #6b7280; text-transform: uppercase; margin-bottom: 20px;">
            Departemen Teknik Industri · Universitas Andalas
        </div>
        <div>
            <a href="https://instagram.com/frqnhmra__" target="_blank" style="color: #9ca3af; text-decoration: none; font-size: 0.75rem; letter-spacing: 1.5px;">
                INSTAGRAM : @frqnhmra__
            </a>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)
