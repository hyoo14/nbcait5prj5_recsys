# -*- coding: utf-8 -*-

import requests
import json
import ast
import torch
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from fastapi import FastAPI

app = FastAPI()
model = SentenceTransformer('xlm-r-large-en-ko-nli-ststb')




def new_format_func(response_dict, keyword):
    result_dict = {}

    for hit in response_dict["hits"]["hits"]:
        title = hit["_source"]["title"]
        movie_code = hit["_source"]["movie_code"]
        img_url = hit["_source"]["img_url"]

        keywords = ast.literal_eval(hit["_source"]["keywords"])
        keyword_str = " ".join([k[0] for k in keywords])

        cmp_pair = [keyword_str, keyword]
        embeddings = model.encode(cmp_pair)
        similarity = cosine_similarity(
                embeddings[0].reshape(1,-1),
                embeddings[1].reshape(1,-1)

                )
        sub_dict = {}
        #sub_dict[keyword_str] = similarity.tolist()
        #sub_dict[title]=keyword_str
        sub_dict["title"]=title
        sub_dict["movie_code"]=movie_code
        sub_dict["img_url"]=img_url
        sub_dict["keywords"]=keyword_str
        
#        result_dict[title] = sub_dict
        result_dict[float(similarity[0][0])]=sub_dict

    sorted_dict = {k: result_dict[k] for k in sorted(result_dict, reverse=True)}

    return sorted_dict


#    return result_dict

def format_func(response_dict, keyword):
    result_dict = {}

    for hit in response_dict["hits"]["hits"]:
        title = hit["_source"]["title"]
#        movie_code = hit["_source"]["movie_code"]
#        img_url = hit["_source"]["img_url"]

        keywords = ast.literal_eval(hit["_source"]["keywords"])
        keyword_str = " ".join([k[0] for k in keywords])

        cmp_pair = [keyword_str, keyword]
        embeddings = model.encode(cmp_pair)
        similarity = cosine_similarity(
                embeddings[0].reshape(1,-1),
                embeddings[1].reshape(1,-1)

                )
        sub_dict = {}
        #sub_dict[keyword_str] = similarity.tolist()
        sub_dict[title]=keyword_str
        #sub_dict["title"]=title
        #sub_dict["movie_code"]=movie_code
        #sub_dict["img_url"]=img_url
        #sub_dict["keywords"]=keyword_str
        
#        result_dict[title] = sub_dict
        result_dict[float(similarity[0][0])]=sub_dict

    sorted_dict = {k: result_dict[k] for k in sorted(result_dict, reverse=True)}

    return sorted_dict


#    return result_dict


    #return dict(sorted(result_dict.items(), key=lambda item: item[1]["similarity"], reverse=True))


@app.get("/test")
def test_keyword(keyword: str):
  url = "http://34.64.212.49:9200/keywords/_search"
  query = {
    "query":{
      "match": {
        "comment": keyword
      }
    },
    "_source": ["title", "keywords", "movie_code", "img_url"]
  }
  response = requests.get(url, headers = {'Content-Type': "application/json"}, json=query)
  if response.status_code == 200:
    return format_func( response.json(), keyword )
  else:
    return {"error": "Failed to fetch data from the external API"}

@app.get("/rec")
def rec_keyword(keyword: str):
  url = "http://34.64.212.49:9200/infos/_search"
  query = {
    "query":{
      "match": {
        "comment": keyword
      }
    },
    "_source": ["title", "keywords", "movie_code", "img_url"]
  }
  response = requests.get(url, headers = {'Content-Type': "application/json"}, json=query)
  if response.status_code == 200:
    return new_format_func( response.json(), keyword )
  else:
    return {"error": "Failed to fetch data from the external API"}

#  if keyword == "boostcamp":
#    return {"message": "api working"}
#  else:
#  if keyword == "boostcamp":
#    return {"message": "api working"}
#  else:
#    return {"message": "invalid keyword"}

