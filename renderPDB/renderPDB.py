# Dependencies
import streamlit as st
from stmol import *
import py3Dmol

# Title and header
st.markdown('''# Usage of stmol :package:_A Streamlit **Component** for render molecular structures within Streamlit Web app._''')
st.sidebar.header("Research your own molecule. :art:")


# Example Input Data (1A2C)
# example_PDB = '''pdb:1A2C'''
example_PDB = '''1A2C'''
initial_label = '''NO'''

# Select input
PDB_ID = st.sidebar.text_area(label = "Please, paste your PDB ID ⬇️",value = example_PDB, height  = 50)
label = st.sidebar.text_area(label = "Please, write SHOW if you want to see aminoacids labels ⬇️",value = initial_label, height  = 50)

# Structure of thrombin inhibited by AERUGINOSIN298-A from a BLUE-GREEN ALGA
#xyzview = py3Dmol.view(query=PDB_ID) 
#xyzview.setStyle({'cartoon':{'color':'blue'}})

if label == '''NO''':
	#showmol(xyzview, height = 500,width=800)
	showmol(render_pdb(id = PDB_ID),height = 800,width=1200)
else:
	showmol(render_pdb_resn(viewer = render_pdb(id = PDB_ID),resn_lst = ['ALA',]),height = 800,width=1200)

