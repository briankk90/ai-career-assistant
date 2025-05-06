import openai
from django.conf import settings

class ResumeGenerator:
    def __init__(self):
        openai.api_key = settings.OPENAI_API_KEY

    def generate_resume(self, user_profile, job):
        prompt = f"""
        Create a tailored resume for a user with the following details:
        Skills: {user_profile.skills}
        Experience: {user_profile.experience}
        Target Job: {job.title} at {job.company}
        Description: {job.description}
        Format the resume as plain text.
        """
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
