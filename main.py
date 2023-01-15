import streamlit as st
import spacy
import IPython
from spacy import displacy
import warnings
warnings.filterwarnings("ignore")


## creating function for test sentence

def evaluateDisplayNer(inp):
  # Loaded newly created model-best

  nlp_custom_ner = spacy.load('model-best')
  test_txt = inp
  user_doc = nlp_custom_ner(test_txt)

  return user_doc
  


st.title('Custom NER: Corona')
st.header('Put your input string : ')
inp = st.text_input(label = "")

doc = evaluateDisplayNer(inp)

colors = {"PATHOGEN": "#F67DE3", "MEDICINE": "#7DF6D9", "MEDICALCONDITION":"#85C1E9"}
options = {"colors": colors} 

st.subheader("-------- List of Entity and their Label --------")
for ent in doc.ents:
  st.write(ent.text, "|", ent.label_, '|')

st.subheader("-------- Entity and Label Display --------")
ent_html = displacy.render(doc, style = 'ent',options= options, jupyter= False)
st.markdown(ent_html, unsafe_allow_html=True)


