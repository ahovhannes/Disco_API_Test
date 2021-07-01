#
# Collection of functions for generating strings
#

class generatedStrings:

    def generateNsymbols(self, c, n):
        """
        For generate spaces

        Args:
            c : Symbol (character)
            n : Quantity of symbols

        Returns:
            String with given quantity of symbols
        """
        generatedSymbols = ""
        for i in range(n):
            generatedSymbols += c
        return generatedSymbols

    def return_parameters_value(self, parameter, valueKind, parameterValue):
        """    
        For return the parameter's value
        
        Args:
                 parameter : Parameter, which values will be returned
                 valueKind : Kind of value, which can be "novalue" or "allvalues"
            parameterValue : The value, which will be returned if valueKind case will be fired

        Returns:
            The parameter's value
        """
        return parameter if parameter!=valueKind else parameterValue

