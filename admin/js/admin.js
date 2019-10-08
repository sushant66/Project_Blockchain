var contract;

        $(document).ready(function()
        {
            var address = //"0xb6e71040E5e3A2f148D4775f6BA04566a85DCb8c"
"0xE5CF4D4b613A93bF69BA07d0b4aF4931A81397dA";   //master

            var abi = [
	{
		"constant": false,
		"inputs": [],
		"name": "clear",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [],
		"name": "get",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [],
		"name": "get2",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "result_1",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "result_2",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	}
];

		web3 = new Web3(web3.currentProvider);	    

		contract = new web3.eth.Contract(abi, address);
	    //var interval = setInterval(x(), 5000);
	    $('#clear').click(function()
        {
         
            web3.eth.getAccounts().then(function(accounts)
            {
                var acc = accounts[0];
                //var address = "0x0e706b06168997700d3cc3c4617db9f4d03e6516";
                return contract.methods.clear().send({from: acc});
            }).then(function(tx)
            {
                console.log(tx);
            }).catch(function(tx)
            {
                console.log(tx);
            })
        })
        })
