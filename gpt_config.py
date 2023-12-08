## for training we are using FewShot prompt template as it suits our case best
from langchain import PromptTemplate, FewShotPromptTemplate
### using open ai and langchian instance to efficiently train and interact with the llm
from langchain import LLMChain
from langchain.chains import LLMChain

### import fewshot templates
from section1_prompt import few_shot_prompt_1
from section2_prompt import few_shot_prompt_2
from section5_prompt import few_shot_prompt_3
from langchain.llms import OpenAI


llm = OpenAI(
    temperature=0.2,
    openai_api_key="your api key",
    model_name="gpt-3.5-turbo-16k",
)



chain1 = LLMChain(llm=llm, prompt=few_shot_prompt_1)
chain2 = LLMChain(llm=llm, prompt=few_shot_prompt_2)
chain3 = LLMChain(llm=llm, prompt=few_shot_prompt_3)
# Run the chain only specifying the input variable.
