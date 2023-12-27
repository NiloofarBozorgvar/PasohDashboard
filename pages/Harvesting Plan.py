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
def display_regime_selection():
    selected_regime = st.radio('Select Regime', ['Heavy', 'Medium', 'Light'] , index=None)
    return selected_regime

def main():
    st.title('Ecology Simulator')
    display_design_element()



# ---------------------------------------------------------------------------------------------Plan 1 Sub table
def display_custom_table_Plan1():
    html_table = """
    <table style="border-collapse: collapse; width: 100%;">
        <thead>
            <tr style="background-color: #104f17; color: #dfe6da; font-size: 12px; border-bottom: 3px solid #ddd;">
                <th style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-top: 3px solid #ddd;">Objective</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;">Number of Trees to Harvest</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;">Number of Remaining Trees</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;">Number of Remaining Species</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;">Remaining Density</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;">New AGB</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;">Carbon Stock</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;">Carbon Loss</th>
            </tr>
        </thead>
        <tbody>
            <tr style="text-align: left; font-size: 14px;">
                <td style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-bottom: 3px solid #ddd;">Economical</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">742</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">1</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
            </tr>
            <tr style="text-align: left; font-size: 14px;">
                <td style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-bottom: 3px solid #ddd;">Diversity</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">742</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">832</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
            </tr>
                <tr style="text-align: left; font-size: 14px;">
                <td style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-bottom: 3px solid #ddd;">Species-based</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">742</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">832</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
            </tr>
                <tr style="text-align: left; font-size: 14px;">
                <td style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-bottom: 3px solid #ddd;">Dominance</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">742</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">832</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
            </tr>
            <!-- Add similar rows for the remaining data -->
        </tbody>
    </table>
    """
    st.markdown(html_table, unsafe_allow_html=True)


# --------------------------------------------------------------------------------------------- Plan2 Sub Table
def display_custom_table_Plan2():
    html_table = """
    <table style="border-collapse: collapse; width: 100%;">
        <thead>
            <tr style="background-color: #266b1c; color: #222577A; font-size: 12px; border-bottom: 3px solid #ddd;">
                <th style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-top: 3px solid #ddd;">Objective</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;">Number of Trees to Harvest</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;">Number of Remaining Trees</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;">Number of Remaining Species</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;">Remaining Density</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;">New AGB</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;">Carbon Stock</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;">Carbon Loss</th>
            </tr>
        </thead>
        <tbody>
            <tr style="text-align: left; font-size: 14px;">
                <td style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-bottom: 3px solid #ddd;">Economical</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">164</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">2</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
            </tr>
            <tr style="text-align: left; font-size: 14px;">
                <td style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-bottom: 3px solid #ddd;">Diversity</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">164</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">1410</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
            </tr>
                <tr style="text-align: left; font-size: 14px;">
                <td style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-bottom: 3px solid #ddd;">Species-based</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">164</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">1410</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
            </tr>
                <tr style="text-align: left; font-size: 14px;">
                <td style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-bottom: 3px solid #ddd;">Dominance</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">164</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">1410</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
            </tr>
            <!-- Add similar rows for the remaining data -->
        </tbody>
    </table>
    """
    st.markdown(html_table, unsafe_allow_html=True)


# ---------------------------------------------------------------------------------------------Plan 3 Sub Table
def display_custom_table_Plan3():
    html_table = """
    <table style="border-collapse: collapse; width: 100%;">
        <thead>
            <tr style="background-color: #4b872b; color: #222577A; font-size: 12px; border-bottom: 3px solid #ddd;">
                <th style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-top: 3px solid #ddd;">Objective</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;">Number of Trees to Harvest</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;">Number of Remaining Trees</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;">Number of Remaining Species</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;">Remaining Density</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;">New AGB</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;">Carbon Stock</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;">Carbon Loss</th>
            </tr>
        </thead>
        <tbody>
            <tr style="text-align: left; font-size: 14px;">
                <td style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-bottom: 3px solid #ddd;">Economical</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">32</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">1542</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
            </tr>
            <tr style="text-align: left; font-size: 14px;">
                <td style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-bottom: 3px solid #ddd;">Diversity</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">32</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">1542</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
            </tr>
                <tr style="text-align: left; font-size: 14px;">
                <td style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-bottom: 3px solid #ddd;">Species-based</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">32</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">1542</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
            </tr>
                <tr style="text-align: left; font-size: 14px;">
                <td style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-bottom: 3px solid #ddd;">Dominance</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">32</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">1542</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
            </tr>
            <!-- Add similar rows for the remaining data -->
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
    "Select years for BDq",
    ("2019", "2021"),
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

st.write("Regimes available for Pasoh")
st.markdown(html, unsafe_allow_html=True)
#__________________________________________________________________________________________________________
st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)
display_design_elementv2('Note: To See the Detail of Regimes and Objective-based Prescription, You Need to Select the Desired Regime from the Radio Button below.')
st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)
# ---------------------------------------------------------------------------------------------------  button
regime_selection = display_regime_selection()

if regime_selection == 'Heavy':
    st.write('Heavy regime')
    df = pd.DataFrame(dataobjectiveheavy)
    display_custom_table_Plan1()
    st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)

    display_design_elementv3(
        'Now based on the objective that you are interested in, you can see the information of the trrees that need to be chop down.')
    st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)


    col1, col2, col3, col4 = st.columns(4)

    if col1.button('Heavy regime; Economical Objective'):
        st.write('Not Available Yet!')

    if col2.button('Heavy regime; Species-based Objective'):
        data = pd.read_csv('Prescription stremlit/HSpices.csv')
        st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)
        data = data[['XCO', 'YCO', 'Species']]
        df = pd.DataFrame(data)
        # Get unique species values for the selectbox
        species_list = df['Species'].unique().tolist()
        mapshow2019(df)



asdasd
    if col3.button('Heavy regime; Diversity Objective'):
        data = pd.read_csv('Prescription stremlit/HDiversity.csv')
        st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)
        data = data[['XCO', 'YCO', 'Species']]
        df = pd.DataFrame(data)
        # Get unique species values for the selectbox
        species_list = df['Species'].unique().tolist()
        mapshow2019(df)

    if col4.button('Heavy regime; Dominance Objective'):
        data = pd.read_csv('Prescription stremlit/HDominance.csv')
        st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)
        data = data[['XCO', 'YCO', 'Species']]
        df = pd.DataFrame(data)
        # Get unique species values for the selectbox
        species_list = df['Species'].unique().tolist()
        mapshow2019(df)


if regime_selection == 'Medium':
    st.write('Medium regime')
    df = pd.DataFrame(dataobjectivemedium)
    display_custom_table_Plan2()
    st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)
    display_design_elementv3(
        ' Now based on the objective that you are interested in, you can see the information of the trrees that need to be chop down.')
    st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)


    col1, col2, col3, col4 = st.columns(4)

    if col1.button('Medium regime; Economical Objective'):
        st.write('Not Available Yet!')

    if col2.button('Medium regime; Species-based Objective'):
        data = pd.read_csv('Prescription stremlit/MSpices.csv')
        st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)
        data = data[['XCO', 'YCO', 'Species']]
        df = pd.DataFrame(data)
        # Get unique species values for the selectbox
        species_list = df['Species'].unique().tolist()
        mapshow2019(df)

    if col3.button('Medium regime; Diversity Objective'):
        data = pd.read_csv('Prescription stremlit/MDiversity.csv')
        st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)
        data = data[['XCO', 'YCO', 'Species']]
        df = pd.DataFrame(data)
        # Get unique species values for the selectbox
        species_list = df['Species'].unique().tolist()
        mapshow2019(df)

    if col4.button('Medium regime; Dominance Objective'):
        data = pd.read_csv('Prescription stremlit/MDominance.csv')
        st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)
        data = data[['XCO', 'YCO', 'Species']]
        df = pd.DataFrame(data)
        # Get unique species values for the selectbox
        species_list = df['Species'].unique().tolist()
        mapshow2019(df)


if regime_selection == 'Light':
    st.write('Light regime')
    df = pd.DataFrame(dataobjectivelight)
    display_custom_table_Plan3()
    st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)

    display_design_elementv3(
        ' Now based on the objective that you are interested in, you can see the information of the trrees that need to be chop down.')
    st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)


    col1, col2, col3, col4 = st.columns(4)

    if col1.button('Light regime; Economical Objective'):
        st.write('Not Available Yet!')

    if col2.button('Light regime; Species-based Objective'):
        data = pd.read_csv('Prescription stremlit/LSpices.csv')
        st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)
        data = data[['XCO', 'YCO', 'Species']]
        df = pd.DataFrame(data)
        # Get unique species values for the selectbox
        species_list = df['Species'].unique().tolist()
        mapshow2019(df)

    if col3.button('Light regime; Diversity Objective'):
        data = pd.read_csv('Prescription stremlit/LDiversity.csv')
        st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)
        data = data[['XCO', 'YCO', 'Species']]
        df = pd.DataFrame(data)
        # Get unique species values for the selectbox
        species_list = df['Species'].unique().tolist()
        mapshow2019(df)

    if col4.button('Light regime; Dominance Objective'):
        data = pd.read_csv('Prescription stremlit/LDominance.csv')
        st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)
        data = data[['XCO', 'YCO', 'Species']]
        df = pd.DataFrame(data)
        # Get unique species values for the selectbox
        species_list = df['Species'].unique().tolist()
        mapshow2019(df)



