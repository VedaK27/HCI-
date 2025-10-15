import streamlit as st
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Blog Name",
    page_icon="📝",
    layout="wide"
)

# Custom CSS to style the blog
st.markdown("""
    <style>
    /* Global styles */
    .stApp {
        background-color: #faf8f3;
    }
    
    /* Hide Streamlit default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Main header */
    .main-header {
        font-size: 3.5rem;
        font-weight: 900;
        padding: 1.5rem 0;
        border-top: 5px solid #000;
        border-bottom: 5px solid #000;
        margin-bottom: 2rem;
        color: #000;
        font-family: 'Arial Black', sans-serif;
    }
    
    /* Featured box */
    .featured-box {
        border: 4px solid #000;
        padding: 3rem 2rem;
        margin: 2rem 0;
        background-color: #fff;
    }
    .featured-title {
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 1rem;
        color: #000;
        line-height: 1.2;
    }
    .featured-wavy {
        font-size: 1.5rem;
        color: #000;
        margin: 1.5rem 0;
    }
    
    /* Buttons */
    .stButton > button {
        background-color: #000;
        color: #fff;
        border: 3px solid #000;
        padding: 0.8rem 2rem;
        font-size: 1.1rem;
        font-weight: bold;
        border-radius: 0;
        cursor: pointer;
    }
    .stButton > button:hover {
        background-color: #333;
        border-color: #333;
    }
    
    /* Navigation buttons */
    .nav-button {
        background-color: transparent !important;
        color: #000 !important;
        border: none !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
    }
    
    /* Section titles */
    .section-title {
        font-size: 2.2rem;
        font-weight: 900;
        margin: 3rem 0 1.5rem 0;
        color: #000;
        font-family: 'Arial Black', sans-serif;
    }
    
    /* Post cards */
    .post-card {
        border: 3px solid #000;
        padding: 0;
        margin: 1rem 0;
        background-color: #fff;
        height: 100%;
    }
    .post-thumbnail {
        border-bottom: 3px solid #000;
        padding: 3rem 1rem;
        text-align: center;
        background-color: #f5f5f5;
        font-weight: bold;
        color: #000;
        font-size: 0.9rem;
    }
    .post-content {
        padding: 1.5rem;
    }
    .post-title {
        font-size: 1.5rem;
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
    
    /* Sidebar boxes */
    .sidebar-box {
        border: 3px solid #000;
        padding: 1.5rem;
        margin: 1.5rem 0;
        background-color: #fff;
    }
    .sidebar-title {
        font-size: 1.4rem;
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
        color: #000;
        font-size: 1rem;
    }
    
    /* Email input */
    .stTextInput > div > div > input {
        border: 2px solid #000;
        border-radius: 0;
        padding: 0.5rem;
        font-size: 1rem;
    }
    
    /* Footer */
    .footer {
        border-top: 4px solid #000;
        padding: 2rem;
        margin-top: 4rem;
        text-align: center;
        color: #000;
        font-size: 1rem;
    }
    .footer-icons {
        font-size: 1.5rem;
        margin: 0.5rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Header with navigation
col1, col2 = st.columns([3, 2])
with col1:
    st.markdown('<div class="main-header">BLOG NAME</div>', unsafe_allow_html=True)

with col2:
    st.write("")
    st.write("")
    nav_col1, nav_col2, nav_col3, nav_col4 = st.columns(4)
    with nav_col1:
        if st.button("HOME", key="nav_home"):
            pass
    with nav_col2:
        if st.button("ABOUT", key="nav_about"):
            pass
    with nav_col3:
        if st.button("CONTACT", key="nav_contact"):
            pass
    with nav_col4:
        if st.button("🔍", key="nav_search"):
            pass

# Main content area with sidebar
main_col, sidebar_col = st.columns([2.5, 1])

with main_col:
    # Featured Article
    st.markdown("""
        <div class="featured-box">
            <div class="featured-title">Compelling Headline for<br>Featured Article</div>
            <div class="featured-wavy">～～～～～～～～～～～～～</div>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("READ MORE", key="featured"):
        st.success("Opening featured article...")
    
    # Recent Posts Section
    st.markdown('<div class="section-title">RECENT POSTS</div>', unsafe_allow_html=True)
    
    # Create three columns for recent posts
    post_col1, post_col2, post_col3 = st.columns(3)
    
    posts = [
        {"title": "INCENT\nTISTS", "author": "Author Name", "date": "Date"},
        {"title": "INCENT\nTISTE", "author": "Author Name", "date": "Date"},
        {"title": "INCENT\nTUSTS", "author": "Author Name", "date": "Date"}
    ]
    
    for col, post in zip([post_col1, post_col2, post_col3], posts):
        with col:
            st.markdown(f"""
                <div class="post-card">
                    <div class="post-thumbnail">IMAGE<br>POST<br>THUMBNAIL</div>
                    <div class="post-content">
                        <div class="post-title">{post['title'].replace(chr(10), '<br>')}</div>
                        <div class="post-meta">{post['author']}, {post['date']}</div>
                        <div class="post-excerpt">～～～～～～<br>～～～～～～<br>～～～～～～</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

with sidebar_col:
    # Newsletter Subscription
    st.markdown("""
        <div class="sidebar-box">
            <div class="sidebar-title">SUBSCRIBE<br>TO NEWSLETTER</div>
            <p style="text-align: center; font-size: 2.5rem; margin: 1rem 0;">✉</p>
        </div>
    """, unsafe_allow_html=True)
    
    email = st.text_input("", placeholder="Enter your email", label_visibility="collapsed", key="email")
    if st.button("Subscribe", key="subscribe"):
        if email:
            st.success("Thanks for subscribing!")
    
    # Popular Posts
    st.markdown("""
        <div class="sidebar-box">
            <div class="sidebar-title">POPULAR POSTS</div>
            <ul class="sidebar-list">
                <li>• SOKK EGUE VB</li>
                <li>• TIKO ITTE SUBES</li>
                <li>• TO BOGT, TIGRES</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    
    # Sidebar
    st.markdown("""
        <div class="sidebar-box">
            <div class="sidebar-title">SIDEBAR</div>
            <ul class="sidebar-list">
                <li>• THAKE THUMBETS</li>
                <li>• COIK SRALS</li>
                <li>• GERAE STINBVSS</li>
                <li>• TANK SRALC</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class="footer">
        <p style="font-weight: 600; margin-bottom: 0.5rem;">FOOTER</p>
        <div class="footer-icons">⬆ 🐦 📷 <span style="margin-left: 1rem;">© 2024 Blog Co.</span></div>
    </div>
""", unsafe_allow_html=True)