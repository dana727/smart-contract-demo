import streamlit as st

st.set_page_config(page_title="Smart Contract Demo", layout="centered")

# --- Header ---
st.title("👜 The Bag That Was Promised")
st.write("A smart contract solution for broken deals in peer-to-peer selling.")

# --- Step 1: The Agreement ---
st.header("1️⃣ The Agreement")
st.markdown("""
**Dana** finds a vintage bag listed by **Layla** for 60 JD.  
Layla promises to hold it until **Friday at 6 PM**.  
But there's no enforcement... until now.
""")

# --- Step 2: Funds Deposited ---
st.header("2️⃣ Funds Deposited – Deal Gets Locked")
st.markdown("""
Dana deposits 60 JD into a smart contract escrow.  
Layla digitally signs the contract to commit to the deal.

If Layla delivers the item on time, she gets paid.  
If she flakes, Dana gets refunded automatically.
""")

# --- Step 3: Smart Contract Outcome ---
st.header("3️⃣ What Happens Next?")

option = st.radio(
    "What did Layla do?",
    ("✅ She delivered the bag", "❌ She ghosted Dana")
)

if option == "✅ She delivered the bag":
    st.success("✔️ Dana confirms receipt. Funds released to Layla!")
    st.balloons()
elif option == "❌ She ghosted Dana":
    st.error("✖️ Deadline passed with no delivery. Dana gets a full refund.")

# --- Footer ---
st.markdown("---")
st.caption("Project by [dana] · Powered by Streamlit")

