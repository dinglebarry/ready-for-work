import sys

from .constants import clothing_output, FAIL, LEAVE
from .validation import validation_factory

def validate_values(clothing_list_str):
    validated_values = []
    input_clothing_values = [int(article) for article in clothing_list_str.split()]
    for value in input_clothing_values:
        validator = validation_factory.get(value)()
        if value in validated_values:
            validated_values.append(FAIL)
        elif validator.validate(validated_values):
            validated_values.append(value)
        else:
            validated_values.append(FAIL)

        if validated_values[-1] in [FAIL, LEAVE]:
            break

    if not validated_values or validated_values[-1] not in [FAIL, LEAVE]:
        validated_values.append(FAIL)

    return ", ".join(clothing_output.get(value) for value in validated_values)

def main():
    clothing_str = sys.argv[-1]
    output = validate_values(clothing_str)
    print(output)

if __name__ == "__main__":
    main()