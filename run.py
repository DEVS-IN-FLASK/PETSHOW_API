import os
from petshow_api import create_app

app = create_app()
port = int(os.environ.get("PORT", 5000))
app.run(host='0.0.0.0', port=port)

 # app.run(host='localhost', port=5000, debug=True)
