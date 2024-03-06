# Streamlit hello world app
import streamlit as st
import pandas as pd



def main():
    st.title('Übung der Woche 2')
    st.subheader('Textelement in Form eines subheaders')
    st.metric(label="Temperatur", value="13 °C", delta="7 °C")
    st.caption('Dataelement in form von Metrics')

    data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma'],
    'Alter': [25, 30, 35, 40, 45],
    'Geschlecht': ['weiblich', 'männlich', 'männlich', 'männlich', 'weiblich'],
    'Beruf': ['Ingenieur', 'Lehrer', 'Arzt', 'Anwalt', 'Designer']
}
    st.dataframe(data)
    st.scatter_chart(data=data, x="Alter", y="Geschlecht")
    st.caption('Data Chart in Form eines Scatter Charts')

    clicked = st.button('Input Widget in Form eines Buttons')

    st.sidebar.write('Das ist die Sidebar')
   
    c= st.container()
    c.write("Dies ist in einem Container")

   

    st.code('streamlit run hello_world.py')

if __name__ == '__main__':
    main()
