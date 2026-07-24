def translator(a):
    """
    Translates a given string into a different format.
    
    Parameters:
    a (str): The input string to be translated.
    
    Returns:
    str: The translated string.
    """
    # Example translation logic (this can be modified as needed)
    if int(a) <= 20:
        translation_dict = {
            '0': 'zero',
            '1': 'uno',
            '2': 'dos',
            '3': 'tres',
            '4': 'cuatro',
            '5': 'cinco',
            '6': 'seis',
            '7': 'siete',
            '8': 'ocho',
            '9': 'nueve',
            '10': 'diez',
            '11': 'once',
            '12': 'doce',
            '13': 'trece',
            '14': 'catorce',
            '15': 'quince',
            '16': 'dieciséis',
            '17': 'diecisiete',
            '18': 'dieciocho',
            '19': 'diecinueve',
            '20': 'veinte'
        }
        return translation_dict[a]  # Return the translated value or the original if not found
    elif int(a) >20 and int(a) < 30:
        translation_dict = ''.join("veinti" + str(translator(str(int(a) - 20))))
        return translation_dict
    elif int(a) >= 30 and int(a) < 100:
        tens = int(a) // 10
        units = int(a) % 10
        translation_dict = {
            '2': 'veinte',
            '3': 'treinta',
            '4': 'cuarenta',
            '5': 'cincuenta',
            '6': 'sesenta',
            '7': 'setenta',
            '8': 'ochenta',
            '9': 'noventa'
        }
        if units == 0:
            return translation_dict[str(tens)]
        else:
            return translation_dict[str(tens)] + " y " + str(translator(str(units)))


def main():
    """
    Main function to execute the translation.
    """
    input_value = input("Enter a number to translate: ")
    translated_value = translator(input_value)
    print(f"Translated value: {translated_value}")   


        
main()

  