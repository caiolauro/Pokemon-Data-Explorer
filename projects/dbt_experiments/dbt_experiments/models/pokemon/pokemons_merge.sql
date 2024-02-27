{{
    config(
        materialized="incremental",
        unique_key="NAME",
        incremental_strategy="merge"
    )
}}

select *
from pokemons
{% if is_incremental() %}
    where 
    (name || hp || attack || defense || specialattack || specialdefense || speed ) 
    not in (select name || hp || attack || defense || specialattack || specialdefense || speed from {{ this }})
{% endif %}