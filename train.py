# Importing necessary dependencies
import spacy
print(spacy.__version__)
from spacy import displacy
from spacy.tokens import DocBin
from tqdm import tqdm
from spacy.util import filter_spans
import json
import warnings
warnings.filterwarnings("ignore")


## Import data

with open('./Dataset/Corona2.json', 'r') as f:
  data = json.load(f)

  ## Now iterate over whole data and collect all these requirements form one list of training data

def data_training(data_json):
  '''
  Here we are creating one list of dictionary whose keys are 'text/content' and 'entities'
  'entities' contain a list of tuple contain start, end and label values
  format: training = [ {'text': string},
            {'entities': [(start , end , label), (.. , .. , .. ).. ]} ]
  i.e training is a list and each index is a dictionary 
  '''
  training = []    ## creating blank traing list
  for example in data_json['examples']:  ## accesing examples key
    temp_dict = {}    ## creating blank dict
    temp_dict['text'] = example['content']  ## creating  'text' key
    temp_dict['entities'] = []   ## creating 'entities' key whose value will be a list
    ## iterate over annotations to get start, end and tag_name 
    for anno in example['annotations']: ## accesing the value of annotation dict key
      start = anno['start']  ## extract the start key value
      end = anno['end']   ## extract the end key value
      label = anno['tag_name'].upper()     ## extract the tag_name key value and uppercasing
      temp_dict['entities'].append((start, end, label))  ## creating tuple of start, end and label & appending on entities
    training.append(temp_dict)   ## appending on training list
  return training

training_data = data_training(data)


## create our our own docbin and can pass any training or test list data
def doc_bin(data_list):
  
  ## Creating blank spacy model
  nlp_en = spacy.blank("en")
  doc_bin = DocBin() ## create docbin object
  for exmpl in tqdm(data_list):
    text = exmpl['text']
    labels = exmpl['entities']
    doc = nlp_en.make_doc(text)  ## Create a Doc from raw text i.e each text will consider as doc
    ents = []  ## creating blank entity list to append entities in this doc object
    for start, end, label in labels:
      ## create each entity as span object
      span = doc.char_span(start, end, label = label, alignment_mode = 'contract')  ## create span object from each doc created
      ## it will find out the given span from doc and will label it
      if span is None:
        print('Skipping Entities')
      else:
        ## now all span will append inside ents list with label to create own or custom entity list
        ents.append(span)

      ## using filter_span it will remove all duplicate span and entity so that to get filtered entities
      filtered_ents = filter_spans(ents)
      ## now putting those enties inside doc.entities
      doc.ents = filtered_ents
      ## now appending that document in the doc bin object
      doc_bin.add(doc)

  return doc_bin


## save training doc bin to disk
training_docBin = doc_bin(training_data)
training_docBin.to_disk('train_corona_docbin.spacy')

