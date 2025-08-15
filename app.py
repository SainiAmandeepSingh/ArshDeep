from pathlib import Path

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


def home_page():
    """Render the authenticated home page."""
    st.balloons()
    st.header("Tere Bina – A Birthday Anthem 🎶")
    st.subheader("Why this song exists 💌")
    st.write(
        """
        From the moment the idea sparked, I knew this song had to be more than a melody. It's my heart,
        recorded, arranged, and wrapped in sound just for you. I sat in my tiny room, headphones on,
        piecing together chords while thinking about your smile. Every lyric was scribbled from
        memories of our time together and the quiet nights I spent in Canada, thousands of miles away,
        missing you more with every snowfall. The hook came to me on the flight home; those lines kept
        echoing until I turned them into music. To make it special, I used AI to shape the instruments
        and even to give a voice to my feelings. The software didn't just sing—it obeyed every tweak I
        made so it could breathe the way I do when I think about you. Today marks a month before your
        birthday, and this track is my promise that I'll keep creating art just for you. No one else
        will ever weave something like this for your heart. I want you to crave the sound of my voice,
        to feel safe when the world is heavy, and to know that every beat is a reminder that you are
        egotistically mine—kise di hor di nahi, sirf meri.
        """
    )
    st.audio(str(SONG_FILE), format="audio/mp3")
    with st.expander("Lyrics 🎤"):
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
