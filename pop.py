import streamlit as st
import time


# Custom CSS for animations, colors, and UI styling
st.markdown(
    """

    <style>
        body { background-color: #f0f2f6; }
        .course-card { 
            transition: transform 0.3s;
            border-radius: 15px;
            background: linear-gradient(135deg, #6a11cb, #2575fc);
            padding: 15px;
            margin: 10px 0;
            box-shadow: 4px 4px 15px rgba(0,0,0,0.2);
            color: white;
            text-align: center;
        }
        .course-card:hover {
            transform: scale(1.05);
            box-shadow: 6px 6px 20px rgba(0,0,0,0.3);
        }
        .course-title {
            font-size: 20px; font-weight: bold;
        }
        .cart-item {
            font-size: 16px; color: #333; background: #dff0d8; padding: 10px; border-radius: 8px; margin-bottom: 5px;
        }
        .checkout-btn {
            background: #ff6b6b; color: white; padding: 10px 20px; border: none; border-radius: 8px;
            font-size: 16px; cursor: pointer;
        }
        .checkout-btn:hover {
            background: #ff4757;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("📚 Physics, Math & Programming Courses")
st.write("Select a course to watch an intro video and add it to your cart!")

# Courses data with YouTube links
courses = {
    "Physics": {
        "Quantum Mechanics": {"price": 49, "video": "https://www.youtube.com/watch?v=p7bzE1E5PMY"},
        "Classical Mechanics": {"price": 39, "video": "https://www.youtube.com/watch?v=IqVoWA0zrPQ"},
        "Thermodynamics": {"price": 29, "video": "https://www.youtube.com/watch?v=XUH9KXkzYIA"},
    },
    "Mathematics": {
        "Linear Algebra": {"price": 35, "video": "https://www.youtube.com/watch?v=kjBOesZCoqc"},
        "Calculus": {"price": 40, "video": "https://www.youtube.com/watch?v=WUvTyaaNkzM"},
        "Probability & Statistics": {"price": 30, "video": "https://www.youtube.com/watch?v=xxpc-HPKN28"},
    },
    "Programming": {
        "Python for Beginners": {"price": 25, "video": "https://www.youtube.com/watch?v=_uQrJ0TkZlc"},
        "Advanced C++": {"price": 45, "video": "https://www.youtube.com/watch?v=18c3MTX0PK0"},
        "Web Development": {"price": 50, "video": "https://www.youtube.com/watch?v=UftSB4DaRU4"},
    }
}

# Initialize cart in session state
if "cart" not in st.session_state:
    st.session_state.cart = {}

# Display course categories and courses
for category, course_list in courses.items():
    st.subheader(category)
    for course, details in course_list.items():
        with st.container():
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown(f"<div class='course-card'><span class='course-title'>{course}</span><br>💰 ${details['price']}</div>", unsafe_allow_html=True)
            with col2:
                if st.button(f"▶️ Watch {course}", key=course):
                    st.video(details["video"])
                    time.sleep(1)
                if st.button(f"🛒 Add {course}", key=f"add_{course}"):
                    st.session_state.cart[course] = details['price']

# Display cart
st.subheader("🛒 Your Cart")
if st.session_state.cart:
    total = sum(st.session_state.cart.values())
    for item, price in st.session_state.cart.items():
        st.markdown(f"<div class='cart-item'>✅ {item}: ${price}</div>", unsafe_allow_html=True)
    st.write(f"**Total: ${total}**")
    if st.button("Proceed to Checkout", key="checkout", help="Click to complete your purchase"):
        st.success("✅ Thank you for your purchase! Payment processing coming soon.")
else:
    st.write("Your cart is empty.")
