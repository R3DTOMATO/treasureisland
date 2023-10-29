import requests
import streamlit as st
import pandas as pd
import urllib 
from urllib.request import urlopen
from urllib.error import URLError


def app():
    @st.cache_data
    def Bookname():
        AWS_BUCKET_URL="https://bookinforbucket.s3.ap-northeast-2.amazonaws.com"
        response = urllib.request.urlopen(AWS_BUCKET_URL)
        df = pd.read_csv(AWS_BUCKET_URL+"book.csv")
        return df.set_index("책제목")
    
    try:
        urllib.request.urlopen("https://bookinforbucket.s3.ap-northeast-2.amazonaws.com")
        df = Bookname()
        bookSelect = st.multiselect(
            label="책이름을 입력하세요",options=list(df.index),default=["나루토"]
        )
        if not bookSelect:
            st.error("책 이름을 선택해주세요")
        else:
            data = df.loc[bookSelect]
            st.write(bookSelect, data.sort_index())

            data = data.T.reset_index()
        
    except URLError as e:
              st.error(
            """
            **This demo requires internet access.**
            Connection error: %s
        """
            % e.reason
        )
              
st.set_page_config(page_title="책검색", page_icon="📊")
st.markdown("# 책검색")
st.sidebar.header("책검색")
st.write(
    """이곳에 책이름 입력해 검색해주세요"""
)

app()
