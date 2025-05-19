import streamlit as st

st.set_page_config(page_title="Smart Contract Demo", layout="centered")

st.title("👜 The Bag That Was Promised")
st.markdown("""
A peer-to-peer deal goes wrong — until code steps in. 
This is an interactive simulation of a smart contract solving a trust problem in everyday life.
""")

# --- Step 1: The Agreement ---
st.header("📜 Step 1: The Verbal Deal")
st.write("Dana agrees to buy a vintage bag from Layla for 60 JD. Layla promises to hold it until Friday.")
if st.button("🤝 I Accept the Verbal Deal"):
    st.session_state.accepted = True

# --- Step 2: Smart Contract Activation ---
if st.session_state.get("accepted"):
    st.header("🔐 Step 2: Smart Contract Activated")
    st.write("Dana deposits the money into a smart contract. Layla signs the digital agreement.")

    st.progress(100)
    st.success("The deal is now locked. Both parties are committed.")

    st.markdown("---")
    st.header("🚚 Step 3: Did Layla Deliver the Item?")
    action = st.radio("Choose what Layla did:", ["✅ Delivered the bag", "❌ Flaked and sold it to someone else"])

    if action == "✅ Delivered the bag":
        st.balloons()
        st.success("Funds released to Layla. Dana received the item. The contract executed successfully.")
    else:
        st.error("Dana didn’t receive the item. Contract auto-refunds the money. Layla gets nothing.")
        st.info("✅ Trust enforced without trust. The contract handled everything.")

# --- Footer ---
st.markdown("---")
st.caption("Built with ❤️ using Streamlit · Smart Contract Simulation by dana")
