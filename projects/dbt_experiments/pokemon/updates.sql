-- Update Bulbasaur's HP
UPDATE pokemons
SET HP = UNIFORM( 0 , 100 , random() )
WHERE Name = 'Bulbasaur';

-- Update Ivysaur's Attack
UPDATE pokemons
SET Attack = UNIFORM( 0 , 100 , random() )
WHERE Name = 'Ivysaur';

-- Update Venusaur's Defense
UPDATE pokemons
SET Defense = UNIFORM( 0 , 100 , random() )
WHERE Name = 'Venusaur';

-- Update Charmander's Special Attack
UPDATE pokemons
SET SpecialAttack = UNIFORM( 0 , 100 , random() )
WHERE Name = 'Charmander';

-- Update Charmeleon's Special Defense
UPDATE pokemons
SET SpecialDefense = UNIFORM( 0 , 100 , random() )
WHERE Name = 'Charmeleon';

-- Update Bulbasaur's Speed
UPDATE pokemons
SET Speed = UNIFORM( 0 , 100 , random() )
WHERE Name = 'Bulbasaur';

-- Update Ivysaur's HP
UPDATE pokemons
SET HP = UNIFORM( 0 , 100 , random() )
WHERE Name = 'Ivysaur';

-- Update Venusaur's Attack
UPDATE pokemons
SET Attack = UNIFORM( 0 , 100 , random() )
WHERE Name = 'Venusaur';

-- Update Charmander's Defense
UPDATE pokemons
SET Defense = UNIFORM( 0 , 100 , random() )
WHERE Name = 'Charmander';

-- Update Charmeleon's Speed
UPDATE pokemons
SET Speed = UNIFORM( 0 , 100 , random() )
WHERE Name = 'Charmeleon';
