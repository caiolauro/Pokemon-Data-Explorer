import streamlit as st
import pandas as pd
import requests

# Function to fetch Pokemon data from PokeAPI
def fetch_pokemon_data():
    pokemon_data = []
    for i in range(1, 101):  # Fetching data for 100 Pokemon
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{i}")
        if response.status_code == 200:
            pokemon = response.json()
            data = {
                "Name": pokemon["name"].capitalize(),
                "Type": pokemon["types"][0]["type"]["name"].capitalize(),
                "HP": pokemon["stats"][0]["base_stat"],
                "Attack": pokemon["stats"][1]["base_stat"],
                "Defense": pokemon["stats"][2]["base_stat"],
                "SpecialAttack": pokemon["stats"][3]["base_stat"],
                "SpecialDefense": pokemon["stats"][4]["base_stat"],
                "Speed": pokemon["stats"][5]["base_stat"],
            }
            pokemon_data.append(data)
    return pokemon_data


# Fetch Pokemon data
pokemon_data = fetch_pokemon_data()

# Create DataFrame
pokemon_df = pd.DataFrame(pokemon_data)

# Streamlit app
st.title("Pokemon Data Explorer")

# Display DataFrame
st.write("## Pokemon Data")
st.write(pokemon_df)

# Summary statistics
st.write("## Summary Statistics")
st.write(pokemon_df.describe())

# Bar chart of Pokemon types
st.write("## Pokemon Types Distribution")
type_counts = pokemon_df["Type"].value_counts()
st.bar_chart(type_counts)

# Scatter plot of Attack vs Defense
st.write("## Attack vs Defense")
st.scatter_chart(pokemon_df[["Attack", "Defense"]])

# Customize Streamlit page style
st.markdown(
    """
    <style>
        .reportview-container {
            background: url('https://cdn.pixabay.com/photo/2016/10/27/22/53/earth-1778406_960_720.jpg');
            background-size: cover;
        }
    </style>
    """,
    unsafe_allow_html=True,
)
