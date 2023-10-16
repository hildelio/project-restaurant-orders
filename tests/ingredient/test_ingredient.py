from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    picanha, cupim = Ingredient("carne"), Ingredient("carne")
    gorgonzola = Ingredient("queijo gorgonzola")

    # Teste de igualdade e hash
    assert hash(picanha) == hash(cupim) and picanha == cupim
    assert hash(picanha) != hash(gorgonzola)
    assert picanha == cupim
    assert picanha == picanha
    assert picanha != gorgonzola

    # Teste de representação
    assert repr(picanha) == "Ingredient('carne')"

    # Teste do nome
    assert picanha.name == "carne"

    # Teste das restrições
    expected_carne_restrictions = {Restriction.ANIMAL_MEAT,
                                   Restriction.ANIMAL_DERIVED}
    assert picanha.restrictions == expected_carne_restrictions
