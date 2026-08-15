import streamlit as st


def show_footer():

    st.markdown(
        """
        <style>

        .footer {

            background: linear-gradient(
                135deg,
                #1E3A8A,
                #0F1F4D
            );

            padding:25px;
            border-radius:20px;
            text-align:center;
            color:white;
            margin-top:40px;

        }


        .footer-title {

            font-size:20px;
            font-weight:700;

        }


        .footer-text {

            font-size:14px;
            color:#BFE0FF;

        }

        </style>
        """,
        unsafe_allow_html=True
    )


    st.markdown(
        """
        <div class="footer">

        <div class="footer-title">
        🥗 NutriNyx
        </div>

        <br>

        <div class="footer-text">
        AI-powered nutrition companion
        <br>
        Know What You Eat. Live Better.
        <br><br>
        © 2026 NutriNyx • Built with ❤️ using Streamlit
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )