from website import create_app

napp=create_app()

if __name__=='__main__':
    napp.run(debug=True)