# Model choice

Our goal was to find (or create) a rather small, fast and effective model for error correction.
Our first choice was to use T5 models: encoder-decoder models which are often used for machine transaltion, but also for error correction.
So, the model is applicable for text generation.

The initial idea was to train a T5-small model, enhanced by distillation with a T5-large model to obtain a good and lightweight model.
Unfortunately, this task appeared to be more challenging than expected, to we decided to perform quantization of the T5-large model. 
This proved to be successful: model size was decreased from 2.8 GB to 0.8 GB, small enough to be used in some web-applications.

# Service

The idea of service was pretty simple: uses inputs some text with spelling errors, the model returns corrected text. 
To implement this service, we chose to use two rather simple HTML pages with Jinja templates and FastAPI for backend.

The realisation and running unstructions can be seen on root page.

# Quality estimation

The model performs quite fast (only a couple of seconds) on small texts, but longer on larger texts. Text generation contains a maximum limits of 150 tokens.

The quality of correction is quite good. Despite our synthetic metric (see ipynb notebook for details) only showed 20% error correction rate (ECR) for `jflegs` dataset, 
during manual tests the results were quite satisfying. The low ECR could be explained by the fact that corrections supplied to `jflegs` do not only contain spelling corrections,
but also restructure phrases a bit.
