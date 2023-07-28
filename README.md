# [NLP-10] 키워드기반 영화 추천 및 리뷰 분석

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

![Untitled 1](https://github.com/boostcampaitech5/level3_nlp_finalproject-nlp-10/assets/126731473/36eb5419-e1dd-4a23-949f-f8704d50dc80)

<aside>
⚫ 단어 빈도수 기반의 BERTopic 모델과 TF-IDF 모델, KoBERT, RoBERTa 모델을 사용하였습니다.

</aside>

![Untitled](%5BNLP-10%5D%20%E1%84%8F%E1%85%B5%E1%84%8B%E1%85%AF%E1%84%83%E1%85%B3%E1%84%80%E1%85%B5%E1%84%87%E1%85%A1%E1%86%AB%20%E1%84%8B%E1%85%A7%E1%86%BC%E1%84%92%E1%85%AA%20%E1%84%8E%E1%85%AE%E1%84%8E%E1%85%A5%E1%86%AB%20%E1%84%86%E1%85%B5%E1%86%BE%20%E1%84%85%E1%85%B5%E1%84%87%E1%85%B2%20%E1%84%87%E1%85%AE%E1%86%AB%E1%84%89%E1%85%A5%E1%86%A8%20c10beb9ff7134ab78e29b7e39c7b0d82/Untitled%201.png)

<aside>
⚫ 왓챠피디아 리뷰 데이터, Naver sentiment movie corpus v1.0 데이터를 사용하였습니다.

</aside>

# 프로젝트 아키텍처

  

![Untitled](%5BNLP-10%5D%20%E1%84%8F%E1%85%B5%E1%84%8B%E1%85%AF%E1%84%83%E1%85%B3%E1%84%80%E1%85%B5%E1%84%87%E1%85%A1%E1%86%AB%20%E1%84%8B%E1%85%A7%E1%86%BC%E1%84%92%E1%85%AA%20%E1%84%8E%E1%85%AE%E1%84%8E%E1%85%A5%E1%86%AB%20%E1%84%86%E1%85%B5%E1%86%BE%20%E1%84%85%E1%85%B5%E1%84%87%E1%85%B2%20%E1%84%87%E1%85%AE%E1%86%AB%E1%84%89%E1%85%A5%E1%86%A8%20c10beb9ff7134ab78e29b7e39c7b0d82/Untitled%202.png)

<aside>
🛠 PostgreSQL과 Elastic ELK stack을 통해 모델 학습된 결과를 신뢰성있게 유지, 관리, 모니터링해주며 서비스의 성능도 올려줍니다.

</aside>
