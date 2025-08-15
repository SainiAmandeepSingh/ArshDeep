import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import streamlit as st

# Authentication constants
AUTH_EMAIL = "ahkaur77@gmail.com"
AUTH_PASSWORD = "Arsh2024"

# Song data
RELEASE_TIME = datetime.datetime(2024, 12, 1, 18, 0, tzinfo=ZoneInfo("America/Toronto"))
SONG_FILE = Path("songs/Tere Bina.mp3")
SONG_LYRICS = """Tere bina main na reh sakda
Gallan vich teri rooh da rang wakda
City vi lagge khaali teri yaad ch
Tere bina main na reh sakda

Tere pair de nishaan vi main yaad rakhda
Phone di screen te main wait karda
Naal tere si taan duniya meri si slow
Ajj vi dil ch bas tu hi glow

Gallan teriyan repeat hundiyan mind vich
Photo teri lockscreen, main find vich
Dooriyan ne sade raah thalle likhe
Par rabb ne saanu ik duje vaste likhe

Tere bina main na reh sakda
Gallan vich teri rooh da rang wakda
City vi lagge khaali teri yaad ch
Tere bina main na reh sakda

Tere smile ch ae meri jaan
Dil de paper te tera hi naam
Door reh ke vi tu mere naal
Ik pal vi na laggi ve khaali haal

Eh dooriyan vi kise din mukan
Asmaan vich likheya ae tera makan
Mere geet, mere sapne, sab tu
Gallan ch sirf tera hi rubaru

Tere bina main na reh sakda
Gallan vich teri rooh da rang wakda
City vi lagge khaali teri yaad ch
Tere bina main na reh sakda
"""


def login_page():
    """Render the login page."""
    st.title("Welcome 🎉")
    st.write(
        "🎉 **Arsh**, today is exactly a month left for your birthday, and I "
        "wanted to try something new, something I've never done before; I wanted "
        "to write a Punjabi song for you... \n\nLog in with your credentials to unlock it. "
        "(Remember, you changed this password 48 hours ago, so you'd better "
        "remember it 😉)"
    )

    # Center the form on the page
    left, center, right = st.columns([1, 2, 1])
    with center:
        with st.form("login_form", clear_on_submit=False):
            email = st.text_input("Email")
            password = st.text_input("Password", type="password")
            submitted = st.form_submit_button("Enter")

        if submitted:
            if email == AUTH_EMAIL and password == AUTH_PASSWORD:
                st.session_state.authed = True
                st.experimental_rerun()
            else:
                st.error("Wrong answer. Try again! 😅")


def countdown_component():
    """Display a countdown to the song release."""
    now = datetime.datetime.now(ZoneInfo("America/Toronto"))
    diff = RELEASE_TIME - now

    if diff.total_seconds() > 0:
        days = diff.days
        hours, remainder = divmod(diff.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        st.title(f"{days}d {hours}h {minutes}m {seconds}s")
    else:
        st.title("0d 0h 0m 0s")


def home_page():
    """Render the authenticated home page."""
    st.header("Countdown to Release ⏳")
    countdown_component()

    now = datetime.datetime.now(ZoneInfo("America/Toronto"))
    if now >= RELEASE_TIME:
        st.audio(str(SONG_FILE), format="audio/mp3")
        if SONG_FILE.exists():
            with open(SONG_FILE, "rb") as f:
                st.download_button("Download", f, file_name=SONG_FILE.name)
        st.markdown(SONG_LYRICS)


def main():
    if "authed" not in st.session_state:
        st.session_state.authed = False

    if st.session_state.authed:
        home_page()
    else:
        login_page()


if __name__ == "__main__":
    main()
