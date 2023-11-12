# LSML2_FP
Final Project for LSML 2 course

## Model preparation

See [ipynb notebook](https://github.com/akondrashov96/LSML2_FP/blob/main/Model_Training.ipynb) for details.

## Documentation

See [docs](https://github.com/akondrashov96/LSML2_FP/tree/main/docs) folder

## Realization

The app is realised using FastAPI interface. 

Running instructions:

0) Do note that github does not allow to host large files, so the model can be downloaded here: https://drive.google.com/file/d/1Q5soR6VALxvPXXmQC-a_h95OrSGYyhuR/view?usp=drive_link
1) To load the server run `uvicorn main:app --host 127.0.0.1 --port 8000` from server folder in cmd or terminal
2) Open http://127.0.0.1:8000 in browser
3) In the text field, enter some text with errors, like on the screen below:

![img_1](https://raw.githubusercontent.com/akondrashov96/LSML2_FP/main/img/Screenshot_1.png)

4) Press "Correct errors!" button and enjoy!

![img_2](https://raw.githubusercontent.com/akondrashov96/LSML2_FP/main/img/Screenshot_2.png)
