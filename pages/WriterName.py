

import streamlit as st
import pandas as pd
from urllib.request import urlopen
from urllib.error import URLError
import urllib
import socket 




def app():
    try:
        print(socket.getaddrinfo('google.com', 443))
    except socket.gaierror as e:
        print('An error occurred: ', e)
    
    
    @st.cache_data
    def Writername():
        AWS_BUCKET_URL="https://bookinforbucket.s3.ap-northeast-2.amazonaws.com"
        response = urlopen(AWS_BUCKET_URL)
        df = pd.read_csv(AWS_BUCKET_URL+"book.csv")
        return df.set_index("작가")
    
    try:
        urlopen("https://bookinforbucket.s3.ap-northeast-2.amazonaws.com")
        df = Writername()
        bookSelect = st.multiselect(
            "작가이름을 입력하세요",list(df.index), ["민"]
        )
        if not bookSelect:
            st.error("작가 이름을 선택해주세요")
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
                
st.set_page_config(page_title="작가 검색", page_icon="📊")
st.markdown("# 작가검색")
st.sidebar.header("작가검색")
st.write(
    """이곳에 작가이름 입력해 검색해주세요"""
)

app()        