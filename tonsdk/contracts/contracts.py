class TonContracts:
    """
    TON SDK contracts JSON API
    https://github.com/tonlabs/TON-SDK/wiki/Core-Library-JSON-API
    """

    def __init__(self, client):
        self._client = client

    def tvm_get(self, function_name: str, code_b64: str, data_b64: str,
                **kwargs) -> dict:
        params = {
            "functionName": function_name,
            "codeBase64": code_b64,
            "dataBase64": data_b64
        }
        params.update(kwargs)

        return self._client.request("tvm.get", params)

    def run_local(self, address: str, abi: dict, function_name: str,
                  inputs: dict, header=None, account=None, key_pair=None,
                  full_run=False, time=None, **kwargs) -> dict:
        # TODO: Update args description
        """
        Run contract locally
        Args:
            address (address): Address string
            abi (dict): Contract JSON ABI (part of function call set)
            function_name (str): Contract fn name (part of function call set)
            inputs (dict): Contract fn inputs (part of function call set)
            header (?, None): Contract header (part of function call set)
            account (?dict): Account struct
            key_pair (dict): Dict with 'public' and 'secret' keys
            full_run (bool):
            time (int, None):
        Returns:
            dict
        """
        params = {
            "address": address,
            "account": account,
            "abi": abi,
            "functionName": function_name,
            "input": inputs,
            "header": header,
            "keyPair": key_pair,
            "fullRun": full_run,
            "time": time
        }
        params.update(kwargs)

        return self._client.request("contracts.run.local", params)

    def run_local_msg(self, address: str, message_base64: str, account=None,
                      abi=None, function_name=None, full_run=False, time=None,
                      **kwargs) -> dict:
        # TODO: Update args description
        """
        Locally run contract with message
        Args:
            address (str): Sender address
            message_base64 (str): Base64 of message BOC
            account (?, None): Some struct wanted
            abi (dict, None): JSON ABI as str
            function_name (str, None): Contract function name
            full_run (bool): ? Full contract run?
            time (int, None): ? What time
        Returns:
            dict
        """
        params = {
            "address": address,
            "messageBase64": message_base64,
            "account": account,
            "abi": abi,
            "function_name": function_name,
            "fullRun": full_run,
            "time": time
        }
        params.update(kwargs)

        return self._client.request("contracts.run.local.msg", params)

    def run(self, address: str, abi: dict, function_name: str, inputs: dict,
            header=None, key_pair=None, try_index=None, **kwargs) -> dict:
        """
        Run contract in blockchain. Pay attention for client configuration,
        is it main net or test test to avoid funds loss.
        Args:
            address (str): Contract address
            abi (dict): Contract JSON ABI
            function_name (str): Contract function name to execute
            inputs (dict): Arguments for function
            key_pair (dict, None): Contract key pair {'public', 'secret'}
            header (?): Contract header
            try_index (int, None): ?
        Returns:
            dict
        """
        params = {
            "address": address,
            "abi": abi,
            "functionName": function_name,
            "input": inputs,
            "header": header,
            "keyPair": key_pair,
            "try_index": try_index
        }
        params.update(kwargs)

        return self._client.request("contracts.run", params)

    def load(self, address: str, **kwargs) -> dict:
        params = {"address": address}
        params.update(kwargs)

        return self._client.request("contracts.load", params)

    def find_shard(self, address: str, shards: [dict], **kwargs) -> dict:
        params = {
            "address": address,
            "shards": shards
        }
        params.update(kwargs)

        return self._client.request("contracts.find.shard", params)

    def convert_address(self, address: str, convert_to: str, b64_params=None,
                        **kwargs) -> dict:
        """
        Address representations
        Args:
            address (str): Address
            convert_to (str): Available values (AccountId, Hex, Base64)
            b64_params (dict): Required only for Base64 convert to.
                               {"url": bool, "test": bool, "bounce": bool}
        Returns:
            dict
        """
        params = {
            "address": address,
            "convertTo": convert_to,
            "base64Params": b64_params
        }
        params.update(kwargs)

        return self._client.request("contracts.address.convert", params)
