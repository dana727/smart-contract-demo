import streamlit as st

st.set_page_config(page_title="Smart Contract Demo", layout="centered")

st.title("👜 The Bag That Was Promised")
st.markdown("""
A peer-to-peer deal goes wrong — until code steps in. 
This is an interactive simulation of a smart contract solving a trust problem in everyday life.
""")

# --- Story Intro ---
st.header("🎭 The Story")

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
    st.header("🎭 The Story")

# --- Story Intro with Images ---
st.header("🎭 The Story (Visual)")

col1, col2 = st.columns(2)
with col1:
    st.image("story_1.png.png", caption="Dana makes a deal with Layla")
with col2:
    st.image("story_2.png.png", caption="Lana offers more. Layla breaks her promise.")

col3, col4 = st.columns(2)
with col3:
    st.image("story_3.png.png", caption="Dana is left disappointed.")
with col4:
    st.image("story_4.png.png", caption="She gets an idea... a smart contract.")



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
    if "layla_collateral" not in st.session_state:
        st.session_state.layla_collateral = False
    if "layla_signed" not in st.session_state:
        st.session_state.layla_signed = False

    # Dana deposits
    if not st.session_state.dana_deposited:
        if st.button("💸 Dana Deposits 30 JD"):
            st.session_state.dana_deposited = True

    if st.session_state.dana_deposited:
        st.success("✔️ Dana deposited 30 JD into the smart contract.")

    # Show escrow
    if st.session_state.dana_deposited and not st.session_state.escrow_displayed:
        if st.button("🔐 Show Escrow Wallet"):
            st.session_state.escrow_displayed = True

    if st.session_state.escrow_displayed:
        st.markdown("💸 ➡️ 🔒 **30 JD is now locked in escrow** (not with Layla).")
        st.info("Funds are safely held in the smart contract.")

    # Layla collateral
    if st.session_state.escrow_displayed and not st.session_state.layla_collateral:
        if st.button("💼 Layla Adds 5 JD Collateral"):
            st.session_state.layla_collateral = True

    if st.session_state.layla_collateral:
        st.success("✔️ Layla's 5 JD collateral is also locked in the smart contract.")
        st.warning("This will be sent to Dana if Layla fails to deliver.")

    # Layla signs
    if st.session_state.layla_collateral and not st.session_state.layla_signed:
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
        st.success("🎉 Item received. Smart contract releases 30 JD to Layla and returns her 5 JD collateral.")
    else:
        st.error("💥 Deadline missed. Smart contract refunds Dana's 30 JD **and** transfers Layla's 5 JD collateral to Dana.")
        st.warning("🔁 Trustless fairness enforced by code.")

# --- Benefits Summary ---
st.markdown("---")
st.header("🔎 Why Did We Need the Smart Contract?")

st.markdown("""
- 🔒 **Funds Held in Escrow:** Buyer’s money isn’t released until terms are met.  
- 💼 **Seller Collateral:** Layla must risk 5 JD if she flakes.  
- ✍️ **Digital Commitment:** Seller locks the deal by signing the contract.  
- ⏱️ **Time-Based Logic:** If the deadline passes, the contract executes automatically.  
- ⚖️ **Trustless & Fair:** Both sides are protected by code — not just hope.

Smart contracts enforce trust, even when people fail to.
""")

# --- Footer ---
st.markdown("---")
st.caption("made with love , student: dana<3")


