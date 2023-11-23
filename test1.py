import pandas as pd
import matplotlib.pyplot as plt

# 데이터 파일 경로
file_path = 'cox-violent-parsed_filt_usable.csv'

# CSV 파일 읽기
df = pd.read_csv(file_path)

# 재범을 한 사람들만 필터링
recidivism_df = df[df['is_violent_recid'] == 1]

# 인종 별로 그룹화하여 재범을 한 사람들의 비율 계산
race_recidivism = recidivism_df['race'].value_counts(normalize=True)

# 원형 차트 생성
colors = ['lightcoral', 'lightskyblue', 'lightgreen', 'orange', 'lightpink']
explode = (0.1,) * len(race_recidivism)  # 각 원의 돌출 정도를 일치시킴

plt.figure(figsize=(8, 8))
plt.pie(race_recidivism, labels=race_recidivism.index, autopct='%1.1f%%', startangle=140, colors=colors, explode=explode)
plt.title('Recidivism by Race')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
plt.savefig('recidivism_by_race.png')  # 이미지 파일로 저장
plt.show()
