abiArray = [
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "name": "_from",
                "type": "address"
            },
            {
                "indexed": false,
                "name": "_latitude",
                "type": "fixed168x10"
            },
            {
                "indexed": false,
                "name": "_longitude",
                "type": "fixed168x10"
            }
        ],
        "name": "Report",
        "type": "event"
    },
    {
        "constant": false,
        "gas": 727,
        "inputs": [
            {
                "name": "addr",
                "type": "address"
            }
        ],
        "name": "isRegistered",
        "outputs": [
            {
                "name": "out",
                "type": "bool"
            }
        ],
        "payable": false,
        "type": "function"
    },
    {
        "constant": false,
        "gas": 3111,
        "inputs": [
            {
                "name": "_latitude",
                "type": "fixed168x10"
            },
            {
                "name": "_longitude",
                "type": "fixed168x10"
            }
        ],
        "name": "inputReport",
        "outputs": [],
        "payable": false,
        "type": "function"
    },
    {
        "constant": false,
        "gas": 106411,
        "inputs": [
            {
                "name": "_first_name",
                "type": "bytes32"
            },
            {
                "name": "_last_name",
                "type": "bytes32"
            }
        ],
        "name": "register",
        "outputs": [],
        "payable": false,
        "type": "function"
    },
    {
        "constant": true,
        "gas": 817,
        "inputs": [
            {
                "name": "arg0",
                "type": "address"
            }
        ],
        "name": "user__enrolled",
        "outputs": [
            {
                "name": "out",
                "type": "bool"
            }
        ],
        "payable": false,
        "type": "function"
    },
    {
        "constant": true,
        "gas": 853,
        "inputs": [
            {
                "name": "arg0",
                "type": "address"
            }
        ],
        "name": "user__first_name",
        "outputs": [
            {
                "name": "out",
                "type": "bytes32"
            }
        ],
        "payable": false,
        "type": "function"
    },
    {
        "constant": true,
        "gas": 883,
        "inputs": [
            {
                "name": "arg0",
                "type": "address"
            }
        ],
        "name": "user__last_name",
        "outputs": [
            {
                "name": "out",
                "type": "bytes32"
            }
        ],
        "payable": false,
        "type": "function"
    }
]
