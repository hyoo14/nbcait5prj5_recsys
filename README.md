# 키워드기반 영화 추천 및 리뷰 분석

프로젝트명: 키워드기반 영화 추천 및 리뷰 분석
프로젝트 한줄 요약: 키워드 기반 영화 추천 및 
팀명: 재준아어디가
팀원: 효건 김, Taehyeong Kim, 성기륜, Hyunwoo Yoo, Seongpyo Hong
도메인: NLP
테크 스택: CSS, ElasticSearch, FastAPI, GCP, Logstash, Numpy, Pandas, PostgreSQL, PyTorch, Python, Selenium, Transformers, TypeScript, WandB, kibana

# 프로젝트 소개

<aside>
🎬 비슷한 사용자가 원하는 영화가 아닌 사용자가 직접 생각한 키워드를 기반으로 영화를 추천해주는 서비스입니다.

</aside>

<aside>
🎭 영화 리뷰에 대한 감정 분석, 스포일러 분석을 제공하여 사용자의 영화 선택 편의성을 증대시킵니다.

</aside>

# 모델과 데이터셋

![](C:\Users\namuh\AppData\Roaming\marktext\images\2023-09-03-15-51-27-image.png)

<aside>
⚫ 단어 빈도수 기반의 BERTopic 모델과 TF-IDF 모델, KoBERT, RoBERTa 모델을 사용하였습니다.

</aside>

![](C:\Users\namuh\AppData\Roaming\marktext\images\2023-09-03-15-51-48-image.png)

<aside>
⚫ 왓챠피디아 리뷰 데이터, Naver sentiment movie corpus v1.0 데이터를 사용하였습니다.

</aside>

# 프로젝트 아키텍처

![](C:\Users\namuh\AppData\Roaming\marktext\images\2023-09-03-15-52-20-image.png)

<aside>
🛠 PostgreSQL과 Elastic ELK stack을 통해 모델 학습된 결과를 신뢰성있게 유지, 관리, 모니터링해주며 서비스의 성능도 올려줍니다.

# 사용 예시

![](C:\Users\namuh\AppData\Roaming\marktext\images\2023-09-03-15-52-57-image.png)



🛠 사용자가 키워드를 입력하면 해당하는 키워드에 해당되는 영화를 찾아서 추천해주며 관련 키워드들도 보여줍니다.
