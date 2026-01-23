import streamlit as st
from gptcode import Bank

bank = Bank()

st.title("🏦 Bank Management System")

menu = st.sidebar.selectbox(
    "Choose an Option",
    ["Create Account", "Deposit Money", "Withdraw Money", "Show Details", "Update Details", "Delete Account"]
)

if menu == "Create Account":
    st.subheader("Create Your Account")
    name = st.text_input("Full Name")
    age = st.number_input("Age", min_value=1)
    email = st.text_input("Email")
    pin = st.text_input("4-digit PIN", type="password")

    if st.button("Create"):
        if name and email and pin:
            result = bank.create_account(name, int(age), email, int(pin))
            st.success(result["msg"])
            if result["status"]:
                st.json(result["account"])
        else:
            st.warning("Please fill all details!")

elif menu == "Deposit Money":
    acc_no = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1)
    if st.button("Deposit"):
        st.success(bank.deposit_money(acc_no, int(pin), int(amount))["msg"])

elif menu == "Withdraw Money":
    acc_no = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1)
    if st.button("Withdraw"):
        st.success(bank.withdraw_money(acc_no, int(pin), int(amount))["msg"])

elif menu == "Show Details":
    acc_no = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    if st.button("Show"):
        result = bank.show_details(acc_no, int(pin))
        if result["status"]:
            st.json(result["data"])
        else:
            st.error(result["msg"])

elif menu == "Update Details":
    acc_no = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    name = st.text_input("New Name (optional)")
    email = st.text_input("New Email (optional)")
    new_pin = st.text_input("New PIN (optional)")
    if st.button("Update"):
        result = bank.update_details(acc_no, int(pin), name, email, new_pin)
        st.success(result["msg"])

elif menu == "Delete Account":
    acc_no = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    if st.button("Delete"):
        result = bank.delete_account(acc_no, int(pin))
        if result["status"]:
            st.success(result["msg"])
        else:
            st.error(result["msg"])
