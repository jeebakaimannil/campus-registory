import streamlit as st

# =====================================================================
# STREAMLIT FRONTEND CONFIGURATION & UI CELL Layout
# =====================================================================
st.set_page_config(page_title="Campus Lab Registry", page_icon="🎓", layout="centered")

st.title("🎓 Campus Lab Registration Portal")
st.write("Fill out the interactive form fields below to generate your official registry sheet.")

# 1. Setting up our dynamic database dictionary to capture inputs from the web UI
extracted_user_data = {}

# 2. Building clean visual text boxes and drop-down selectors
extracted_user_data["name"] = st.text_input("Enter your full name:", placeholder="e.g. Mohammed Rehan")

# Capturing age cleanly as a sliding track wrapper
extracted_user_data["age"] = st.slider("Select your current age:", min_value=16, max_value=30, value=18)

# Blood group selector drop-down component tray
extracted_user_data["blood"] = st.selectbox(
    "Select your official blood group:",
    ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]
)

# 3. Form submission button gate check
if st.button("🚀 Compile & Verify Registration Sheet"):
    if extracted_user_data["name"].strip() == "":
        st.error("🚨 Validation Failure: Please enter a valid name before submitting!")
    else:
        st.success("🎉 Profile Verified & Securely Registered!")

        # Displaying the completed digital frontend form sheet inside a visual window frame box
        st.markdown("### 📋 OFFICIAL CAMPUS RECORD SHEET")
        st.info(f"**Name:** {extracted_user_data['name'].upper()}")
        st.info(f"**Age Metrics:** {extracted_user_data['age']} Years Old")
        st.info(f"**Blood Group Category:** {extracted_user_data['blood']}")
