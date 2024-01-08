import streamlit as st
import pandas as pd
import plotly.express as px

# ----------------------------------------------------------------------------------------------------Text Box
def display_design_element():
    st.subheader("🔍📝Insight and Prediction:")

    text = (
        " In the following you can see the predicted information on Pasoh Forest trees 🎯. "
    )
    font_size = 17
    font_color = "#333333"
    border_color = "#8D6A9F"
    background_color = "wight"
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
#-------------------------------------------------------------------------------bar chart function 2019
def clustering2019(x_axis_ranges , df):
    df_ranges = pd.DataFrame(index=x_axis_ranges)
    for column in df.columns:
        col_values = []
        for x_range in x_axis_ranges:
            if '-' in x_range:
                start, end = map(int, x_range.split('-'))
                filtered_values = df[column][(df[column] >= start) & (df[column] <= end)]
            else:
                filtered_values = df[column][df[column] == int(x_range)]
            col_values.append(filtered_values.count())
        df_ranges[column] = col_values

    fig = px.bar(df_ranges, x=['1-5', '6-11', '12-17', '18-23', '24<'], y=df_ranges.columns, barmode='group',
                 color_discrete_sequence=px.colors.qualitative.Dark24)

    # Updating the layout
    fig.update_layout(
        title=dict(text='Actual and Predicted Number of Trees (In each DBH Classes) 2019', x=0.10,
                   font=dict(color='dark green')),

        xaxis_title=dict(text='DBH Class', font=dict(color='purple')),
        yaxis_title=dict(text='Number of Trees', font=dict(color='purple')),
        xaxis=dict(tickangle=45)

    )
    # Displaying the chart using Streamlit
    st.plotly_chart(fig)

#-----------------------------------------------------------------------------------------------bar chart function 2021
def clustering2021(x_axis_ranges , df):
    df_ranges = pd.DataFrame(index=x_axis_ranges)
    for column in df.columns:
        col_values = []
        for x_range in x_axis_ranges:
            if '-' in x_range:
                start, end = map(int, x_range.split('-'))
                filtered_values = df[column][(df[column] >= start) & (df[column] <= end)]
            else:
                filtered_values = df[column][df[column] == int(x_range)]
            col_values.append(filtered_values.count())
        df_ranges[column] = col_values

    custom_colors = ['orange', 'blue', 'orange', 'blue', 'orange']  # Add more colors as needed

    fig = px.bar(df_ranges, x=['1-5', '6-11', '12-17', '18-23', '24<'], y=df_ranges.columns, barmode='group',
                 color_discrete_sequence=custom_colors * 2)

    # Updating the layout
    fig.update_layout(
        title=dict(text='Actual and Predicted Number of Trees (In each DBH Classes) 2021', x=0.10,
                   font=dict(color='dark green')),

        xaxis_title=dict(text='DBH Class', font=dict(color='Blue')),
        yaxis_title=dict(text='Number of Trees', font=dict(color='Blue')),
        xaxis=dict(tickangle=45)
    )

    # Displaying the chart using Streamlit
    st.plotly_chart(fig)
#----------------------------------------------------------------------------------Option Bar
st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)

option = st.selectbox(
        "Information of forest trees in year:",
        ("2019", "2021"),
    )
st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)

#--------------------------------------------------------------------------------------Call Bar Chart 2019
if option =='2019':
    df = pd.read_csv('DBH2019.csv')
    df = df[['Predicted DBH for 2019' , 'Actual DBH for 2019']]
    # Define the ranges for x-axis
    #st.write(df)
    # ----------------Call the clustering function with your specified ranges and DataFrame
    x_axis_ranges = ['1-14', '15-29', '30-44', '45-58', '59-200']
    result = clustering2019(x_axis_ranges, df)  # 'df' is my DataFrame
    print(result)


#---------------------------------------------------------------------------------------------Bar chart 2021
if option =='2021':
    df = pd.read_csv('DBH2021.csv')
    df = df[['Predicted DBH for 2021' , 'Actual DBH for 2021']]
    # ----------------Call the clustering function with your specified ranges and DataFrame
    x_axis_ranges = ['1-14', '15-29', '30-44', '45-58', '59-200']
    result = clustering2021(x_axis_ranges, df)  # 'df' is my DataFrame
    print(result)

#-------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------Text Box
st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)

def display_design_element():
    st.subheader("📣📣 As an appropriate growth, at least a 1cm increase in DBH every year is expected in each tree. "
                 "In the following, you can see the name of Species with expected growth.")

    text = (
        " 1:SHORL1, 2:NEPHCO, 3:EUGERI, 4:SARADE, 5:SHORM1, 6:MACACO, 7:SHORAC, "
        "8:XANTEU, 9:XANTST, 10:RYPAKU, 11:EUGEP4, 12:DIPTC1, 13:CASTME, 14:ARTORI, "
        "15:SHORL2, 16:SHORP2, 17:SAR1GR, 18:BRACHO, 19:SANTTO, 20:MESUFE, 21:XYLOFS, "
        "22:CLE1SU, 23:CYNOMA, 24:PTYCCO, 25:ARCHBU, 26:CALODI, 27:ARCHCL, 28:DIOSBU, "
        "29:DIALPL, 30:ELAERU, 31:BOUEOP, 32:MONOMA, 33:CANTDI, 34:SINDWA, 35:MACALO, "
        "36:ELAEFL, 37:STYRBE, 38:SHORP1, 39:SANTLA, 40:POL1JE, 41:LITHCU, 42:EUGEFL. "
    )
    font_size = 18
    font_color = "#333333"
    border_color = "green"
    background_color = "wight"
    border_width = 2

    styled_text = f"""
        <div style="padding: 10px; border: {border_width}px solid {border_color};
                    border-radius: 5px; background-color: {background_color};">
            <p style="font-size: {font_size}px; color: {font_color};">{text}</p>
        </div>
    """

    st.markdown(styled_text, unsafe_allow_html=True)

display_design_element()
#-------------------------------------------------------------------------------------------------Good Growth
import streamlit as st
import pandas as pd

# Load your dataset
# Replace 'your_data.csv' with your actual data file path
df = pd.read_csv('All1521.csv')

# Filter for DBH values in years 2019 and 2021
filtered_df = df[(df['Year'] == 2019) | (df['Year'] == 2021)]

# Remove trees with 0 DBH in both 2019 and 2021
zero_dbh_trees = filtered_df.pivot_table(index='TAG', columns='Year', values='DBH', aggfunc='max')
zero_dbh_trees = zero_dbh_trees[(zero_dbh_trees[2019] != 0) | (zero_dbh_trees[2021] != 0)].index
filtered_df = df[df['TAG'].isin(zero_dbh_trees)]

# Check for at least 2cm growth in DBH for remaining trees
remaining_trees = filtered_df['TAG'].unique()
trees_with_growth = []

for tag in remaining_trees:
    dbh_2019 = filtered_df[(filtered_df['TAG'] == tag) & (filtered_df['Year'] == 2019)]['DBH'].values[0]
    dbh_2021 = filtered_df[(filtered_df['TAG'] == tag) & (filtered_df['Year'] == 2021)]['DBH'].values[0]
    species_name = filtered_df[(filtered_df['TAG'] == tag)]['Species'].values[0]
    xco = filtered_df[(filtered_df['TAG'] == tag) & (filtered_df['Year'] == 2021)]['XCO'].values[0]
    yco = filtered_df[(filtered_df['TAG'] == tag) & (filtered_df['Year'] == 2021)]['YCO'].values[0]

    if dbh_2021 - dbh_2019 >= 2:
        trees_with_growth.append({'TAG': tag, 'Species': species_name, 'XCO': xco, 'YCO': yco})

# Display names of species with trees that have at least 2cm growth in DBH
st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)
st.subheader('If you want, you can see the details of each specie 🔍')

selected_species = st.selectbox('Select Species', sorted(list(set([tree['Species'] for tree in trees_with_growth]))))

if selected_species:
    st.write(f"Species: {selected_species}")

    species_trees = [tree for tree in trees_with_growth if tree['Species'] == selected_species]

    if st.button('Show Details'):
        if species_trees:
            st.write("Details of trees with good growth:")
            growth_df = pd.DataFrame(species_trees)
            st.table(growth_df[['TAG', 'XCO', 'YCO']])
        else:
            st.write("No trees met the criteria for this species.")
else:
    st.write("Please select a species.")

#----------------------------------------------------------------------------------------

