def convert_to_property_statement(code):
    return ('s:').join(code.split(':'))

def convert_to_qualifier_statement(code):
    return ('q:').join(code.split(':'))
