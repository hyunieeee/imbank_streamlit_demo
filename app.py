# _*_ coding: utf-8 _*_
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt

@st.cache_data
def load_data():
    df = sns.load_dataset('tips')
    return df 

def main(): 
    st.title('여기에서부터 시작')
    tips = load_data()

    m_tips = tips.loc[tips['sex']== 'Male',:]
    f_tips = tips.loc[tips['sex']== 'Female',:]

    #시각화 차트
    fig, ax = plt.subplots(ncols=2, figsize=(10,6), sharex=True, sharey=True)
    ax[0].scatter(x=m_tips['total_bill'],y=m_tips['tip'])
    ax[0].set_title('Male')
    ax[1].scatter(x=f_tips['total_bill'], y=f_tips['tip'])
    ax[1].set_title('Female')

    st.pyplot(fig)

    st.sidebar()

if __name__=='__main__':
    main()