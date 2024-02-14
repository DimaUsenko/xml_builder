# Python 3.11
build_env: # Ubuntu
	python -m venv venv
	source venv/bin/activate
	pip install -r requirements.txt
run_app:
	streamlit run app.py