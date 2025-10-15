import streamlit as st
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="The Minimalist Mind",
    page_icon="📝",
    layout="wide"
)

# Custom CSS to style the blog
st.markdown("""
    <style>
    .stApp {
        background-color: #fafafa;
    }

    #MainMenu, footer, header {visibility: hidden;}

    .main-header {
        font-size: 3.2rem;
        font-weight: 900;
        padding: 1.5rem 0;
        border-top: 4px solid #000;
        border-bottom: 4px solid #000;
        margin-bottom: 2rem;
        color: #000;
        font-family: 'Arial Black', sans-serif;
    }

    .featured-box {
        border: 3px solid #000;
        padding: 3rem 2rem;
        margin: 2rem 0;
        background-color: #fff;
    }
    .featured-title {
        font-size: 2.2rem;
        font-weight: bold;
        margin-bottom: 1rem;
        color: #000;
        line-height: 1.2;
    }

    .stButton > button {
        background-color: #000;
        color: #fff;
        border: 3px solid #000;
        padding: 0.7rem 2rem;
        font-size: 1rem;
        font-weight: bold;
        border-radius: 0;
        cursor: pointer;
    }
    .stButton > button:hover {
        background-color: #333;
        border-color: #333;
    }

    .nav-button {
        background-color: transparent !important;
        color: #000 !important;
        border: none !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
    }

    .section-title {
        font-size: 2rem;
        font-weight: 900;
        margin: 3rem 0 1.5rem 0;
        color: #000;
        font-family: 'Arial Black', sans-serif;
    }

    .post-card {
        border: 3px solid #000;
        padding: 0;
        margin: 1rem 0;
        background-color: #fff;
    }
    .post-thumbnail {
        border-bottom: 3px solid #000;
        padding: 3rem 1rem;
        text-align: center;
        background-color: #f5f5f5;
        font-weight: bold;
        color: #000;
    }
    .post-content { padding: 1.5rem; }
    .post-title {
        font-size: 1.4rem;
        font-weight: 900;
        text-align: center;
        margin: 1rem 0;
        color: #000;
    }
    .post-meta {
        text-align: center;
        font-size: 0.9rem;
        color: #333;
        margin: 0.5rem 0;
    }
    .post-excerpt {
        text-align: center;
        color: #000;
        margin: 1rem 0;
        line-height: 1.4;
    }

    .sidebar-box {
        border: 3px solid #000;
        padding: 1.5rem;
        margin: 1.5rem 0;
        background-color: #fff;
    }
    .sidebar-title {
        font-size: 1.3rem;
        font-weight: 900;
        margin-bottom: 1rem;
        color: #000;
        text-align: center;
    }
    .sidebar-list {
        list-style-type: none;
        padding-left: 0;
        color: #000;
    }
    .sidebar-list li {
        margin: 0.8rem 0;
        font-size: 1rem;
    }

    .footer {
        border-top: 3px solid #000;
        padding: 2rem;
        margin-top: 4rem;
        text-align: center;
        color: #000;
        font-size: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Header with navigation
col1, col2 = st.columns([3, 2])
with col1:
    st.markdown('<div class="main-header">THE MINIMALIST MIND</div>', unsafe_allow_html=True)

with col2:
    st.write("")
    nav1, nav2, nav3, nav4 = st.columns(4)
    with nav1:
        if st.button("HOME", key="nav_home"):
            st.info("You are already on the home page.")
    with nav2:
        if st.button("ABOUT", key="nav_about"):
            st.info("A blog about design, productivity, and simple living.")
    with nav3:
        if st.button("CONTACT", key="nav_contact"):
            st.info("Email: contact@minimalistmind.com | Instagram: @minimalistmind")
    with nav4:
        if st.button("🔍", key="nav_search"):
            st.info("Search feature coming soon.")

# Main content and sidebar
main_col, sidebar_col = st.columns([2.5, 1])

with main_col:
    st.markdown("""
        <div class="featured-box">
            <div class="featured-title">How Simplicity Fuels Creativity</div>
            <p style="color:#000; font-size:1.1rem;">In a world obsessed with more—more tools, more apps, more options—true creativity often emerges from less. Discover how minimalism can sharpen your focus and unlock deeper inspiration.</p>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("READ MORE", key="featured"):
        st.success("Opening full article...")

    st.markdown('<div class="section-title">RECENT POSTS</div>', unsafe_allow_html=True)

    post_col1, post_col2, post_col3 = st.columns(3)
    posts = [
        {"title": "Digital Declutter in 3 Steps", "author": "Veda Kimbahune", "date": "Oct 2025", "excerpt": "Reclaim your focus by organizing your digital life."},
        {"title": "Why White Space Matters", "author": "Veda Kimbahune", "date": "Oct 2025", "excerpt": "Good design isn’t about adding more—it’s about removing clutter."},
        {"title": "Morning Routines That Work", "author": "Veda Kimbahune", "date": "Sep 2025", "excerpt": "Simplify your mornings and set the tone for productivity."}
    ]

    for col, post in zip([post_col1, post_col2, post_col3], posts):
        with col:
            st.markdown(f"""
                <div class="post-card">
                    <div class="post-thumbnail">IMAGE<br>PLACEHOLDER</div>
                    <div class="post-content">
                        <div class="post-title">{post['title']}</div>
                        <div class="post-meta">{post['author']} — {post['date']}</div>
                        <div class="post-excerpt">{post['excerpt']}</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

with sidebar_col:
    st.markdown("""
        <div class="sidebar-box">
            <div class="sidebar-title">SUBSCRIBE</div>
            <p style="text-align:center;font-size:1rem;">Get updates on simplicity, design, and focus delivered to your inbox.</p>
        </div>
    """, unsafe_allow_html=True)
    email = st.text_input("", placeholder="Enter your email", label_visibility="collapsed")
    if st.button("Subscribe", key="subscribe"):
        if email:
            st.success(f"Thanks for subscribing, {email}!")

    st.markdown("""
        <div class="sidebar-box">
            <div class="sidebar-title">POPULAR POSTS</div>
            <ul class="sidebar-list">
                <li>• The Art of Doing Nothing</li>
                <li>• Designing Calm Interfaces</li>
                <li>• The Power of Fewer Goals</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="sidebar-box">
            <div class="sidebar-title">CONNECT</div>
            <ul class="sidebar-list">
                <li>📧 contact@minimalistmind.com</li>
                <li>📸 instagram.com/minimalistmind</li>
                <li>🐦 twitter.com/minimalistmind</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class="footer">
        <p style="font-weight:600;">Made with ❤️ by The Minimalist Mind</p>
        <p>© 2025 MinimalistMind — All Rights Reserved</p>
    </div>
""", unsafe_allow_html=True)
