import datetime
from pathlib import Path

import streamlit as st

# Authentication constants
AUTH_EMAIL = "ahahkaur77@gmail.com"
AUTH_PASSWORD = "Arsh2024"

# Song data
SONGS = [
    {
        "title": "Tere Bina",
        "release_date": datetime.datetime(2024, 12, 1),
        "file": Path("songs/Tere Bina.mp3"),
        "lyrics": "Lyrics coming soon",
    }
]


def login_page():
    """Render the login page."""
    st.title("Welcome")
    st.write("To unlock the music, solve the riddle.")

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
                st.error("Wrong riddle answer. Try again!")


def countdown_component():
    """Display a countdown to the next song release."""
    now = datetime.datetime.now()
    upcoming_dates = sorted(
        [song["release_date"] for song in SONGS if song["release_date"] > now]
    )

    if not upcoming_dates:
        st.write("All songs released!")
        return

    diff = upcoming_dates[0] - now
    days = diff.days
    hours, remainder = divmod(diff.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    st.metric("Countdown", f"{days}d {hours}h {minutes}m {seconds}s")


def songs_component():
    """List songs with lyrics and download links."""
    for song in SONGS:
        st.header(song["title"])
        with st.expander("Lyrics"):
            st.write(song["lyrics"])

        if song["file"].exists():
            with open(song["file"], "rb") as f:
                st.download_button(
                    "Download",
                    f,
                    file_name=song["file"].name,
                )
        else:
            st.write("Download not available")


def home_page():
    """Render the authenticated home page."""
    st.title("Upcoming Release")
    countdown_component()
    songs_component()


def main():
    if "authed" not in st.session_state:
        st.session_state.authed = False

    if st.session_state.authed:
        home_page()
    else:
        login_page()


if __name__ == "__main__":
    main()
