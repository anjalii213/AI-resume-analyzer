from langchain_core.prompts import PromptTemplate
from models.llm import llm

def ats_analysis(resume,jd):
    prompt = PromptTemplate(
        input_variables = ["resume","jd"],
        template = """
        YOU ARE AN ATS SYSTEM.
        Analyse the resume by the job description.

        Resume:{resume}
        Job Description :{jd}

        Provide:
        1. ATS match percentage
        2. Missing keywords in resume
        3. Further improvements
        4. Future skills"""
    )
    chain = prompt | llm
    response = chain.invoke({
        "resume": resume, "jd": jd
    })

    return response.content
        
    