import random
import streamlit as st


# A small pool of quotes — one is picked at random each time the page loads.
QUOTES = [
    "Take care of your body. It's the only place you have to live.",
    "Let food be thy medicine and medicine be thy food.",
    "Health is not about the weighing scale, it's about how you feel.",
    "Small daily habits build lifelong health.",
    "Eating well is a form of self-respect.",
    "Your diet is a bank account. Good food choices are good investments.",
]


def show_home():

    # ==============================
    # PAGE CSS
    # ==============================

    st.markdown(
        """
        <style>

        .home-section-title {
            color: #1E3A8A;
            font-size: 26px;
            font-weight: 700;
            margin-top: 30px;
            margin-bottom: 18px;
        }

        .feature-card {
            background: white;
            border-radius: 22px;
            padding: 28px 22px;
            text-align: center;
            min-height: 190px;
            box-shadow: 0 8px 25px rgba(30,58,138,0.08);
            transition: transform 0.2s ease;
        }

        .feature-card:hover {
            transform: translateY(-4px);
        }

        .feature-icon {
            font-size: 34px;
            margin-bottom: 10px;
        }

        .feature-title {
            font-size: 18px;
            font-weight: 700;
            color: #1E3A8A;
            margin-bottom: 8px;
        }

        .feature-text {
            font-size: 14px;
            color: #64748B;
            line-height: 1.5;
        }

        .step-badge {
            width: 42px;
            height: 42px;
            border-radius: 50%;
            background: #1E3A8A;
            color: white;
            font-weight: 800;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 12px auto;
        }

        </style>
        """,
        unsafe_allow_html=True
    )


    # ==============================
    # HERO
    # ==============================

    quote = random.choice(QUOTES)

    st.html(
        f"""
        <div style="
            background: linear-gradient(135deg, #1E3A8A, #3B82F6);
            padding: 50px 45px;
            border-radius: 25px;
            color: white;
            margin-bottom: 30px;
        ">

            <div style="
                font-size: 46px;
                font-weight: 800;
            ">
                NutriNyx 🥗
            </div>

            <div style="
                font-size: 19px;
                margin-top: 12px;
                opacity: 0.9;
            ">
                Your AI-powered nutrition companion — understand your food,
                track your health, and eat smarter.
            </div>

            <div style="
                margin-top: 26px;
                padding-top: 18px;
                border-top: 1px solid rgba(255,255,255,0.25);
                font-size: 16px;
                font-style: italic;
                opacity: 0.95;
            ">
                "{quote}"
            </div>

        </div>
        """
    )


    # ==============================
    # WHAT NUTRINYX DOES
    # ==============================

    st.markdown(
        '<div class="home-section-title">✨ What You Can Do</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    features = [
        ("🥗", "Food Analyzer", "Enter or describe a meal and instantly break down its nutritional value."),
        ("📊", "Nutrition Report", "See a clear picture of your intake and how it stacks up against your goals."),
        ("🤖", "AI Recommendations", "Get personalized, AI-generated suggestions to improve your diet."),
    ]

    for col, (icon, title, text) in zip([col1, col2, col3], features):
        with col:
            st.html(
                f"""
                <div class="feature-card">
                    <div class="feature-icon">{icon}</div>
                    <div class="feature-title">{title}</div>
                    <div class="feature-text">{text}</div>
                </div>
                """
            )


    # ==============================
    # HOW IT WORKS
    # ==============================

    st.markdown(
        '<div class="home-section-title">🚀 How It Works</div>',
        unsafe_allow_html=True
    )

    s1, s2, s3 = st.columns(3)

    steps = [
        ("1", "Tell us what you ate", "Log or describe a meal in the Food Analyzer."),
        ("2", "We analyze it", "NutriNyx breaks it down into calories, macros, and more."),
        ("3", "Get smart guidance", "Receive AI-backed tips tailored to your health goals."),
    ]

    for col, (num, title, text) in zip([s1, s2, s3], steps):
        with col:
            st.html(
                f"""
                <div class="feature-card">
                    <div class="step-badge">{num}</div>
                    <div class="feature-title">{title}</div>
                    <div class="feature-text">{text}</div>
                </div>
                """
            )


    # ==============================
    # CALL TO ACTION
    # ==============================

    st.html(
        """
        <div style="
            margin-top: 30px;
            background: linear-gradient(135deg, #EFF6FF, #F4F8FF);
            border-radius: 22px;
            padding: 25px;
            border-left: 6px solid #3B82F6;
            box-shadow: 0 8px 25px rgba(30,58,138,0.06);
            text-align: center;
            font-size: 16px;
            color: #475569;
        ">
            👉 Head to <b>Food Analyzer</b> from the sidebar to get started.
        </div>
        """
    )