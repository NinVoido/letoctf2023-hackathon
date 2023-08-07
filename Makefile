install-deps:
	pip install -r requirements.txt
run:
	uvicorn src.main:app --reload --port 8000 --host 0.0.0.0
