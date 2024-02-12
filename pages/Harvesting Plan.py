import streamlit as st
import pandas as pd
import streamlit as st
import plotly.express as px


# ----------------------------------------------------------------------------------------------------Text Box1
def display_design_element():
    st.subheader("Regime and Objective-based Simulation for Stand Prescription")

    text = (
        "In this section we will see the different prescription scenarios. Also the implication of the prescription is explained below. ")
    font_size = 17
    font_color = "#333333"  # Dark grey
    border_color = "#39e75f"  # Orange
    border_width = 2

    # Display the bordered text box for design visualization
    st.markdown(
        f"""
        <div style="padding:10px; border: {border_width}px solid {border_color}; border-radius: 5px;">
            <p style="font-size: {font_size}px; color: {font_color};">{text}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ----------------------------------------------------------------------------------------------------Text Box1
def display_design_elementv2(text):
    textconvert = (text)
    font_size = 15
    font_color = "#333333"  # Dark grey
    border_color = "#919B3e"  # Orange
    border_width = 1.5

    # Display the bordered text box for design visualization
    st.markdown(
        f"""
        <div style="padding:10px; border: {border_width}px solid {border_color}; border-radius: 5px;">
            <p style="font-size: {font_size}px; color: {font_color};">{textconvert}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
#---------------------------------------------------------------------------------------------------Text Box 2

def display_design_elementv3(text):
    textconvert = (text)
    font_size = 15
    font_color = "#287443"  # Dark grey
    border_color = "#bdbc25"  # Orange
    border_width = 1.5

    # Display the bordered text box for design visualization
    st.markdown(
        f"""
        <div style="padding:10px; border: {border_width}px solid {border_color}; border-radius: 5px;">
            <p style="font-size: {font_size}px; color: {font_color};">{textconvert}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    #---------------------------------------------------------------------------------------------Radio Buttons
def display_objective_selection():
    selected_objective = st.radio('Select you forest management objective:', ['Economical (Note: Data for Economical objective is not available now.)', 'Diversity', 'Species-based', 'Dominance'] , index=None)
    return selected_objective

def main():
    st.title('Ecology Simulator')
    display_design_element()



# ------------------------------------------------------------------------------------objective economicsal Sub table
def display_custom_table_Objective_economical():
    html_table = """
    <table style="border-collapse: collapse; width: 100%;">
        <thead>
            <tr style="background-color: #104f17; color: #dfe6da; font-size: 9.2px; border-bottom: 3px solid #ddd;">
                <th style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-top: 3px solid #ddd;">Regimes</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;">Total # Trees to Harvest</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;"># Remaining Species</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;"># Trees to harvest in DBH Class 24<</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;"># Trees to harvest in DBH Class 18-23</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;"># Trees to harvest in DBH Class 12-17</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;"># Trees to harvest in DBH Class 6-11</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;"># Trees to harvest in DBH Class 1-5</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;">Remaining Density</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;">New AGB</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;">Carbon Stock</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;">Carbon Loss</th>
            </tr>
        </thead>
        <tbody>
            <tr style="text-align: left; font-size: 14px;">
                <td style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-bottom: 3px solid #ddd;">Heavy Regime</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">742</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">1</td>
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
            <tr style="text-align: left; font-size: 14px;">
                <td style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-bottom: 3px solid #ddd;">Meduim Regime</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">742</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">832</td>
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
                <tr style="text-align: left; font-size: 14px;">
                <td style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-bottom: 3px solid #ddd;">Light Regime</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">742</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">832</td>
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


# ------------------------------------------------------------------------------------ objective diversity Sub Table
def display_custom_table_objective_Diversity():
    html_table = """
    <table style="border-collapse: collapse; width: 100%;">
        <thead>
            <tr style="background-color: #266b1c; color: #dfe6da; font-size: 9.2px; border-bottom: 3px solid #ddd;">
                <th style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-top: 3px solid #ddd;">Regimes</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;">Total # Trees to Harvest</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;"># Remaining Species</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;"># Trees to harvest in DBH Class 24<</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;"># Trees to harvest in DBH Class 18-23</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;"># Trees to harvest in DBH Class 12-17</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;"># Trees to harvest in DBH Class 6-11</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;"># Trees to harvest in DBH Class 1-5</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;">Remaining Density</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;">New AGB</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;">New Carbon Stock</th>
            </tr>
        </thead>
        <tbody>
            <tr style="text-align: left; font-size: 14px;">
                <td style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-bottom: 3px solid #ddd;">Heavy Regime</td>
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
                <td style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-bottom: 3px solid #ddd;">Meduim Regime</td>
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
                <td style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-bottom: 3px solid #ddd;">Light Regime</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">32</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">361</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">28</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">4</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">1930.84</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">1466</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">13.67M</td>
            </tr>
        </tbody>
    </table>
    """
    st.markdown(html_table, unsafe_allow_html=True)


# ---------------------------------------------------------------------------------------objective species Sub Table
def display_custom_table_objective_species():
    html_table = """
       <table style="border-collapse: collapse; width: 100%;">
        <thead>
            <tr style="background-color: #4b872b; color: #dfe6da; font-size: 9.2px; border-bottom: 3px solid #ddd;">
                <th style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-top: 3px solid #ddd;">Regimes</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;">Total # Trees to Harvest</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;"># Remaining Species</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;"># Trees to harvest in DBH Class 24<</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;"># Trees to harvest in DBH Class 18-23</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;"># Trees to harvest in DBH Class 12-17</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;"># Trees to harvest in DBH Class 6-11</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;"># Trees to harvest in DBH Class 1-5</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;">Remaining Density</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;">New AGB</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;">New Carbon Stock</th>
            </tr>
        </thead>
        <tbody>
            <tr style="text-align: left; font-size: 14px;">
                <td style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-bottom: 3px solid #ddd;">Heavy Regime</td>
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
                <td style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-bottom: 3px solid #ddd;">Meduim Regime</td>
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
                <td style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-bottom: 3px solid #ddd;">Light Regime</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">32</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">358</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">26</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">4</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">2</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">1948.32</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">1482.17</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">14.01M</td>
            </tr>
        </tbody>
    </table>
    """
    st.markdown(html_table, unsafe_allow_html=True)
# ---------------------------------------------------------------------------------------objective dominance Sub Table
def display_custom_table_objective_dominance():
    html_table = """
       <table style="border-collapse: collapse; width: 100%;">
        <thead>
            <tr style="background-color: #4b872b; color: #dfe6da; font-size: 9.2px; border-bottom: 3px solid #ddd;">
                <th style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-top: 3px solid #ddd;">Regimes</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;">Total # Trees to Harvest</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;"># Remaining Species</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;"># Trees to harvest in DBH Class 24<</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;"># Trees to harvest in DBH Class 18-23</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;"># Trees to harvest in DBH Class 12-17</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;"># Trees to harvest in DBH Class 6-11</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;"># Trees to harvest in DBH Class 1-5</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;">Remaining Density</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;">New AGB</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;">New Carbon Stock</th>
            </tr>
        </thead>
        <tbody>
            <tr style="text-align: left; font-size: 14px;">
                <td style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-bottom: 3px solid #ddd;">Heavy Regime</td>
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
                <td style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-bottom: 3px solid #ddd;">Meduim Regime</td>
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
                <td style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-bottom: 3px solid #ddd;">Light Regime</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">32</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">362</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">29</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">3</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">1931.08</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">1467.02</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">13.66M</td>
            </tr>
        </tbody>
    </table>
    """
    st.markdown(html_table, unsafe_allow_html=True)

# ---------------------------------------------------------------------------------------------Call Text Box


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



if __name__ == "__main__":
    main()

    st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)
# --------------------------------------------------------------------------------------------------------regimes table
# Create the data for the table
import streamlit as st
import pandas as pd

datatable = {
    'Plan ID': ['Plan 1: BDq Heavy regime', 'Plan 2: BDq Medium regime', 'Plan 3: BDq Light regime'],
    '#trees to harvest': [742, 164, 32],
    'Carbon loss': [7175435, 1379174, 298168],
    'Economic value': [742169, 532467, 149835]
}

dataobjectiveheavy = {
    'Objective': ['Economical', 'Diversity', 'Species-based', 'Dominance'],
    '# Trees to Harvest': [385, 74, None, None],
    '# Remaining Trees': [385, 74, None, None],
    '# Remaining Species': [385, 74, None, None],
    'Remaining Density': [385, 74, None, None],
    'New AGB': [385, 74, None, None],
    'Carbon Stock': [385, 74, None, None],
    'Carbon Loss': [385, 74, None, None],
}

dataobjectivemedium = {
    'Objective': ['Economical', 'Diversity', 'Species-based', 'Dominance'],
    '# Trees to Harvest': [385, 74, None, None],
    '# Remaining Trees': [385, 74, None, None],
    '# Remaining Species': [385, 74, None, None],
    'Remaining Density': [385, 74, None, None],
    'New AGB': [385, 74, None, None],
    'Carbon Stock': [385, 74, None, None],
    'Carbon Loss': [385, 74, None, None],
}

dataobjectivelight = {
    'Objective': ['Economical', 'Diversity', 'Species-based', 'Dominance'],
    '# Trees to Harvest': [385, 74, None, None],
    '# Remaining Trees': [385, 74, None, None],
    '# Remaining Species': [385, 74, None, None],
    'Remaining Density': [385, 74, None, None],
    'New AGB': [385, 74, None, None],
    'Carbon Stock': [385, 74, None, None],
    'Carbon Loss': [385, 74, None, None],
}
# --------------------------------------------------Select Box

option = st.selectbox(
    "Select the Prescription Method",
    ("BDq",), index=None
)

# Create a DataFrame
df = pd.DataFrame(datatable)

# ------------------------------------------------------------------------------------------- the Main table
html = f"""
    <table style="font-size: 18px; text-align: left; border-collapse: collapse; width: 100%;">
        <thead>
            <tr>
                <th style="background-color: #919B3e; color: #222577A; font-size: 14px; padding: 8px; border-bottom: 3px solid #ddd; border-left: 3px solid #ddd; border-top: 3px solid #ddd;">Plan ID</th>
                <th style="background-color: #919B3e; color: #222577A; font-size: 14px; padding: 8px; border-bottom: 3px solid #ddd; border-left: 3px solid #ddd; border-top: 3px solid #ddd;">#trees to harvest</th>
                <th style="background-color: #919B3e; color: #222577A; font-size: 14px; padding: 8px; border-bottom: 3px solid #ddd; border-left: 3px solid #ddd; border-top: 3px solid #ddd;">Carbon loss</th>
                <th style="background-color: #919B3e; color: #222577A; font-size: 14px; padding: 8px; border-bottom: 3px solid #ddd; border-left: 3px solid #ddd; border-top: 3px solid #ddd; border-right: 3px solid #ddd;">Economic value</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td style="font-size: 14px; color: #423025; padding: 12px; border-bottom: 3px solid #ddd; border-right: 3px solid #ddd; border-left: 3px solid #ddd;">Plan 1: BDq Heavy regime</td>
                <td style="font-size: 14px; color: #4f483f; padding: 8px; border-bottom: 1px solid #ddd;">742</td>
                <td style="font-size: 14px; color: #4f483f; padding: 8px; border-bottom: 1px solid #ddd;">7175435</td>
                <td style="font-size: 14px; color: #4f483f; padding: 8px; border-bottom: 1px solid #ddd;">742169</td>
            </tr>
            <tr>
                <td style="font-size: 14px; color: #423025; padding: 12px; border-bottom: 3px solid #ddd; border-right: 3px solid #ddd; border-left: 3px solid #ddd;">Plan 1: BDq Medium regime</td>
                <td style="font-size: 14px; color: #4f483f; padding: 8px; border-bottom: 1px solid #ddd;">164</td>
                <td style="font-size: 14px; color: #4f483f; padding: 8px; border-bottom: 1px solid #ddd;">1379174</td>
                <td style="font-size: 14px; color: #4f483f; padding: 8px; border-bottom: 1px solid #ddd;">532467</td>
            </tr>
            <tr>
                <td style="font-size: 14px; color: #423025; padding: 12px; border-bottom: 3px solid #ddd; border-right: 3px solid #ddd; border-left: 3px solid #ddd;">Plan 1: BDq Light regime</td>
                <td style="font-size: 14px; color: #4f483f; padding: 8px; border-bottom: 1px solid #ddd;">32</td>
                <td style="font-size: 14px; color: #4f483f; padding: 8px; border-bottom: 1px solid #ddd;">298168</td>
                <td style="font-size: 14px; color: #4f483f; padding: 8px; border-bottom: 1px solid #ddd;">149835</td>
            </tr>
        </tbody>
    </table>
"""
if option == "BDq":
    st.write("Regimes available for Pasoh")
    st.markdown(html, unsafe_allow_html=True)
    #__________________________________________________________________________________________________________
    st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)
    display_design_elementv2('Note: To See the Detail of Regimes and Objective-based Prescription, You Need to Select the Desired Regime from the Radio Button below.')
    st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)
    # ---------------------------------------------------------------------------------------------------  button
    regime_selection = display_objective_selection()

    if regime_selection == 'Economical':
        st.write('Economical Objective')
        df = pd.DataFrame(dataobjectiveheavy)
        display_custom_table_Objective_economical()
        st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)

        display_design_elementv3(
            'Now based on the objective and regime that you are interested in, you can see the location of the trrees that need to be chop down.')
        st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)


        col1, col2, col3 = st.columns(3)

        if col1.button(' Economical Objective; Heavy regime'):
            st.write('Not Available Yet!')

        if col2.button('Economical Objective; Medium regime'):
            st.write('Not Available Yet!')


        if col3.button('Economical Objective; Light regime'):
            st.write('Not Available Yet!')




    if regime_selection == 'Diversity':
        st.write('Diversity Objective')
        df = pd.DataFrame(dataobjectivemedium)
        display_custom_table_objective_Diversity()
        st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)
        display_design_elementv3(
            ' Now based on the objective and regime that you are interested in, you can see the Location of the trrees that need to be chop down.')
        st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)


        col1, col2, col3 = st.columns(3)

        if col1.button('Diversity Objective; Heavy regime'):
            data = pd.read_csv('Prescription stremlit/HDiversity.csv')
            st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)
            data = data[['XCO', 'YCO', 'Species']]
            df = pd.DataFrame(data)
            # Get unique species values for the selectbox
            species_list = df['Species'].unique().tolist()
            mapshow2019(df)

        if col2.button('Diversity Objective; Medium regime'):
            data = pd.read_csv('Prescription stremlit/MDiversity.csv')
            st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)
            data = data[['XCO', 'YCO', 'Species']]
            df = pd.DataFrame(data)
            # Get unique species values for the selectbox
            species_list = df['Species'].unique().tolist()
            mapshow2019(df)

        if col3.button('Diversity Objective; Light regime'):
            data = pd.read_csv('Prescription stremlit/LDiversity.csv')
            st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)
            data = data[['XCO', 'YCO', 'Species']]
            df = pd.DataFrame(data)
            # Get unique species values for the selectbox
            species_list = df['Species'].unique().tolist()
            mapshow2019(df)


    if regime_selection == 'Species-based':
        st.write('Species-based Objective')
        df = pd.DataFrame(dataobjectivemedium)
        display_custom_table_objective_species()
        st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)
        display_design_elementv3(
            'Now based on the objective and regime that you are interested in, you can see the Location of the trrees that need to be chop down.')
        st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)

        if col1.button('Species-based Objective; Heavy regime'):
            data = pd.read_csv('Prescription stremlit/HSpices.csv')
            st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)
            data = data[['XCO', 'YCO', 'Species']]
            df = pd.DataFrame(data)
            # Get unique species values for the selectbox
            species_list = df['Species'].unique().tolist()
            mapshow2019(df)

        if col2.button('Species-based Objective; Medium regime'):
            data = pd.read_csv('Prescription stremlit/MSpices.csv')
            st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)
            data = data[['XCO', 'YCO', 'Species']]
            df = pd.DataFrame(data)
            # Get unique species values for the selectbox
            species_list = df['Species'].unique().tolist()
            mapshow2019(df)

        if col3.button('Species-based Objective; Light regime'):
            data = pd.read_csv('Prescription stremlit/LSpices.csv')
            st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)
            data = data[['XCO', 'YCO', 'Species']]
            df = pd.DataFrame(data)
            # Get unique species values for the selectbox
            species_list = df['Species'].unique().tolist()
            mapshow2019(df)

    if regime_selection == 'Dominance':
        st.write('Dominance Objective')
        df = pd.DataFrame(dataobjectivemedium)
        display_custom_table_objective_dominance()
        st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)
        display_design_elementv3(
            ' Now based on the objective and regime that you are interested in, you can see the Location of the trrees that need to be chop down.')
        st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)

        if col1.button('Dominance Objective; Heavy regime'):
            data = pd.read_csv('Prescription stremlit/HDominance.csv')
            st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)
            data = data[['XCO', 'YCO', 'Species']]
            df = pd.DataFrame(data)
            # Get unique species values for the selectbox
            species_list = df['Species'].unique().tolist()
            mapshow2019(df)

        if col2.button('Dominance Objective; Medium regime'):
            data = pd.read_csv('Prescription stremlit/MDominance.csv')
            st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)
            data = data[['XCO', 'YCO', 'Species']]
            df = pd.DataFrame(data)
            # Get unique species values for the selectbox
            species_list = df['Species'].unique().tolist()
            mapshow2019(df)

        if col3.button('Dominance Objective; Light regime'):
            data = pd.read_csv('Prescription stremlit/LDominance.csv')
            st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)
            data = data[['XCO', 'YCO', 'Species']]
            df = pd.DataFrame(data)
            # Get unique species values for the selectbox
            species_list = df['Species'].unique().tolist()
            mapshow2019(df)
           # st.balloons()