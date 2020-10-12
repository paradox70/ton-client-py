from typing import Dict, Any

from tonclient.decorators import Response
from tonclient.module import TonModule


class TonBoc(TonModule):
    """ Free TON boc SDK API implementation """
    @Response.parse_message
    def parse_message(self, boc: str) -> Dict[str, Any]:
        """
        :param boc: Base64 encoded BOC
        :return:
        """
        return self.request(function_name='boc.parse_message', boc=boc)

    @Response.parse_transaction
    def parse_transaction(self, boc: str) -> Dict[str, Any]:
        """
        :param boc: Base64 encoded BOC
        :return:
        """
        return self.request(function_name='boc.parse_transaction', boc=boc)

    @Response.parse_account
    def parse_account(self, boc: str) -> Dict[str, Any]:
        """
        :param boc: Base64 encoded BOC
        :return:
        """
        return self.request(function_name='boc.parse_account', boc=boc)

    @Response.parse_block
    def parse_block(self, boc: str) -> Dict[str, Any]:
        """
        :param boc: Base64 encoded BOC
        :return:
        """
        return self.request(function_name='boc.parse_block', boc=boc)

    @Response.get_blockchain_config
    def get_blockchain_config(self, block_boc: str) -> str:
        """
        :param block_boc: Base64 encoded block boc
        :return:
        """
        return self.request(
            function_name='boc.get_blockchain_config', block_boc=block_boc)