import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import streamlit as st

st.set_page_config(
    page_title="Arsh's Birthday Song",
    page_icon="🎂",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Authentication constants
AUTH_EMAIL = "ahkaur77@gmail.com"
AUTH_PASSWORD = "Arsh2004"

# Song data
RELEASE_TIME = datetime.datetime(2024, 12, 1, 18, 0, tzinfo=ZoneInfo("America/Toronto"))
SONG_FILE = Path("songs/Tere Bina.mp3")
SONG_LYRICS = """Tere bina main na reh sakda ❤️
Gallan vich teri rooh da rang wakda 💫
City vi lagge khaali teri yaad ch 🌆
Tere bina main na reh sakda 💔

Tere pair de nishaan vi main yaad rakhda 👣
Phone di screen te main wait karda 📱
Naal tere si taan duniya meri si slow 🐢
Ajj vi dil ch bas tu hi glow ✨

Gallan teriyan repeat hundiyan mind vich 🔁
Photo teri lockscreen, main find vich 📸
Dooriyan ne sade raah thalle likhe 🛣️
Par rabb ne saanu ik duje vaste likhe 🙏

Tere bina main na reh sakda ❤️
Gallan vich teri rooh da rang wakda 💫
City vi lagge khaali teri yaad ch 🌆
Tere bina main na reh sakda 💔

Tere smile ch ae meri jaan 😊
Dil de paper te tera hi naam 📝
Door reh ke vi tu mere naal 🤝
Ik pal vi na laggi ve khaali haal 🕰️

Eh dooriyan vi kise din mukan 📅
Asmaan vich likheya ae tera makan ☁️
Mere geet, mere sapne, sab tu 🎵
Gallan ch sirf tera hi rubaru 🌟

Tere bina main na reh sakda ❤️
Gallan vich teri rooh da rang wakda 💫
City vi lagge khaali teri yaad ch 🌆
Tere bina main na reh sakda 💔
"""


def login_page():
    """Render the login page."""
    st.markdown("<h2 style='text-align:center;'>Welcome 🎉</h2>", unsafe_allow_html=True)
    st.write(
        "🎂 **Arsh**, we're exactly a month away from your birthday! I wrote, "
        "composed, and even taught an AI to sing this Punjabi love song just for you. "
        "This little app will be our home for every new song I release for you, "
        "starting with this birthday track. To unlock it, prove you're the real star "
        "by remembering the password you changed 48 hours ago—because obviously this "
        "gift is password-protected. 😜"
    )
    st.caption(
        "P.S. The lines like 'Tere bina main na reh sakda' came straight from my heart, music and all. 🎶"
    )
    st.caption("Every future release will live here so you never miss a beat of our story. 💞")

    with st.sidebar:
        st.header("🔐 Unlock the surprise")
        st.caption(
            "Only the one who knows the secret email and its latest password may pass! ✨ "
            "This gate keeps the surprise safe until you're ready."
        )
        with st.form("login_form", clear_on_submit=False):
            email = st.text_input("Email")
            password = st.text_input("Password", type="password")
            submitted = st.form_submit_button("Enter 🎈")

        if submitted:
            if email == AUTH_EMAIL and password == AUTH_PASSWORD:
                st.session_state.authed = True
                st.rerun()
            else:
                st.error("Wrong answer. Try again! 😅")


def countdown_component():
    """Display a countdown to the song release."""
    now = datetime.datetime.now(datetime.timezone.utc).astimezone(ZoneInfo("America/Toronto"))
    diff = RELEASE_TIME - now

    if diff.total_seconds() > 0:
        days = diff.days
        hours, remainder = divmod(diff.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        st.subheader(f"{days}d {hours}h {minutes}m {seconds}s")
    else:
        st.subheader("0d 0h 0m 0s")


def home_page():
    """Render the authenticated home page."""
    st.header("Countdown to Release ⏳")
    countdown_component()

    now = datetime.datetime.now(ZoneInfo("America/Toronto"))
    if now >= RELEASE_TIME:
        st.balloons()
        st.subheader("Why this song exists 💌")
        st.write(
            "I poured my heart into this track to celebrate your birthday and to mark "
            "the beginning of many songs I'll create just for you. Press play, close "
            "your eyes, and feel the love in every beat."
        )
        st.audio(str(SONG_FILE), format="audio/mp3")
        st.write("### Lyrics")
        lyrics_md = SONG_LYRICS.replace("\n", "  \n")
        st.markdown(lyrics_md)


def main():
    if "authed" not in st.session_state:
        st.session_state.authed = False

    if st.session_state.authed:
        home_page()
    else:
        login_page()


if __name__ == "__main__":
    main()
