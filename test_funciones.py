import pytest
from funciones import dijsktra, minimo_no_visitado

@pytest.mark.parametrize(
    "input_red, input_inicio, result",
    [
        ({
            "A" : {'nodes':['B']},
            "B" : {'nodes':['A','C']},
            "C" : {'nodes':['B','D','G']},
            "D" : {'nodes':['C','E']},
            "E" : {'nodes':['D','F']},
            "F" : {'nodes':['E','I']},
            "G" : {'nodes':['C','H']},
            "H" : {'nodes':['G','I']},
            "I" : {'nodes':['H','F']},
        }, 'A', 
        {
            "A" : 0,
            "B" : 1,
            "C" : 2,
            "D" : 3,
            "E" : 4,
            "F" : 5,
            "G" : 3,
            "H" : 4,
            "I" : 5,
        }
        ),
        ({
            "A" : {'nodes':['B']},
            "B" : {'nodes':['A','C']},
            "C" : {'nodes':['B','D','G']},
            "D" : {'nodes':['C','E']},
            "E" : {'nodes':['D','F']},
            "F" : {'nodes':['E','I']},
            "G" : {'nodes':['C','I']},
            "H" : {'nodes':[]},
            "I" : {'nodes':['G','F']},
        }, 'A', 
        {
            "A" : 0,
            "B" : 1,
            "C" : 2,
            "D" : 3,
            "E" : 4,
            "F" : 5,
            "G" : 3,
            "H" : float('inf'),
            "I" : 4,
        }
        ),
        ({
            "A" : {'nodes':['B']},
            "B" : {'nodes':['A','C']},
            "C" : {'nodes':['B','D','G']},
            "D" : {'nodes':['C','E']},
            "E" : {'nodes':['D','F']},
            "F" : {'nodes':['E','I']},
            "G" : {'nodes':['C','H']},
            "H" : {'nodes':['G','I']},
            "I" : {'nodes':['H','F']},
        }, 'G', 
        {
            "A" : 3,
            "B" : 2,
            "C" : 1,
            "D" : 2,
            "E" : 3,
            "F" : 3,
            "G" : 0,
            "H" : 1,
            "I" : 2,
        }
        ),
    ]
)

def test_dijsktra_distancia(input_red,input_inicio,result):
    assert dijsktra(input_red, input_inicio)[0] == result

@pytest.mark.parametrize(
    "red, inicio, resultado",
    [
        ({
            "A" : {'nodes':['B']},
            "B" : {'nodes':['A','C']},
            "C" : {'nodes':['B','D','G']},
            "D" : {'nodes':['C','E']},
            "E" : {'nodes':['D','F']},
            "F" : {'nodes':['E','I']},
            "G" : {'nodes':['C','H']},
            "H" : {'nodes':['G','I']},
            "I" : {'nodes':['H','F']},
        }, 'A', 
        {
            "A" : 'A',
            "B" : 'A->B',
            "C" : 'A->B->C',
            "D" : 'A->B->C->D',
            "E" : 'A->B->C->D->E',
            "F" : 'A->B->C->D->E->F',
            "G" : 'A->B->C->G',
            "H" : 'A->B->C->G->H',
            "I" : 'A->B->C->G->H->I',
        }
        ),
        ({
            "A" : {'nodes':['B']},
            "B" : {'nodes':['A','C']},
            "C" : {'nodes':['B','D','G']},
            "D" : {'nodes':['C','E']},
            "E" : {'nodes':['D','F']},
            "F" : {'nodes':['E','I']},
            "G" : {'nodes':['C','I']},
            "H" : {'nodes':[]},
            "I" : {'nodes':['G','F']},
        }, 'A', 
        {
            "A" : 'A',
            "B" : 'A->B',
            "C" : 'A->B->C',
            "D" : 'A->B->C->D',
            "E" : 'A->B->C->D->E',
            "F" : 'A->B->C->D->E->F',
            "G" : 'A->B->C->G',
            "H" : '',
            "I" : 'A->B->C->G->I',
        }
        ),
        ({
            "A" : {'nodes':['B']},
            "B" : {'nodes':['A','C']},
            "C" : {'nodes':['B','D','G']},
            "D" : {'nodes':['C','E']},
            "E" : {'nodes':['D','F']},
            "F" : {'nodes':['E','I']},
            "G" : {'nodes':['C','H']},
            "H" : {'nodes':['G','I']},
            "I" : {'nodes':['H','F']},
        }, 'G', 
        {
            "A" : 'G->C->B->A',
            "B" : 'G->C->B',
            "C" : 'G->C',
            "D" : 'G->C->D',
            "E" : 'G->C->D->E',
            "F" : 'G->H->I->F',
            "G" : 'G',
            "H" : 'G->H',
            "I" : 'G->H->I',
        }
        ),
    ]
)

def test_dijsktra_camino(red,inicio,resultado):
    assert dijsktra(red, inicio)[1] == resultado


@pytest.mark.parametrize(
    "visitado, distancia, estacion",
    [
        ({
            "A" : 1,
            "B" : 1,
            "C" : 1,
            "D" : 1,
            "E" : 1,
            "F" : 1,
            "G" : 1,
            "H" : 1,
            "I" : 1,
        },
        {
            "A" : 4,
            "B" : 3,
            "C" : 1,
            "D" : 2,
            "E" : 4,
            "F" : 3,
            "G" : 5,
            "H" : 5,
            "I" : 6,
        }, 
            -1
        ),
        ({
            "A" : 0,
            "B" : 0,
            "C" : 0,
            "D" : 0,
            "E" : 0,
            "F" : 0,
            "G" : 0,
            "H" : 0,
            "I" : 0,
        },
        {
            "A" : float('inf'),
            "B" : float('inf'),
            "C" : float('inf'),
            "D" : float('inf'),
            "E" : float('inf'),
            "F" : float('inf'),
            "G" : 0,
            "H" : 1,
            "I" : 45,
        }, 
            'G'
        ),
        ({
            "A" : 1,
            "B" : 1,
            "C" : 1,
            "D" : 0,
            "E" : 0,
            "F" : 0,
            "G" : 1,
            "H" : 0,
            "I" : 1,
        },
        {
            "A" : 0,
            "B" : 3,
            "C" : 2,
            "D" : 4,
            "E" : float('inf'),
            "F" : float('inf'),
            "G" : 1,
            "H" : 5,
            "I" : 3,
        }, 
            'D'
        )
    ]
)

def test_minimo_no_visitado_multi(visitado,distancia,estacion):
    assert minimo_no_visitado(visitado, distancia) == estacion