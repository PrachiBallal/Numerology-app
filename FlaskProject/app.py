import streamlit as st


def reduce_to_single_digit(number):
    # convert number to digits
    total = sum(int(d) for d in str(number))

    # keep reducing
    while total > 9:
        total = sum(int(d) for d in str(total))

    return total

chaldean_chart = {
    'A' : 1, 'I' : 1, 'J' : 1, 'Q': 1, 'Y':1,
    'B':2, 'K': 2, 'R':2,
    'C':3, 'G':3, 'L':3, 'S':3,
    'D':4, 'M':4, 'T':4,
    'E':5, 'H':5, 'N':5, 'X':5,
    'U':6, 'V':6, 'W':6,
    'O':7, 'Z':7,
    'F':8, 'P':8
}


st.title("Name Numerology")

#Input box
name = st.text_input("Enter your name")
bdate = st.text_input("Enter your birthdate")
bmonth = st.text_input("Enter your month")
byear = st.text_input("Enter your year")

bnum = reduce_to_single_digit((bdate+bmonth+byear))
name = name.upper()
result = 0
details = []

for char in name:
    if char in chaldean_chart:
        value = chaldean_chart[char]
        result += value

num = reduce_to_single_digit(result)

#Submit butt3200202269on
if st.button("Result"):
    st.markdown(
        f"<h2>Your Numerology Number is <span style='color:orange;'>{num}</span><h2>",
        unsafe_allow_html = True
    )
    st.markdown(
        f"<h2>Your Destiny Number is <span style='color:orange;'>{bnum}</span><h2>",
        unsafe_allow_html=True
    )

