# estoque003
# mk dir projeto
cd projeto
git clone https://github.com/deciosn/estoque003.git
sudo apt install python3-pip -y
pip install django
django-admin startproject  projeto_cad_usuarios
cd projeto_cad_usuarios
django-admin startapp app_cad_usuarios
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
