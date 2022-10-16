# Streamlit is necessary to create a web-app
import streamlit as st

# St_speckmol is for molecular visualization (only for .xyz files)
from st_speckmol import speck_plot

# Title and header
st.markdown('''# st-speckmol :package:_A Streamlit **Component** for creating Speck molecular structures within Streamlit Web app._''')
st.sidebar.header("Add your own xyz coordinates below. :art:")

# Example Input Data (first row number of atoms, second
example_xyz ='''5 
methane molecule (in ångströms)
C        0.000000        0.000000        0.000000 
H        0.000000        0.000000        1.089000 
H        1.026719        0.000000       -0.363000 
H       -0.513360       -0.889165       -0.363000 
H       -0.513360        0.889165       -0.363000'''

# Select input
_xyz = st.sidebar.text_area(label = "Please, paste your coordinates ⬇️",value = example_xyz, height  = 200)
	

# Render structure and show molecule's name
st.code(_xyz.splitlines()[1])
res = speck_plot(_xyz)

# Extra information
with st.sidebar.expander("Notes:",expanded=True):
    
    st.markdown(":pushpin:Check out these [xyz_mol_examples folder](https://github.com/avrabyt/st-speckmol/tree/main/xyz_mol_examples). **(The format is critical).**")
    st.markdown("♻️ You can also convert any .pdb files to xyz - [code.](https://github.com/avrabyt/st-speckmol/blob/62d59ff6a059239f64626ef10f0bd9dfa2520d2e/st_speckmol/utils.py#L3)")
