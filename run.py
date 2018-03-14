from app import app
import os 

if __name__ =='__main__':
    app.run(host=os.getenv('IP', 'localhost'),
        port=int(os.getenv('PORT', 4444)))
