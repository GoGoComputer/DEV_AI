
 # dev in WSL Ubuntu
 
 # activate myvenv
    # terminal: cd DEV_AI_PYTHON
    # terminal: source myvenv/bin/activate
    
    
    
# first time setup in WSL Ubuntu terminal
# teminal: sudo apt update
# teminal: sudo apt install python3
# teminal: python3 --version
# teminal: sudo apt install python3-pip
# teminal: pip3 --version

# teminal: pip3 install langchain
# teminal: pip3 install openai
# teminal: pip3 install faiss-cpu
# teminal: pip3 install tiktoken
# teminal: pip3 install python-dotenv



# If Langchain is not working, please check the following. 
# Path issue: In some cases, this may be caused by a problem with the Python path settings. 
# This can be resolved by checking and adjusting the Python path settings on your system.

# Here's how to resolve Python path issues in Visual Studio Code (VS Code):

# Select Python Interpreter: Open your Python project in VS Code, 
# go to the top menu and select 'View' > 'Command Palette...' or open the command palette using (Ctrl+Shift+P or Cmd+Shift+P). 
# Type 'Python: Select Interpreter' to view a list of available Python interpreters. From this list, select the Python interpreter you want to use.



from dotenv import load_dotenv
import os

load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')

from collections import deque
from typing import Dict, List, Optional, Any

from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import BaseLLM
from langchain.vectorstores.base import VectorStore
from pydantic import BaseModel, Field
from langchain.chains.base import Chain

from langchain.vectorstores import FAISS
from langchain.docstore import InMemoryDocstore

# Define your embedding model
embeddings_model = OpenAIEmbeddings()
# Initialize the vectorstore as empty
import faiss

embedding_size = 1536
index = faiss.IndexFlatL2(embedding_size)
vectorstore = FAISS(embeddings_model.embed_query, index, InMemoryDocstore({}), {})



# first LLM Chain


class TaskCreationChain(LLMChain):
    """Chain to generates tasks."""

    @classmethod
    def from_llm(cls, llm: BaseLLM, verbose: bool = True) -> LLMChain:
        """Get the response parser."""
        task_creation_template = (
            "You are a task creation AI that uses the result of an execution agent"
            " to create new tasks with the following objective: {objective},"
            " The last completed task has the result: {result}."
            " This result was based on this task description: {task_description}."
            " These are incomplete tasks: {incomplete_tasks}."
            " Based on the result, create new tasks to be completed"
            " by the AI system that do not overlap with incomplete tasks."
            " Return the tasks as an array."
        )
        prompt = PromptTemplate(
            template=task_creation_template,
            input_variables=[
                "result",
                "task_description",
                "incomplete_tasks",
                "objective",
            ],
        )
        return cls(prompt=prompt, llm=llm, verbose=verbose)
    
    
# Second LLM Chain


class TaskPrioritizationChain(LLMChain):
    """Chain to prioritize tasks."""

    @classmethod
    def from_llm(cls, llm: BaseLLM, verbose: bool = True) -> LLMChain:
        """Get the response parser."""
        task_prioritization_template = (
            "You are a task prioritization AI tasked with cleaning the formatting of and reprioritizing"
            " the following tasks: {task_names}."
            " Consider the ultimate objective of your team: {objective}."
            " Do not remove any tasks. Return the result as a numbered list, like:"
            " #. First task"
            " #. Second task"
            " Start the task list with number {next_task_id}."
        )
        prompt = PromptTemplate(
            template=task_prioritization_template,
            input_variables=["task_names", "next_task_id", "objective"],
        )
        return cls(prompt=prompt, llm=llm, verbose=verbose)


# Third LLM Chain

class ExecutionChain(LLMChain):
    """Chain to execute tasks."""

    @classmethod
    def from_llm(cls, llm: BaseLLM, verbose: bool = True) -> LLMChain:
        """Get the response parser."""
        execution_template = (
            "You are an AI who performs one task based on the following objective: {objective}."
            " Take into account these previously completed tasks: {context}."
            " Your task: {task}."
            " Response:"
        )
        prompt = PromptTemplate(
            template=execution_template,
            input_variables=["objective", "context", "task"],
        )
        return cls(prompt=prompt, llm=llm, verbose=verbose)
    
    
    
# BabyAGI Controller

# First Task

def get_next_task(
    task_creation_chain: LLMChain,
    result: Dict,
    task_description: str,
    task_list: List[str],
    objective: str,
) -> List[Dict]:
    """Get the next task."""
    incomplete_tasks = ", ".join(task_list)
    response = task_creation_chain.run(
        result=result,
        task_description=task_description,
        incomplete_tasks=incomplete_tasks,
        objective=objective,
    )
    new_tasks = response.split("\\n")
    return [{"task_name": task_name} for task_name in new_tasks if task_name.strip()]


# Second Task

def prioritize_tasks(
    task_prioritization_chain: LLMChain,
    this_task_id: int,
    task_list: List[Dict],
    objective: str,
) -> List[Dict]:
    """Prioritize tasks."""
    task_names = [t["task_name"] for t in task_list]
    next_task_id = int(this_task_id) + 1
    response = task_prioritization_chain.run(
        task_names=task_names, next_task_id=next_task_id, objective=objective
    )
    new_tasks = response.split("\\n")
    prioritized_task_list = []
    for task_string in new_tasks:
        if not task_string.strip():
            continue
        task_parts = task_string.strip().split(".", 1)
        if len(task_parts) == 2:
            task_id = task_parts[0].strip()
            task_name = task_parts[1].strip()
            prioritized_task_list.append({"task_id": task_id, "task_name": task_name})
    return prioritized_task_list

# Last

def _get_top_tasks(vectorstore, query: str, k: int) -> List[str]:
    """Get the top k tasks based on the query."""
    results = vectorstore.similarity_search_with_score(query, k=k)
    if not results:
        return []
    sorted_results, _ = zip(*sorted(results, key=lambda x: x[1], reverse=True))
    return [str(item.metadata["task"]) for item in sorted_results]

def execute_task(
    vectorstore, execution_chain: LLMChain, objective: str, task: str, k: int = 5
) -> str:
    """Execute a task."""
    context = _get_top_tasks(vectorstore, query=objective, k=k)
    return execution_chain.run(objective=objective, context=context, task=task)


# class Baby AGI code


class BabyAGI(Chain, BaseModel):
    """Controller model for the BabyAGI agent."""

    task_list: deque = Field(default_factory=deque)
    task_creation_chain: TaskCreationChain = Field(...)
    task_prioritization_chain: TaskPrioritizationChain = Field(...)
    execution_chain: ExecutionChain = Field(...)
    task_id_counter: int = Field(1)
    vectorstore: VectorStore = Field(init=False)
    max_iterations: Optional[int] = None

    class Config:
        """Configuration for this pydantic object."""

        arbitrary_types_allowed = True

    def add_task(self, task: Dict):
        self.task_list.append(task)

    def print_task_list(self):
        print("\033[95m\033[1m" + "\n*****TASK LIST*****\n" + "\033[0m\033[0m")
        for t in self.task_list:
            print(str(t["task_id"]) + ": " + t["task_name"])

    def print_next_task(self, task: Dict):
        print("\033[92m\033[1m" + "\n*****NEXT TASK*****\n" + "\033[0m\033[0m")
        print(str(task["task_id"]) + ": " + task["task_name"])

    def print_task_result(self, result: str):
        print("\033[93m\033[1m" + "\n*****TASK RESULT*****\n" + "\033[0m\033[0m")
        print(result)

    @property
    def input_keys(self) -> List[str]:
        return ["objective"]

    @property
    def output_keys(self) -> List[str]:
        return []

    def _call(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        """Run the agent."""
        objective = inputs["objective"]
        first_task = inputs.get("first_task", "Make a todo list")
        self.add_task({"task_id": 1, "task_name": first_task})
        num_iters = 0
        while True:
            if self.task_list:
                self.print_task_list()

                # Step 1: Pull the first task
                task = self.task_list.popleft()
                self.print_next_task(task)

                # Step 2: Execute the task
                result = execute_task(
                    self.vectorstore, self.execution_chain, objective, task["task_name"]
                )
                this_task_id = int(task["task_id"])
                self.print_task_result(result)

                # Step 3: Store the result in Pinecone
                result_id = f"result_{task['task_id']}_{num_iters}"
                self.vectorstore.add_texts(
                    texts=[result],
                    metadatas=[{"task": task["task_name"]}],
                    ids=[result_id],
                )

                # Step 4: Create new tasks and reprioritize task list
                new_tasks = get_next_task(
                    self.task_creation_chain,
                    result,
                    task["task_name"],
                    [t["task_name"] for t in self.task_list],
                    objective,
                )
                for new_task in new_tasks:
                    self.task_id_counter += 1
                    new_task.update({"task_id": self.task_id_counter})
                    self.add_task(new_task)
                self.task_list = deque(
                    prioritize_tasks(
                        self.task_prioritization_chain,
                        this_task_id,
                        list(self.task_list),
                        objective,
                    )
                )
            num_iters += 1
            if self.max_iterations is not None and num_iters == self.max_iterations:
                print(
                    "\033[91m\033[1m" + "\n*****TASK ENDING*****\n" + "\033[0m\033[0m"
                )
                break
        return {}

    @classmethod
    def from_llm(
        cls, llm: BaseLLM, vectorstore: VectorStore, verbose: bool = False, **kwargs
    ) -> "BabyAGI":
        """Initialize the BabyAGI Controller."""
        task_creation_chain = TaskCreationChain.from_llm(llm, verbose=verbose)
        task_prioritization_chain = TaskPrioritizationChain.from_llm(
            llm, verbose=verbose
        )
        execution_chain = ExecutionChain.from_llm(llm, verbose=verbose)
        return cls(
            task_creation_chain=task_creation_chain,
            task_prioritization_chain=task_prioritization_chain,
            execution_chain=execution_chain,
            vectorstore=vectorstore,
            **kwargs,
        )
        
        
        
# Do Test

OBJECTIVE = "Write a weather report for Seoul today"

llm = OpenAI(temperature=0)

# Logging of LLMChains
verbose = False
# If None, will keep on going forever
max_iterations: Optional[int] = 3
baby_agi = BabyAGI.from_llm(
    llm=llm, vectorstore=vectorstore, verbose=verbose, max_iterations=max_iterations
)

baby_agi({"objective": OBJECTIVE})



# terminal: pip install langchain-community
# terminal: pip install langchain-openai
# terminal: pip install pydantic==1.10.12 


# 랭체인은 계속 바뀌는 라이브러리라 실습 할 것 이면 알려주는 사람하고
# 버전을 고정해서 설치하고 실습을 진행해야 한다.


""" 렝체인(LangChain)은 대규모 언어 모델(LLM)을 사용하여 애플리케이션을 생성을 단순화하도록 설계된 프레임워크입니다. LLM 통합 프레임워크로서 랭체인의 사용 사례는 문서 분석 및 요약, 챗봇, 코드 분석을 포함하여 일반적인 LLM의 사용 사례와 크게 겹칩니다.

랭체인은 다음과 같은 특징을 가지고 있습니다.

단순한 API: 랭체인은 간단한 API를 제공하여 개발자가 LLM을 쉽게 사용할 수 있도록 합니다.
다양한 LLM 지원: 랭체인은 Google AI의 LaMDA, OpenAI의 GPT-3, Facebook의 RoBERTa 등 다양한 LLM을 지원합니다.
확장성: 랭체인은 다양한 플랫폼과 언어를 지원하여 확장성이 뛰어납니다.
랭체인은 다음과 같은 분야에서 활용될 수 있습니다.

문서 분석 및 요약: 랭체인을 사용하여 문서를 분석하고 요약할 수 있습니다.
챗봇: 랭체인을 사용하여 챗봇을 개발할 수 있습니다.
코드 분석: 랭체인을 사용하여 코드를 분석할 수 있습니다.
랭체인은 2022년 10월에 오픈 소스 프로젝트로 출시되었습니다. 현재 GitHub에서 다운로드할 수 있습니다.

랭체인은 대규모 언어 모델을 사용하는 애플리케이션을 개발하는 데 유용한 프레임워크입니다. 단순한 API와 다양한 LLM 지원을 통해 개발자는 LLM을 쉽게 사용할 수 있습니다.

다음은 랭체인을 사용하여 개발한 애플리케이션의 몇 가지 예입니다.

문서 분석 및 요약 애플리케이션: 이 애플리케이션은 문서를 분석하고 요약하여 사용자가 빠르게 정보를 파악할 수 있도록 도와줍니다.
챗봇: 이 챗봇은 LLM을 사용하여 사용자의 질문에 대한 정보를 제공하고 대화를 나눌 수 있습니다.
코드 분석 애플리케이션: 이 애플리케이션은 LLM을 사용하여 코드를 분석하고 오류를 찾을 수 있도록 도와줍니다.
랭체인은 대규모 언어 모델의 사용을 확대하고 다양한 분야에서 활용될 수 있는 가능성을 보여주는 프레임워크입니다. """




""" 파이썬 랭체인은 파이썬으로 작성된 랭체인의 구현체입니다. 파이썬 랭체인은 다음과 같은 특징을 가지고 있습니다.

간단한 API: 파이썬 랭체인은 랭체인의 기본 API를 그대로 구현하여 사용하기 쉽습니다.
다양한 LLM 지원: 파이썬 랭체인은 랭체인과 마찬가지로 다양한 LLM을 지원합니다.
확장성: 파이썬 랭체인은 랭체인과 마찬가지로 다양한 플랫폼과 언어를 지원하여 확장성이 뛰어납니다.
파이썬 랭체인을 사용하려면 먼저 다음과 같이 설치해야 합니다.

pip install langchain
설치가 완료되면 다음과 같이 LLM을 사용할 수 있습니다.

Python
from langchain import OpenAI

llm = OpenAI()

text = llm("오늘 날씨는 어때요?")

print(text)
코드를 사용할 때는 주의하시기 바랍니다. 자세히 알아보기
이 코드는 OpenAI의 GPT-3 모델을 사용하여 "오늘 날씨는 어때요?"라는 질문에 대한 답을 생성합니다.

파이썬 랭체인은 다음과 같은 분야에서 활용될 수 있습니다.

문서 분석 및 요약: 파이썬 랭체인을 사용하여 문서를 분석하고 요약할 수 있습니다.
챗봇: 파이썬 랭체인을 사용하여 챗봇을 개발할 수 있습니다.
코드 분석: 파이썬 랭체인을 사용하여 코드를 분석할 수 있습니다.
파이썬 랭체인은 파이썬으로 대규모 언어 모델을 사용하는 애플리케이션을 개발하는 데 유용한 프레임워크입니다. 단순한 API와 다양한 LLM 지원을 통해 개발자는 LLM을 쉽게 사용할 수 있습니다.

다음은 파이썬 랭체인을 사용하여 개발한 애플리케이션의 몇 가지 예입니다.

문서 분석 및 요약 애플리케이션: 이 애플리케이션은 파이썬 랭체인을 사용하여 문서를 분석하고 요약하여 사용자가 빠르게 정보를 파악할 수 있도록 도와줍니다.
챗봇: 이 챗봇은 파이썬 랭체인을 사용하여 사용자의 질문에 대한 정보를 제공하고 대화를 나눌 수 있습니다.
코드 분석 애플리케이션: 이 애플리케이션은 파이썬 랭체인을 사용하여 코드를 분석하고 오류를 찾을 수 있도록 도와줍니다.
파이썬 랭체인은 대규모 언어 모델의 사용을 확대하고 다양한 분야에서 활용될 수 있는 가능성을 보여주는 프레임워크입니다. """


