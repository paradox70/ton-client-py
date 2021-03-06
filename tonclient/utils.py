from typing import Union, Dict

from tonclient.decorators import Response
from tonclient.module import TonModule


class TonUtils(TonModule):
    """ Free TON utils SDK API implementation """
    @Response.convert_address
    def convert_address(
            self, address: str, output_format: Union[str, Dict[str, bool]]
    ) -> str:
        """
        :param address: Account address in any format
        :param output_format: Format to convert to.
                'types.AddressStringFormat' class may help
        :return:
        """
        return self.request(
            method='utils.convert_address', address=address,
            output_format=output_format)
