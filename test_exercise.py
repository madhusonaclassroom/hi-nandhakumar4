import pytest
import exercise

def test_exercise():
    input_values = ["Scott"]
    output = []

    def mock_input(s=None):
        if s is not None:
            
            output.append(s)
            return input_values[0]
        else:
            
            output.append("")
            print(output)
            return input_values[0]    
    

    exercise.input = mock_input
    
    exercise.print = lambda s : output.append(s)    

    exercise.main()
    

    assert output == ["","Hi Scott"]

test_exercise()