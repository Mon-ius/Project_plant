from app import app
import os 

app.run(host=os.getenv('IP', 'localhost'),
     port=int(os.getenv('PORT', 4444)),debug=True)
