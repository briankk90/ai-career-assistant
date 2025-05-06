import pinecone
import openai
from django.conf import settings

class JobMatcher:
    def __init__(self):
        pinecone.init(api_key=settings.PINECONE_API_KEY, environment="us-west1-gcp")
        self.index = pinecone.Index("jobs")
        openai.api_key = settings.OPENAI_API_KEY

    def generate_embedding(self, text):
        response = openai.Embedding.create(input=text, model="text-embedding-ada-002")
        return response["data"][0]["embedding"]

    def match_jobs(self, user_profile):
        user_text = f"{user_profile.skills} {user_profile.experience} {user_profile.preferences}"
        user_embedding = self.generate_embedding(user_text)
        query_result = self.index.query(vector=user_embedding, top_k=5, include_metadata=True)
        return query_result["matches"]
