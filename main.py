# importing the needed libraries
from fastapi import FastAPI
import uvicorn
 
# creating the app
app = FastAPI()


# Writing a function for the landing page with a fastapi decorator            
@app.get('/')
def get_root():
	return {'message': 'Welcome to the test'}

# Writing a function for the prediction with a fastapi decorator that fetches the message  
@app.get('/return_test}')
async def detect_spam_path(message: str):
	return {'Hello':'World'}

# run the app
if __name__ == '__main__':
    uvicorn.run(app)