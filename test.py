
import spacy
from spacy import displacy


## creating function for test sentence
def evaluateDisplayNer():
  # Loaded newly created model-best

  nlp_custom_ner = spacy.load('model-best')
  test_txt = input(str('Put your input string:'))
  print('')
  user_doc = nlp_custom_ner(test_txt)
  colors = {"PATHOGEN": "#F67DE3", "MEDICINE": "#7DF6D9", "MEDICALCONDITION":"#85C1E9"}
  options = {"colors": colors} 
  print('')
  for ent in user_doc.ents:
    print(ent.text, "|", ent.label_, '|', spacy.explain(ent.label_))

  print('-------DISPLACY------')
  displacy.render(user_doc, style = 'ent',options= options, page=True)

evaluateDisplayNer()