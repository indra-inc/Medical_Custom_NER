# Custom NER using SpacyV3

- According to Wikipedia, Named Entity Recognition (NER) is a subtask of information extraction that seeks to locate and classify named entities mentioned in unstructured text into pre-defined categories such as person names, organizations, locations, medical codes, time expressions, quantities, monetary values, percentages, etc.
NER can be implemented with either statistical or rule-based methods, both of which require a large amount of labeled training data and are typically trained in a fully or semi-supervised manner.

## Dataset :  [Medical NER](https://www.kaggle.com/datasets/finalepoch/medical-ner "Medical NER")

### About Dataset
### Context

This dataset was created to train a Spacy model to perform Named Entity Recognition for three categories:

- Medical condition names (example: influenza, headache, malaria)
- Medicine names (example : aspirin, penicillin, ribavirin, methotrexate)
- Pathogens ( example: Corona Virus, Zika Virus, cynobacteria, E. Coli)

### Content
The Corona2.json file contains annotated text which was generated using LightTag online tool.
The Corona.json is subset of the content contained in Corona2.json (for most uses, please ignore this file)

### Acknowledgements
Text used for annotating was picked up from Wikipedia and manually tagged by me using LightTag

### Inspiration
This dataset was put together to support my efforts of analyzing the CORD 19 Research challenge ( https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge ). I thought it would be great idea to train a NER tagger that can identify entities of interest from the document.

## Steps after saving docBin.spacy:-
1. Create `base_config.cfg` file from https://spacy.io/usage/training as per requirement
2. Run below command which will create final `config.cfg` file
``` python
python -m spacy init fill-config base_config.cfg config.cfg

```
3. Run this command and put the train and test path
``` python
python -m spacy train config.cfg --output ./ --paths.train ./train_corona_docbin.spacy --paths.dev ./train_corona_docbin.spacy --gpu-id 0
```
4. Check local folder which store `model-best` and `model-last` folder 
5. Load `model-best` for evaluation

## Adding Snippets:-

![image](https://user-images.githubusercontent.com/97096513/212550719-3b6a337f-aebe-45d4-8522-c8d1cdc46176.png)

![image](https://user-images.githubusercontent.com/97096513/212550739-e17abb0c-8ba3-4471-9f64-d00bd291128b.png)

![image](https://user-images.githubusercontent.com/97096513/212551053-b6702c74-d1d7-48aa-b061-6f23b195d894.png)

![image](https://user-images.githubusercontent.com/97096513/212551097-17445b70-3688-484a-8665-89828fc8c988.png)


## Streamlit App Link: [Medical_NER_App](https://indra-inc-medical-custom-ner.streamlit.app/ "Medical_NER_App")


<img align="center" src="Medical_Custom_NER.gif" width="1000" height="500"/>
