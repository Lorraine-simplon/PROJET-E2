from website import create_app # lien avec la page __init__.py

app = create_app()

if __name__ == '__main__':
    app.run(debug=True) # permet de mettre à jour sans avoir à run 

