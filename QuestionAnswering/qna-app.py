#pip install azure-ai-language-questionanswering - at Question answering folder : open with Integrated terminal
from azure.core.credentials import AzureKeyCredential
from azure.ai.language.questionanswering import QuestionAnsweringClient
ai_key=1234 #from env (key and endpoint from your Azure subscription)
ai_endpoint=2345 #from env 
ai_project_name = 123 #from env
ai_deployment_name= 123 #from env
# Create client using endpoint and key
credential = AzureKeyCredential(ai_key)
ai_client = QuestionAnsweringClient(endpoint=ai_endpoint, credential=credential)
# Submit a question and display the answer
user_question = ''
while user_question.lower() != 'quit':
    user_question = input('\nQuestion:\n')
    response = ai_client.get_answers(question=user_question,
                                    project_name=ai_project_name,
                                    deployment_name=ai_deployment_name)
    
    #run app: python qna-app.py