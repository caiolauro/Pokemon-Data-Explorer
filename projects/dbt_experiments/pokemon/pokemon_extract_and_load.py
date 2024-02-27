import pandas as pd
import requests
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas


def get_snowflake_con_and_cursor():
    con = snowflake.connector.connect(
        user="XXX",
        role="XXX_ADMIN",
        database="XXX_DB_DEV",
        warehouse="XXX_WH",
        account="XXX.eu-west-1",
        schema="TEST",
        authenticator="externalbrowser",
    )

    cursor = con.cursor()

    return con, cursor


con, cursor = get_snowflake_con_and_cursor()


def fetch_pokemon_data(n=100):
    pokemon_data = []
    print(f"Fetching {n} pokemons...")
    for i in range(1, n + 1):  # Fetching data for 100 Pokemon
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

pokemon_df.columns = list(map(str.upper, pokemon_df.columns))

write_pandas(con, pokemon_df, "POKEMONS")
