import builtins
import pytest
import mock
import game
import stage
import main
import actions


# def test_main():
#     with mock.patch.object(builtins, 'input', lambda _: 'nineteen'):
#         with pytest.raises(TypeError):
            

#     with mock.patch.object(builtins, 'input', lambda _: '8'):
#         with pytest.raises(ValueError):
#             assert main.main()

""" ACTIONS.PY FUNCTION TEST """

def test_menu():
    with mock.patch.object(builtins, 'input', lambda _: 'qsddsqdq'):
        assert actions.menu() == ValueError
        
def test_menu():
    with mock.patch.object(builtins, 'input', lambda _: '1578'):
        assert actions.menu() == ValueError
        
@pytest.mark.parametrize(
    "result",
    [(24),(15),(48),(24)]
)
def test_attack(result):
    assert actions.attack() == result

@pytest.mark.parametrize(
    "result",
    [(24),(15),(48),(24)]
)
def test_potion(result):
    assert actions.potion() == result
    
@pytest.mark.parametrize(
    "result",
    [(24),(15),(48),(24)]
)
def test_fire_scroll(result):
    assert actions.fire_scroll() == result
    
@pytest.mark.parametrize(
    "result",
    [(24),(15),(48),(24)]
)
def test_ice_scroll(result):
    assert actions.ice_scroll() == result
    
@pytest.mark.parametrize(
    "result",
    [(24),(15),(48),(24)]
)
def test_lightning_scroll(result):
    assert actions.lightning_scroll() == result

""" PARTY.PY FUNCTIONS TEST """

def test_player_turn():
    with mock.patch.object(__builtins__, 'input', lambda: 'qsddsqdq'):
        assert game.player_turn() == ValueError
        
def test_player_turn():
    with mock.patch.object(__builtins__, 'input', lambda: '1578'):
        assert game.player_turn() == ValueError
        
def test_game():
    pass #Must flow well

@pytest.mark.parametrize(
    "liste, result",
    [([''],True), ([''],True), ([''],True), ([''],True)]
)
def test_save(liste, result):
    assert game.save(liste) == result

""" STAGE.PY FUNCTIONS TEST """

@pytest.mark.parametrize(
    "result",
    [(['enemy'])]
)
def test_stage(result):
    assert stage.stage() == result

@pytest.mark.parametrize(
    "result",
    [(['gold', 'potion'],['gold', 'potion'])]
)
def test_gold(result):
    assert stage.gold() == result 

@pytest.mark.parametrize(
    "result",
    [(['gold', 'potion'],['gold', 'potion'])]
)
def test_shop(result):
    assert stage.shop() == result
        
""" MAIN.PY FUNCTIONS TEST """

def test_main():
    pass #Must flow well

