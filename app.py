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
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        padding: 1rem 0;
        border-bottom: 3px solid black;
        margin-bottom: 2rem;
    }
    .featured-box {
        border: 3px solid black;
        padding: 2rem;
        margin: 2rem 0;
        background-color: #f8f9fa;
    }
    .featured-title {
        font-size: 2rem;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    .post-card {
        border: 2px solid black;
        padding: 1rem;
        margin: 1rem 0;
        background-color: white;
    }
    .post-thumbnail {
        border: 2px solid black;
        padding: 2rem;
        text-align: center;
        background-color: #f0f0f0;
        margin-bottom: 1rem;
    }
    .section-title {
        font-size: 1.8rem;
        font-weight: bold;
        margin: 2rem 0 1rem 0;
    }
    .sidebar-box {
        border: 2px solid black;
        padding: 1rem;
        margin: 1rem 0;
        background-color: #f8f9fa;
    }
    .footer {
        border-top: 2px solid black;
        padding: 1rem;
        margin-top: 3rem;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Header with navigation
col1, col2 = st.columns([2, 1])
with col1:
    st.markdown('<div class="main-header">📝 BLOG NAME</div>', unsafe_allow_html=True)

with col2:
    nav_col1, nav_col2, nav_col3, nav_col4 = st.columns(4)
    with nav_col1:
        st.button("HOME")
    with nav_col2:
        st.button("ABOUT")
    with nav_col3:
        st.button("CONTACT")
    with nav_col4:
        st.button("🔍")

# Main content area with sidebar
main_col, sidebar_col = st.columns([2, 1])

with main_col:
    # Featured Article
    st.markdown("""
        <div class="featured-box">
            <div class="featured-title">Compelling Headline for Featured Article</div>
            <p style="margin: 1rem 0;">~~~~~~~~~~~~~~~~~~~~~~~~~~~</p>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("READ MORE", key="featured"):
        st.info("Opening featured article...")
    
    # Recent Posts Section
    st.markdown('<div class="section-title">RECENT POSTS</div>', unsafe_allow_html=True)
    
    # Create three columns for recent posts
    post_col1, post_col2, post_col3 = st.columns(3)
    
    posts = [
        {"title": "INCENT TISTS", "author": "Author Name", "date": "Date"},
        {"title": "INCENT TISTE", "author": "Author Name", "date": "Date"},
        {"title": "INCENT TUSTS", "author": "Author Name", "date": "Date"}
    ]
    
    for col, post in zip([post_col1, post_col2, post_col3], posts):
        with col:
            st.markdown(f"""
                <div class="post-card">
                    <div class="post-thumbnail">IMAGE<br>POST<br>THUMBNAIL</div>
                    <h3 style="text-align: center; margin: 1rem 0;">{post['title']}</h3>
                    <p style="text-align: center; font-size: 0.9rem;">{post['author']}, {post['date']}</p>
                    <p style="text-align: center;">~~~~~~~~~~~<br>~~~~~~~~~~~<br>~~~~~~~~~~~</p>
                </div>
            """, unsafe_allow_html=True)

with sidebar_col:
    # Newsletter Subscription
    st.markdown("""
        <div class="sidebar-box">
            <h3 style="text-align: center;">SUBSCRIBE<br>TO NEWSLETTER</h3>
            <p style="text-align: center; font-size: 2rem;">✉️</p>
        </div>
    """, unsafe_allow_html=True)
    
    email = st.text_input("Email", placeholder="your@email.com", label_visibility="collapsed")
    if st.button("Subscribe"):
        st.success("Subscribed successfully!")
    
    # Popular Posts
    st.markdown("""
        <div class="sidebar-box">
            <h3>POPULAR POSTS</h3>
            <ul style="list-style-type: none; padding-left: 0;">
                <li>• SOKK EGUE VB</li>
                <li>• TIKO ITTE SUBES</li>
                <li>• TO BOGT, TIGRES</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    
    # Sidebar
    st.markdown("""
        <div class="sidebar-box">
            <h3>SIDEBAR</h3>
            <ul style="list-style-type: none; padding-left: 0;">
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
        <p>FOOTER</p>
        <p>⬆️ 🐦 📷 © 2024 Blog Co.</p>
    </div>
""", unsafe_allow_html=True)