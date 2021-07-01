#
# Collection of functions worked with URL
#

class bddUrl:

    def urlBuilder(self, host, parameters):
        """
        Create URL from host and parameters

        Args:
            host       : The URL to send data to
            parameters : dictionary

        Returns:
            Parametrised URL address
        """
        parametersOneLine = ""
        for key, value in parameters.items():
            parametersOneLine += "&"+str(key)+"="+str(value)
        parametersOneLine = parametersOneLine[1:]
        url = host+"?"+parametersOneLine
        return url
