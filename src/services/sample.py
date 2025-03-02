"""
Sample service file to demonstrate the structure
"""


class SampleService:
    """
    This is a sample service
    """

    def __init__(self):
        self.sample_attr = "sample_attr"

    def sample_method(self) -> str:
        """
        This is a sample method.

        Returns
        -------
        str
            The sample attribute.
        """
        return self.sample_attr
