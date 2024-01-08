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
#-----------------------------------------------------------------

st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)
st.write('For **Medium Regime**, you will see the Number of Trees need to be harvest and the carbon loss, '
         'if this regime be applied. 🪵🪓')

#----------------------------------------------------------------------------------------------------medium Table

def display_table_Medium():
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
                <td style="font-size: 14px; color: #423025; padding: 12px; border-bottom: 3px solid #ddd; border-right: 3px solid #ddd; border-left: 3px solid #ddd;">BDq Medium regime</td>
                <td style="font-size: 14px; color: #4f483f; padding: 8px; border-bottom: 1px solid #ddd;">164</td>
                <td style="font-size: 14px; color: #4f483f; padding: 8px; border-bottom: 1px solid #ddd;">1379174</td>
                <td style="font-size: 14px; color: #4f483f; padding: 8px; border-bottom: 1px solid #ddd;">532467</td>
            </tr>
        </tbody>
    </table>
    """

    st.markdown(html_table, unsafe_allow_html=True)

display_table_Medium()

#-------------------------------------------------------------------

st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)
st.write(' 📣📣  Here, based on the objective you have, you can see the details of prescription plan ⛑️')

#------------------------------------------------------------------------------------------------Objective Table


def display_table_objective():
    html_table = """
       <table style="border-collapse: collapse; width: 100%;">
        <thead>
            <tr style="background-color: #31572C; color: #dfe6da; font-size: 9.2px; border-bottom: 3px solid #ddd;">
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
                <td style="padding: 8px; border-right: 1px solid #ddd;">164</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">342</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">38</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">30</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">62</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">24</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">10</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">1653.80</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">1255.66</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">11.71M</td>
            </tr>
            <tr style="text-align: left; font-size: 14px;">
                <td style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-bottom: 3px solid #ddd;">Species-Based Objective</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">164</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">348</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">38</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">32</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">60</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">24</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">10</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">1698.20</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">1301.42</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">11.80M</td>
            </tr>
                <tr style="text-align: left; font-size: 14px;">
                <td style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-bottom: 3px solid #ddd;">Dominance Objective</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">164</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">342</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">38</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">32</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">64</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">22</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">8</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">1586.80</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">1282.21</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">11.66M</td>
            </tr>
                <tr style="text-align: left; font-size: 14px;">
                <td style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-bottom: 3px solid #ddd;">Economical Objective</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">164</td>
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


if col1.button('***Diversity*** Objective;and Medium regime'):
    data = pd.read_csv('Prescription stremlit/MDiversity.csv')
    st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)
    data = data[['XCO', 'YCO', 'Species']]
    df = pd.DataFrame(data)
    species_list = df['Species'].unique().tolist()
    mapshow2019(df)

if col2.button('***Species-based*** Objective; Medium regime'):
    data = pd.read_csv('Prescription stremlit/MSpices.csv')
    st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)
    data = data[['XCO', 'YCO', 'Species']]
    df = pd.DataFrame(data)
    species_list = df['Species'].unique().tolist()
    df = df.drop(index=14)
    mapshow2019(df)

if col3.button('***Dominance*** Objective; Medium regime'):
    data = pd.read_csv('Prescription stremlit/MDominance.csv')
    st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)
    data = data[['XCO', 'YCO', 'Species']]
    df = pd.DataFrame(data)
    species_list = df['Species'].unique().tolist()
    df = df.drop(index=24)
    mapshow2019(df)

if col4.button('***Economical*** Objective; Medium regime'):
    st.write('No Data Available Yet!')


