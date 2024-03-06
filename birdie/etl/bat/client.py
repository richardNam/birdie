# Example url: https://bringatrailer.com/listing/2003-toyota-land-cruiser-42/


class BringATrailerClient:
    """ This client can handle http calls to the
    Bring A Trailer website. The expected response is the HTML
    for each vehicle listing.

    """
    def __init__(self, key):
        self.key = key

    def get_vin_response(self, unique_id):
        """ The single vin based caller for this class. Will fetch
        the HTML for a unique VIN.

        Parameters
        ----------

        unique_id : str
            A unique value that maps to the id of the product being sold. Primary
            key for the product being sold.

        Returns
        -------

        response : dict[Any, Any]

        """
        #TODO (richard): calls the private (or public) methods for the caller to
        #get the data that they need.
        pass



