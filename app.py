import streamlit as st

st.set_page_config(page_title="Smart Contract Demo", layout="centered")

st.title("👜 The Bag That Was Promised")
st.markdown("""
A peer-to-peer deal goes wrong — until code steps in. 
This is an interactive simulation of a smart contract solving a trust problem in everyday life.
""")

# --- Step 1: Confirm the Deal ---
st.header("📍 Step 1: Agreement Initiated")

st.markdown("**Buyer (Dana) and seller (Layla) agree on:**")

if "item_confirmed" not in st.session_state:
    st.session_state.item_confirmed = False
if "price_confirmed" not in st.session_state:
    st.session_state.price_confirmed = False
if "deadline_confirmed" not in st.session_state:
    st.session_state.deadline_confirmed = False

col1, col2, col3 = st.columns(3)
with col1:
    if not st.session_state.item_confirmed:
        if st.button("👜 Confirm Item"):
            st.session_state.item_confirmed = True
    else:
        st.success("Item Confirmed ✅")

with col2:
    if not st.session_state.price_confirmed:
        if st.button("💰 Confirm Price"):
            st.session_state.price_confirmed = True
    else:
        st.success("Price Confirmed 💵")

with col3:
    if not st.session_state.deadline_confirmed:
        if st.button("⏳ Confirm Deadline"):
            st.session_state.deadline_confirmed = True
    else:
        st.success("Deadline Confirmed ⏰")

# --- Step 2: Funds Deposited ---
if all([
    st.session_state.item_confirmed,
    st.session_state.price_confirmed,
    st.session_state.deadline_confirmed
]):
    st.markdown("---")
    st.header("💳 Step 2: Funds Deposited")
    
    if "dana_deposited" not in st.session_state:
        st.session_state.dana_deposited = False
    if "layla_signed" not in st.session_state:
        st.session_state.layla_signed = False

    if not st.session_state.dana_deposited:
        if st.button("💸 Dana Deposits 30 JD"):
            st.session_state.dana_deposited = True
            st.success("✔️ Funds locked in a neutral smart contract. Not with the seller.")
            st.info("🔐 Escrow initiated. Dana's money is safe.")
    elif not st.session_state.layla_signed:
        if st.button("🖊️ Layla Signs the Digital Contract"):
            st.session_state.layla_signed = True
            st.success("✔️ Layla is now legally committed to the deal.")
            st.info("📜 All conditions locked. The contract is ready to execute.")

# --- Step 3: Delivery or Refund ---
if st.session_state.get("dana_deposited") and st.session_state.get("layla_signed"):
    st.markdown("---")
    st.header("📦 Step 3: Delivery or Refund")
    st.write("What happened next?")
    choice = st.radio("Layla's action:", ["✅ Delivered on time", "❌ Ghosted Dana"])

    if choice == "✅ Delivered on time":
        st.success("🎉 Item received. Smart contract releases funds to Layla.")
        st.balloons()
    else:
        st.error("💥 Deadline missed. Smart contract refunds Dana automatically.")
        st.warning("🔁 Fairness enforced. Trustless transaction complete.")

# --- Footer ---
st.markdown("---")
st.caption("Built with ❤️ using Streamlit · Smart Contract Simulation by [Your Name]")

