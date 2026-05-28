from langchain_core.prompts import PromptTemplate
from models.llm import llm

def interview_question(resume,jd):
    prompt = PromptTemplate(
        input_variables = ["resume","jd"],
        template = """
        Based on this resume and job description , provide interview question.

        The format of question should be 
        -technical question
        -Hr question
        -Behavioral question

        Resume:{resume}
        Job Description : {jd}"""

    )
    chain = prompt|llm
    response = chain.invoke({
        "resume" : resume, "jd":jd
    })

    return response.content