import asyncio

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from browser_use import Agent
from browser_use.browser import Browser

load_dotenv()

# Initialize the model
llm = ChatOpenAI(
	model='gpt-4o',
	temperature=0.0,
)
#task = 'Find the founders of browser-use and draft them a short personalized message'
task="""
	-Abra o site https://www.serasa.com.br/
	-selecione "Para empresas"
	-selecione Acessar
	-insira login: 37347899
	-Digite a senha: Condo@24
	-Click Acessar
	-Feche o popup (se existir)
	-Acessar: Serasa Relatório Básico PJ
	-Insira o CNPJ: 18.710.080/0001-34
	-Selecionar no dropdown: "Relatório Avançado"
	-Click: Gerar relatório
	-No popup Conheça a situação dos sócios, clique em "Sim quero incluir"
	-Salvar os dados da página
	-Encerrar
"""

browser_session = BrowserSession()

agent = Agent(
	task=task,
	llm=llm,
	browser_session=browser_session,
)

async def main():
	await agent.run()


if __name__ == '__main__':
	asyncio.run(main())
