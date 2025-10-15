import streamlit as st
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Modern Blog",
    page_icon="📝",
    layout="wide"
)

# Custom CSS for modern attractive UI
st.markdown("""
    <style>
    /* Global */
    body {
        background-color: #fafafa;
        font-family: 'Inter', sans-serif;
    }

    .main-header {
        font-size: 3rem;
        font-weight: 800;
        color: #4b0082;
        letter-spacing: 1px;
        padding: 1rem 0;
        border-bottom: 4px solid #b19cd9;
        margin-bottom: 2rem;
    }

    /* Navigation */
    .stButton button {
        background-color: #ffffff;
        border: 2px solid #b19cd9;
        color: #4b0082;
        border-radius: 20px;
        padding: 0.5rem 1rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    .stButton button:hover {
        background-color: #b19cd9;
        color: white;
        border-color: #b19cd9;
        box-shadow: 0px 0px 10px rgba(177, 156, 217, 0.4);
    }

    /* Featured Box */
    .featured-box {
        border: none;
        background: linear-gradient(135deg, #ede7f6, #f3e5f5);
        padding: 2rem;
        border-radius: 16px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        margin-bottom: 2rem;
    }
    .featured-title {
        font-size: 2rem;
        font-weight: 700;
        color: #4b0082;
        margin-bottom: 1rem;
    }

    /* Post Cards */
    .post-card {
        border: none;
        background: white;
        padding: 1.2rem;
        border-radius: 16px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        transition: transform 0.2s ease, box-shadow 0.3s ease;
    }
    .post-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 18px rgba(0,0,0,0.1);
    }
    .post-thumbnail {
        border-radius: 12px;
        height: 160px;
        background: linear-gradient(135deg, #d1c4e9, #e1bee7);
        color: #4b0082;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 600;
        font-size: 1.1rem;
        margin-bottom: 1rem;
    }

    /* Sidebar Boxes */
    .sidebar-box {
        border: none;
        background-color: #f4f0fa;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        margin: 1rem 0;
    }
    .sidebar-box h3 {
        color: #4b0082;
        text-align: center;
        margin-bottom: 1rem;
    }

    /* Section Title */
    .section-title {
        font-size: 1.8rem;
        font-weight: 700;
        color: #4b0082;
        margin: 2rem 0 1rem 0;
        border-left: 6px solid #b19cd9;
        padding-left: 0.6rem;
    }

    /* Footer */
    .footer {
        border-top: 2px solid #d1c4e9;
        padding: 2rem 0;
        text-align: center;
        color: #4b0082;
        margin-top: 4rem;
        font-size: 0.9rem;
    }
    </style>
""", unsafe_allow_html=True)

# Header with navigation
col1, col2 = st.columns([2, 1])
with col1:
    st.markdown('<div class="main-header">📝 MODERN BLOG</div>', unsafe_allow_html=True)
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
    st.markdown("""
        <div class="featured-box">
            <div class="featured-title">✨ The Future of Minimal Web Design</div>
            <p>Discover how minimal layouts and subtle animations redefine digital experiences in 2025...</p>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("READ MORE", key="featured"):
        st.info("Opening featured article...")

    st.markdown('<div class="section-title">📚 Recent Posts</div>', unsafe_allow_html=True)
    
    post_col1, post_col2, post_col3 = st.columns(3)
    posts = [
        {"title": "Why UX Simplicity Wins", "author": "Jane Doe", "date": "Oct 2025"},
        {"title": "Top 5 Design Trends", "author": "John Smith", "date": "Sept 2025"},
        {"title": "Color Psychology 101", "author": "Alice Brown", "date": "Aug 2025"}
    ]
    
    for col, post in zip([post_col1, post_col2, post_col3], posts):
        with col:
            st.markdown(f"""
                <div class="post-card">
                    <div class="post-thumbnail">IMAGE PREVIEW</div>
                    <h3 style="text-align:center;color:#4b0082;">{post['title']}</h3>
                    <p style="text-align:center;font-size:0.9rem;color:gray;">{post['author']} • {post['date']}</p>
                    <p style="text-align:center;">Short excerpt about the post...</p>
                </div>
            """, unsafe_allow_html=True)

with sidebar_col:
    st.markdown("""
        <div class="sidebar-box">
            <h3>📬 Subscribe to Newsletter</h3>
            <p style="text-align:center;font-size:2rem;">✉️</p>
        </div>
    """, unsafe_allow_html=True)
    
    email = st.text_input("Email", placeholder="your@email.com", label_visibility="collapsed")
    if st.button("Subscribe"):
        st.success("Subscribed successfully!")

    st.markdown("""
        <div class="sidebar-box">
            <h3>🔥 Popular Posts</h3>
            <ul style="list-style:none;padding-left:0;color:#4b0082;">
                <li>• The Art of Typography</li>
                <li>• Designing for Accessibility</li>
                <li>• AI Tools for Designers</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="sidebar-box">
            <h3>🧭 Categories</h3>
            <ul style="list-style:none;padding-left:0;color:#4b0082;">
                <li>• UI/UX Design</li>
                <li>• Productivity</li>
                <li>• Frontend Tips</li>
                <li>• Creative Workflow</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

st.markdown("""
    <div class="footer">
        <p>Made with 💜 using Streamlit</p>
        <p>⬆️ 🐦 📷 © 2025 Modern Blog</p>
    </div>
""", unsafe_allow_html=True)
