import streamlit as st

st.set_page_config(page_title="Smart Contract Demo", layout="centered")

st.title("👜 The Bag That Was Promised")
st.write("A smart contract solution to prevent broken deals in online selling.")

# --- Characters Section ---
st.header("🎭 Meet the Characters")
st.image("1", caption="Dana wants to buy the bag")
st.image("2", caption="Layla found someone whor offers a higher price)
st.image("3", caption="dana is dissapointed")

# --- Confirmations ---
st.header("✅ Confirm the Deal")

if "item_confirmed" not in st.session_state:
    st.session_state.item_confirmed = False
if "price_confirmed" not in st.session_state:
    st.session_state.price_confirmed = False
if "deadline_confirmed" not in st.session_state:
    st.session_state.deadline_confirmed = False

if not st.session_state.item_confirmed:
    if st.button("👜 Confirm Item"):
        st.session_state.item_confirmed = True
else:
    st.success("Item Confirmed ✅")

if not st.session_state.price_confirmed:
    if st.button("💰 Confirm Price"):
        st.session_state.price_confirmed = True
else:
    st.success("Price Confirmed 💵")

if not st.session_state.deadline_confirmed:
    if st.button("🕒 Confirm Deadline"):
        st.session_state.deadline_confirmed = True
else:
    st.success("Deadline Confirmed ⏳")

# --- Smart Contract Trigger ---
if all([
    st.session_state.item_confirmed,
    st.session_state.price_confirmed,
    st.session_state.deadline_confirmed
]):
    st.markdown("---")
    st.header("🔄 Smart Contract Execution")
    st.write("All terms are confirmed. The smart contract is now active.")
    option = st.radio("What did Layla do?", ["✅ Delivered the item", "❌ Ghosted Dana"])
    if option == "✅ Delivered the item":
        st.success("✔️ Funds released to Layla!")
        st.balloons()
    else:
        st.error("✖️ Deadline missed. Dana gets a full refund.")

st.markdown("---")
st.caption("Built with ❤️ using Streamlit · Project by dana")
