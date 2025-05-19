import streamlit as st

st.set_page_config(page_title="Smart Contract Demo", layout="centered")

st.title("👜 The Bag That Was Promised")
st.markdown("""
A peer-to-peer deal goes wrong — until code steps in. 
This is an interactive simulation of a smart contract solving a trust problem in everyday life.
""")

# --- Story Intro ---
st.header("🎭 Meet the Story")

with st.expander("📖 Click to reveal the short story"):
    st.markdown("""
    Dana saw a beautiful vintage bag listed online by Layla. They agreed on a price of **60 JD** and a pickup deadline by **Friday at 6 PM**. 
    
    Layla said: "I'll hold it for you."
    Dana replied: "Perfect! I'll come Friday."
    
    But when Friday came... someone else had offered a higher price.
    
    Layla sold it.

    Dana was left betrayed.

    Let’s simulate how a smart contract would’ve saved this deal.
    """)
    
st.markdown("#### This is what happened before the smart contract…")

col1, col2 = st.columns(2)
with col1:
    st.image("story_1.png.png", caption="Dana contacts Layla to buy the bag")
with col2:
    st.image("story_2.png.png", caption="Lana offers more money. Layla takes it.")

col3, col4 = st.columns(2)
with col3:
    st.image("story_3.png.png", caption="Dana is left disappointed and empty-handed.")
with col4:
    st.image("story_4.png.png", caption="She gets an idea... A smart contract.")

st.markdown("---")

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
    if "escrow_displayed" not in st.session_state:
        st.session_state.escrow_displayed = False
    if "layla_signed" not in st.session_state:
        st.session_state.layla_signed = False

    # Phase 1 – Dana deposits
    if not st.session_state.dana_deposited:
        if st.button("💸 Dana Deposits 30 JD"):
            st.session_state.dana_deposited = True

    if st.session_state.dana_deposited:
        st.success("✔️ Dana deposited 30 JD into the smart contract.")

    # Phase 2 – Escrow animation
    if st.session_state.dana_deposited and not st.session_state.escrow_displayed:
        if st.button("🔐 Show Escrow Wallet"):
            st.session_state.escrow_displayed = True

    if st.session_state.escrow_displayed:
        st.markdown("💸 ➡️ 🔒 **30 JD is now locked in escrow** (not with Layla).")
        st.info("Funds are safely held in the smart contract.")

    # Phase 3 – Layla signs
    if st.session_state.escrow_displayed and not st.session_state.layla_signed:
        if st.button("🖊️ Layla Signs the Digital Contract"):
            st.session_state.layla_signed = True

    if st.session_state.layla_signed:
        st.success("✔️ Layla is now legally committed to the deal.")
        st.info("📜 All conditions are now locked. Ready for execution.")


# --- Step 3: Delivery or Refund ---
if st.session_state.get("dana_deposited") and st.session_state.get("layla_signed"):
    st.markdown("---")
    st.header("📦 Step 3: Delivery or Refund")
    st.write("What happened next?")
    choice = st.radio("Layla's action:", ["✅ Delivered on time", "❌ Ghosted Dana"])

    if choice == "✅ Delivered on time":
        st.success("🎉 Item received. Smart contract releases funds to Layla.")
        
    else:
        st.error("💥 Deadline missed. Smart contract refunds Dana automatically.")
        st.warning("🔁 Fairness enforced. Trustless transaction complete.")

# --- Footer ---
st.markdown("---")
st.caption("Built with ❤️ using Streamlit · Smart Contract Simulation by dana")

