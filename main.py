import streamlit as st
import spacy
import IPython
from spacy import displacy
import warnings
warnings.filterwarnings("ignore")


## creating function for test sentence
@st.cache
def evaluateDisplayNer(inp):
  # Loaded newly created model-best

  nlp_custom_ner = spacy.load('model-best')
  test_txt = inp
  print('')
  user_doc = nlp_custom_ner(test_txt)

  return user_doc
  


st.title('Custom NER: Corona')
st.header('Put your input string : ')
inp = st.text_input()
st.write('Your Input String is: ', inp)
doc = evaluateDisplayNer(inp)

colors = {"PATHOGEN": "#F67DE3", "MEDICINE": "#7DF6D9", "MEDICALCONDITION":"#85C1E9"}
options = {"colors": colors} 

st.subheader('The Result is: ')
for ent in doc.ents:
  st.write(ent.text, "|", ent.label_, '|', spacy.explain(ent.label_))

print('-------DISPLACY------')
ent_html = displacy.render(doc, style = 'ent',options= options, jupyter= False)
st.markdown(ent_html, unsafe_allow_html=True)


