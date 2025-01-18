install:
	pip install -r requirements.txt
	spacy download en_core_web_sm

	rm -rf ./uploads
