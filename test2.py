import pandas as pd
import plotly.express as px

# 엑셀 파일을 pandas 데이터프레임으로 읽기
df = pd.read_csv('cox-violent-parsed_filt_usable.csv')

# Plotly를 사용하여 바 그래프 생성

fig = px.pie(df, names='race', values='is_recid', title='is_recid_bar_chart')

# 이미지 파일로 저장 (예: PNG 형식)
#fig.write_html('output_pie_chart.')
fig.write_image('output_bar_chart.png')