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

# Day 2 message content
DAY2_MESSAGE = """Mood Today: 🎵🔥❤️🥵💌

Hey Sweetheart ❤️

Today is 15th almost 16th August so technically one month minus one day until your birthday arrives, but I couldn’t wait. I couldn’t just sit and let the days pass like nothing was happening. My heart was restless, my mind was in overdrive, and my body kept giving me these heatwaves 🔥… that hot, urgey, craving mood 🥵. I felt this push inside me to do something that would live forever, something that wouldn’t just be a gift but a piece of my soul 💌.

This song Tere Bina 🎵… it’s not just a track. It’s my heart ❤️, my love 🫀, my obsession 🔥 all poured into music. Every lyric ✍️ was written by me, every word born from the deepest corners of my journey in Canada 🇨🇦… the same journey where so many moments and feelings for you came alive 🌙✨. The hook line came to me the very day I returned, like my heart whispered it straight into my mind 💭, as if it was sent from a place where only you and I exist. In that moment, I knew it wasn’t just a lyric… it was a truth meant only for you 💖. This song belongs to you, the same way I do fully, completely, forever.

I composed it 🎹, produced it 🎛️, and shaped the AI singing 🎤, guiding every note, every breath, every pause, every rise and fall so it would feel exactly how I want you to feel when you hear it 😌.

Sweetheart, Tere Bina is for my one and only Arsh 💕. I don’t want anyone to take the place I have in your life. I know it sounds bad 😅, but I want you to be always mine. Even in the future, when you have your husband, your children 👨‍👩‍👧, your own life… I want to have a place in your heart that is irreplaceable. A place that is just mine. Sirf meri. Always ❤️.

I want you to choose me over everyone, even the people who are in your life now or will come later. I want to make a place where it’s impossible for you to get away from me… from my emotions, my feelings, my presence… from craving that hug 🫂 only I can give, from that kiss 💋 that no one else can ever satisfy. I want to be that person you can’t live without, can’t break away from, can’t stay away from.

You might stay with others, but I want your mind 🧠, your heart ❤️, and your soul 🕊️… and in all three, sirf mera hi naam likheya hove. I know maybe it shouldn’t be like this, but I want you to feel the safest with me and the most loved with me 🛡️💓. I know it’s possessive 😌, but I want to reach that level where you must come to me… like a lifelong addiction 😮‍💨 you can’t escape. Even if you get angry 😤, frustrated 😔, or mad at me, you still come back, because my love, my jhallak, pulls you back every single time.

Maybe I haven’t reached that level yet 😌, but I will. And when I do, I’ll be the happiest man alive ❤️. There’s still a longer way to go, but I’m already walking toward it.

So press play on Tere Bina 🎶, close your eyes 👁️‍🗨️, and let me own every thought in your mind for the next few minutes… because I love you more than the song can ever say ❤️🔥🥵.
"""


def render_song_section():
    """Render the title, message, song, and lyrics."""
    st.header("Tere Bina – Missing Anthem 🎶")
    st.markdown("# 📅 15 & 16 August – Day 2")
    st.markdown("> \"Some gifts fade… but this one will echo in your heart forever.\" 🎶❤️")
    st.markdown(DAY2_MESSAGE)
    st.audio(str(SONG_FILE), format="audio/mp3")
    with st.expander("Lyrics 🎤"):
        lyrics_md = SONG_LYRICS.replace("\n", "  \n")
        st.markdown(lyrics_md)


def login_page():
    """Render the login page."""
    render_song_section()

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
    render_song_section()


def main():
    if "authed" not in st.session_state:
        st.session_state.authed = False

    if st.session_state.authed:
        home_page()
    else:
        login_page()


if __name__ == "__main__":
    main()
