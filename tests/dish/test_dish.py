from src.models.dish import Dish  # noqa: F401, E261, E501

from src.models.ingredient import Ingredient, Restriction

import pytest


# Req 2
def test_dish():
    # Criando ingredientes
    picanha = Ingredient("carne")
    gorgonzola = Ingredient("queijo gorgonzola")

    # Criando pratos
    picanha_ao_molho_gorgonzola = Dish("Picanha com Gorgonzola", 50.0)
    escondidinho_de_picanha = Dish("Escondidinho de Picanha", 40.0)
    picanha_recheada = Dish("Picanha Recheada", 60.0)

    # Adicionando ingredientes
    picanha_ao_molho_gorgonzola.add_ingredient_dependency(picanha, 1)
    picanha_ao_molho_gorgonzola.add_ingredient_dependency(gorgonzola, 2)

    escondidinho_de_picanha.add_ingredient_dependency(picanha, 1)
    escondidinho_de_picanha.add_ingredient_dependency(gorgonzola, 2)

    picanha_recheada.add_ingredient_dependency(picanha, 1)

    # Teste de igualdade e hash
    assert picanha_ao_molho_gorgonzola.name == "Picanha com Gorgonzola"
    assert hash(
        picanha_ao_molho_gorgonzola
    ) == hash(picanha_ao_molho_gorgonzola)
    assert picanha_ao_molho_gorgonzola == picanha_ao_molho_gorgonzola
    assert picanha_ao_molho_gorgonzola != picanha_recheada
    assert hash(picanha_ao_molho_gorgonzola) != hash(picanha_recheada)

    # Teste de representação
    assert repr(
        picanha_ao_molho_gorgonzola
    ) == "Dish('Picanha com Gorgonzola', R$50.00)"

    # Teste de ingredientes
    assert picanha_ao_molho_gorgonzola.recipe.get(picanha) == 1
    assert picanha_ao_molho_gorgonzola.recipe.get(gorgonzola) == 2
    assert picanha_ao_molho_gorgonzola.get_ingredients() == {
        picanha, gorgonzola
    }

    # Teste das restrições
    assert picanha_ao_molho_gorgonzola.get_restrictions() == {
        Restriction.ANIMAL_MEAT,
        Restriction.ANIMAL_DERIVED,
        Restriction.LACTOSE
    }

    # Teste do preço
    with pytest.raises(TypeError):
        Dish("Invalid Dish", "invalid_price")
    with pytest.raises(ValueError):
        Dish("Invalid Dish", -1.0)
    with pytest.raises(ValueError):
        Dish("Invalid Dish", 0.0)
