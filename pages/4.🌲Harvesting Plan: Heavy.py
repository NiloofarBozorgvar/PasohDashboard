import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np



# ----------------------------------------------------------------------------------------------------Text Box
def display_design_element():
    st.subheader("Regime and Objective-based Simulation for Stand Prescription")

    text = (
        "In this section, we will see the different prescription scenarios. "
        "Also, the implications of the prescription are explained below."
    )
    font_size = 17
    font_color = "#333333"
    border_color = "#C4661F"
    background_color = "#F5F6F2"
    border_width = 2

    styled_text = f"""
        <div style="padding: 10px; border: {border_width}px solid {border_color};
                    border-radius: 5px; background-color: {background_color};">
            <p style="font-size: {font_size}px; color: {font_color};">{text}</p>
        </div>
    """

    st.markdown(styled_text, unsafe_allow_html=True)

st.title('Ecology Simulator')
display_design_element()
#--------------------------------------------------------------------------Text

st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)
st.write('For **Heavy Regime**, you will see the Number of Trees need to be harvest and the carbon loss, '
         'if this regime be applied. 🪵🪓')

#----------------------------------------------------------------------------------------------------Heavy Table

def display_table_heavy():
    html_table = """
    <table style="font-size: 18px; text-align: left; border-collapse: collapse; width: 100%;">
        <thead>
            <tr>
                <th style="background-color: #919B3e; color: #222577A; font-size: 14px; padding: 8px; border-bottom: 3px solid #ddd; border-left: 3px solid #ddd; border-top: 3px solid #ddd;">Plan</th>
                <th style="background-color: #919B3e; color: #222577A; font-size: 14px; padding: 8px; border-bottom: 3px solid #ddd; border-left: 3px solid #ddd; border-top: 3px solid #ddd;">#trees to harvest</th>
                <th style="background-color: #919B3e; color: #222577A; font-size: 14px; padding: 8px; border-bottom: 3px solid #ddd; border-left: 3px solid #ddd; border-top: 3px solid #ddd;">Carbon loss</th>
                <th style="background-color: #919B3e; color: #222577A; font-size: 14px; padding: 8px; border-bottom: 3px solid #ddd; border-left: 3px solid #ddd; border-top: 3px solid #ddd; border-right: 3px solid #ddd;">Economic value</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td style="font-size: 14px; color: #423025; padding: 12px; border-bottom: 3px solid #ddd; border-right: 3px solid #ddd; border-left: 3px solid #ddd;">BDq Heavy regime</td>
                <td style="font-size: 14px; color: #4f483f; padding: 8px; border-bottom: 1px solid #ddd;">742</td>
                <td style="font-size: 14px; color: #4f483f; padding: 8px; border-bottom: 1px solid #ddd;">7175435</td>
                <td style="font-size: 14px; color: #4f483f; padding: 8px; border-bottom: 1px solid #ddd;">742169</td>
            </tr>
        </tbody>
    </table>
    """

    st.markdown(html_table, unsafe_allow_html=True)

display_table_heavy()

#-------------------------------------------------------------------

st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)
st.write(' 📣📣  Here, based on the objective you have, you can see the details of prescription plan ⛑️')

#------------------------------------------------------------------------------------------------Objective Table


def display_table_objective():
    html_table = """
       <table style="border-collapse: collapse; width: 100%;">
        <thead>
            <tr style="background-color: #132A13; color: #dfe6da; font-size: 9.2px; border-bottom: 3px solid #ddd;">
                <th style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-top: 3px solid #ddd;">Regimes</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;">Total # Trees to Harvest</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;"># Remaining Species</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;"># Trees to harvest DBH Class 24<</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;"># Trees to harvest DBH Class 18-23</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;"># Trees to harvest DBH Class 12-17</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;"># Trees to harvest DBH Class 6-11</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;"># Trees to harvest DBH Class 1-5</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;">Remaining Density</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;">New AGB</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;">New Carbon Stock</th>
            </tr>
        </thead>
        <tbody>
            <tr style="text-align: left; font-size: 14px;">
                <td style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-bottom: 3px solid #ddd;">Diversity Objective</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">742</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">308</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">38</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">37</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">98</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">382</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">187</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">440.73</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">334.63</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">9.07M</td>
            </tr>
            <tr style="text-align: left; font-size: 14px;">
                <td style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-bottom: 3px solid #ddd;">Species-Based Objective</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">742</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">320</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">38</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">37</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">104</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">379</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">184</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">432.92</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">341.51</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">9M</td>
            </tr>
                <tr style="text-align: left; font-size: 14px;">
                <td style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-bottom: 3px solid #ddd;">Dominance Objective</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">742</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">288</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">38</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">37</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">102</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">380</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">185</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">456.01</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">360.08</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">9.1M</td>
            </tr>
                <tr style="text-align: left; font-size: 14px;">
                <td style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-bottom: 3px solid #ddd;">Economical Objective</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">742</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
            </tr>
        </tbody>
    </table>
    """
    st.markdown(html_table, unsafe_allow_html=True)

display_table_objective()

#-----------------------------------------------------------------------------------------------
def mapshow2019(df):
    df['Species'] = df['Species'].astype('category')  # Convert 'SP' column to categorical

    fig = px.scatter(df, x='XCO', y='YCO', color='Species')

    # Update title attributes
    fig.update_layout(
        title=dict(text='Actual Location of Trees', x=0.3, y=0.9,  # Adjust x and y to change title position
                   font=dict(color='dark green', size=20, family='Arial')),  # Change title font attributes
        xaxis_title=dict(text='XCO Title', font=dict(color='green')),  # Change x-axis title and color
        yaxis_title=dict(text='YCO Title', font=dict(color='green'))  # Change y-axis title and color
    )

    st.plotly_chart(fig)

st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)
st.write(' 🔔 Now by chossing buttons below 👇, you will se the 📍location of trees than need to be harvest base on your Objective.')

st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)


if col1.button('***Diversity*** Objective;and Heavy regime'):
    data = pd.read_csv('Prescription stremlit/HDiversity.csv')
    st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)
    data = data[['XCO', 'YCO', 'Species']]
    df = pd.DataFrame(data)
    species_list = df['Species'].unique().tolist()
    mapshow2019(df)

if col2.button('***Species-based*** Objective; Heavy regime'):
    data = pd.read_csv('Prescription stremlit/HSpices.csv')
    st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)
    data = data[['XCO', 'YCO', 'Species']]
    df = pd.DataFrame(data)
    species_list = df['Species'].unique().tolist()
    mapshow2019(df)

if col3.button('***Dominance*** Objective; Heavy regime'):
    data = pd.read_csv('Prescription stremlit/HDominance.csv')
    st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)
    data = data[['XCO', 'YCO', 'Species']]
    df = pd.DataFrame(data)
    species_list = df['Species'].unique().tolist()
    df = df.drop(index=24)
    mapshow2019(df)

if col4.button('***Economical*** Objective; Heavy regime'):
    st.write('No Data Available Yet!')

#--------------------------------------------------------------------------Text

#st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)
#st.write('See 🪵🪓')
